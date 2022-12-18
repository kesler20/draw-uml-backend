from typing import Protocol, List, Iterable, Tuple, Any, Optional, Union, TypedDict, Dict


class ResponseDataParams(TypedDict):
    name: str
    type: str


class ResponseMethodRepresentation(TypedDict):
    visibility: str
    signature: str
    returnType: str
    comment: str
    params: List[ResponseDataParams]


class MethodRepresentation(TypedDict):
    signature: str
    params: List[List[str]]
    decorator: str
    return_type: str
    description: str


class ClassRepresentation(TypedDict):
    class_name: str
    description: str
    methods: List[Union[MethodRepresentation, ResponseMethodRepresentation]]
    fields: List[List[str]]
    properties: List[List[str]]


class DataFrameLocator(Protocol):
    loc: Union[List[List[Any]], List[Any]]

    def __getitem__(self, other: Any, another: Any = None):
        ...

    def __setitem__(self, item: Any, anotherItem: Any = None) -> Any:
        ...


class ResponseDataParamPosition(TypedDict):
    x: int
    y: int


class ResponseDataParamsMetadata(TypedDict):
    visibility: str
    signature: str
    returnType: str
    comment: str
    params: List[ResponseDataParams]


class CreateClassResponseData(TypedDict):
    objectName: str
    color: str
    comment: str
    gridTable: List[ResponseDataParamsMetadata]
    connection: bool


class CreateClassResponse(TypedDict):
    id: str
    type: str
    position: ResponseDataParamPosition
    data: CreateClassResponseData
    width: int
    height: int
    selected: bool
    positionAbsolute: ResponseDataParamPosition
    dragging: bool
