"""
Generated class for Signature. 
Time: 2024-07-22 14:02:49
"""

from fhirmodels.R4.Coding import *
from fhirmodels.R4.Extension import *
from fhirmodels.R4.Reference import *
from fhirmodels.fhir_base_model import FhirBaseModel


class Signature(FhirBaseModel):
    """Base StructureDefinition for Signature Type: A signature along with supporting context. The signature may be a digital signature that is cryptographic in nature, or some other signature acceptable to the domain. This other signature may be as simple as a graphical image representing a hand-written signature, or a signature ceremony Different signature approaches have different utilities.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Coding type: Indication of the reason the entity signed the object(s)
    :param str when: When the signature was created
    :param Reference who: Who signed
    :param Reference onBehalfOf: The party represented
    :param str targetFormat: The technical format of the signed resources
    :param str sigFormat: The technical format of the signature
    :param str data: The actual signature content (XML DigSig. JWS, picture, etc.)
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "type": {"class_name": "Coding", "is_contained": False},
        "who": {"class_name": "Reference", "is_contained": False},
        "onBehalfOf": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        type: list["Coding"] = None,
        when: "str" = None,
        who: "Reference" = None,
        onBehalfOf: "Reference" = None,
        targetFormat: "str" = None,
        sigFormat: "str" = None,
        data: "str" = None,
    ):

        self.id = id
        self.extension = extension or []
        self.type = type or []
        self.when = when
        self.who = who
        self.onBehalfOf = onBehalfOf
        self.targetFormat = targetFormat
        self.sigFormat = sigFormat
        self.data = data

    @classmethod
    def from_dict(cls, data: dict) -> "Signature":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Signature":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
