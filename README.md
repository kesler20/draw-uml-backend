# DrawUML Backend

the structure of the codebase is characterised by the following main folders:
- python
- typescript
these are where their respective files are stored
then there is a read_only folder where the files are read from
and a response folder where the response to the existing code is written too

## Tests

the only test is the integration test ``test_app.py``

## Improvements
- add an append and a write function to the base class to refactor these out from all the other classes
a potential implementation of the append class
```python
from interfaces.os_interface import File

filename = ""
content = ""
File(filename).append(content)
```
- add a pre-processin stage where you can change the types of the data to the adequaste one
- add the test generation script
- adapt the new code implementations to the new requirements
- improve the design doc generation by adding inheritance
- add the lambda field default_factory on fields where the types are not builtins
- remove the clean up method from the BaseClass