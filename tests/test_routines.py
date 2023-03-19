from _test_base import *
import os
import shutil
from draw_uml_backend.file import File
from pathlib import Path

msg = '''
Routine 1 includes creating all the files from a new drawUml diagram
/create/new/#
'''
print(msg)

msg = '''
Routine 2 includes creating all the files from an existing source code pasted from the drawUml diagram
to the code to read file
/create/new/#
'''
print(msg)

context = (response_code_path,
           source_code_path,
           new_code_response,
           types_file, documentation_path,
           )

# refresh output folder
shutil.rmtree(OUTPUT_RESPONSE)
os.mkdir(OUTPUT_RESPONSE)


def test_routine2():
    routine(0, context=context, existing=True, diagram=True, types=True, code=True, test=True, dataclass=True)
    # assert File(Path(expected_result_routine2)).readlines() == File(Path(types_file)).readlines()

def test_routine1():
    routine(0, context=context, new=True, diagram=True, types=True, code=True, test=True, dataclass=True)
    assert File(Path(expected_result_routine1)).readlines() == File(Path(documentation_path)).readlines()