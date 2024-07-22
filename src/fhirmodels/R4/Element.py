"""
Generated class for Element. 
Time: 2024-07-22 14:02:49
"""

from fhirmodels.R4.Extension import *
from fhirmodels.fhir_base_model import FhirBaseModel


class Element(FhirBaseModel):
    """Base StructureDefinition for Element Type: Base definition for all elements in a resource.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
    ):

        self.id = id
        self.extension = extension or []

    @classmethod
    def from_dict(cls, data: dict) -> "Element":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Element":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
