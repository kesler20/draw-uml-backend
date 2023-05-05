
from typing import TypedDict, List, Any, Union, Dict, Tuple, Optional, Protocol
            
            
class Person(Protocol):   
        
    def get_full_name(self, last_name : str) -> str:
        ...
          