
from typing import List, Any, Union, Dict, Optional, Tuple
from dataclasses import dataclass
    
class OperatingSystemInterface(object):
    """OperatingSystemInterface is a class"""
    
    
    def __init__(self) -> None:
        """__init__ has the following params
        """
        ...        
                  
    
    def __enter__(self) -> os:
        """__enter__ has the following params
        """
        ...        
                  
    
    def __exit__(self) -> os:
        """__exit__ has the following params
        """
        ...        
                  
    
    def gcu(self) -> str:
        """gcu has the following params
        """
        ...        
                  
    
    def copy_file_from_folder(self, file : str, source_folder : str="jaguar") -> None:
        """copy_file_from_folder has the following params
        
        Parameters
        ----------
            
        file str
            to be passed as parameter 2
        source_folder str="jaguar"
            to be passed as parameter 3
        
        Returns
        -------
        None
        """
        ...
                          
    
    def move_folder_resources(self, destination_path : str) -> None:
        """move_folder_resources has the following params
        
        Parameters
        ----------
            
        destination_path str
            to be passed as parameter 2
        
        Returns
        -------
        None
        """
        ...
                          
    
    def read_word_in_directory(self, word : str) -> 'list[str]':
        """read_word_in_directory has the following params
        
        Parameters
        ----------
            
        word str
            to be passed as parameter 2
        
        Returns
        -------
        'list[str]'
        """
        ...
                          