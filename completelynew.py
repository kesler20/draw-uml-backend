
from typing import List, Any, Union, Dict, Optional, Tuple
from dataclasses import dataclass
from output._types import type
        
@dataclass
class CompletelyNew:
    """CompletelyNew is a class"""
    
    another : int
    smae_one : int
    __this_funct() : str
    
    @property
    def this_funct()(self):
        """this_funct() property getter"""
        return self.__this_funct()
                
    def set_this_funct()(self,this_funct() : str):
        """this_funct() property setter"""
        self.__this_funct() = this_funct()
            
    
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
                      