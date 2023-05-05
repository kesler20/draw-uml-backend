
from typing import List, Any, Union, Dict, Optional, Tuple
from output._types import *
        
class Person(object):
    """Person is 
    This should represent a person in real life
    
    
    Example
    -------
    
    ```python
    person = Person()
    
    person.get_full_name(last_name)
                
    ```        
        
    """
    
    def __init__(self, name : str, age : int) -> None:
        # signature description
        self.name = name
        # signature description
        self.age = age
    
    def get_full_name(self, last_name : str) -> str:
        """get_full_name return name and last name
        
        Parameters
        ----------
            
        last_name : str
            the family name of the person
        
        Returns
        -------
        str
            the full name of the person `<first name> <last name>`
        """
        ...
                          