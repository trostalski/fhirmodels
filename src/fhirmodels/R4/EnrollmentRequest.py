"""
Generated class for EnrollmentRequest. 
Time: 2024-07-22 14:02:49
"""

from fhirmodels.R4.Reference import *
from fhirmodels.R4.Resource import *
from fhirmodels.R4.Extension import *
from fhirmodels.R4.Meta import *
from fhirmodels.R4.Identifier import *
from fhirmodels.R4.Narrative import *
from fhirmodels.R4.DomainResource import *


class EnrollmentRequest(DomainResource):
    """This resource provides the insurance enrollment details to the insurer regarding a specified coverage.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business Identifier
    :param str status: active | cancelled | draft | entered-in-error
    :param str created: Creation date
    :param Reference insurer: Target
    :param Reference provider: Responsible practitioner
    :param Reference candidate: The subject to be enrolled
    :param Reference coverage: Insurance information
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "insurer": {"class_name": "Reference", "is_contained": False},
        "provider": {"class_name": "Reference", "is_contained": False},
        "candidate": {"class_name": "Reference", "is_contained": False},
        "coverage": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        meta: "Meta" = None,
        implicitRules: "str" = None,
        language: "str" = None,
        text: "Narrative" = None,
        contained: list["Resource"] = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        identifier: list["Identifier"] = None,
        status: "str" = None,
        created: "str" = None,
        insurer: "Reference" = None,
        provider: "Reference" = None,
        candidate: "Reference" = None,
        coverage: "Reference" = None,
    ):

        self.resourceType = "EnrollmentRequest"

        self.id = id
        self.meta = meta
        self.implicitRules = implicitRules
        self.language = language
        self.text = text
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.status = status
        self.created = created
        self.insurer = insurer
        self.provider = provider
        self.candidate = candidate
        self.coverage = coverage

    @classmethod
    def from_dict(cls, data: dict) -> "EnrollmentRequest":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "EnrollmentRequest":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
