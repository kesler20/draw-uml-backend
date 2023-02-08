from pathlib import Path
from dataclasses import dataclass, field
from typing import List, Set
try:
    from _base import BaseReader
except ModuleNotFoundError:
    try:
        from draw_uml_backend._base import BaseReader
    except ModuleNotFoundError:
        from src.draw_uml_backend._base import BaseReader


@dataclass
class TypeChecker(BaseReader):

    types_file: str
    __built_in_types: List[str] = field(default_factory=lambda: ["str", "None", "float", "dict", "set",
                                                                 "int", "complex", "list", "tuple", "bool"])
    __typing_types: List[str] = field(
        default_factory=lambda: ["Dict", "List", "Tuple", "Optional", "Any", "Union", "Set"])
    
    __mutable_types: List[str] = field(default_factory=lambda: ["List","list"]) 

    @property
    def built_in_types(self) -> List[str]:
        return self.__built_in_types

    @property
    def typing_types(self) -> List[str]:
        return self.__typing_types

    @property
    def mutable_types(self) -> List[str]:
        return self.__mutable_types

    @property
    def novel_types(self) -> Set[str]:
        # get all the types from the source code
        types: List[str] = []
        # append all the fields
        for callable in self.source.methods:
            types.append(callable['return_type'])
            for param in callable['params']:
                try:
                    types.append(param[1])
                except IndexError:
                    print("this param has no type", param)
        # append all the properties
        for property in self.source.properties:
            try:
                types.append(property[1])
            except IndexError:
                print("this property has no type", property)

        # append all the fields
        for field in self.source.fields:
            try:
                types.append(field[1])
            except IndexError:
                print("this field has no type", field)

        clean_types = [type.split("[")[0] for type in types]
        novel_types = list(filter(lambda item: item not in [
            *self.built_in_types, *self.typing_types], clean_types))
        print("these are the novel types", set(novel_types))
        return set(novel_types)

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
        source = self.source.source
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

    def init_types_file(self):
        self.clean_up(self.types_file)
        if not Path(self.types_file).exists():
            imports = '''
from typing import TypedDict, List, Any, Union, Dict, Tuple, Optional, Protocol
            '''
            self.write(self.types_file, imports)

    def append_novel_types_to_types_path(self) -> None:
        classes_to_append_to_types_file = ""
        for type in self.novel_types:
            classes_to_append_to_types_file += '''

class {}(Protocol):
    ...
            '''.format(type.replace("()", ""))
        self.append(self.types_file, classes_to_append_to_types_file)

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

class {}(TypedDict):'''.format(self.source.class_name)

            for name, name_type in self.source.properties:
                init_type += '''
    {}: {}'''.format(name, name_type)
        else:
            # if the class has methods, make a protocol
            init_type = '''
            
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
        self.append(self.types_file, init_type)
