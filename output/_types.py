
from typing import TypedDict, List, Any, Union, Dict, Tuple, Optional, Protocol
            

class int = 99(Protocol):
    ...
            

class type(Protocol):
    ...
            
            
class Computer(Protocol):   
        
    def execute(self, name : type) -> str:
        ...
          
    def foo(self, name : type) -> list:
        ...
          