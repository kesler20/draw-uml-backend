import pytest 
import os
from database import SQLDatabaseInterface
import database as database
import unittest
import random 
import string

def random_string(length):
    return "".join(random.choice(string.ascii_letters) for m in range(length))


class TestSQLSessionAPI(unittest.TestCase):
    def setUp(self) -> None:
        self.session = SQLDatabaseInterface("test_python_template")
        self.users = [{ "email" : random_string(5), "hashed_password" : random_string(5)}  for _ in range(5)]

    # test that a value is created with the right values
    def test_create_and_read(self):
        for user in self.users:
            new_user = database.User(**user)
            self.session.add_value(new_user)
        self.assertEqual(len(self.session.read_all_values(database.User)),len(self.users))
    
    # test that all the values are deleted
    def test_delete(self):
        # create starting users
        for user in self.users:
            new_user = database.User(**user)
            self.session.add_value(new_user)
        
        number_of_users_to_delete = 4

        for index, user in enumerate(self.users):
            if index < number_of_users_to_delete:
                self.session.delete_value(database.User,**user)
        self.assertEqual(len(self.session.read_all_values(database.User)), len(self.users) - number_of_users_to_delete)

    # test that the values can be updated
    def test_update(self):
        # create starting users
        for user in self.users:
            new_user = database.User(**user)
            self.session.add_value(new_user)
        
        self.session.update_value(database.User,"email","kesler",email=self.users[-1]["email"])

        self.assertEqual(self.session.read_value(database.User,email="kesler").email,"kesler")


    def tearDown(self) -> None:
        self.session.delete_all_values(database.User)
        