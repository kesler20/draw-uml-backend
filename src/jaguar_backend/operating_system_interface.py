from pathlib import Path
from src.jaguar_backend.file import File
import re
from typing import List, Any, Union, Dict, Optional, Tuple
import os
import shutil
import sys
from src.jaguar_backend._base import WorkflowRepresentation


def _print(msg):
    print(f"\n {msg} \n")


class OperatingSystemInterface:
    """OperatingSystemInterface is a class
    you can access the interface like a resource manager such as

    ```python
    with OperatingSystemInterface(directory) as osi:
        osi.do_something()
    # alternatively if there are multiple calls that you want to make you can use
    osi = OperatingSystemInterface()
    with osi as oi:
        oi.system("echo hello world")
    ```
    """

    def __init__(self, directory=os.getcwd()) -> None:
        self.directory: str = directory
        self.workflow_ui = WorkflowRepresentation()

    def __enter__(self) -> os:
        '''signature description'''
        os.chdir(self.directory)
        return os

    def __exit__(self, *args) -> os:
        '''signature description'''
        os.chdir(os.getcwd())

    def gcf(self) -> str:
        """returns the current folder where the file is being run"""
        if sys.platform == "linux":
            return __file__.split("protocol")[1].split(r"/")[1]
        else:
            return __file__.split("protocol")[1].split(r"\ ".replace(" ", ""))[1]

    def gcu(self) -> str:
        """gcu has the following params"""
        '''Get the current user i.e. C:/Users/CBE-User 05'''
        return os.path.abspath(__file__).split(r"\protocol")[0]

    def create_a_virtualenvironment(self, venv: str):
        """create_a_virtualenvironment"""

        self.workflow_ui.pp(f"creatin a new virtual environment {venv} 🐍✨")
        _print(f"conda create -n {venv}")
        os.system(f"conda create -n {venv}")
        _print("make sure that you change the vscode virtual environment to the newly created one ❗❗❗")
        _print("make sure you have installed jaguar_backend by going to the jaguar_backend and activate the new environment, after run pip install -e . ❗❗❗")
        _print("if you have an existing requirements.txt and requirements_dev.txt file then run: 'python _dev.py setup-env <env-name>' ❗❗❗")
    
    def setup_venv(self, venv: str):
        _print(f"pip install -r requirements.txt")
        os.system(f"pip install -r requirements.txt")
        _print(f"pip install -r requirements_dev.txt")
        os.system(f"pip install -r requirements_dev.txt")

    def delete_virtualenvironment(self, venv: str):
        _print(venv)
        self.workflow_ui.pp(f"deleting the {venv} virtual environment ❌")
        _print(f"conda env remove --name {venv}")
        os.system(f"conda env remove --name {venv}")
        _print(f"conda env list")
        os.system(f"conda env list")

    def install_package(self, package: str):
        self.workflow_ui.pp(f"installing... {package} ⚙️")
        _print(f"pip install {package}")
        os.system(f"pip install {package}")
        _print(f"pip freeze > requirements.txt")
        os.system(f"pip freeze > requirements.txt")
        _print(f"conda list")
        os.system(f"conda list")
        _print(f"pip show {package}")
        os.system(f"pip show {package}")
        # update the pipfile and the setup.cfg files
        # get the version of the file
        package_version = list(filter(lambda line: line.find(package) != -1, File(Path("requirements.txt")).readlines())
                               )[0].replace(package, "").replace("\n", "")
        pip_file = [line.replace("\n", "") for line in File(Path("Pipfile")).readlines()]
        os.remove("Pipfile")
        for line in pip_file:
            File(Path("Pipfile")).append(line)
            if line.find("[packages]") != -1:
                self.workflow_ui.pp(f'added a new line to the Pipfile -> 👿 {package} = "{package_version.replace(">=","==")}"',)
                File(Path("Pipfile")).append(f'{package} = "{package_version.replace(">=","==")}"')

        setup_cfg = [line.replace("\n", "") for line in File(Path("setup.cfg")).readlines()]
        os.remove("setup.cfg")
        for line in setup_cfg:
            File(Path("setup.cfg")).append(line)
            if line.find("install_requires =") != -1:
                package_version = package_version.replace("==", ">=")
                self.workflow_ui.pp(f'added a new line to the setup.cfg -> ⚙️  {package}{package_version}',)
                File(Path("setup.cfg")).append(f'    {package}{package_version}')

    def copy_file_from_jaguar(self, file: str, source_folder: Optional[str] = "jaguar_backend") -> None:
        """The folder that you are currently working on will be used as destination file
        The source folder will be searched in the protocol folder and is jaguar_backend by default
        the file which will be replace in the local directory has path 
        ``os.path.join(self.directory,file)``

        Parameters
        ---

        file str
            the file that we want to move to the root directory from the source_folder
        source_folder : str
            the folder where the file will be searched, this is jaguar_backend by default

        Returns
        ---
        result: None
        """

        source = os.path.join(os.path.abspath(__file__).split(
            r"\{}".format(source_folder))[0], source_folder, file)
        destination = os.path.join(self.directory, file)

        _print(r'''
        copying {} 
        ---> into 
        {}
        '''.format(source, destination))
        _print(os.getcwd())
        shutil.copy(source, destination)

    def copy_folder_from_jaguar(self, folder: str, source_folder: Optional[str] = os.path.join("protocol", "jaguar_backend")) -> None:
        """The folder that you are currently working on will be used as destination folder
        The source folder will be searched in the protocol folder and is protocol by default
        the folder which will be replace in the local directory has path 
        ``os.path.join(self.directory,folder)``

        Parameters
        ---

        folder str
            the folder that we want to move to the root directory from the source_folder
        source_folder : str
            the folder where the folder will be searched, this is protocol by default

        Returns
        ---
        result: None
        """

        source = os.path.join(os.path.abspath(__file__).split(
            r"\{}".format(source_folder))[0], source_folder, folder)
        destination = os.path.join(self.directory, folder)

        _print(r'''
        copying {} 
        ---> into 
        {}
        '''.format(source, destination))
        _print(os.getcwd())
        try:
            shutil.copytree(source, destination)
        except FileExistsError as err:
            _print(err)
            _print("copying the folder again...⚙️")
            shutil.rmtree(destination)
            shutil.copytree(source, destination)

    def delete_folder(self, folder: str):
        root_dir = os.path.abspath(__file__.split("protocol")[0])
        folder = os.path.join(root_dir, "protocol", folder)
        _print("deleting the following folder 🗑️", folder)
        os.system(f"rmdir /S /Q {folder}")

    def copy_folder(self, source_folder: str, destination_folder: str = None) -> None:
        """copy_folder

        copy the folders found in the given paths
        the folder will be searched in the ``protocol`` folder

        Parameters
        ---
        source_folder : str
            the name of the folder we want to copy from
        destination_folder : str
            the name of the folder we want to copy to
        """
        destination = os.getcwd() if destination_folder is None else destination_folder
        root_dir = os.path.abspath(__file__.split("protocol")[0])
        shutil.copytree(
            os.path.join(root_dir, "protocol", source_folder),
            os.path.join(root_dir, "protocol", destination)
        )

    def copy_file(self, source_file: str, destination_file: str = None) -> None:
        """copy_file

        copy the files found in the given paths
        the file will be searched in the ``protocol`` file

        Parameters
        ---
        source_file : str
            the name of the file we want to copy from
        destination_file : str
            the name of the file we want to copy to
        """
        destination = os.getcwd() if destination_file is None else destination_file
        root_dir = os.path.abspath(__file__.split("protocol")[0])
        shutil.copy(
            os.path.join(root_dir, "protocol", source_file),
            os.path.join(root_dir, "protocol", destination)
        )

    def convert_javascript_files_to_typescript(self):
        """convert_javascript_files_to_typescript"""

        directory = os.path.join(os.getcwd(), "src")
        for root, directories, files in os.walk(directory):
            for file in files:
                file = os.path.join(root, file)
                if file.endswith(".js"):
                    os.rename(file, file.replace(".js", ".ts"))

    def initialise_typescript_environment(self):
        """initialise_typescript_environment"""

        self.workflow_ui.pp("install typescript as a development dependency 🌃⏬")
        os.system("npm i typescript --d")
        self.workflow_ui.pp("install the typescript compiler 🖨️🌃")
        os.system("npm i ts-node --d")
        os.system("npx tsc --init")

    def move_folder_resources(self, source_path: str, destination_path: str) -> None:
        """move_folder_resources 
        the directory passed as a property will be used as a source path

        Parameters
        ---

        destination_path str
            this is the folder where the files will be moved to
        source_path str
            this is the folder where the files will be moved from

        Returns
        ---
        result: None
        """
        for resource in os.listdir(source_path):
            destination_dir = os.path.join(destination_path, resource)
            source_dir = os.path.join(source_path, resource)
            os.rename(source_dir, destination_dir)

    def replace_word_in_folder(self, old_word: str, new_word: str, directory: str):
        """replace_word_in_folder
        this method will replace every instance of the old word in the given directory with
        the new word
        """
        content = {}
        for root, directories, files in os.walk(directory):
            try:
                for file in files:
                    file = os.path.join(root, file)
                    with open(file, "r") as f:
                        content[file] = f.read().replace(old_word, new_word)
            except:
                pass
        for root, directories, files in os.walk(directory):
            try:
                for file in files:
                    file = os.path.join(root, file)
                    with open(file, "w") as f:
                        f.write(content[file])
            except:
                pass

    def read_word_in_directory(self, word: str) -> 'list[str]':
        """read_word_in_directory has the following params

        Parameters
        ---

        word str
            The word that will be searched on the current directory

        Example
        ---

        for example this function can be used by moving the Os interface to the desired 
        directory to search
        ```python
        with OperatingSystemInterface(desired_directory) as osi:
            list_of_files = osi.read_word_in_directory("<class_name>")
        print(list_of_files)
        ```
        Returns
        ---
        result: 'list[str]'
        """
        result = []
        for root, directories, files in os.walk(self.directory):
            for file in files:
                with open(os.path.join(self.directory, file)) as f:
                    content = f.read()
                    if content.find(word) != -1:
                        result.append(file)

        return result
