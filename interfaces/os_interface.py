from src.draw_uml_backend._types import ClassRepresentation
import platform
import json
from typing import Any, Dict, List, Union
import os
from pathlib import Path
import shutil

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


class OperatingSystemInterface(object):
    '''
    you can access the interface like a resource manager such as
    ```python
    with OperatingSystemInterface(directory) as osi:
        osi.do_something()
    # alternatively if there are multiple calls that you want to make you can use
    osi = OperatingSystemInterface()
    with osi as oi:
        oi.system("echo hello world")
    ```
    '''

    def __init__(self, directory=os.getcwd()) -> None:
        self.directory: str = directory

    def __enter__(self) -> Any:
        '''signature description'''
        os.chdir(self.directory)
        return os

    def __exit__(self, *args) -> Any:
        '''signature description'''
        os.chdir(os.getcwd())

    def gcu(self) -> str:
        '''Get the current user i.e. C:/Users/CBE-User 05'''
        if platform.system() == "Linux":
            root_path = os.path.join(*os.path.dirname(
                __file__).split("/")[:5])
        else:
            root_path = os.path.join(*os.path.dirname(
                __file__).split(r"\ ".replace(" ", ""))[:3])

        root_path = root_path.replace(":", r":\ ".replace(" ", ""))
        print(root_path)
        return root_path

    def copy_file_from_folder(self, file, source_folder="jaguar") -> None:
        '''
        The folder that you are currently working on will be used as destination file
        The source folder will be searched in the protocol folder and is jaguar by default
        the file which will be replace in the local directory has path ``os.path.join(self.directory,file)``
        '''

        source = os.path.join(
            r"C:\Users\Uchek\protocol", source_folder, file)
        destination = os.path.join(self.directory, file)

        print(r'''
        copying {}
        ---> into
        {}
        '''.format(source, destination))
        print(os.getcwd())
        shutil.copy(source, destination)

    def move_folder_resources(self, destination_path: str) -> None:
        '''the directory passed as a property will be used as a source path'''
        for resource in os.listdir(self.directory):
            destination_dir = os.path.join(destination_path, resource)
            source_dir = os.path.join(self.directory, resource)
            os.rename(source_dir, destination_dir)

    def read_word_in_directory(self, word: str) -> List[str]:
        '''signature description'''
        result = []
        for root, directories, files in os.walk(self.directory):
            for file in files:
                print(file)
                with open(file) as f:
                    content = f.read()
                    if content.find(word) != -1:
                        result.append(file)

        return result
