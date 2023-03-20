from dataclasses import dataclass, field
import os
from typing import Set
from draw_uml_backend.types_pre_processing import TypeChecker
from draw_uml_backend._base import BaseReader, BASE_OUTPUT_RESPONSE_PATH


@dataclass
class ClassBuilder(BaseReader):

    dataclasses: bool
    __final_class_representation: str = field(init=False, default="")

    @property
    def output_file(self):
        return os.path.join(BASE_OUTPUT_RESPONSE_PATH, self.source.class_name.lower() + ".py")

    @property
    def final_class_representation(self):
        return self.__final_class_representation

    def set_final_class_representation(self, final_class: str):
        self.__final_class_representation = final_class

    def build_final_class(self):
        """Print the final class representation
        and save it on the output file

        Returns
        -------
        self
        """
        print(self.__final_class_representation)
        self.write(self.output_file, self.final_class_representation)
        return self.__final_class_representation

    def add_imports(self, types_path: str, types: Set[str]):
        """Add imports of the final class file
        This is achieved in layers
        - initially all the imports from typing are added
        - then optional imports such as dataclasses
        - finally any extra types passed to the method 

        Parameters
        ----------

        types_path : str
            this is the path of the types file
            often output/types.py
        
        types : set[str]
            this is a collection of the non-built in
            types that the class uses
        
        Returns
        -------
        self
        """
        list_types = list(types)
        clean_list_types = [
            _type if "=" not in list(_type) else _type.split("=")[0].replace(" ", "")
            for _type in list_types
        ]

        imports = """
from typing import List, Any, Union, Dict, Optional, Tuple"""

        if self.dataclasses:
            imports += """
from dataclasses import dataclass, field"""

        types_import = ""
        for type in clean_list_types:
            if type == clean_list_types[-1]:
                types_import += f"{type}"
            else:
                types_import += f"{type}, "

        imports += f"""
from {types_path} import {types_import if types_import != "" else "*"}
        """
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
        
        Returns
        -------
        self
        """

        if self.dataclasses:
            self.__final_class_representation += f'''
@dataclass
class {self.source.class_name}:
    """{self.source.class_name} is a class
    
    {self.add_class_description_example()}
    """
    '''
        else:
            self.__final_class_representation += f'''
class {self.source.class_name}(object):
    """{self.source.class_name} is a class
    
    {self.add_class_description_example()}
    """
    '''
        return self

    def add_properties(self):
        """This method generates the correct properties 
        ```txt
        depending on the type of dataclass
        this is because it calls the internal method `__add_public_fields`
        ```

        Returns
        -------
        self
        """
        if self.dataclasses:
            self.__add_public_fields()
            return self

        # add the properties as params __init__(self,prop1,prop2...)
        property_as_param = ""
        for property, property_types in self.source.properties:
            property_as_param += (
                f", {property} : {property_types}"
                if property == self.source.properties[-1][0]
                else f", {property} : {property_types}"
            )

        # pass that to the starting property
        starting_property = (
            """"""
            if len(self.source.properties) == 0
            else """
    def __init__(self{}) -> None:""".format(
                property_as_param
            )
        )

        property_to_add = ""
        for property in self.source.properties:
            property_to_add += """
        self.{} = {}""".format(
                property[0], property[0]
            )
        starting_property += property_to_add

        self.__final_class_representation += starting_property
        return self

    def add_class_description_example(self) -> str:
        # group all the function calls
        content = ""
        function_call = ""
        for method in self.source.methods:
            # only show public methods on your example
            if method["signature"].startswith("__"):
                pass
            else:
                params = ""
                try:
                    for param in method["params"]:
                        if param == method["params"][-1]:
                            params += f"{param[0]}"
                        else:
                            params += f"{param[0]}, "
                except IndexError:
                    pass

                function_call += f"""
    {self.source.class_name.lower()}.{method["signature"]}({params})
                """
        # remove self params on method calls
        function_call = function_call.replace("self, ", "")
        function_call = function_call.replace("self", "")
        content += f"""
    Example
    -------
    {self.source.class_name.lower()} = {self.source.class_name}()
    {function_call}
        """

        return content

    def __add_field_method(self, field_type: str, private: bool):
        """This method takes the field in the following format
        ```txt
        str = "protocol_database.xlsx"
        ```
        Or it takes mutable types such as `list`
        and returns the correct `field` method from `dataclasses`
        
        Parameters
        ----------
        field_type : str
            this is the field type which can be mutable type
            `List[int] = [1,2,3,4]`
            or it can be a field with a default value
            `str = "protocol_database.xlsx"`
        private : bool
            this refers to whether the field is private or not
            if the field is neither private nor mutable, this will return the 
            `field_type` string unmodified

        Returns
        -------
        str
          the correct `field` method from `dataclasses`
        """
        checker = TypeChecker("", "")

        _type = field_type
        inner_type = ""
        default_value = ""

        # take the initial part of something like this `str = "protocol_database.xlsx"`
        # separate default value `"protocol_database.xlsx"` from its type `str`
        # and remove any spaces as well as the inner types i.e. `[str]`
        if field_type.find("=") != -1:
            _type = field_type.split("=")[0].replace(" ", "")
            default_value = field_type.split("=")[1].replace(" ", "")

        if _type.find("[") != -1:
            inner_type = _type.split("[")[1].replace("]", "")

        # reconstruct the cleaner type in the following form `list[str]` -> List
        _type = _type.replace(f"[{inner_type}]", "")
        _type = checker.convert_builtin_to_typing(_type)

        if _type in checker.mutable_types:
            return f"{_type}[{inner_type}] = field(init=False, default_factory=lambda : {default_value})"
        else:
            if private:
                return f"{_type} = field(init=False, default={default_value})"

        return field_type

    def __add_public_fields(self):
        """This method generates this part of the code
        ```python
        filename: str = "protocol_database.xlsx"
        """

        # assuming that fields come in the following format
        # [["filename", " str = \"protocol_database.xlsx\""]]

        initial_field = """"""
        for field, field_type in self.source.properties:

            field_type = self.__add_field_method(field_type, False)
            initial_field += f"""
    {field} : {field_type}"""

        self.__final_class_representation += initial_field
        return self

    def add_private_fields(self):
        """This method generates this part of the code
        ```python
        __filename: str = field(init=False, default="protocol_database.xlsx")

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
                field_type = self.__add_field_method(field_type, True)

                initial_field += f"""
    __{field} : {field_type}"""

        else:
            for field, field_type in self.source.fields:
                initial_field += f"""
        self.__{field} : {field_type}"""

        # create setters and getters, since all private fields require
        # setters and getters
        for field, field_type in self.source.fields:
            initial_field += f'''
    
    @property
    def {field}(self):
        """{field} property getter"""
        return self.__{field}
            '''

        # create setters
        for field, field_type in self.source.fields:
            initial_field += f'''    
    def set_{field}(self,{field} : {field_type.split("=")[0].replace(" ", "")}):
        """{field} property setter"""
        self.__{field} = {field}
            '''

        self.__final_class_representation += initial_field
        return self

    def add_methods(self):
        """
        - This method generates the larger part of the code
        it generates all the methods of the class

        - Each part of the signature is generated indipendently and put together
        in the final line:

        ```python
            {f"@{decorators}" if decorators != "" else ""}
        def {method['signature'].replace("()", "")}(self{params_to_pass}) -> {method['return_type']}:
            ""{method['signature'].replace("()", "")} {"has the following params" if method["description"] == "" else method['description']}{comment}""
        ```
        """
        # assuming that self.source.methods is a collection of the following data structure
        # {
        #   "signature": "filename",
        #   "params": [["self"]],
        #   "decorator": "property",
        #   "return_type": "str"
        # },

        # build the method using the params
        initial_method = ""
        for method in self.source.methods:
            # build initial params
            params_to_pass = ""
            params = method["params"]
            decorators = method["decorator"]

            # build the comment which will change for each params
            # if the params looks like the following [['self']]
            if params[0][0] == "self" and len(params) == 1:
                comment = '''
        """
        ...        
                '''
            else:
                comment = """
        
        Parameters
        ----------
            """

            # for each param construct the comment and the params_to_pass (self,param_1:str,...)
            # then add to initial_method
            for index, param in enumerate(params):
                # do not consider the self param
                if param[0] != "self":
                    # MAJORITY OF THE LOGIC IS CONTAINED IN THIS BLOCK WHERE WE ASSUME THAT THE PARAMETER IS NOT SELF
                    # THE PARAM ARRAY SHOULD BE OF THE FOLLOWING FORM ['param_name','param_type']
                    if len(param) > 1:
                        params_to_pass += (
                            f", {param[0]} : {param[1]}"
                            if param == params[-1]
                            else f", {param[0]} : {param[1]}"
                        )

                    else:
                        # if there is more than one item in the parameter array use the second item as a type
                        params_to_pass += (
                            f", {param[0]} : {None}"
                            if param == params[-1]
                            else f", {param[0]} : {None}"
                        )

                    comment += f"""
        {param[0]} : {None if len(param) == 1 else param[1]}
            to be passed as parameter {index + 1}"""

                    # for the last param to comment
                    if param == params[-1]:
                        comment += f'''
        
        Returns
        -------
        {method['return_type']}
        """
        ...
                        '''

            # build initial method
            initial_method += f'''
    {f"@{decorators}" if decorators != "" else ""}
    def {method['signature'].replace("()", "")}(self{params_to_pass}) -> {method['return_type']}:
        """{method['signature'].replace("()", "")} {"has the following params" if method["description"] == "" else method['description']}{comment}  '''

        self.__final_class_representation += initial_method
        return self
