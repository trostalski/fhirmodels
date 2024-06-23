import io
import json
import logging
import os
import tarfile
import typing as t
from dataclasses import dataclass

import requests

from fhirmodels import constants as _c
from fhirmodels import utils

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class IgDependency:
    """The URL and version of a package dependency."""

    url: str
    version: str


@dataclass(frozen=True)
class PackageMaintainer:
    """The name and email of a package maintainer."""

    name: str
    email: str


@dataclass(frozen=True)
class PackageInfo:
    """Metadata parsed from a package's package.json file.
    See documentation for the package.json file at:
    https://confluence.hl7.org/pages/viewpage.action?pageId=35718629#NPMPackageSpecification-Packagemanifest
    """

    name: str
    version: str
    description: str | None
    canonical: str | None
    title: str | None
    url: str | None
    fhirVersions: list[str] | None
    dependencies: t.Collection["IgDependency"] | None
    keywords: tuple[str] | None
    author: str | None
    maintainers: list["PackageMaintainer"] | None
    jurisdiction: str | None
    license: str | None


class FhirPackageLoader:
    """Loads a FHIR package from a `.tar.gz` or `.tgz` file following NPM conventions."""

    def __init__(self):
        pass

    def load_from_version(
        self, fhir_version: t.Literal["R4", "R4B", "R5"]
    ) -> "FhirPackage":
        """Loads a FHIR package for a specified FHIR version."""
        version_urls = _c.FHIR_VERSION_PACKAGE_URLS
        url = version_urls[fhir_version]
        return self.load_from_npm(url, name=fhir_version)

    def load_from_path(self, path: str, name: str = None) -> "FhirPackage":
        """Loads a FHIR package from a local path."""
        package = FhirPackage()
        # check if valid directory
        if not os.path.isdir(path):
            raise ValueError(f"Path is not a directory: {path}")
        for file in utils.walk_directory(path):
            if not utils.is_json_file(file):
                continue
            filename = os.path.basename(file)
            content = utils.read_json_file(file)
            resource_type = content.get("resourceType")
            package.add_file(
                data=content, filename=filename, resource_type=resource_type
            )
        return package

    def load_from_npm(self, url: str, name: str = None):
        """Loads a FHIR npm package from an URL."""
        with requests.get(url, stream=True) as res:
            res.raise_for_status()
            package_bytes = res.content
            package_buffer = io.BytesIO(package_bytes)
        return FhirPackage.from_npm_file(npm_file=package_buffer, name=name)

    def load_from_simplifier(self, name: str, version: str):
        """Loads a FHIR npm package from simplifier.net."""
        url = f"https://packages.simplifier.net/{name}/{version}"
        return self.load_from_npm(url, name=name)


class FhirPackage:
    """Represents a FHIR package. In case a FHIR base version is loaded,
    the name should be equivalent to the FHIR version (e.g. "R4")."""

    def __init__(
        self,
        package_info: t.Optional[dict] = None,
        code_systems: t.Optional[list[dict]] = None,
        search_parameters: t.Optional[list[dict]] = None,
        structure_definitions: t.Optional[list[dict]] = None,
        value_sets: t.Optional[list[dict]] = None,
        capability_statements: t.Optional[list[dict]] = None,
        concept_maps: t.Optional[list[dict]] = None,
        name: t.Optional[str] = None,
    ):
        self.package_info = package_info
        self.code_systems = code_systems or []
        self.search_parameters = search_parameters or []
        self.structure_definitions = structure_definitions or []
        self.value_sets = value_sets or []
        self.capability_statements = capability_statements or []
        self.concept_maps = concept_maps or []
        self.name = name

        # Initialize dictionaries for O(1) lookup by URL
        self._code_systems_by_url = {
            cs["url"]: cs for cs in self.code_systems if "url" in cs
        }
        self._value_sets_by_url = {
            vs["url"]: vs for vs in self.value_sets if "url" in vs
        }
        self._search_parameters_by_url = {
            sp["url"]: sp for sp in self.search_parameters if "url" in sp
        }
        self._structure_definitions_by_url = {
            sd["url"]: sd for sd in self.structure_definitions if "url" in sd
        }
        self._capability_statements_by_url = {
            cs["url"]: cs for cs in self.capability_statements if "url" in cs
        }
        self._concept_maps_by_url = {
            cm["url"]: cm for cm in self.concept_maps if "url" in cm
        }

    @classmethod
    def from_npm_file(cls, npm_file: t.BinaryIO, name: str = None):
        """Loads a FHIR package from a `.tar.gz` or `.tgz` file following NPM conventions."""
        package_info = None
        code_systems = []
        search_parameters = []
        structure_definitions = []
        value_sets = []
        capability_statements = []
        concept_maps = []
        for filename, content in _read_fhir_package_npm(npm_file):
            content_json: dict = json.loads(content)
            resource_type = content_json.get("resourceType")
            if os.path.basename(filename) == "package.json":
                package_info = _parse_package_info(content_json)
            if resource_type == _c.CODESYSTEM:
                code_systems.append(content_json)
            elif resource_type == _c.SEARCHPARAMETER:
                search_parameters.append(content_json)
            elif resource_type == _c.STRUCTUREDEFINITION:
                structure_definitions.append(content_json)
            elif resource_type == _c.VALUESET:
                value_sets.append(content_json)
            elif resource_type == _c.CAPABILITYSTATEMENT:
                capability_statements.append(content_json)
            elif resource_type == _c.CONCEPTMAP:
                concept_maps.append(content_json)
            else:
                # skipping file
                continue

        return cls(
            package_info=package_info,
            code_systems=code_systems,
            search_parameters=search_parameters,
            structure_definitions=structure_definitions,
            value_sets=value_sets,
            capability_statements=capability_statements,
            concept_maps=concept_maps,
            name=name,
        )

    def get_codesystem_by_url(self, url: str):
        return self._code_systems_by_url.get(url)

    def get_valueset_by_url(self, url: str):
        return self._value_sets_by_url.get(url)

    def get_searchparameter_by_url(self, url: str):
        return self._search_parameters_by_url.get(url)

    def get_structuredefinition_by_url(self, url: str):
        return self._structure_definitions_by_url.get(url)

    def get_capabilitystatement_by_url(self, url: str):
        return self._capability_statements_by_url.get(url)

    def get_conceptmap_by_url(self, url: str):
        return self._concept_maps_by_url.get(url)

    @property
    def resource_structure_definitions(self):
        return self._get_structure_definitions_by_kind(_c.STRUC_DEF_RESOURCE)

    @property
    def base_resource_structure_definitions(self):
        resources = self._get_structure_definitions_by_kind(_c.STRUC_DEF_RESOURCE)
        base_resources = [
            r
            for r in resources
            if r.get("baseDefinition") == _c.DOMAIN_RESOURCE_STRUC_DEF_URL
        ]
        return base_resources

    @property
    def complex_type_structure_definitions(self):
        return self._get_structure_definitions_by_kind(_c.STRUC_DEF_COMPLEX_TYPE)

    @property
    def primitive_type_structure_definitions(self):
        return self._get_structure_definitions_by_kind(_c.STRUC_DEF_PRIMITIVE_TYPE)

    @property
    def logical_structure_definitions(self):
        return self._get_structure_definitions_by_kind(_c.STRUC_DEF_LOGICAL)

    @property
    def base_capability_statement(self) -> dict | None:
        """Packages might contain multiple capability statements.
        This method returns the base capability statement identified by the id.
        """
        for cs in self.capability_statements:
            if cs["id"] == "base":
                return cs
        return None

    def add_file(
        self,
        data: dict,
        filename: str,
        resource_type: str | None = None,
    ):
        if filename == "package.json":
            package_info = _parse_package_info(data)
            self.package_info = package_info
        elif resource_type == _c.CODESYSTEM:
            self.add_code_system(data)
        elif resource_type == _c.SEARCHPARAMETER:
            self.add_search_parameter(data)
        elif resource_type == _c.STRUCTUREDEFINITION:
            self.add_structure_definition(data)
        elif resource_type == _c.VALUESET:
            self.add_value_set(data)
        elif resource_type == _c.CAPABILITYSTATEMENT:
            self.add_capability_statement(data)
        elif resource_type == _c.CONCEPTMAP:
            self.add_concept_map(data)
        else:
            # skipping file
            return

    def add_structure_definition(self, structure_definition: dict):
        self.structure_definitions.append(structure_definition)
        self._structure_definitions_by_url[structure_definition["url"]] = (
            structure_definition
        )

    def add_code_system(self, code_system: dict):
        self.code_systems.append(code_system)
        self._code_systems_by_url[code_system["url"]] = code_system

    def add_search_parameter(self, search_parameter: dict):
        self.search_parameters.append(search_parameter)
        self._search_parameters_by_url[search_parameter["url"]] = search_parameter

    def add_value_set(self, value_set: dict):
        self.value_sets.append(value_set)
        self._value_sets_by_url[value_set["url"]] = value_set

    def add_capability_statement(self, capability_statement: dict):
        self.capability_statements.append(capability_statement)
        self._capability_statements_by_url[capability_statement["url"]] = (
            capability_statement
        )

    def add_concept_map(self, concept_map: dict):
        self.concept_maps.append(concept_map)
        self._concept_maps_by_url[concept_map["url"]] = concept_map

    def _get_structure_definitions_by_kind(
        self, kind: t.Literal["resource", "complex-type", "primitive-type", "logical"]
    ):
        return [sd for sd in self.structure_definitions if sd["kind"] == kind]


def _read_fhir_package_npm(npm_file: t.BinaryIO) -> t.Iterator[t.Tuple[str, str]]:
    """Yields the file entries for JSON resources in `npm_file` and their contents."""
    with tarfile.open(fileobj=npm_file, mode="r:gz") as f:
        for member in f.getmembers():
            if member.name.endswith(".json"):
                content = f.extractfile(member)
                if content is not None:
                    # using utf-8-sig to remove dealing with BOM, https://stackoverflow.com/questions/57152985/what-is-the-difference-between-utf-8-and-utf-8-sig
                    yield member.name, content.read().decode("utf-8-sig")
            else:
                # logger.info("Skipping  entry: %s.", member.name)
                continue


def _parse_package_info(json_obj: dict[str, t.Any]) -> "PackageInfo":
    """Creates an PackageInfo object given the contents of a package.json file."""
    return PackageInfo(
        name=json_obj["name"],
        version=json_obj["version"],
        canonical=json_obj.get("canonical"),
        title=json_obj.get("title"),
        description=json_obj.get("description"),
        dependencies=tuple(
            IgDependency(url=url, version=version)
            for url, version in json_obj.get("dependencies", {}).items()
        ),
        author=json_obj.get("author"),
        fhirVersions=json_obj.get("fhirVersions"),
        jurisdiction=json_obj.get("jurisdiction"),
        keywords=json_obj.get("keywords"),
        license=json_obj.get("license"),
        maintainers=[
            PackageMaintainer(
                name=maintainer.get("name", ""), email=maintainer.get("email", "")
            )
            for maintainer in json_obj.get("maintainers", [])
        ],
        url=json_obj.get("url"),
    )
