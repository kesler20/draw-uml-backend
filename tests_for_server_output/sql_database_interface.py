from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import Any, Optional, List


class SQLDatabaseInterface:
    """The SQLDatabaseInterface allows to implement CRUD operations on the tables of an SQL database.
    This is dove via SQLAlchemy tables which are the ORMs in python.

    initialise the SQLDatabaseInterface in two main ways:

    Example
    -------
    using a fastapi application
    where the dependencies are the following
    ```python
    SQLALCHEMY_DATABASE_URL = "sqlite:///python_template.sqlite3"
    engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    # ========== YIELD DATABASE CONNECTION ============
    def get_db():
        try:
            db = SessionLocal()
            yield db
        finally:
            db.close()


    # note: normally you'd want to use migrations
    Base.metadata.create_all(bind=engine)
    ```

    As such the class can be instantiated in the server logic as follows

    ```python
    # create a mew user
    @app.post("/users/", response_model=schema.User)
    async def create_user(user: schema.UserCreate, db: Session = Depends(get_db)):
        # hash password before storing it
        hashed_password = hash_password(user.password)
        db_user = sql_db_interface.add_value(models.User(email=user.email, hashed_password=hashed_password))
        return db_user
    ```
    """

    def __init__(self, db_name: str = "python_template") -> None:
        SQLALCHEMY_DATABASE_URL = f"sqlite:///{db_name}.sqlite3"
        engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False},echo=True)

        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

        # note: normally you'd want to use migrations
        self.engine = engine
        self.session = SessionLocal()

    def __enter__(self) -> Any:
        return self

    def __exit__(self, *args) -> None:
        """close the session to allow other processes to access the database"""
        self.session.close()

    def add_value(self, new_row: Any) -> Any:
        """add_value this method will add a row to the given table. i.e.

        ## Example
        ```python
        new_row = User(name='Alice', age=30)
        session = SQLDatabaseInterface()
        session.add_value(new_row)
        ```

        Parameters
        ---

        new_row Any
            this is the instance of the table class that we want to insert
            i.e. new_user = User(name='Alice')

        Returns
        ---
        result: None
        """
        # Insert a new row into the table
        self.session.add(new_row)
        self.session.commit()
        self.session.refresh(new_row)
        return new_row
    
    def add_values(self,class_table: Any, new_row: List[Any]) -> List[Any]:
        """add_values this method will add a row to the given table. i.e.

        ## Example
        ```python
        new_row = User(name='Alice', age=30)
        session = SQLDatabaseInterface()
        session.add_values(new_row)
        ```

        Parameters
        ---

        new_row Any
            this is the instance of the table class that we want to insert
            i.e. new_user = User(name='Alice')

        Returns
        ---
        result: None
        """
        # Insert a new row into the table
        self.session.add_all(new_row)
        self.session.commit()
        return self.read_all_values(class_table)
    
    def update_value(self, class_table: Any, key: str, value: Any, **kwargs: Any) -> Any:
        """update_value will update a record in the table

        ## Example
        ```python
        # this line will update the record email from Kesler to0 John
        session.update_value(database.User, "email", "John", email="Kesler")
        ```
        
        Parameters
        ----------
        class_table : Any
            this is the table of the database that the record we want
            to update is in
        
        key : str
            the column of the record we want to update
        value : Any
            the updated value of the record
        
        kwargs : Any
            key value pairs used to locate the record in the database
        
        Returns
        -------
        Any
            return all the new values of the database
        """
        self.session.query(class_table).filter_by(**kwargs).update({key: value})
        self.session.commit()
        return self.read_all_values(class_table)


    def read_value(self, class_table: Any, **kwargs: Any) -> Optional[Any]:
        """read_value this will read a specific value (row) from the given table.

        # Example
        ```python
        session = SQLDatabaseInterface()
        session.read_value(User,name="Mark")
        ```

        Parameters
        ---

        class_table type
            this is the name of the class of the table i.e. User
        **kargs tuple
            this is the key value pair that we want to use for our query i.e.
            name='Paul'

        Returns
        ---
        result: tuple
            this will return all the records which meet the given conditions, i.e.
            if we are looking for name='Paul' it will return all the rows with the name 'Paul'
        """
        row = self.session.query(class_table).filter_by(**kwargs).first()
        if row is None:
            return None
        self.session.refresh(row)
        return row

    def read_all_values(self, class_table: Any) -> Any:
        """read_all_values this method will read all the values from the SQL table

        # Example
        ```python
        sesion = SQLDatabaseInterface()
        session.read_all_values(User)
        ```

        Parameters
        ---

        class_table type
            this is the name of the class of the table i.e. User

        Returns
        ---
        result: Any
        """
        # Query for all rows in the table
        return self.session.query(class_table).all()

    def read_all_values_with_pagination(
        self, class_table: Any, number_of_objects_per_page: int, current_page_number: int
    ) -> Any:
        """`read_all_values_with_pagination` this method will read all the values from the SQL table

        # Example
        ```python
        sesion = SQLDatabaseInterface()
        session.read_all_values_with_pagination(User)
        ```

        Parameters
        ---

        class_table type
            this is the name of the class of the table i.e. User

        Returns
        ---
        result: Any
        """
        offset_number = (current_page_number - 1) * number_of_objects_per_page
        return (
            self.session.query(class_table)
            .offset(offset_number)
            .limit(number_of_objects_per_page)
            .all()
        )

    def delete_all_values(self, class_table: Any) -> None:
        """delete_value this method can be used to delete a specific value on the table or all the values which meet a specific condition.
        the row can be identified with a key value pair.

        ## Example
        ```python
        session = SQLDatabaseInterface()
        session.delete_value(User,name="Paula")
        ```

        Parameters
        ---

        class_table type
            this is the name of the class of the table i.e. User
        **kargs tuple
            this is the key value pair that we want to use for our query i.e.
            name='Paul', this will mean that we wabnt to delete all the users
            named Paul

        Returns
        ---
        result: None
        """
        # Delete a row from the table
        rows_to_delete = self.session.query(class_table).all()
        for row_to_delete in rows_to_delete:
            self.session.delete(row_to_delete)
        self.session.commit()

    def delete_value(self, class_table: Any, **kwargs: Any) -> None:
        """delete_value this method can be used to delete a specific value on the table or all the values which meet a specific condition.
        the row can be identified with a key value pair.

        ## Example
        ```python
        session = SQLDatabaseInterface()
        session.delete_value(User,name="Paula")
        ```

        Parameters
        ---

        class_table type
            this is the name of the class of the table i.e. User
        **kargs tuple
            this is the key value pair that we want to use for our query i.e.
            name='Paul', this will mean that we wabnt to delete all the users
            named Paul

        Returns
        ---
        result: None
        """
        # Delete a row from the table
        rows_to_delete = self.session.query(class_table).filter_by(**kwargs).all()
        for row_to_delete in rows_to_delete:
            self.session.delete(row_to_delete)
        self.session.commit()
