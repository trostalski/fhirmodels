"""
Generated class for Flag. 
Time: 2024-07-22 14:02:49
"""

from fhirmodels.R4.CodeableConcept import *
from fhirmodels.R4.Period import *
from fhirmodels.R4.Reference import *
from fhirmodels.R4.Resource import *
from fhirmodels.R4.Extension import *
from fhirmodels.R4.Meta import *
from fhirmodels.R4.Identifier import *
from fhirmodels.R4.Narrative import *
from fhirmodels.R4.DomainResource import *


class Flag(DomainResource):
    """Prospective warnings of potential issues when providing care to the patient.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business identifier
    :param str status: active | inactive | entered-in-error
    :param CodeableConcept category: Clinical, administrative, etc.
    :param CodeableConcept code: Coded or textual message to display to user
    :param Reference subject: Who/What is flag about?
    :param Period period: Time period when flag is active
    :param Reference encounter: Alert relevant during encounter
    :param Reference author: Flag creator
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "category": {"class_name": "CodeableConcept", "is_contained": False},
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        "subject": {"class_name": "Reference", "is_contained": False},
        "period": {"class_name": "Period", "is_contained": False},
        "encounter": {"class_name": "Reference", "is_contained": False},
        "author": {"class_name": "Reference", "is_contained": False},
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
        category: list["CodeableConcept"] = None,
        code: "CodeableConcept" = None,
        subject: "Reference" = None,
        period: "Period" = None,
        encounter: "Reference" = None,
        author: "Reference" = None,
    ):

        self.resourceType = "Flag"

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
        self.category = category or []
        self.code = code
        self.subject = subject
        self.period = period
        self.encounter = encounter
        self.author = author

    @classmethod
    def from_dict(cls, data: dict) -> "Flag":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Flag":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
