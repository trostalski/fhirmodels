"""
Generated class for Coding. 
Time: 2024-07-22 14:02:49
"""

from fhirmodels.R4.Extension import *
from fhirmodels.fhir_base_model import FhirBaseModel


class Coding(FhirBaseModel):
    """Base StructureDefinition for Coding Type: A reference to a code defined by a terminology system.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param str system: Identity of the terminology system
    :param str version: Version of the system - if relevant
    :param str code: Symbol in syntax defined by the system
    :param str display: Representation defined by the system
    :param bool userSelected: If this coding was chosen directly by the user
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        system: "str" = None,
        version: "str" = None,
        code: "str" = None,
        display: "str" = None,
        userSelected: "bool" = None,
    ):

        self.id = id
        self.extension = extension or []
        self.system = system
        self.version = version
        self.code = code
        self.display = display
        self.userSelected = userSelected

    @classmethod
    def from_dict(cls, data: dict) -> "Coding":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Coding":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
