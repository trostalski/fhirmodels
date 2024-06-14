"""
Generated class for Distance. 
Time: 2024-06-14 18:56:04
"""
from fhirmodels.fhir_base_model import FhirBaseModel
from fhirmodels.R5.Extension import *


class Distance(FhirBaseModel):
    """ Distance Type: A length - a value with a unit that is a physical distance.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param float value: Numerical value (with implicit precision)
    :param str comparator: < | <= | >= | > | ad - how to understand the value
    :param str unit: Unit representation
    :param str system: System that defines coded unit form
    :param str code: Coded form of the unit
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        
        
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  value:  'float'  = None,  comparator:  'str'  = None,  unit:  'str'  = None,  system:  'str'  = None,  code:  'str'  = None, ):
        
        self.id = id 
        self.extension = extension or []
        self.value = value 
        self.comparator = comparator 
        self.unit = unit 
        self.system = system 
        self.code = code 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Distance":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Distance":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()