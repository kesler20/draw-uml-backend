import json
from typing import Dict, List
import os
import time

FILENAME = "test.md"

with open("existing_code_response.json", "r") as file:
    data = json.loads(file.read())

metadata: Dict = data[0]

os.remove(FILENAME)


class DiagramBuilder(object):

    def __init__(self, metadata, output_filename) -> None:
        self.class_name = metadata['class name']
        self.description = metadata['description']
        self.methods = metadata['methods']
        self.fields = metadata['fields']
        self.properties = metadata['properties']
        self.output_file = output_filename

    def init(self):
        """This method should be called first"""
        initial_layout = '''

```mermaid
classDiagram'''
        with open(self.output_file, "a") as out:
            out.seek(1)
            out.write("# Design Overview")
            out.write(initial_layout)

    def generate_connections(self):
        connections = '''
   Person <|-- Student
'''
        with open(self.output_file, "a") as out:
            out.write(connections)

    def generate_classes(self):
        """this method should be called last"""
        name = self.class_name
        methods = [(method['signature'], method['return type'])
                   for method in self.methods]
        properties = [(props, props_type)
                      for props, props_type in self.properties]
        fields = [(field, field_type)
                  for field, field_type in self.fields]

        final_class = ""
        for prop, prop_type in properties:
            final_class += """
   {} : +{} {}""".format(name, prop, prop_type)

        for field, field_type in fields:
            final_class += """
   {} : -{} {}""".format(name, field, field_type)

        for method, return_type in methods:
            final_class += """
   {} : +{}() {}""".format(name, method, return_type)

        final_class += """
```
        """
        with open(self.output_file, "a") as out:
            out.write(final_class)


cls = DiagramBuilder(metadata, FILENAME)
cls.init()
cls.generate_classes()
