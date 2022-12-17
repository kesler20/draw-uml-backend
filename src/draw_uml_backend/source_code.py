from pathlib import Path
from typing import List, Callable, Collection, Any, Dict
from draw_uml_backend.file import File
from draw_uml_backend._types import ClassRepresentation, CreateClassResponse, MethodRepresentation


default_class = {
    "class_name": "",
    "description": "",
    "methods": [
        {
            "signature": "",
            "params": [[""]],
            "decorator": "",
            "return_type": "str"
        }],
    "fields": [["", ""]],
    "properties": []
}


class SourceCode:
    def __init__(self, response_code_path: str) -> None:
        self.response_code_path = Path(response_code_path)
        self.source: ClassRepresentation = self.read_and_clean_source()
        self.class_name = self.source['class_name']
        self.description = self.source['description']
        self.methods = self.source['methods']
        self.fields = self.source['fields']
        self.properties = self.source['properties']

    def my_filter(self, cb: Callable[[Any], Any], arr: Collection[Any]) -> Any:
        return filter(cb, arr)

    def format_new_code_response(self, new_code_response: str, new_code_converted: str):
        global default_class
        content: List[List[CreateClassResponse]] = File(
            Path(new_code_response)).get_json()
        default_classes : List[ClassRepresentation] = []

        for class_object_with_metadata in content[0]:
            class_object = class_object_with_metadata['data']
            default_class['class_name'] = class_object['objectName']
            default_class['description'] = class_object['comment']
            default_class['methods'] = list(self.my_filter(
                lambda item: item['signature'].find("()") != -1, class_object['gridTable']))
            default_class['properties'] = list(self.my_filter(
                lambda item: item['visibility'].find("+") != -1, class_object['gridTable']))
            default_class['fields'] = list(
                self.my_filter(lambda item: item['visibility'].find("-") != -1, class_object['gridTable']))
            default_classes.append(default_class)

        clean_classes = []
        for default_class in default_classes:
            signature = []
            properties = []
            fields = []
            for method in default_class['methods']:
                signature_object: MethodRepresentation = {
                    'signature': "", 'params': [], "decorator": "", "return_type": ""}
                signature_object['signature'] = method["signature"].replace(
                    "()", "")
                signature_object['description'] = method['comment']
                signature_object['params'] = [[params['name'], params['type']]
                                              for params in method['params']]
                signature_object['decorator'] = ""
                signature_object['return_type'] = method['returnType']
                signature.append(signature_object)

            for property in default_class['properties']:
                properties_object = []
                properties_object = [[params['name'], params['type']]
                                     for params in property['params']]
                # properties_object[0].append(property['comment'])
                properties.append(properties_object[0])

            for field in default_class['fields']:
                fields_object = []
                fields_object = [[params['name'], params['type']]
                                 for params in field['params']]
                # fields_object[0].append(field['comment'])
                fields.append(fields_object[0])

            default_class['methods'] = signature
            default_class['properties'] = properties
            default_class['fields'] = fields
        clean_classes.append(default_class)

        File(Path(new_code_converted)).write_json(clean_classes)
        print(clean_classes)

    def read_and_clean_source(self) -> ClassRepresentation:
        """read one class at a time, then pop from the array
        do the required cleanups and preprocessing of the class"""

        # remove the end of line delimiter from every line of the response_code file (json file)
        try:
            source: ClassRepresentation = File(
                self.response_code_path).get_json()[-1]
            return source
        except IndexError:
            File(self.response_code_path).write_json(default_class)
            default_source: ClassRepresentation = File(
                self.response_code_path).get_json()[-1]
            return default_source
