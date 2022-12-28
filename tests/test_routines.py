from _test_base import *
import os
import shutil

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
shutil.rmtree(BASE_OUTPUT_DIRECTORY)
os.mkdir(BASE_OUTPUT_DIRECTORY)

def test_routine2():
    routine(0, context=context, existing=True, diagram=True, types=True, code=True, test=True, dataclass=True)

def test_routine1():
    routine(0, context=context, new=True, diagram=True, types=True, code=True, test=True, dataclass=True)
