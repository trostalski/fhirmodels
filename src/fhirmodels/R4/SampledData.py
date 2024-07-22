"""
Generated class for SampledData. 
Time: 2024-07-22 14:02:49
"""

from fhirmodels.R4.Quantity import *
from fhirmodels.R4.Extension import *
from fhirmodels.fhir_base_model import FhirBaseModel


class SampledData(FhirBaseModel):
    """Base StructureDefinition for SampledData Type: A series of measurements taken by a device, with upper and lower limits. There may be more than one dimension in the data.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Quantity origin: Zero value and units
    :param float period: Number of milliseconds between samples
    :param float factor: Multiply data by this before adding to origin
    :param float lowerLimit: Lower limit of detection
    :param float upperLimit: Upper limit of detection
    :param int dimensions: Number of sample points at each time point
    :param str data: Decimal values with spaces, or "E" | "U" | "L"
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "origin": {"class_name": "Quantity", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        origin: "Quantity" = None,
        period: "float" = None,
        factor: "float" = None,
        lowerLimit: "float" = None,
        upperLimit: "float" = None,
        dimensions: "int" = None,
        data: "str" = None,
    ):

        self.id = id
        self.extension = extension or []
        self.origin = origin
        self.period = period
        self.factor = factor
        self.lowerLimit = lowerLimit
        self.upperLimit = upperLimit
        self.dimensions = dimensions
        self.data = data

    @classmethod
    def from_dict(cls, data: dict) -> "SampledData":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "SampledData":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
