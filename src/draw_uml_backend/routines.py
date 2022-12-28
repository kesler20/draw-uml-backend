from typing import Tuple
import os
try:
    from class_builder import ClassBuilder
    from code_reader import PythonCodeReader
    from diagram_generator import DiagramGenerator
    from test_builder import TestBuilder
    from source_code import SourceCode
    from types_pre_processing import TypeChecker
    from _base import BASE_OUTPUT_RESPONSE_PATH
except ModuleNotFoundError:
    try:
        from draw_uml_backend.class_builder import ClassBuilder
        from draw_uml_backend.code_reader import PythonCodeReader
        from draw_uml_backend.diagram_generator import DiagramGenerator
        from draw_uml_backend.test_builder import TestBuilder
        from draw_uml_backend.source_code import SourceCode
        from draw_uml_backend.types_pre_processing import TypeChecker
        from draw_uml_backend._base import BASE_OUTPUT_RESPONSE_PATH
    except ModuleNotFoundError:
        from src.draw_uml_backend.class_builder import ClassBuilder
        from src.draw_uml_backend.code_reader import PythonCodeReader
        from src.draw_uml_backend.diagram_generator import DiagramGenerator
        from src.draw_uml_backend.test_builder import TestBuilder
        from src.draw_uml_backend.source_code import SourceCode
        from src.draw_uml_backend.types_pre_processing import TypeChecker
        from src.draw_uml_backend._base import BASE_OUTPUT_RESPONSE_PATH

# for existing code
response_code_path = os.path.join("responses", "response.json")
source_code_path = os.path.join("read_only", "code_to_read.py")
# for new code
new_code_response = os.path.join("responses", "new_code_response.json")

# for both new code and existing code
types_file = os.path.join(BASE_OUTPUT_RESPONSE_PATH, "_types.py")

# diagrams directory
documentation_path = os.path.join(BASE_OUTPUT_RESPONSE_PATH, "design_doc.md")


def routine(object_id, context: Tuple[str] = (response_code_path,
                                              source_code_path,
                                              new_code_response,
                                              types_file, documentation_path,
                                              ), new=False, existing=False, diagram=False, types=False, code=False, test=False, dataclass=False):
    # parse context into namespace
    response_code_path, source_code_path, new_code_response, types_file, documentation_path = context
    # format the new_code coming from the API
    src = SourceCode(response_code_path)
    if new:
        src.format_new_code_response(new_code_response, response_code_path, object_id)

    # read code from the existing code path
    code_reader = PythonCodeReader(source_code_path, response_code_path)
    if existing:
        code_reader.read()

    # generate types
    if types:
        type_checker = TypeChecker(response_code_path, types_file)
        type_checker.init_types_file()
        type_checker.append_novel_types_to_types_path()
        type_checker.generate_types()

    # generate diagram
    if diagram:
        diagram_generator = DiagramGenerator(
            response_code_path, documentation_path)
        diagram_generator.init()
        diagram_generator.generate_connections()
        diagram_generator.generate_classes()

    # generate code from the new code path
    if code:
        class_builder = ClassBuilder(
            response_code_path, dataclass)
        class_builder.add_imports(f"{BASE_OUTPUT_RESPONSE_PATH}._types", type_checker.novel_types).add_class_definition(
        ).add_properties().add_private_fields().add_methods().build_final_class()

    if test:
        TestBuilder(response_code_path, "io").add_initial_import().add_class_name().construct_set_up(
        ).add_functions().add_tearDown().add_main_function_call().build_test_class()

        TestBuilder(response_code_path, "side effects").add_initial_import().add_class_name().construct_set_up(
        ).add_functions().add_tearDown().add_main_function_call().build_test_class()

        TestBuilder(response_code_path, "manual test").add_initial_import().add_manual_tests().build_test_class()
