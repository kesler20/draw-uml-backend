from dataclasses import dataclass
from typing import Set
try:
    from draw_uml_backend._base import BaseReader
except ModuleNotFoundError:
    from src.draw_uml_backend._base import BaseReader


@dataclass
class ClassBuilder(BaseReader):

    output_file: str
    dataclasses: bool
    __final_class_representation: str = ""

    @property
    def final_class_representation(self):
        return self.__final_class_representation

    def set_final_class_representation(self, final_class: str):
        self.__final_class_representation = final_class

    def build_final_class(self):
        """Print the final class representation
        and save it on the output file
        """
        print(self.__final_class_representation)
        self.write(self.output_file, self.final_class_representation)
        return self.__final_class_representation

    def add_imports(self, types_path: str, types: Set[str]):
        types = list(types)
        imports = '''
from typing import List, Any, Union, Dict, Optional, Tuple'''
        if self.dataclasses:
            imports += '''
from dataclasses import dataclass'''
        types_import = ""
        for type in types:
            if type == types[-1]:
                types_import += f"{type}"
            else:
                types_import += f"{type}, "

        imports += '''
from {} import {}
        '''.format(types_path, types_import)
        self.__final_class_representation += imports
        return self

    def add_class_definition(self):
        """This method generates the following part of the code

        ```python
        from typing import List, Any, Union, Dict
        from dataclasses import dataclass


        @dataclass
        class TasksApi(GoogleApi):
          '''TasksApi(GoogleApi) is a class'''
        ```
        """

        if self.dataclasses:
            self.__final_class_representation += '''
@dataclass
class {}:
    """{} is a class"""
    '''.format(self.source.class_name, self.source.class_name)
        else:
            self.__final_class_representation += '''
class {}(object):
    """{} is a class"""
    '''.format(self.source.class_name, self.source.class_name)

        return self

    def add_properties(self):
        """This method generates the following part of the code"""
        if self.dataclasses:
            self.__add_public_fields()
            return self

        # add the properties as params __init__(self,prop1,prop2...)
        property_as_param = ""
        for property, property_types in self.source.properties:
            property_as_param += f"{property} : {property_types}" if property == self.source.properties[
                -1][0] else f"{property} : {property_types}, "

        # pass that to the starting property
        starting_property = '''''' if len(self.source.properties) == 0 else '''
    def __init__(self{}) -> None:'''.format(property_as_param)

        property_to_add = ""
        for property in self.source.properties:
            property_to_add += '''
        self.{} = {}'''.format(property[0], property[0])
        starting_property += property_to_add

        self.__final_class_representation += starting_property
        return self

    def __add_public_fields(self):
        """This method generates this part of the code
        ```python
        filename: str = "protocol_database.xlsx"
        """

        # assuming that fields come in the following format
        # [["filename", " str = \"protocol_database.xlsx\""]]

        initial_field = """"""
        for field, field_type in self.source.properties:
            initial_field += """
    {} : {}""".format(field, field_type)

        self.__final_class_representation += initial_field
        return self

    def add_private_fields(self):
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
        ```
        """

        # assuming that fields come in the following format
        # [["filename", " str = \"protocol_database.xlsx\""]]

        initial_field = """"""
        if self.dataclasses:
            for field, field_type in self.source.fields:
                initial_field += """
    __{} : {}""".format(field, field_type)
        else:
            for field, field_type in self.source.fields:
                initial_field += """
        self.__{} : {}""".format(field, field_type)

        # create getters
        for field, field_type in self.source.fields:
            initial_field += '''
    
    @property
    def {}(self):
        """{} property getter"""
        return self.__{}
            '''.format(field, field, field)

        # create setters
        for field, field_type in self.source.fields:
            initial_field += '''    
    def set_{}(self,{} : {}):
        """{} property setter"""
        self.__{} = {}
            '''.format(field, field, field_type.split("=")[0].replace(" ", ""), field, field, field)

        self.__final_class_representation += initial_field
        return self

    def add_methods(self):
        """This method generates the larger part of the code
        """
        # assuming that self.source.methods is a collection of the following data structure
        # {
        #   "signature": "filename",
        #   "params": [["self"]],
        #   "decorator": "property",
        #   "return type": "str"
        # },

        # build the method using the params
        initial_method = ""
        for method in self.source.methods:
            # build initial params
            params = method['params']
            decorators = method['decorator']

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
                    '''.format(method['return_type'])

            # build initial method
            initial_method += '''
    {}
    def {}(self{}) -> {}:
        """{} {}{}  '''.format(f"@{decorators}" if decorators != "" else "", method['signature'].replace("()", ""),
                               params_to_pass, method['return_type'], method['signature'].replace(
                                   "()", ""),
                               "has the following params" if method["description"] == "" else method['description'], comment)

        self.__final_class_representation += initial_method
        return self
