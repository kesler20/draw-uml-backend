from class_builder import ClassBuilder
from code_reader import PythonCodeReader
from diagram_generator import DiagramGenerator
from test_builder import TestBuilder
from read_only.source_code import SourceCode
from types_pre_processing import TypeChecker

# for existing code
response_code_path = r"responses\existing_code_response.json"
source_code_path = r"read_only\code_to_read.py"
# for new code
new_response_code_path = r"responses\new_code_response.json"
new_source_code_path = r"responses\new_code_converted.json"
# for both new code and existing code
types_file = r"responses\_types.py"
# diagrams directory
documentation_path = "diagrams.md"
# format the new_code coming from the API
src = SourceCode(response_code_path)
src.format_new_code_response(new_response_code_path, new_source_code_path)

# read code from the existing code path
code_reader = PythonCodeReader(response_code_path, source_code_path)
code_reader.read()

# generate types
type_checker = TypeChecker(new_source_code_path, types_file)
type_checker.init_types_file()
type_checker.append_novel_types_to_types_path()
type_checker.generate_types()

# generate diagram
diagram_generator = DiagramGenerator(new_source_code_path, documentation_path)
diagram_generator.init()
diagram_generator.generate_connections()
diagram_generator.generate_classes()

# generate code from the new code path
dataclass = True
class_builder = ClassBuilder(new_source_code_path, "test.py", dataclass)
class_builder.add_imports("responses._types", type_checker.novel_types).add_class_definition(
).add_properties().add_private_fields().add_methods().build_final_class()
