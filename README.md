# DrawUML Backend

## Design Overview

The software can be divided in this 3 main layers
The dataprocessing layer processes the classes which arrive from the front end one by one
the file generation layer generates the files such as the diagram file and the _types file
this can be organised by routines such that makes the design more modular and easily testable

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

## Note

for generating class diagrams you can also run 
```python
pyreverse -o png -p draw_uml_backend src/draw_uml_backend
```

make sure that you have Graphviz installed if you don't run
```linux
sudo apt-get install graphviz
```

### Using the drawSQL plugin

for automating the  generation of `SQLAlchemy` classes from `drawSQL` we assume that relationships 
are built into the tables i.e 

<div style="display:flex; justify-content: center; align-items: center; width: 100%;">
  <img style="width: 50%;" src="/img/drawSQL-documentation-export-2023-03-24 (1).png" alt="" srcset="">
</div>

therefore we want to keep tables in singular i.e. `User` and in camel notation 
such as `UnitOperation`, have foreign keys map to ids of other tables and to be named `<table_reference>_id` and to set columns 
which map to other tables i.e. if I want to pass an `owner` which is a user object to an `Item` class
```python
item = Item(owner=User(name="Paul"))
```
then we can name the column with a leading slash i.e. `owner_`. This will map to generating a `relationship`
on the class which are used to pass objects rather than values

Example of using the database models generated through the drawSQL function

```python
Session = sessionmaker(bind=create_engine(
    f"sqlite:///__main__.sqlite3", echo=True))

session = Session()
names = [
    {"name": "Mark"},
    {"name": "Luci"},
    {"name": "Julia"}
]

users = [User(**name) for name in names]
items = [Items(user) for user in users]

session.add_all(users)
session.add_all(items)
session.commit()

users: List[User] = session.query(User).all()
print([user.name for user in users])
for user in users:
    print(user.items)
```

For modifying the `schema.py` generated file add a property that is unique within the table on the `TableCreate` object of the schema.
Add a property on the constructor for all the rows which are `relationships` in tables which have a foreignkey, this will allow to relate
the table to at least one of its foreign table as the argument will be required tio be passed.

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

- [ ] the structure of the codebase can be characterised by having a `python` folder and a `typescript` folder at the root
      these are where their respective files are stored
      then there is a read_only folder where the files are read from
      and a response folder where the response to the existing code is written too
- [ ]	add typescript React code
- [ ]	add typescript classes
- [ ] add a TypedDict with the second table in the database in the server generation functioon to allow the first table to 
      reference the second in the constructor

```python
class User(TypedDict):
    name : str
```
