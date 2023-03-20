
from typing import List, Any, Union, Dict, Optional, Tuple
from output._types import type
        
class Commander(object):
    """Commander is a class
    
    
    Example
    -------
    
    ```python
    commander = Commander()
    
    commander.run(name)
                
    commander.execute(n)
                
    ```        
        
    """
    
    def __init__(self, command : list[str] = ["first command"], void : int) -> None:
        self.command = command
        self.void = void
    
    def run(self, name : type) -> int:
        """run signature description
        
        Parameters
        ----------
            
        name : type
            to be passed as parameter 1
        
        Returns
        -------
        int
        """
        ...
                          
    
    def execute(self, n : int) -> list:
        """execute this will execute the algoritghm
        
        Parameters
        ----------
            
        n : int
            to be passed as parameter 1
        
        Returns
        -------
        list
        """
        ...
                          