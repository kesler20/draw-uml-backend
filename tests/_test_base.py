import platform
try:
    from draw_uml_backend.class_builder import ClassBuilder
    from draw_uml_backend.code_reader import PythonCodeReader
    from draw_uml_backend.diagram_generator import DiagramGenerator
    from draw_uml_backend.test_builder import TestBuilder
    from draw_uml_backend.source_code import SourceCode
    from draw_uml_backend.types_pre_processing import TypeChecker
    from draw_uml_backend.routines import routine
except ModuleNotFoundError:
    from src.draw_uml_backend.class_builder import ClassBuilder
    from src.draw_uml_backend.code_reader import PythonCodeReader
    from src.draw_uml_backend.diagram_generator import DiagramGenerator
    from src.draw_uml_backend.test_builder import TestBuilder
    from src.draw_uml_backend.source_code import SourceCode
    from src.draw_uml_backend.types_pre_processing import TypeChecker
    from src.draw_uml_backend.routines import routine

# initialise context variables
if platform.system() == "Linux":
    # for existing code
    response_code_path = r"tests/responses/response.json"
    source_code_path = r"tests/read_only/code_to_read.py"

    # for new code
    new_code_response = r"tests/responses/new_code_response.json"

    # for both new code and existing code
    types_file = r"tests/responses/_types.py"

    # diagrams directory
    documentation_path = r"tests/responses/design_doc.md"

    # code output file
    code_output_file = r"tests/responses/code_output.py"

    # path to the test file
    test_file_path_io = r"tests/responses/_test_io.py"
    test_file_path_side_effects = r"tests/responses/_test_side_effects.py"

    # expected_code paths
    # routine 1
    routine_1_expected_output_response_code_path = r"tests/routine_1_expected_output/responses/response.json"
    routine_1_expected_output_source_code_path = r"tests/routine_1_expected_output/read_only/code_to_read.py"

    routine_1_expected_output_new_code_response = r"tests/routine_1_expected_output/responses/new_code_response.json"

    routine_1_expected_output_types_file = r"tests/routine_1_expected_output/responses/_types.py"

    routine_1_expected_output_documentation_path = r"tests/routine_1_expected_output/responses/design_doc.md"

    routine_1_expected_output_code_output_file = r"tests/routine_1_expected_output/responses/code_output.py"

    routine_1_expected_output_test_file_path_io = r"tests/routine_1_expected_output/responses/_test_io.py"
    routine_1_expected_output_test_file_path_side_effects = r"tests/routine_1_expected_output/responses/_test_side_effects.py"

    # routine 2
    routine_2_expected_output_response_code_path = r"tests/routine_2_expected_output/responses/response.json"
    routine_2_expected_output_source_code_path = r"tests/routine_2_expected_output/read_only/code_to_read.py"

    routine_2_expected_output_new_code_response = r"tests/routine_2_expected_output/responses/new_code_response.json"

    routine_2_expected_output_types_file = r"tests/routine_2_expected_output/responses/_types.py"

    routine_2_expected_output_documentation_path = r"tests/routine_2_expected_output/responses/design_doc.md"

    routine_2_expected_output_code_output_file = r"tests/routine_2_expected_output/responses/code_output.py"

    routine_2_expected_output_test_file_path_io = r"tests/routine_2_expected_output/responses/_test_io.py"
    routine_2_expected_output_test_file_path_side_effects = r"tests/routine_2_expected_output/responses/_test_side_effects.py"
else:
    # for existing code
    response_code_path = r"tests\responses\response.json"
    source_code_path = r"tests\read_only\code_to_read.py"

    # for new code
    new_code_response = r"tests\responses\new_code_response.json"

    # for both new code and existing code
    types_file = r"tests\responses\_types.py"

    # diagrams directory
    documentation_path = r"tests\responses\design_doc.md"

    # code output file
    code_output_file = r"tests\responses\code_output.py"

    # path to the test file
    test_file_path_io = r"tests\responses\_test_io.py"
    test_file_path_side_effects = r"tests\responses\_test_side_effects.py"

    # expected_code paths
    # routine 1
    routine_1_expected_output_response_code_path = r"tests\routine_1_expected_output\responses\response.json"
    routine_1_expected_output_source_code_path = r"tests\routine_1_expected_output\read_only\code_to_read.py"

    routine_1_expected_output_new_code_response = r"tests\routine_1_expected_output\responses\new_code_response.json"

    routine_1_expected_output_types_file = r"tests\routine_1_expected_output\responses\_types.py"

    routine_1_expected_output_documentation_path = r"tests\routine_1_expected_output\responses\design_doc.md"

    routine_1_expected_output_code_output_file = r"tests\routine_1_expected_output\responses\code_output.py"

    routine_1_expected_output_test_file_path_io = r"tests\routine_1_expected_output\responses\_test_io.py"
    routine_1_expected_output_test_file_path_side_effects = r"tests\routine_1_expected_output\responses\_test_side_effects.py"

    # routine 2
    routine_2_expected_output_response_code_path = r"tests\routine_2_expected_output\responses\response.json"
    routine_2_expected_output_source_code_path = r"tests\routine_2_expected_output\read_only\code_to_read.py"

    routine_2_expected_output_new_code_response = r"tests\routine_2_expected_output\responses\new_code_response.json"

    routine_2_expected_output_types_file = r"tests\routine_2_expected_output\responses\_types.py"

    routine_2_expected_output_documentation_path = r"tests\routine_2_expected_output\responses\design_doc.md"

    routine_2_expected_output_code_output_file = r"tests\routine_2_expected_output\responses\code_output.py"

    routine_2_expected_output_test_file_path_io = r"tests\routine_2_expected_output\responses\_test_io.py"
    routine_2_expected_output_test_file_path_side_effects = r"tests\routine_2_expected_output\responses\_test_side_effects.py"
