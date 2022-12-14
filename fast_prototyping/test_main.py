
class TestClassBuilder(object):

    def __init__(self, class_name, methods, properties) -> None:
        self.class_name: tuple(str, str) = class_name
        self.methods = methods
        self.properties = properties

    def build_initial_import(self):
        return '''
import unittest
import {}

print("Testing:" + {}.__doc__)
        '''.format(self.class_name[0], self.class_name[0])

    def build_class_name(self) -> str:
        # the class name is a tuple with a name of the class
        # and its class description
        comment = f"'''{self.class_name[1]}'''"
        return '''

class Test_{}(unittest.TestCase):        
    {}
        '''.format(self.class_name[0], comment)

    def build_constructor_head(self) -> str:
        # constructor is a collection of tuples with the name of the method and each type
        constructor_parameters = ""
        for property, property_type in self.properties:
            if self.properties[-1][0] == property:
                constructor_parameters += f" {property}: {property_type}"
            else:
                constructor_parameters += f" {property}: {property_type}, "
        return '''
    def setUp(self,{}) -> None:'''.format(constructor_parameters)

    def build_constructor_body(self) -> str:
        constructor_parameters = ""
        for property, _ in self.properties:
            if property is self.properties[0][0]:
                constructor_parameters += f'''
        self.{self.class_name[0].lower()} = {self.class_name[0]}()'''
            else:
                constructor_parameters += f'''
        self.{property} = {property}
        '''
        return constructor_parameters

    def build_class_methods(self) -> str:
        # methods are tuples with 3 values
        # ( method signature, method description, the return type of the method)
        class_body = ""
        for signature, description, return_type in self.methods:
            description = f"'''{description}'''"
            class_body += f'''
    
    def test_{signature[:signature.find("()")]}(self) -> {return_type}:
        {description}
        pass'''
        return class_body

    def check_types(self, classes: 'list[str]') -> str:
        built_in_types = ["str", "None", "float","dict", "set",
                          "int", "complex", "list", "tuple", "bool"]
        # search for all the other types
        new_classes = ""
        other_types = []
        for _, property_type in self.properties:
            if property_type in built_in_types:
                pass
            else:
                other_types.append(property_type)
        for _, __, method_types in self.methods:
            if method_types in built_in_types:
                pass
            elif method_types in classes:
                pass
            else:
                other_types.append(method_types)
        for property_type in other_types:
            new_classes += f'''
import {property_type}'''
        return new_classes

    def build_tearDown(self):
        return '''
    def tearDown(self):
        pass
        '''

    def build_main_function_call(self):
        return '''
if __name__ == "__main__":
    unittest.main()
        '''


if __name__ == "__main__":
    diagram = [
        [
            {
                "id": "node-1",
                "type": "umlDiagram",
                "position": {"x": 98, "y": 280},
                "data": {
                    "objectName": "Account",
                    "color": "rgb(104, 190, 184)",
                    "comment": "Object Description",
                    "gridTable": [
                        {
                            "visibility": "+",
                            "signature": "username",
                            "type": "str",
                            "comment": "signature description"
                        },
                        {
                            "visibility": "+",
                            "signature": "accountID",
                            "type": "int",
                            "comment": "signature description"
                        },
                        {
                            "visibility": "+",
                            "signature": "channel",
                            "type": "Channel",
                            "comment": "signature description"
                        }
                    ],
                    "connection": False
                },
                "width": 500,
                "height": 222,
                "selected": False,
                "positionAbsolute": {"x": 98, "y": 280},
                "dragging": False
            },
            {
                "id": "node-2",
                "type": "umlDiagram",
                "position": {"x": 885, "y": 98},
                "data": {
                    "objectName": "Channel",
                    "comment": "Object Description",
                    "color": "rgb(72, 14, 183)",
                    "gridTable": [
                        {
                            "visibility": "+",
                            "signature": "channelID",
                            "type": "int",
                            "comment": "signature description"
                        },
                        {
                            "visibility": "+",
                            "signature": "participant",
                            "type": "Account",
                            "comment": "signature description"
                        }
                    ]
                },
                "width": 500,
                "height": 171,
                "selected": True,
                "positionAbsolute": {"x": 885, "y": 98},
                "dragging": False
            }
        ],
        [
            {
                "source": "node-2",
                "sourceHandle": "100aundefined",
                "target": "node-1",
                "targetHandle": "200bundefined",
                "id": "reactflow__edge-node-2100aundefined-node-1200bundefined"
            }
        ]
    ]

    meta_data = diagram[0]
    final_class = ""
    class_names = [object["data"]['objectName'] for object in meta_data]
    for object in meta_data:
        class_name = (object["data"]['objectName'], object["data"]['comment'])
        methods = []
        properties = []
        for method in object["data"]["gridTable"]:
            if method["signature"].find("()") == -1:
                properties.append((method["signature"], method["type"]))
            else:
                methods.append(
                    (method["signature"], method["comment"], method["type"]))

        new_class = TestClassBuilder(class_name, methods, properties)

        if class_name[0] is class_names[0]:
            final_class += new_class.check_types(class_names)
            final_class += new_class.build_initial_import()

        final_class += new_class.build_class_name()
        final_class += new_class.build_constructor_head()
        final_class += new_class.build_constructor_body()
        final_class += new_class.build_class_methods()
        final_class += new_class.build_tearDown()

        if class_name[0] is class_names[-1]:
            final_class += new_class.build_main_function_call()

        with open('test_file.py', "w") as f:
            f.write(final_class)

# TODO: implement parameters for functions and default values for those parameters
