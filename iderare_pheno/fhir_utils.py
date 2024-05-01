from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel
from typing import List, Union

app = FastAPI()

class Coding(BaseModel):
    system: str
    code: str

class CodeableConcept(BaseModel):
    coding: List[Coding]

class Observation(BaseModel):
    resourceType: str = "Observation"
    code: CodeableConcept
    interpretation: List[CodeableConcept]

class Condition(BaseModel):
    resourceType: str = "Condition"
    code: CodeableConcept

class OtherResource(BaseModel):
    resourceType: str

class BundleEntry(BaseModel):
    resource: Union[Observation, Condition, OtherResource]

class Bundle(BaseModel):
    resourceType: str = "Bundle"
    entry: List[BundleEntry]

class TermCode(BaseModel):
    system: str
    code: str

allowable_resource_list = ["Observation", "Condition"]
prefix_dict = {
    "http://loinc.org": "LOINC",
    "http://snomed.info/sct": "SNOMEDCT",
    "http://hl7.org/fhir/sid/icd-10" : "ICD-10",
    "http://human-phenotype-ontology.org" : "HP",
    "http://www.omim.org" : "OMIM",
    "http://www.orpha.net" : "ORPHA"

}

def resource_object(resource, resource_type, index=None):
    try:
        if resource_type == "Observation":
            code_coding = resource.code.coding[0]
            if prefix_dict[code_coding.system] == "LOINC":
                if hasattr(resource, 'interpretation') and resource.interpretation:
                    interpretation_coding = resource.interpretation[0].coding[0]
                    return prefix_dict[code_coding.system] + ':' + code_coding.code + '|' + interpretation_coding.code
                else:
                    if index is not None:
                        return f"Observation : Bundle.entry[{index}].resource.interpretation not existed."
                    else : 
                        raise HTTPException(status_code=400, detail=f"No {resource_type}.interpretation existed in the resource.")
            else:
                return prefix_dict[code_coding.system] + ':' + code_coding.code
        elif resource_type == "Condition":
            code_coding = resource.code.coding[0]
            return prefix_dict[code_coding.system] + ':' + code_coding.code
        else:
            raise HTTPException(status_code=400, detail=f"Unsupported FHIR resource type: {resource_type}")
    except IndexError:
        raise HTTPException(status_code=400, detail=f"Missing required fields in FHIR resource type: {resource_type}")
    
    # return TermCode(system=code_coding.system, code=code_coding.code)

@app.post("/fhir/parse/bundle")
async def fhir_batch_parse(bundle: Bundle) -> Response:
    prefixes = prefix_dict.values()
    term_codes = []
    i = -1
    for entry in bundle.entry:
        i += 1
        resource_type = entry.resource.resourceType
        if resource_type in allowable_resource_list:
            term_codes.append(resource_object(entry.resource, resource_type, i))
        else:
            continue
    result = [x for x in term_codes if x.split(':')[0] in prefixes]
    error = [x for x in term_codes if x.split(':')[0] not in prefixes]
    return {"result" : result, "error" : error}

@app.post("/fhir/parse/resource")
async def fhir_parse(resource: Union[Observation, Condition]) -> Response:
    return {"result" : resource_object(resource, resource.resourceType)}