"""
Generated class for RelatedPerson. 
Time: 2024-07-22 14:02:49
"""

from fhirmodels.R4.CodeableConcept import *
from fhirmodels.R4.Period import *
from fhirmodels.R4.Reference import *
from fhirmodels.R4.Resource import *
from fhirmodels.R4.Extension import *
from fhirmodels.R4.BackboneElement import *
from fhirmodels.R4.Meta import *
from fhirmodels.R4.Address import *
from fhirmodels.R4.Attachment import *
from fhirmodels.R4.Identifier import *
from fhirmodels.R4.HumanName import *
from fhirmodels.R4.Narrative import *
from fhirmodels.R4.ContactPoint import *
from fhirmodels.R4.DomainResource import *


class Communication(FhirBaseModel):
    """A language which may be used to communicate with about the patient's health.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept language: The language which can be used to communicate with the patient about his or her health
    :param bool preferred: Language preference indicator
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "language": {"class_name": "CodeableConcept", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        language: "CodeableConcept" = None,
        preferred: "bool" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.language = language
        self.preferred = preferred

    @classmethod
    def from_dict(cls, data: dict) -> "RelatedPerson":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "RelatedPerson":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class RelatedPerson(DomainResource):
    """Information about a person that is involved in the care for a patient, but who is not the target of healthcare, nor has a formal responsibility in the care process.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: A human identifier for this person
    :param bool active: Whether this related person's record is in active use
    :param Reference patient: The patient this person is related to
    :param CodeableConcept relationship: The nature of the relationship
    :param HumanName name: A name associated with the person
    :param ContactPoint telecom: A contact detail for the person
    :param str gender: male | female | other | unknown
    :param str birthDate: The date on which the related person was born
    :param Address address: Address where the related person can be contacted or visited
    :param Attachment photo: Image of the person
    :param Period period: Period of time that this relationship is considered valid
    :param Communication communication: A language which may be used to communicate with about the patient's health
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "patient": {"class_name": "Reference", "is_contained": False},
        "relationship": {"class_name": "CodeableConcept", "is_contained": False},
        "name": {"class_name": "HumanName", "is_contained": False},
        "telecom": {"class_name": "ContactPoint", "is_contained": False},
        "address": {"class_name": "Address", "is_contained": False},
        "photo": {"class_name": "Attachment", "is_contained": False},
        "period": {"class_name": "Period", "is_contained": False},
        "communication": {"class_name": "Communication", "is_contained": True},
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
        active: "bool" = None,
        patient: "Reference" = None,
        relationship: list["CodeableConcept"] = None,
        name: list["HumanName"] = None,
        telecom: list["ContactPoint"] = None,
        gender: "str" = None,
        birthDate: "str" = None,
        address: list["Address"] = None,
        photo: list["Attachment"] = None,
        period: "Period" = None,
        communication: list["Communication"] = None,
    ):

        self.resourceType = "RelatedPerson"

        self.id = id
        self.meta = meta
        self.implicitRules = implicitRules
        self.language = language
        self.text = text
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.active = active
        self.patient = patient
        self.relationship = relationship or []
        self.name = name or []
        self.telecom = telecom or []
        self.gender = gender
        self.birthDate = birthDate
        self.address = address or []
        self.photo = photo or []
        self.period = period
        self.communication = communication or []

    @classmethod
    def from_dict(cls, data: dict) -> "RelatedPerson":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "RelatedPerson":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
