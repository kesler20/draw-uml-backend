
from typing import TypedDict, List, Any, Union, Dict, Tuple, Optional, Protocol
            
            
class Controller(Protocol):   
        
    def activate(self, control_value : int) -> bool:
        ...
          