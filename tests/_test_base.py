import os
try:
    from draw_uml_backend.routines import routine
except ModuleNotFoundError:
    from src.draw_uml_backend.routines import routine

# for existing code
response_code_path = os.path.join("tests", "responses", "response.json")
source_code_path = os.path.join("tests", "read_only", "code_to_read.py")
# for new code
new_code_response = os.path.join("tests", "responses", "new_code_response.json")

# for both new code and existing code
types_file = os.path.join("test_output", "_types.py")

# diagrams directory
documentation_path = os.path.join("test_output", "design_doc.md")

BASE_OUTPUT_DIRECTORY = "test_output"