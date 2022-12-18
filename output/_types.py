
from typing import TypedDict, List, Any, Union, Dict, Tuple, Optional, Protocol
            

class CompletedFile(TypedDict):
    coon: str

class Compelted(TypedDict):
    this: int

class Val(Protocol):
    ...
            
            
class ManagerCoordinator(Protocol):   
        
    def run(self, message : str) -> str:
        ...
          