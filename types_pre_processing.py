from pathlib import Path
from read_only.source_code import SourceCode
from dataclasses import dataclass, field
from typing import List
from interfaces.os_interface import File
from _base import BaseReader


@dataclass
class TypeChecker(BaseReader):

    types_file: str
    __built_in_types: List[str] = field(default_factory=lambda: ["str", "None", "float", "dict", "set"
                                                                 "int", "complex", "list", "tuple", "bool"])
    __typing_types: List[str] = field(
        default_factory=lambda: ["Dict", "List", "Tuple"])

    def convert_builtin_to_typing(self, type: str) -> str:
        if type == 'list':
            return 'List'
        elif type == 'tuple':
            return 'Tuple'
        elif type == 'dict':
            return 'Dict'
        else:
            return type

    def change_source_to_typing(self):
        source = self.source.read_and_clean_source()
        # pre-processing step for the data and the function types to turn them into typing types
        source['properties'] = [[name[0], self.convert_builtin_to_typing(
            name[1])] for name in source['properties']]
        source['fields'] = [[name[0], self.convert_builtin_to_typing(
            name[1])] for name in source['fields']]
        clean_callable_functions = []

        for callable in source['methods']:
            try:
                callable['params'] = [[param[0], self.convert_builtin_to_typing(
                    param[1])] for param in callable['params']]
                callable['return_type'] = self.convert_builtin_to_typing(
                    callable['return_type'])
                clean_callable_functions.append(callable)
            except IndexError:
                print(callable)
        source['methods'] = clean_callable_functions
        return source

    def append_novel_types_to_types_path(self) -> None:
        # get all the types from the source code
        types = []
        for callable in self.source.methods:
            try:
                types.append(callable['params'][1])
                types.append(callable['return_type'])
            except IndexError:
                print(callable)

        # get only the types which are not in built_ins
        novel_types = [
            _type if _type in self.__built_in_types else None for _type in types]
        for novel_type in novel_types:
            if novel_type is not None:
                File(Path(self.types_file)).append(novel_type)

    def convert_typing_to_builtin(self, type: str) -> str:
        if type == 'List':
            return 'list'
        elif type == 'Tuple':
            return 'tuple'
        elif type == 'Dict':
            return 'dict'
        else:
            return type

    def generate_types(self):
        if len(self.source.methods) == 0:
            # if the class does not have methods,
            # make a typed dict
            init_type = '''
from typing import TypedDict, List, Any, Union, Dict, Tuple, Optional

class {}(TypedDict):'''.format(self.source.class_name)

            for name, name_type in self.source.properties:
                init_type += '''
{}: {}'''.format(name, name_type)
        else:
            # if the class has methods, make a protocol
            init_type = '''
from typing import Protocol, List, Any, Union, Dict, Tuple, Optional

class {}(Protocol):   
        '''.format(self.source.class_name)

            for method in self.source.methods:
                for param in method['params']:
                    params_to_pass = ""
                    if len(param) > 1:
                        params_to_pass += f", {param[0]} : {param[1]}" if param == method['params'][-1] else f", {param[0]} : {param[1]},"

                init_type += '''
    def {}(self{}) -> {}:
        ...
          '''.format(method['signature'], params_to_pass, method['return_type'])
        self.clean_up(self.types_file)
        File(Path(self.types_file)).append(init_type)
