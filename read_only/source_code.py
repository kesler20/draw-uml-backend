from types_pre_processing import TypeChecker
from typing import List
from interfaces.os_interface import File
from _types import ClassRepresentation


class SourceCode:
    def __init__(self, response_code_path: str) -> None:
        self.source: ClassRepresentation = self.read_and_clean_source(
            response_code_path)
        self.class_name = self.source['class_name']
        self.description = self.source['description']
        self.methods = self.source['methods']
        self.fields = self.source['fields']
        self.properties = self.source['properties']
        self.type_checker = TypeChecker()

    def format_new_code_response(self):
        ...

    def read_and_clean_source(self, response_code_path: str) -> ClassRepresentation:
        """read one class at a time, then pop from the array
        do the required cleanups and preprocessing of the class"""

        # remove the end of line delimiter from every line of the response_code file (json file)
        source: ClassRepresentation = [line.replace('\n', "") for line in File(
            response_code_path).readlines()][-1]
        # pre-processing step for the data and the function types to turn them into typing types
        source['properties'] = [[name[0], self.type_checker.convert_builtin_to_typing(
            name[1])] for name in source['properties']]
        source['fields'] = [[name[0], self.type_checker.convert_builtin_to_typing(
            name[1])] for name in source['fields']]
        clean_callable_functions = []
        for callable in source['methods']:
            try:
                callable['params'] = [[param[0], self.type_checker.convert_builtin_to_typing(
                    param[1])] for param in callable['params']]
                callable['return type'] = self.type_checker.convert_builtin_to_typing(
                    callable['return type'])
                clean_callable_functions.append(callable)
            except IndexError:
                print(callable)
        source['methods'] = clean_callable_functions
        return source
