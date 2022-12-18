# DrawUML Backend

# Design Overview

The software can be divided in this 3 main layers
The dataprocessing layer processes the classes which arrive from the front end one by one
the file generation layer generates the files such as the diagram file and the _types file
this cna be organised by routines such that makes the design more modular and easily testable


<div style="display: flex; justify-content: center; align-items: center; width: 100%;">
  <img src="/software_architecture.jpg" alt="draw uml schema" srcset="" style="width: 50%;">
</div>

The api endpoints can foolow the following convention
``/method/version/file_type/file_type_metadata``
for instance:
``/create/new/diagram``
``get/existing/python/code``
``create/new/python/type``

## Tests
the only test is the integration test `test_app.py`

## Improvements

- [ ] add the lambda field default_factory on fields where the types are not builtins
- [ ] should the tests include an absolute path, or a path generated using the os module
- [ ] remove the clean up method from the BaseClass
- [ ] increase the scalability of the app by allow it to analys multiple classes
- [ ] add an endpoint for dataclas and not dataclass
- [ ] the structure of the codebase can be characterised by having a `python` folder and a `typescript` folder at the root
      these are where their respective files are stored
      then there is a read_only folder where the files are read from
      and a response folder where the response to the existing code is written too
