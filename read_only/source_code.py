from pathlib import Path
from typing import List
from interfaces.os_interface import File
from _types import ClassRepresentation

default_class = [
    {
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
]


class SourceCode:
    def __init__(self, response_code_path: str) -> None:
        self.response_code_path = Path(response_code_path)
        self.source: ClassRepresentation = self.read_and_clean_source()
        self.class_name = self.source['class_name']
        self.description = self.source['description']
        self.methods = self.source['methods']
        self.fields = self.source['fields']
        self.properties = self.source['properties']

    def format_new_code_response(self):
        ...

    def read_and_clean_source(self) -> ClassRepresentation:
        """read one class at a time, then pop from the array
        do the required cleanups and preprocessing of the class"""

        # remove the end of line delimiter from every line of the response_code file (json file)
        try:
            source: ClassRepresentation = File(self.response_code_path).get_json()[-1]
            return source
        except IndexError:
            File(self.response_code_path).write_json(default_class[0])
            default_source: ClassRepresentation = File(self.response_code_path).get_json()[-1]
            return default_source



