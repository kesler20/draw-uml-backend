
from typing import TypedDict, List, Any, Union, Dict, Tuple, Optional, Protocol
            

class type(Protocol):
    ...
            
            
class ComandManager(Protocol):   
        
    def execute(self, name : type) -> None:
        ...
          
    def get_data(self, vv : int) -> list:
        ...
          
    def __run(self, name : type) -> None:
        ...
          