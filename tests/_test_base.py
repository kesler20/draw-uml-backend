import os
from draw_uml_backend.routines import routine

# for existing code
response_code_path = os.path.join("tests", "responses", "response.json")
source_code_path = os.path.join("tests", "read_only", "code_to_read.py")
# for new code
new_code_response = os.path.join("tests", "responses", "new_code_response.json")

# for the test output response
OUTPUT_RESPONSE = os.path.join("tests","test_output")

# for both new code and existing code
types_file = os.path.join(OUTPUT_RESPONSE, "_types.py")

# diagrams directory
documentation_path = os.path.join(OUTPUT_RESPONSE, "design_doc.md")

# expected results
expected_result_routine1 = os.path.join("tests", "routine_1_expected_result.txt")
expected_result_routine2 = os.path.join("tests", "routine_2_expected_result.txt")