
from typing import TypedDict, List, Any, Union, Dict, Tuple, Optional, Protocol
            

class (Protocol):
    ...
            

class Path(Protocol):
    ...
            

class  Path(Protocol):
    ...
            
            
class CodeReader(ABC)(Protocol):   
        
    def source_code_path(self) -> Path:
        ...
          
    def response_code_path(self) -> Path:
        ...
          
    def set_response_code_path(self, path : str) -> :
        ...
          
    def set_source_code_path(self, path : str) -> :
        ...
          
    def read(self) -> None:
        ...
          
            
class Controller(Protocol):   
        
    def activate(self, control_value : int) -> bool:
        ...
          