# DrawUML Backend

# Design Overview

The software can be divided in this 3 main layers
The dataprocessing layer processes the classes which arrive from the front end one by one
the file generation layer generates the files such as the diagram file and the _types file
this cna be organised by routines such that makes the design more modular and easily testable

<div style="display: flex; justify-content: center; align-items: center; width: 100%;">
  <img src="/img/software_architecture.jpg" alt="draw uml schema" srcset="" style="width: 50%;">
</div>

The api endpoints can foolow the following convention
``/method/version/file_type/file_type_metadata``
for instance:
``/create/new/diagram``
``get/existing/python/code``
``create/new/python/type``

in the source code the response_code_path refers to the json generated from the existing source code
new_response code path is the json generated from the UI and this should be converted into the
response_code_path into the common format  

## Tests

the only test is the integration test `test_routines.py` however a better way to test the code is to run the gunicorn instance locally, and then either copy and paste the response of the diagram from the frontend
or copy the code that you want to paste as existing code
to check the files being downloaded you can do it directly on the browser by opening the file on a seperate window
to run automatic tests

>to run manual tests
```bash
python -m pytest tests
```

>to run manual tests
```bash
python src\draw_uml_backend\manual_test.py
```

## Improvements

- [ ] add the lambda field default_factory on fields where the types are not builtins
- [ ] the structure of the codebase can be characterised by having a `python` folder and a `typescript` folder at the root
      these are where their respective files are stored
      then there is a read_only folder where the files are read from
      and a response folder where the response to the existing code is written too
- [ ] make the system type safe and make the tests
- [ ] when you submit existing code and the fields are already assignerd, the assignment statement is considered as a type
- [ ] when you submit existing code and the fields are already assigned, the assignment statement is considered as a type
for instance import _base.filename if the test class needs to be called with a filename variable, the user will then be able to pass all those variables from the _base file which should also be downloaded
- [ ] include guard clauses on public methods ?
- [ ] remove self from the existing file response as it complicates other things down the line
- [ ] this can be further improved by allowing the user to choose what to create:
```python
@app.post('/create/{format}/files/{dataclasses}/{with_types}')
async def create_new_diagram(dataclasses: bool,format: bool, with_types: bool, diagram=Body(...)):
    # refresh the output folder
    shutil.rmtree(BASE_OUTPUT_RESPONSE_PATH)
    os.mkdir(BASE_OUTPUT_RESPONSE_PATH)
    # write the diagram to the new code response  code path
    File(Path(new_code_response)).write_json(diagram)
    # get the number of objects created
    for object_id in range(len(diagram[0])):
        routine(object_id, new=format, diagram=True, types=with_types, code=True, test=True,dataclass=dataclasses)
    return {"response": "okay"}
```

this would then correlate to radio buttons from the client side which will generate the required request
Improve the drawUML:
- [ ]	making simpler tests using pytest (the goal is to test IO using pytest to test for types and states of the functions, test side effects (the contracts of the class), test edge cases)
- [ ]	making less dependencies
- [ ]	add a Flask server to try to return a folder
- [ ]	add the toggle on and off for the code with data classes
- [ ]	add typescript React code
- [ ]	add Sqlalchemy data-type converter
