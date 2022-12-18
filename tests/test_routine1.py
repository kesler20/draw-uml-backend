import time
from _test_base import *
import filecmp

msg = '''
Routine 1 includes creating all the files from a new drawUml diagram
/create/new/#
'''
print(msg)


def test_routine1():
    routine((response_code_path,
            source_code_path,
            new_code_response,
            types_file, documentation_path,
            code_output_file,
            test_file_path_io,
            test_file_path_side_effects
             ), new=True, diagram=True, types=True, code=True, test=True, dataclass=True)

    context = [response_code_path,
               source_code_path,
               new_code_response,
               documentation_path, ]
    expected_output_context = [routine_1_expected_output_response_code_path,
                               routine_1_expected_output_source_code_path,
                               routine_1_expected_output_new_code_response,
                               routine_1_expected_output_documentation_path, ]
                               
    for index, filename in enumerate(context):
        with open(filename, "r") as file, open(expected_output_context[index], "r") as expected_file:
            assert file.read() == expected_file.read()