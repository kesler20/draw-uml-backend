from _test_base import *

msg = '''
Routine 2 includes creating all the files from an existing source code pasted from the drawUml diagram
to the code to read file
/create/new/#
'''
print(msg)


def test_routine2():
    routine((response_code_path,
            source_code_path,
            new_code_response,
            types_file, documentation_path,
            code_output_file,
            test_file_path_io,
            test_file_path_side_effects
             ), existing=True, diagram=True, types=True, code=True, test=True, dataclass=True)
