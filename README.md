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
- add the lambda field default_factory on fields where the types are not builtins
- should the tests include an absolute path, or a path generated using the os module
- remove the clean up method from the BaseClass
- increase the scalability of the app by allow it to analys multiple classes
- add an endpoint for dataclas and not dataclass
