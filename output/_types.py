
from typing import TypedDict, List, Any, Union, Dict, Tuple, Optional, Protocol
            

class ClassRoom(Protocol):
    ...
            

class Student(TypedDict):
    name: str
    age: int
    class_room: ClassRoom

class ClassRoom(TypedDict):
    subect: str