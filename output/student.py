
from typing import List, Any, Union, Dict, Optional, Tuple
from dataclasses import dataclass, field
from output._types import ClassRoom
        
@dataclass
class Student:
    """Student is
    Object Description
    
    
    Example
    -------
    
    ```python
    student = Student()
    
    ```        
        
    """
    
    name : str
    age : int
    class_room : ClassRoom