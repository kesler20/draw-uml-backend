
from typing import List, Any, Union, Dict, Optional, Tuple
from dataclasses import dataclass
from output._types import type
        
@dataclass
class ComandManager:
    """ComandManager is a class"""
    
    another_property : int
    __testing_it : int
    
    @property
    def testing_it(self):
        """testing_it property getter"""
        return self.__testing_it
                
    def set_testing_it(self,testing_it : int):
        """testing_it property setter"""
        self.__testing_it = testing_it
            
    
    def execute(self, name : type) -> None:
        """execute signature description
        
        Parameters
        ---
            
        name type
            to be passed as parameter 1
        
        Returns
        ---
        result: None
        """
        ...
                          
    
    def get_data(self, p : str, vv : int) -> list:
        """get_data The new data of the mangeer
        
        Parameters
        ---
            
        p str
            to be passed as parameter 1
        vv int
            to be passed as parameter 2
        
        Returns
        ---
        result: list
        """
        ...
                          
    
    def __run(self, name : type) -> None:
        """__run signature description
        
        Parameters
        ---
            
        name type
            to be passed as parameter 1
        
        Returns
        ---
        result: None
        """
        ...
                          