from dataclasses import dataclass

try:
    from _base import BaseReader
except ModuleNotFoundError:
    try:
        from draw_uml_backend._base import BaseReader
    except ModuleNotFoundError:
        from src.draw_uml_backend._base import BaseReader


@dataclass
class DiagramGenerator(BaseReader):
    """To use the diagram generator do the following
    ```python        
    cls = DiagramBuilder(metadata, FILENAME)
    cls.init()
    cls.generate_connections()
    cls.generate_classes()
    ```
    """

    output_file: str

    def init(self):
        self.clean_up(self.output_file)
        """This method should be called first"""
        initial_layout = """

```mermaid
classDiagram"""
        with open(self.output_file, "a") as out:
            out.write(initial_layout)

    def generate_connections(self):
        # the default dependant class is object
        dependent_class = "object"
        # check if the name has a class Name(DependantClass)
        if self.source.class_name.find("(") != -1:
            dependent_class = self.source.class_name.split("(")[1].split(")")[0]

        connections = """
   {} <|-- {}""".format(
            self.source.class_name, dependent_class
        )
        with open(self.output_file, "a") as out:
            out.write(connections)

    def generate_classes(self):
        """this method should be called last"""
        name = self.source.class_name
        methods = [(method["signature"], method["return_type"]) for method in self.source.methods]
        properties = [
            (props, props_type.split("=")[0].replace(" ", ""))
            for props, props_type in self.source.properties
        ]
        fields = [
            (field, field_type.split("=")[0].replace(" ", ""))
            for field, field_type in self.source.fields
        ]

        final_class = ""
        for prop, prop_type in properties:
            final_class += """
   {} : + {} {}""".format(
                name, prop, prop_type
            )

        for field, field_type in fields:
            final_class += """
   {} : - {} {}""".format(
                name, field, field_type
            )

        for method, return_type in methods:
            final_class += """
   {} : + {}() {}""".format(
                name, method, return_type
            )

        final_class += """
```
        """
        with open(self.output_file, "a") as out:
            out.write(final_class)
