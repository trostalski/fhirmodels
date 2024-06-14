# FHIRmodels

## Overview

**FHIRmodels** is a straightforward Python package designed for working with [FHIR](https://hl7.org/fhir/) data as Python objects. It offers a less strict approach compared to similar packages, such as [fhir.resources](https://github.com/nazrulworld/fhir.resources), and does not include validation functionality.

## Installation

To install FHIRmodels, use pip:

```bash
pip install fhirmodels
```

## Usage

### Creating a Patient

You can create a `Patient` object with the following example:

```python
from fhirmodels.R4 import Patient, HumanName, ContactPoint

patient = Patient(
    id="123",
    birthDate="2020-01-01",
    gender="male",
    active=True,
    name=[HumanName(family="Doe", given=["John"])],
    telecom=[ContactPoint(system="phone", value="1234567890")]
)

print(patient.as_dict())
```

### Creating from dictionary

You can create a FHIR object using a dictionary and the `from_dict` method:

```python
from fhirmodels.R4 import Condition

sample_condition = {
    "resourceType": "Condition",
    "id": "example",
    "identifier": [{"system": "http://example.org", "value": "12345"}],
    "clinicalStatus": {
        "coding": [
            {
                "system": "http://terminology.hl7.org/CodeSystem/condition-clinical",
                "code": "active",
            }
        ]
    },
    "code": {
        "coding": [
            {
                "system": "http://snomed.info/sct",
                "code": "386661006",
                "display": "Fever",
            }
        ]
    },
}

condition = Condition.from_dict(sample_condition)

print(condition.as_dict())
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request on GitHub.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
