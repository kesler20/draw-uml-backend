
from typing import List, Any, Union, Dict, Optional, Tuple
from dataclasses import dataclass, field
from output._types import ,  Path, Path
        
@dataclass
class CodeReader(ABC):
    """CodeReader(ABC) is
    
    
    
    Example
    -------
    
    ```python
    codereader(abc) = CodeReader(ABC)()
    
    codereader(abc).source_code_path()
                
    codereader(abc).response_code_path()
                
    codereader(abc).set_response_code_path(path)
                
    codereader(abc).set_source_code_path(path)
                
    codereader(abc).read()
                
    ```        
        
    """
    
    # field description
    __source_code_path :  Path = field(init=False, default=)
    # field description
    __response_code_path :  Path = field(init=False, default=)
    
    @property
    def source_code_path(self):
        """source_code_path property getter"""
        return self.__source_code_path
            
    
    @property
    def response_code_path(self):
        """response_code_path property getter"""
        return self.__response_code_path
                
    def set_source_code_path(self,source_code_path : Path):
        """source_code_path property setter"""
        self.__source_code_path = source_code_path
                
    def set_response_code_path(self,response_code_path : Path):
        """response_code_path property setter"""
        self.__response_code_path = response_code_path
            
    @abstractmethod
    def source_code_path(self) -> Path:
        """source_code_path has the following params
        """
        ...        
                  
    @abstractmethod
    def response_code_path(self) -> Path:
        """response_code_path has the following params
        """
        ...        
                  
    @abstractmethod
    def set_response_code_path(self, path : str) -> :
        """set_response_code_path has the following params
        
        Parameters
        ----------
            
        path : str
            path is a str to be passed as 2 param
        
        Returns
        -------
        
            path is a str to be passed as 2 param
        """
        ...
                          
    @abstractmethod
    def set_source_code_path(self, path : str) -> :
        """set_source_code_path has the following params
        
        Parameters
        ----------
            
        path : str
            path is a str to be passed as 2 param
        
        Returns
        -------
        
            path is a str to be passed as 2 param
        """
        ...
                          
    @abstractmethod
    def read(self) -> None:
        """read has the following params
        """
        ...        
                  