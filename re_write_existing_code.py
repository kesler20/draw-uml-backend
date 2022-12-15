import json
from typing import Dict, List
import os
import time
from dictionary_of_types import convert_builtin_to_typing

with open("existing_code_response.json", "r") as file:
    data = json.loads(file.read())

metadata: Dict = data[0]
os.remove("test.py")

# pre-processing step for the data and the function types to turn them into typing types
names = [[name[0], convert_builtin_to_typing(name[1])] for name in names]
clean_callable_functions = []
for callable in callable_functions:
    callable['params'] = [[param[0], convert_builtin_to_typing(param[1])] for param in callable['params']]
    callable['return type'] = convert_builtin_to_typing(callable['return type'])
    clean_callable_functions.append(callable)


class ClassBuilder(object):

    def __init__(self, metadata, output_filename) -> None:
        self.class_name = metadata['class name']
        self.description = metadata['description']
        self.methods = metadata['methods']
        self.fields = metadata['fields']
        self.properties = metadata['properties']
        self.output_file = output_filename

    def generate_class(self):
        """This method generates the following part of the code

        ```python
        from typing import List, Any, Union, Dict
        from dataclasses import dataclass


        @dataclass
        class TasksApi(GoogleApi):
          '''TasksApi(GoogleApi) is a class'''
        ```
        """

        # start from relevant imports
        imports = '''
from typing import List, Any, Union, Dict, Optional, Tuple
from _types import *
from dataclasses import dataclass

'''
        # use dataclasses by default
        dataclass_name = '''
@dataclass
class {}:
    """{} is a class"""
'''.format(self.class_name, self.class_name)

        print(imports + dataclass_name)
        # write to the output file
        with open(self.output_file, "a") as out:
            out.write(imports + dataclass_name)

    def generate_properties(self):
        """This method generates the following part of the code"""

        # add the properties as params __init__(self,prop1,prop2...)
        property_as_param = ""
        for property, property_types in self.properties:
            property_as_param += f"{property}:{property_types}" if property == self.properties[
                -1] else f"{property}:{property_types},"

        # pass that to the starting property
        starting_property = '''''' if len(self.properties) == 0 else '''
    def __init__(self,{}) -> None:
'''.format(property_as_param)

        property_to_add = ""
        for property in self.properties:
            property_to_add += '''
    self.{} = {}
'''.format(property, property)
        starting_property += property_to_add

        print(starting_property)

        # write to the output file
        with open(self.output_file, "a") as out:
            out.write(starting_property)

    def generate_public_fields(self):
        """This method generates this part of the code
        ```python
        filename: str = "protocol_database.xlsx"
        """

        # assuming that fields come in the following format
        # [["filename", " str = \"protocol_database.xlsx\""]]

        initial_field = """"""
        for field, field_type in self.properties:
            initial_field += """
    {}:{}
""".format(field, field_type)

        print(initial_field)
        # write to the output file
        with open(self.output_file, "a") as out:
            out.write(initial_field)

    def generate_fields(self):
        """This method generates this part of the code
        ```python
        __filename: str = "protocol_database.xlsx"

        @property
        def filename(self):
            '''filename property getter'''
            return self.__filename

        def set_filename(self,filename :  str):
            '''filename property setter'''
            self.__filename = filename
        """

        # assuming that fields come in the following format
        # [["filename", " str = \"protocol_database.xlsx\""]]

        initial_field = """"""
        for field, field_type in self.fields:
            initial_field += """
    __{}:{}
""".format(field, field_type)

        # create getters
        for field, field_type in self.fields:
            initial_field += '''
    @property
    def {}(self):
        """{} property getter"""
        return self.__{}
            '''.format(field, field, field)

        # create setters
        for field, field_type in self.fields:
            initial_field += '''
    def set_{}(self,{} : {}):
        """{} property setter"""
        self.__{} = {}
            '''.format(field, field, field_type.split("=")[0].replace(" ", ""), field, field, field)

        print(initial_field)
        # write to the output file
        with open(self.output_file, "a") as out:
            out.write(initial_field)

    def generate_methods(self):
        """This method generates the larger part of the code
        """
        # assuming that self.methods is a collection of the following data structure
        # {
        #   "signature": "filename",
        #   "params": [["self"]],
        #   "decorator": "property",
        #   "return type": "str"
        # },

        # build the method using the params
        initial_method = ""
        for method in self.methods:
            # build initial params
            params = method['params']

            # for each param construct the comment and the params_to_pass (self,param_1:str,...)
            # then add to initial_method
            for index, param in enumerate(params):
                params_to_pass = ""
                # do not consider the self param
                if param[0] == "self":
                    comment = '''"""
        ...
                    '''
                else:
                    # build the comment which will change for each params
                    comment = """
        
        Params
        ---
                """
                    # MAJORITY OF THE LOGIC IS CONTAINED IN THIS BLOCK WHERE WE ASSUME THAT THE PARAMETER IS NOT SELF
                    # THE PARAM ARRAY SHOULD BE OF THE FOLLOWING FORM ['param_name','param_type']
                    if len(param) > 1:
                        params_to_pass += f", {param[0]} : {param[1]}" if param == params[-1] else f", {param[0]} : {param[1]},"

                    else:
                        # if there is more than one item in the parameter array use the second item as a type
                        params_to_pass += f", {param[0]} : {None}" if param == params[-1] else f", {param[0]} : {None},"

                    comment += """
        {} {}
            to be passed as parameter {}
                    """.format(param[0], None if len(param) == 1 else param[1], index + 1)
                    comment += '''
        Returns
        ---
        result: {}
        """
        ...
                    '''.format(method['return type'])

            # build initial method
            initial_method += '''
    def {}(self{}) -> {}:
        """{} has the following params{}  '''.format(method['signature'], params_to_pass, method['return type'], method['signature'], comment)

        print(initial_method)
        # write to the output file
        with open(self.output_file, "a") as out:
            out.write(initial_method)


cls = ClassBuilder(metadata, "test.py")
cls.generate_class()
cls.generate_properties()
cls.generate_fields()
cls.generate_methods()
