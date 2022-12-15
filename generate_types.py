from dictionary_of_types import convert_builtin_to_typing

class_name = "TestFoo"
names = [["cool", "str"], ["prop_call", "bool"], ["another_property", "int"]]
callable_functions = [{
    "signature": "put_column",
    "params": [
        ["column_name", "str"],
        ["column_values", "List[Any]"],
        ["table_name", "str"]
    ],
    "return type": "None"
},
    {
    "signature": "insert_column",
        "params": [
            ["column_index", "int"],
            ["column_name", "str"],
            ["column_values", "List[Any]"],
            ["table_name", "str"]
        ],
    "return type": "None"
}]

# pre-processing step for the data and the function types to turn them into typing types
names = [[name[0], convert_builtin_to_typing(name[1])] for name in names]
clean_callable_functions = []
for callable in callable_functions:
    callable['params'] = [[param[0], convert_builtin_to_typing(param[1])] for param in callable['params']]
    callable['return type'] = convert_builtin_to_typing(callable['return type'])
    clean_callable_functions.append(callable)

class DictionaryTypes(object):

    def __init__(self) -> None:
        self.class_name = class_name
        self.properties = names
        self.methods = callable_functions

    def generate_types(self):
        if len(self.methods) == 0:
            # if the class does not have methods,
            # make a typed dict
            init_type = '''
from typing import TypedDict

class {}(TypedDict):'''.format(self.class_name)

            for name, name_type in self.properties:
                init_type += '''
  {}: {}'''.format(name, name_type)
        else:
            # if the class has methods, make a protocol
            init_type = '''
from typing import Protocol

class {}(Protocol):   
          '''.format(self.class_name)

            for method in self.methods:
                for param in method['params']:
                    params_to_pass = ""
                    if len(param) > 1:
                        params_to_pass += f", {param[0]} : {param[1]}" if param == method['params'][-1] else f", {param[0]} : {param[1]},"

                init_type += '''
  def {}(self{}) -> {}:
    ...
            '''.format(method['signature'], params_to_pass, method['return type'])

        print(init_type)


cls = DictionaryTypes()
cls.generate_types()
