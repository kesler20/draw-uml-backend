
from typing import TypedDict, List, Any, Union, Dict, Tuple, Optional, Protocol
import os

class ReactApplication(Protocol):   
        
    def __init__(self) -> None:
        ...
          
    def initialise_env_file(self, *args : Tuple[Any]) -> None:
        ...
          
    def initialise_npm_process(self, *args : Tuple[Any]) -> None:
        ...

class Path(Protocol):
    ...
            
class AmplifyApplication(Protocol):   
        
    def __init__(self) -> None:
        ...
          
    def update_amplify_application(self) -> None:
        ...
          
    def modify_amplify_application(self) -> None:
        ...
          
    def initialize_amplify_application(self) -> None:
        ...
          
    def push_to_amplify(self) -> None:
        ...
          
class OperatingSystemInterface(Protocol):   
        
    def __init__(self) -> None:
        ...
          
    def __enter__(self) -> os:
        ...
          
    def __exit__(self) -> os:
        ...
          
    def gcu(self) -> str:
        ...
          
    def copy_file_from_folder(self, file) -> None:
        ...
          
    def move_folder_resources(self, destination_path : str) -> None:
        ...
          
    def read_word_in_directory(self, word : str) -> 'list[str]':
        ...
        
           
class File(Protocol):   
        
    def __init__(self, filename : Path) -> None:
        ...
          
    def read(self) -> str:
        ...
          
    def append(self, content : str) -> None:
        ...
          
    def write(self, content : str) -> None:
        ...
          
    def readlines(self) -> 'list[str]':
        ...
          
    def get_json(self) -> Any:
        ...
          
    def write_json(self, content: Union[Dict[str, Any], List[Any]]) -> None:
        ...
          
    def writeline(self, content : str) -> None:
        ...
          
    def read_line_by_condition(self) -> 'list[str]':
        ...
          
    def delete(self) -> None:
        ...
        
class GithubRepository(Protocol):   
        
    def test_and_push_to_github(self) -> None:
        ...
          
    def push_to_github(self) -> None:
        ...
          
    def push_new_repo_to_github(self) -> None:
        ...
          
    def push_new_branch_to_github(self) -> None:
        ...
          
    def style_commit_message(self, commit_message : str) -> str:
        ...
          