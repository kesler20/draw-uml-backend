from read_only.source_code import SourceCode
from dataclasses import dataclass
from typing import List
from interfaces.os_interface import File


@dataclass
class TypeChecker:
    __built_in_types: List[str] = ["str", "None", "float", "dict", "set"
                                   "int", "complex", "list", "tuple", "bool"]
    __typing_types: List[str] = ["Dict", "List", "Tuple"]

    def convert_builtin_to_typing(self, type) -> str:
        if type == 'list':
            return 'List'
        elif type == 'tuple':
            return 'Tuple'
        elif type == 'dict':
            return 'Dict'
        else:
            return type

    def generate_types(self, types: List[str], types_file: str) -> None:
        novel_types = [
            _type if _type in self.__built_in_types else None for _type in types]
        for novel_type in novel_types:
            if novel_type is not None:
                File(types_file).append(novel_type)

    def convert_typing_to_builtin(self, type) -> str:
        if type == 'List':
            return 'list'
        elif type == 'Tuple':
            return 'tuple'
        elif type == 'Dict':
            return 'dict'
        else:
            return type


class TypesGenerator(object):
    source = SourceCode()

    def generate_types(self):
        if len(self.source.methods) == 0:
            # if the class does not have methods,
            # make a typed dict
            init_type = '''
from typing import TypedDict

class {}(TypedDict):'''.format(self.source.class_name)

            for name, name_type in self.source.properties:
                init_type += '''
{}: {}'''.format(name, name_type)
        else:
            # if the class has methods, make a protocol
            init_type = '''
from typing import Protocol

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
          '''.format(method['signature'], params_to_pass, method['return type'])

        print(init_type)
