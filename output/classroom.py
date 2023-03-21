
from typing import List, Any, Union, Dict, Optional, Tuple
from output._types import *
        
class ClassRoom(object):
    """ClassRoom is 
    This refers to the class room with all the students
    
    
    Example
    -------
    
    ```python
    classroom = ClassRoom()
    
    ```        
        
    """
    
    def __init__(self, subect : str) -> None:
        self.subect = subect