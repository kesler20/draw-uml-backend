from class_builder import ClassBuilder
from code_reader import PythonCodeReader
from diagram_generator import DiagramGenerator
from test_builder import TestBuilder
from read_only.source_code import SourceCode
from types_pre_processing import TypeChecker

response_code_path = r"responses\existing_code_response.json"
source_code_path = r"read_only\code_to_read.py"

code_reader = PythonCodeReader(source_code_path, response_code_path)
src = SourceCode(response_code_path)
type_checker = TypeChecker()
type_checker.generate_types()
