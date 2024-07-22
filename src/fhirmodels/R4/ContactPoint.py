"""
Generated class for ContactPoint. 
Time: 2024-07-22 14:02:49
"""

from fhirmodels.R4.Period import *
from fhirmodels.R4.Extension import *
from fhirmodels.fhir_base_model import FhirBaseModel


class ContactPoint(FhirBaseModel):
    """Base StructureDefinition for ContactPoint Type: Details for all kinds of technology mediated contact points for a person or organization, including telephone, email, etc.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param str system: phone | fax | email | pager | url | sms | other
    :param str value: The actual contact point details
    :param str use: home | work | temp | old | mobile - purpose of this contact point
    :param int rank: Specify preferred order of use (1 = highest)
    :param Period period: Time period when the contact point was/is in use
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "period": {"class_name": "Period", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        system: "str" = None,
        value: "str" = None,
        use: "str" = None,
        rank: "int" = None,
        period: "Period" = None,
    ):

        self.id = id
        self.extension = extension or []
        self.system = system
        self.value = value
        self.use = use
        self.rank = rank
        self.period = period

    @classmethod
    def from_dict(cls, data: dict) -> "ContactPoint":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ContactPoint":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
