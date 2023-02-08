from typing import List, Any, Union, Dict, Optional, Tuple, Callable, Collection
import json
import os
from pathlib import Path

class File:
    
    def __init__(self, filename : Path) -> None:
        """The class has the following properties

        Parameters
        ---

        filename Path
            to be passed as parameter 2
        
        Returns
        ---
        result: None
        """
        self.filename = filename.as_posix()
                          
    def read(self) -> str:
        """read has the following params
        """
        with open(self.filename, "r") as file:
            content = file.read()
        return content        
                     
    def append(self, content : str) -> None:
        """append has the following params
        
        Parameters
        ---
            
        content str
            to be passed as parameter 2
        
        Returns
        ---
        result: None
        """
        with open(self.filename, "a") as file:
            file.write(content + "\n")
                    
    def write(self, content : str) -> None:
        """write has the following params
        
        Parameters
        ---
            
        content str
            to be passed as parameter 2
        
        Returns
        ---
        result: None
        """
        with open(self.filename, "w") as file:
            file.write(content)
                        
    def readlines(self) -> 'list[str]':
        """readlines has the following params
        """
        with open(self.filename, "r") as file:
            content = file.readlines()
        return content        
                     
    def get_json(self) -> Any:
        """get_json has the following params
        """
        with open(self.filename, "r") as json_file:
            content = json.loads(json_file.read())
        return content       
                  
    def write_json(self, content: Union[Dict[str, Any], List[Any]]) -> None:
        """write_json has the following params
        
        Parameters
        ---
            
        content Union[Dict[str,Any]
            to be passed as parameter 2
        
        Returns
        ---
        result: None
        """
        with open(self.filename, "w") as json_file:
            json_file.write(json.dumps(content, indent=2))
                            
    def writeline(self, content : str) -> None:
        """writeline has the following params
        
        Parameters
        ---
            
        content str
            to be passed as parameter 2
        
        Returns
        ---
        result: None
        """
        with open(self.filename, "w") as file:
            file.write(f"{content}\n")
                          
    def read_line_by_condition(self, condition: Callable[[Any], Collection[Any]]) -> List[str]:
        """read_line_by_condition has the following params
        
        Parameters
        ---

        condition : str
            condition should be a function which is applied
            to filter through the list of the lines of the file
        
        Returns
        ---
        Result : list[str]
        """
        with open(self.filename, "r") as file:
            content: List[str] = file.readlines()

        return list(filter(condition, content))       
    
    def delete(self) -> None:
        """delete has the following params
        """
        os.remove(self.filename)        
                  