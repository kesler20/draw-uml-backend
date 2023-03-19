from pathlib import Path
from typing import List
from abc import ABC, abstractmethod

try:
    from _types import ClassRepresentation
    from file import File
except ModuleNotFoundError:
    try:
        from draw_uml_backend._types import ClassRepresentation
        from draw_uml_backend.file import File
    except ModuleNotFoundError:
        from src.draw_uml_backend._types import ClassRepresentation
        from src.draw_uml_backend.file import File


class CodeReader(ABC):
    """The CodeReader reads code from the ``read_only`` folder and generates the response 
    to the ``response`` folder

    The Reader uses the ``Path`` object for the ``source_code_path`` ``field``
    the Path object provides a number of useful methods that make it easier to work with files and directories.
    For example, you can use the .exists() method to check whether a file or directory exists,
    the .mkdir() method to create a new directory,
    and the .glob() method to find all files in a directory that match a specific pattern.
    """

    __source_code_path: Path
    __response_code_path: Path

    @property
    @abstractmethod
    def source_code_path(self) -> Path:
        ...

    @property
    @abstractmethod
    def response_code_path(self) -> Path:
        ...

    @abstractmethod
    def set_response_code_path(self, path: str):
        ...

    @abstractmethod
    def set_source_code_path(self, path: str):
        ...

    @abstractmethod
    def read(self) -> None:
        ...


class PythonCodeReader(CodeReader):
    """The CodeReader Implementation for reading python code"""

    def __init__(self, source_code_path: str, response_code_path: str) -> None:
        self.__source_code_path: Path = Path("")
        self.__response_code_path: Path = Path("")
        self.set_source_code_path(source_code_path)
        self.set_response_code_path(response_code_path)

    def __repr__(self) -> str:
        representation = {
            k.replace("_PythonCodeReader__", ""): self.__dict__[k] for k in self.__dict__.keys()
        }
        return f"""PythonCodeReader({representation})"""

    @property
    def source_code_path(self) -> Path:
        return self.__source_code_path

    @property
    def response_code_path(self) -> Path:
        return self.__response_code_path

    def set_response_code_path(self, path: str):
        self.__response_code_path = Path(path)
        return self

    def set_source_code_path(self, path: str):
        self.__source_code_path = Path(path)
        return self

    def __get_source_code(self) -> List[str]:
        return [line.replace("\n", "") for line in File(self.source_code_path).readlines()]

    def read(self) -> None:
        source_code = self.__get_source_code()

        # this is a list of lists containing all the information of each class in a programme
        classes_name_space: List[ClassRepresentation] = []

        # this flag will allow us to understand whether ywe are in the first, second etc.. class
        class_flag = -1
        function_flag = -1
        comment_flag = 0

        # use the reserved key words from the programming language to understand the programme
        for line_number, line in enumerate(source_code):
            # Find the class names
            if line.find("class ") != -1:
                class_flag += 1
                # reset the function flag as you are inside a new class
                function_flag = -1
                # the line might look like the following
                # class class_name:
                # class class_name(object):
                # assuming that we want to keep the inheritance
                if line.find(":") != -1:
                    class_name = line.split("class ")[1].split(":")[0]
                classes_name_space.append(
                    {
                        "class_name": class_name,
                        "description": "",
                        "methods": [],
                        "fields": [],
                        "properties": [],
                    }
                )

            # Find the properties
            if line.find("def __init__") != -1:
                # find params names and types
                # params are usually delineated by brackets
                params = line.split("(")[1].split(")")[0]

                # remove self
                params = params.replace("self,", "")

                dirty_param_names_and_types: List[str] = params.split(":")
                param_names_and_types: List[List[str]] = [
                    i.split(",") for i in dirty_param_names_and_types
                ]

                # remove nested lists
                param_names_and_types_list: List[str] = []
                for param_type in param_names_and_types:
                    for val in param_type:
                        param_names_and_types_list.append(val)

                # the param list should be of the form [param1, type, param2, type, ...]
                # if the number of params names and types is uneven then there are some types missing
                if (
                    len(param_names_and_types_list) % 2 != 0
                    and param_names_and_types_list[0] != "self"
                ):
                    print("\nthe following params might miss some types\n", params)
                    print("")
                else:
                    # avoid methods which only have self
                    if param_names_and_types_list != ["self"]:

                        # merge the collection types which may have been separated when
                        clean_param_names_and_types = []
                        for index, param_types in enumerate(param_names_and_types_list):
                            count = 0
                            for char in list(param_types):
                                if char == "[":
                                    count += 1
                                elif char == "]":
                                    count -= 1
                                else:
                                    pass
                            if count > 0:
                                clean_param_names_and_types.append(
                                    param_types + "," + param_names_and_types_list[index + 1]
                                )
                            elif count < 0:
                                pass
                            else:
                                clean_param_names_and_types.append(param_types)

                        try:
                            grouped_names_types = [
                                [
                                    clean_param_names_and_types[i].replace(" ", ""),
                                    clean_param_names_and_types[i + 1].replace(" ", ""),
                                ]
                                for i in range(0, len(clean_param_names_and_types), 2)
                            ]
                            for grouped_params in grouped_names_types:
                                classes_name_space[class_flag]["properties"].append(grouped_params)
                        except IndexError:
                            print(clean_param_names_and_types)

            # Find the fields
            if line.find("__") != -1 and line.find("__(") == -1 and line.find(":") != -1:
                field_line = line.split("__")[1]
                classes_name_space[class_flag]["fields"].append(field_line.split(":"))

            # Find the methods
            if line.find("def ") != -1:
                # make sure that we are inside a class
                if class_flag >= 0:
                    # find the signature
                    # the line might look like the following assuming that the programme is typed
                    # def foo(param1: str, param2: int, optional_param: Optional[int] = None) -> None:
                    signature = line.split("def ")[1].split("(")[0]
                    classes_name_space[class_flag]["methods"].append(
                        {
                            "signature": signature,
                            "params": [],
                            "decorator": "",
                            "return_type": "",
                            "description": "",
                        }
                    )
                    function_flag += 1

                    try:
                        if source_code[line_number - 1].find("@"):
                            property_name = (
                                source_code[line_number - 1].split("@")[1].replace(" ", "")
                            )
                            classes_name_space[class_flag]["methods"][function_flag][
                                "decorator"
                            ] = property_name
                    except IndexError:
                        pass

                    # remove self
                    line = line.replace("self,", "")
                    classes_name_space[class_flag]["methods"][function_flag]["params"].append(
                        ["self"]
                    )

                    # get the return type
                    try:
                        return_type = line.split(" -> ")[1].replace(":", "")
                        classes_name_space[class_flag]["methods"][function_flag][
                            "return_type"
                        ] = return_type
                    except IndexError:
                        print("\nthis line misses a return type\n", line)
                        print("")

                    # find params names and types
                    # params are usually delineated by brackets
                    params = line.split("(")[1].split(")")[0]
                    dirty_param_names_and_types = params.split(":")
                    param_names_and_types = [i.split(",") for i in dirty_param_names_and_types]

                    # remove nested lists
                    new_param_names_and_types_list: List[str] = []
                    for param_type in param_names_and_types:
                        for val in param_type:
                            new_param_names_and_types_list.append(val)

                    # the param list should be of the form [param1, type, param2, type, ...]
                    # if the number of params names and types is uneven then there are some types missing
                    if (
                        len(new_param_names_and_types_list) % 2 != 0
                        and new_param_names_and_types_list[0] != "self"
                    ):
                        print("\nthe following line might miss some types\n", line)
                        print("")
                    else:
                        # avoid methods which only have self
                        if new_param_names_and_types_list != ["self"]:

                            # merge the collection types which may have been separated when
                            new_clean_param_names_and_types: List[str] = []
                            for index, param_types in enumerate(new_param_names_and_types_list):
                                count = 0
                                for char in list(param_types):
                                    if char == "[":
                                        count += 1
                                    elif char == "]":
                                        count -= 1
                                    else:
                                        pass
                                if count > 0:
                                    new_clean_param_names_and_types.append(
                                        param_types
                                        + ","
                                        + new_param_names_and_types_list[index + 1]
                                    )
                                elif count < 0:
                                    pass
                                else:
                                    new_clean_param_names_and_types.append(param_types)

                            try:
                                grouped_names_types = [
                                    [
                                        new_clean_param_names_and_types[i].replace(" ", ""),
                                        new_clean_param_names_and_types[i + 1].replace(" ", ""),
                                    ]
                                    for i in range(0, len(new_clean_param_names_and_types), 2)
                                ]
                                for grouped_params in grouped_names_types:
                                    classes_name_space[class_flag]["methods"][function_flag][
                                        "params"
                                    ].append(grouped_params)
                            except IndexError:
                                print(new_clean_param_names_and_types)

        File(self.response_code_path).write_json(classes_name_space)
