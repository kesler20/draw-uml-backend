from draw_uml_backend._types import ClassRepresentation
import json
from typing import Any, Dict, List, Union
import os
from pathlib import Path

class File(object):
    '''Object Description'''

    def __init__(self, filename: Path) -> None:
        self.filename = filename.as_posix()

    def read(self) -> str:
        '''signature description'''
        with open(self.filename, "r") as file:
            content = file.read()
        return content

    def append(self, content: str) -> None:
        """Append to a file"""
        with open(self.filename, "a") as file:
            file.write(content)

    def write(self, content: str) -> None:
        '''signature description'''
        with open(self.filename, "w") as file:
            file.write(content)

    def readlines(self) -> 'list[str]':
        '''signature description'''
        with open(self.filename, "r") as file:
            content = file.readlines()
        return content

    def get_json(self) -> Any:
        """get a json file as a dictionary"""
        with open(self.filename, "r") as json_file:
            content = json.loads(json_file.read())
        return content
    
    def write_json(self, content: Union[Dict[str, Any],List[ClassRepresentation]]) -> None:
        """get a json file as a dictionary
        
        Param
        ---
        content dict
          dictionary which is dumped to the given json file"""
        
        with open(self.filename, "w") as json_file:
            json_file.write(json.dumps(content,indent=2))

    def writeline(self, content: str) -> None:
        '''signature description'''
        with open(self.filename, "w") as file:
            file.write(f"{content}\n")

    def read_line_by_condition(self, condition) -> 'list[str]':
        '''
        condition should be a function which is applied
        to filter through the list of the lines of the file   
        '''
        with open(self.filename, "w") as file:
            content = file.readlines()

        return list(filter(condition, content))

    def delete(self) -> None:
        '''signature description'''
        os.remove(self.filename)
