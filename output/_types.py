
from typing import TypedDict, List, Any, Union, Dict, Tuple, Optional, Protocol
            

class type(Protocol):
    ...
            
            
class Commander(Protocol):   
        
    def run(self, name : type) -> int:
        ...
          
    def execute(self, n : int) -> list:
        ...
          