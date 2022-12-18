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