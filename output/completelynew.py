
from typing import List, Any, Union, Dict, Optional, Tuple
from dataclasses import dataclass
from output._types import type, list
        
@dataclass
class CompletelyNew:
    """CompletelyNew is a class"""
    
    another : int
    smae_one : int
    __new_field : list = ["Val"]
    
    @property
    def new_field(self):
        """new_field property getter"""
        return self.__new_field
                
    def set_new_field(self,new_field : list):
        """new_field property setter"""
        self.__new_field = new_field
            
    
    def this_funct(self, name : type) -> str:
        """this_funct signature description
        
        Parameters
        ---
                
        name type
            to be passed as parameter 1
                    
        Returns
        ---
        result: str
        """
        ...
                      