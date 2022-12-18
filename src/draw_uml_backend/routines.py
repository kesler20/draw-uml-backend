from typing import Tuple
import platform
try:
    from draw_uml_backend.class_builder import ClassBuilder
    from draw_uml_backend.code_reader import PythonCodeReader
    from draw_uml_backend.diagram_generator import DiagramGenerator
    from draw_uml_backend.test_builder import TestBuilder
    from draw_uml_backend.source_code import SourceCode
    from draw_uml_backend.types_pre_processing import TypeChecker
except ModuleNotFoundError:
    from src.draw_uml_backend.class_builder import ClassBuilder
    from src.draw_uml_backend.code_reader import PythonCodeReader
    from src.draw_uml_backend.diagram_generator import DiagramGenerator
    from src.draw_uml_backend.test_builder import TestBuilder
    from src.draw_uml_backend.source_code import SourceCode
    from src.draw_uml_backend.types_pre_processing import TypeChecker

if platform.system() == "Linux":
    # for existing code
    response_code_path = r"responses/response.json"
    source_code_path = r"read_only/code_to_read.py"

    # for new code
    new_code_response = r"responses/new_code_response.json"

    # for both new code and existing code
    types_file = r"responses/_types_output.py"

    # diagrams directory
    documentation_path = r"responses/diagrams_output.md"

    # code output file
    code_output_file = r"responses/code_output.py"

    # path to the test file
    test_file_path_io = r"responses/_test_io.py"
    test_file_path_side_effects = r"responses/_test_side_effects.py"
else:
    # for existing code
    response_code_path = r"responses\response.json"
    source_code_path = r"read_only\code_to_read.py"

    # for new code
    new_code_response = r"responses\new_code_response.json"

    # for both new code and existing code
    types_file = r"responses\_types_output.py"

    # diagrams directory
    documentation_path = r"responses\diagrams_output.md"

    # code output file
    code_output_file = r"responses\code_output.py"

    # path to the test file
    test_file_path_io = r"responses\_test_io.py"
    test_file_path_side_effects = r"responses\_test_side_effects.py"


def routine(context: Tuple[str] = (response_code_path,
                                   source_code_path,
                                   new_code_response,
                                   types_file, documentation_path,
                                   code_output_file,
                                   test_file_path_io,
                                   test_file_path_side_effects
                                   ), new=False, existing=False, diagram=False, types=False, code=False, test=False, dataclass=False):
    # parse context into namespace
    response_code_path, source_code_path, new_code_response, types_file, documentation_path, code_output_file, test_file_path_io, test_file_path_side_effects = context
    # format the new_code coming from the API
    src = SourceCode(response_code_path)
    if new:
        src.format_new_code_response(new_code_response, response_code_path)

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
            response_code_path, code_output_file, dataclass)
        class_builder.add_imports("responses._types", type_checker.novel_types).add_class_definition(
        ).add_properties().add_private_fields().add_methods().build_final_class()

    if test:
        cls = TestBuilder(response_code_path, test_file_path_side_effects).add_initial_import().add_class_name().construct_set_up()
        for method in src.methods:
            params = ""
            try:
                for param in method['params']:
                    if param == method['params'][-1]:
                        params += f"{param[0]} : {param[1]}"
                    else:
                        params += f"{param[0]} : {param[1]}, "
            except IndexError:
                pass
            cls.construct_function_side_effects(method['signature'], params, method['return_type'])
        cls.add_tearDown().add_main_function_call().build_test_class()

        cls = TestBuilder(response_code_path, test_file_path_io).add_initial_import().add_class_name().construct_set_up()
        for method in src.methods:
            params = ""
            try:
                for param in method['params']:
                    if param == method['params'][-1]:
                        params += f"{param[0]} : {param[1]}"
                    else:
                        params += f"{param[0]} : {param[1]}, "
            except IndexError:
                pass
            cls.construct_function_io(method['signature'], params, method['return_type'])
        cls.add_tearDown().add_main_function_call().build_test_class()
