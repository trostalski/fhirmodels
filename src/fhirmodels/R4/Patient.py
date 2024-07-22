"""
Generated class for Patient. 
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


class Contact(FhirBaseModel):
    """A contact party (e.g. guardian, partner, friend) for the patient.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept relationship: The kind of relationship
    :param HumanName name: A name associated with the contact person
    :param ContactPoint telecom: A contact detail for the person
    :param Address address: Address for the contact person
    :param str gender: male | female | other | unknown
    :param Reference organization: Organization that is associated with the contact
    :param Period period: The period during which this contact person or organization is valid to be contacted relating to this patient
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "relationship": {"class_name": "CodeableConcept", "is_contained": False},
        "name": {"class_name": "HumanName", "is_contained": False},
        "telecom": {"class_name": "ContactPoint", "is_contained": False},
        "address": {"class_name": "Address", "is_contained": False},
        "organization": {"class_name": "Reference", "is_contained": False},
        "period": {"class_name": "Period", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        relationship: list["CodeableConcept"] = None,
        name: "HumanName" = None,
        telecom: list["ContactPoint"] = None,
        address: "Address" = None,
        gender: "str" = None,
        organization: "Reference" = None,
        period: "Period" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.relationship = relationship or []
        self.name = name
        self.telecom = telecom or []
        self.address = address
        self.gender = gender
        self.organization = organization
        self.period = period

    @classmethod
    def from_dict(cls, data: dict) -> "Patient":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Patient":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Communication(FhirBaseModel):
    """A language which may be used to communicate with the patient about his or her health.:param str id: Unique id for inter-element referencing
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
    def from_dict(cls, data: dict) -> "Patient":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Patient":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Link(FhirBaseModel):
    """Link to another patient resource that concerns the same actual patient.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference other: The other patient or related person resource that the link refers to
    :param str type: replaced-by | replaces | refer | seealso
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "other": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        other: "Reference" = None,
        type: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.other = other
        self.type = type

    @classmethod
    def from_dict(cls, data: dict) -> "Patient":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Patient":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Patient(DomainResource):
    """Demographics and other administrative information about an individual or animal receiving care or other health-related services.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: An identifier for this patient
    :param bool active: Whether this patient's record is in active use
    :param HumanName name: A name associated with the patient
    :param ContactPoint telecom: A contact detail for the individual
    :param str gender: male | female | other | unknown
    :param str birthDate: The date of birth for the individual
    :param bool deceasedBoolean: Indicates if the individual is deceased or not
    :param str deceasedDateTime: Indicates if the individual is deceased or not
    :param Address address: An address for the individual
    :param CodeableConcept maritalStatus: Marital (civil) status of a patient
    :param bool multipleBirthBoolean: Whether patient is part of a multiple birth
    :param int multipleBirthInteger: Whether patient is part of a multiple birth
    :param Attachment photo: Image of the patient
    :param Contact contact: A contact party (e.g. guardian, partner, friend) for the patient
    :param Communication communication: A language which may be used to communicate with the patient about his or her health
    :param Reference generalPractitioner: Patient's nominated primary care provider
    :param Reference managingOrganization: Organization that is the custodian of the patient record
    :param Link link: Link to another patient resource that concerns the same actual person
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "name": {"class_name": "HumanName", "is_contained": False},
        "telecom": {"class_name": "ContactPoint", "is_contained": False},
        "address": {"class_name": "Address", "is_contained": False},
        "maritalStatus": {"class_name": "CodeableConcept", "is_contained": False},
        "photo": {"class_name": "Attachment", "is_contained": False},
        "contact": {"class_name": "Contact", "is_contained": True},
        "communication": {"class_name": "Communication", "is_contained": True},
        "generalPractitioner": {"class_name": "Reference", "is_contained": False},
        "managingOrganization": {"class_name": "Reference", "is_contained": False},
        "link": {"class_name": "Link", "is_contained": True},
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
        name: list["HumanName"] = None,
        telecom: list["ContactPoint"] = None,
        gender: "str" = None,
        birthDate: "str" = None,
        deceasedBoolean: "bool" = None,
        deceasedDateTime: "str" = None,
        address: list["Address"] = None,
        maritalStatus: "CodeableConcept" = None,
        multipleBirthBoolean: "bool" = None,
        multipleBirthInteger: "int" = None,
        photo: list["Attachment"] = None,
        contact: list["Contact"] = None,
        communication: list["Communication"] = None,
        generalPractitioner: list["Reference"] = None,
        managingOrganization: "Reference" = None,
        link: list["Link"] = None,
    ):

        self.resourceType = "Patient"

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
        self.name = name or []
        self.telecom = telecom or []
        self.gender = gender
        self.birthDate = birthDate
        self.deceasedBoolean = deceasedBoolean
        self.deceasedDateTime = deceasedDateTime
        self.address = address or []
        self.maritalStatus = maritalStatus
        self.multipleBirthBoolean = multipleBirthBoolean
        self.multipleBirthInteger = multipleBirthInteger
        self.photo = photo or []
        self.contact = contact or []
        self.communication = communication or []
        self.generalPractitioner = generalPractitioner or []
        self.managingOrganization = managingOrganization
        self.link = link or []

    @classmethod
    def from_dict(cls, data: dict) -> "Patient":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Patient":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
