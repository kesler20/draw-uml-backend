
from typing import List, Any, Union, Dict, Optional, Tuple
from dataclasses import dataclass, field
from output._types import *
        
@dataclass
class Controller:
    """Controller is
    This is an interface with the PID controller hardware
    
    
    Example
    -------
    
    ```python
    controller = Controller()
    
    controller.activate(control_value)
                
    ```        
        
    """
    
    # the status of the controller
    status : int
    
    def activate(self, control_value : int) -> bool:
        """activate control the process given a target set point
        
        Parameters
        ----------
            
        control_value : int
            the set point of the control we want to perform
        
        Returns
        -------
        bool
            boolean representing whether the control was performed successfully
        """
        ...
                          