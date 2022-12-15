from typing import List, TypedDict

class MethodRepresentation(TypedDict):
    signature: str
    params: List[List[str]]
    decorator: str
    return_type: str

class ClassRepresentation(TypedDict):
    class_name: str
    description: str
    methods : List[MethodRepresentation]
    fields: List[List[str]]
    properties: List[List[str]]