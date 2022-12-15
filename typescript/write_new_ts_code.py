

class UserInputClassifier(object):

    def __init__(self, object_name, signatures):
        self.object_name = object_name
        self.signatures = signatures


class JsClassBuilder(object):

    def __init__(self, class_name, methods, properties) -> None:
        self.class_name = class_name
        self.methods = methods
        self.properties = properties

    def build_class_name(self, first_class_in_programme: bool) -> str:
        # the class name is a tuple with a name of the class
        # and its class description
        if first_class_in_programme:
            return '''
/*
* {}
*/
export default class {} {}'''.format(self.class_name[1], self.class_name[0], "{")
        else:
            return '''
/*
* {}
*/
export class {} {}'''.format(self.class_name[1], self.class_name[0], "{")

    def build_constructor_head(self) -> str:
        # constructor is a collection of tuples with the name of the method and each type
        constructor_parameters = ""
        for property, property_type in self.properties:
            if self.properties[-1][0] == property:
                constructor_parameters += f" {property}"
            else:
                constructor_parameters += f" {property},"
        return '''
    constructor({}) {}'''.format(constructor_parameters, "{")

    def build_constructor_body(self) -> str:
        constructor_parameters = ""
        for property, _ in self.properties:
            if self.properties[-1][0] == property:
                constructor_parameters += '''
        this.{} = {};
    {}'''.format(property, property, "}")
            else:
                constructor_parameters += f'''
        this.{property} = {property};'''
        return constructor_parameters

    def build_class_methods(self) -> str:
        # methods are tuples with 3 values
        # ( method signature, method description, the return type of the method)
        class_body = ""
        for signature, description, return_type in self.methods:
            class_body += '''
    
    /*
    * {}
    */
    {}() {}
        return;
    {}'''.format(description, signature[:signature.find('()')], "{", "}")
        return class_body + '''
}
'''


if __name__ == "__main__":
    # generate the user input
    methods = [("foo", "this is the description of foo", "str"), ("fizz",
                                                                  "this is the description of fizz", "str"), ("buzz", "this is the description of buzz", "int")]
    class_name = ('BuiltClassName',
                  "This is a class which is built using the ClassBuilder")
    properties = [("client", "str"),
                  ("subscription", "str"), ("status", "str")]
    new_class = JsClassBuilder(class_name, methods, properties)
    final_class = ""
    final_class += new_class.build_class_name()
    final_class += new_class.build_constructor_head()
    final_class += new_class.build_constructor_body()
    final_class += new_class.build_class_methods()

    with open('file.js', "w") as f:
        f.write(final_class)


# TODO: implement parameters for functions and default values for those parameters
