
from typing import TypedDict, List, Any, Union, Dict, Tuple, Optional, Protocol
            
            
class DatabaseInterface(Protocol):   
        
    def create(self, body : dict) -> dict:
        ...
          
    def read(self, name : str) -> dict:
        ...
          
    def update(self, name : str) -> dict:
        ...
          
    def delete(self, name : str) -> dict:
        ...
          