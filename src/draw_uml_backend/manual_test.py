import os
import shutil
from routines import routine

# refresh the output folder
shutil.rmtree(os.path.join(os.getcwd(),"output"))
os.mkdir(os.path.join(os.getcwd(),"output"))

# get the number of objects created
routine(0, existing=True, diagram=True, types=True, code=True, test=True, dataclass=True)