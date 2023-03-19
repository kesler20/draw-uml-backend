
from typing import List, Any, Union, Dict, Optional, Tuple
from dataclasses import dataclass, field
from output._types import int, type
        
@dataclass
class Computer:
    """Computer is a class"""
    
    memory : int
    run : List[str] = field(init=False, default_factory=lambda : ["Helloworld"])
    __foll : int = field(init=False, default=99)
    
    @property
    def foll(self):
        """foll property getter"""
        return self.__foll
                
    def set_foll(self,foll : int):
        """foll property setter"""
        self.__foll = foll
            
    
    def execute(self, name : type) -> str:
        """execute signature description
        
        Parameters
        ----------
            
        name : type
            to be passed as parameter 1
        
        Returns
        -------
        str
        """
        ...
                          
    
    def foo(self, name : type) -> list:
        """foo signature description
        
        Parameters
        ----------
            
        name : type
            to be passed as parameter 1
        
        Returns
        -------
        list
        """
        ...
                          