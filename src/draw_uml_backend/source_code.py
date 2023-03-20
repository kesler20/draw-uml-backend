from pathlib import Path
from typing import List, Callable, Collection, Any, Dict, Union
from draw_uml_backend.file import File
from draw_uml_backend._types import ClassRepresentation, CreateClassResponse, MethodRepresentation


default_methods: List[MethodRepresentation] = [
    {"signature": "", "params": [[""]], "decorator": "", "return_type": "str", "description": "str"}
]

default_class: ClassRepresentation = {
    "class_name": "",
    "description": "",
    "methods": default_methods,
    "fields": [{0: "", 1: ""}],
    "properties": [],
}


class SourceCode:
    def __init__(self, response_code_path: str) -> None:
        self.response_code_path = Path(response_code_path)
        self.source: ClassRepresentation = self.__read_and_clean_source()
        self.class_name = self.source["class_name"]
        self.description = self.source["description"]
        self.methods = self.source["methods"]
        self.fields = self.source["fields"]
        self.properties = self.source["properties"]

    def __my_filter(self, cb: Callable[[Any], Any], arr: Collection[Any]) -> Any:
        return filter(cb, arr)

    def __read_and_clean_source(self) -> ClassRepresentation:
        """read one class at a time, then pop from the array
        do the required cleanups and preprocessing of the class"""

        # remove the end of line delimiter from every line of the response_code file (json file)
        try:
            source: ClassRepresentation = File(self.response_code_path).get_json()[0]
            return source
        except KeyError:
            File(self.response_code_path).write_json(default_class)
            default_source: ClassRepresentation = File(self.response_code_path).get_json()
            return default_source

    def format_new_code_response(self, new_code_response: str, new_code_converted: str, n: int):
        global default_class

        # get the file content
        content: List[List[CreateClassResponse]] = File(Path(new_code_response)).get_json()
        # initialise the intermediary class representation
        default_classes: List[ClassRepresentation] = []
        class_object = content[0][n]["data"]

        # get the class name and description
        default_class["class_name"] = class_object["objectName"]
        default_class["description"] = class_object["comment"]

        # get the class methods from the class_object gridTable
        # class_object is of type CreateClassResponseData
        public_methods = list(
            self.__my_filter(
                lambda item: item["signature"].find("()") != -1
                and item["visibility"].find("+") != -1,
                class_object["gridTable"],
            )
        )
        private_methods = list(
            self.__my_filter(
                lambda item: item["signature"].find("()") != -1
                and item["visibility"].find("-") != -1,
                class_object["gridTable"],
            )
        )

        default_class["methods"] = public_methods
        for method in private_methods:
            method["signature"] = f"__{method['signature']}"
            default_class["methods"].append(method)

        # get the properties and the private fields
        default_class["properties"] = list(
            self.__my_filter(
                lambda item: item["visibility"].find("+") != -1
                and item["signature"].find("()") == -1,
                class_object["gridTable"],
            )
        )
        default_class["fields"] = list(
            self.__my_filter(
                lambda item: item["visibility"].find("-") != -1
                and item["signature"].find("()") == -1,
                class_object["gridTable"],
            )
        )
        default_classes.append(default_class)

        clean_classes = []
        for default_class in default_classes:
            signature = []
            properties = []
            fields = []
            for method in default_class["methods"]:
                signature_object: MethodRepresentation = {
                    "signature": "",
                    "params": [],
                    "decorator": "",
                    "return_type": "",
                    "description": "",
                }
                signature_object["signature"] = method["signature"].replace("()", "")
                signature_object["description"] = method["comment"]
                signature_object["params"] = [
                    [params["name"], params["type"]] for params in method["params"]
                ]
                signature_object["decorator"] = ""
                signature_object["return_type"] = method["returnType"]

                signature.append(signature_object)

            for property in default_class["properties"]:
                properties.append([property["signature"], property["returnType"]])

            for field in default_class["fields"]:
                fields.append([field["signature"], field["returnType"]])

            default_class["methods"] = signature
            default_class["properties"] = properties  # type: ignore [typeddict-item]
            default_class["fields"] = fields  # type: ignore [typeddict-item]
        clean_classes.append(default_class)

        File(Path(new_code_converted)).write_json(clean_classes)
        print(clean_classes)
