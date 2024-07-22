"""
Generated class for Reference. 
Time: 2024-07-22 14:02:49
"""

from fhirmodels.R4.Identifier import *
from fhirmodels.R4.Extension import *
from fhirmodels.fhir_base_model import FhirBaseModel


class Reference(FhirBaseModel):
    """Base StructureDefinition for Reference Type: A reference from one resource to another.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param str reference: Literal reference, Relative, internal or absolute URL
    :param str type: Type the reference refers to (e.g. "Patient")
    :param Identifier identifier: Logical reference, when literal reference is not known
    :param str display: Text alternative for the resource
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        reference: "str" = None,
        type: "str" = None,
        identifier: "Identifier" = None,
        display: "str" = None,
    ):

        self.id = id
        self.extension = extension or []
        self.reference = reference
        self.type = type
        self.identifier = identifier
        self.display = display

    @classmethod
    def from_dict(cls, data: dict) -> "Reference":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Reference":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
