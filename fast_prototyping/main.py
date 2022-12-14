

class UserInputClassifier(object):

    def __init__(self, object_name, signatures):
        self.object_name = object_name
        self.signatures = signatures


class ClassBuilder(object):

    def __init__(self, class_name, methods, properties) -> None:
        self.class_name = class_name
        self.methods = methods
        self.properties = properties

    def build_class_name(self) -> str:
        # the class name is a tuple with a name of the class
        # and its class description
        comment = f"'''{self.class_name[1]}'''"
        return '''

class {}(object):        
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
    def __init__(self,{}) -> None:'''.format(constructor_parameters)

    def build_constructor_body(self) -> str:
        constructor_parameters = ""
        for property, _ in self.properties:
            constructor_parameters += f'''
        self.{property} = {property}'''
        return constructor_parameters

    def build_class_methods(self) -> str:
        # methods are tuples with 3 values
        # ( method signature, method description, the return type of the method)
        class_body = ""
        for signature, description, return_type in self.methods:
            description = f"'''{description}'''"
            class_body += f'''
    
    def {signature[:signature.find("()")]}(self) -> {return_type}:
        {description}
        pass'''
        return class_body

    def check_types(self, classes: 'list[str]') -> str:
        built_in_types = ["str", "None", "float","dict","set"
                          "int", "complex", "list", "tuple", "bool"]
        # search for all the other types
        new_classes = ""
        other_types = []
        for _, property_type in self.properties:
            if property_type in built_in_types:
                pass
            elif property_type in classes:
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

class {property_type}(object):
    pass            
    '''
        return new_classes

# TODO: implement parameters for functions and default values for those parameters
