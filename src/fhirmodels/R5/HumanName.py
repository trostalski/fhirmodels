"""
Generated class for HumanName. 
Time: 2024-06-14 18:56:04
"""

from fhirmodels.fhir_base_model import FhirBaseModel
from fhirmodels.R5.Extension import *
from fhirmodels.R5.Period import *


class HumanName(FhirBaseModel):
    """HumanName Type: A name, normally of a human, that can be used for other living entities (e.g. animals but not organizations) that have been assigned names by a human and may need the use of name parts or the need for usage information.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param str use: usual | official | temp | nickname | anonymous | old | maiden
    :param str text: Text representation of the full name
    :param str family: Family name (often called 'Surname')
    :param str given: Given names (not always 'first'). Includes middle names
    :param str prefix: Parts that come before the name
    :param str suffix: Parts that come after the name
    :param Period period: Time period when name was/is in use
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
        use: "str" = None,
        text: "str" = None,
        family: "str" = None,
        given: list["str"] = None,
        prefix: list["str"] = None,
        suffix: list["str"] = None,
        period: "Period" = None,
    ):

        self.id = id
        self.extension = extension or []
        self.use = use
        self.text = text
        self.family = family
        self.given = given or []
        self.prefix = prefix or []
        self.suffix = suffix or []
        self.period = period

    @classmethod
    def from_dict(cls, data: dict) -> "HumanName":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "HumanName":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
