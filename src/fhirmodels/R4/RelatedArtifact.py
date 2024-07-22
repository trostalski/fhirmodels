"""
Generated class for RelatedArtifact. 
Time: 2024-07-22 14:02:49
"""

from fhirmodels.R4.Extension import *
from fhirmodels.R4.Attachment import *
from fhirmodels.fhir_base_model import FhirBaseModel


class RelatedArtifact(FhirBaseModel):
    """Base StructureDefinition for RelatedArtifact Type: Related artifacts such as additional documentation, justification, or bibliographic references.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param str type: documentation | justification | citation | predecessor | successor | derived-from | depends-on | composed-of
    :param str label: Short label
    :param str display: Brief description of the related artifact
    :param str citation: Bibliographic citation for the artifact
    :param str url: Where the artifact can be accessed
    :param Attachment document: What document is being referenced
    :param str resource: What resource is being referenced
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "document": {"class_name": "Attachment", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        type: "str" = None,
        label: "str" = None,
        display: "str" = None,
        citation: "str" = None,
        url: "str" = None,
        document: "Attachment" = None,
        resource: "str" = None,
    ):

        self.id = id
        self.extension = extension or []
        self.type = type
        self.label = label
        self.display = display
        self.citation = citation
        self.url = url
        self.document = document
        self.resource = resource

    @classmethod
    def from_dict(cls, data: dict) -> "RelatedArtifact":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "RelatedArtifact":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
