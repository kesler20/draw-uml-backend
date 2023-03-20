
from typing import List, Any, Union, Dict, Optional, Tuple
from dataclasses import dataclass, field
from output._types import *
        
@dataclass
class ClassRoom:
    """ClassRoom is
    This refers to the class room with all the students
    
    
    Example
    -------
    
    ```python
    classroom = ClassRoom()
    
    ```        
        
    """
    
    subect : str