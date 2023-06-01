import pytest
from parametrize import parametrize
from _test_base import *
from _types import *
import unittest
from databaseinterface import DatabaseInterface
print("Testing:" + DatabaseInterface.__doc__)
        
class Test_DatabaseInterface(unittest.TestCase):        
    """This is the interface to the database of the wiz_app system (the resourcemanager). 

To get started import the database and the valid modes of the database from the business rules.

```python
from wiz_app_connector.infrastructure.db.wiz_app_db import DatabaseInterface
from wiz_app_connector.domain.business_rules import ValidDatabaseMode
# setup a database with a development mode
db = DatabaseInterface("v1",ValidDatabaseMode.DEV)

# send a post request
db.use_url(endpoint="sensor").create(body={})"""
        
    def setUp(self):
        self.test_client = DatabaseInterface(
            version
            ,mode
        )
        
    @parametrize("body,dict",[
        (body,dict),
        (None,[],dict),
        ("","",dict),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_create(self,body,expected):
        """test the `create` method which accepts the following arguments:
        
        Parameters
        ----------
        body : dict

        Returns
        -------
        dict
        """
        test_result = self.test_client.create(body)
        self.assertEqual(type(test_result),type(expected)) 
    
    @parametrize("name,dict",[
        (name,dict),
        (None,[],dict),
        ("","",dict),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_read(self,name,expected):
        """test the `read` method which accepts the following arguments:
        
        Parameters
        ----------
        name : str

        Returns
        -------
        dict
        """
        test_result = self.test_client.read(name)
        self.assertEqual(type(test_result),type(expected)) 
    
    @parametrize("name,dict",[
        (name,dict),
        (None,[],dict),
        ("","",dict),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_update(self,name,expected):
        """test the `update` method which accepts the following arguments:
        
        Parameters
        ----------
        name : str

        Returns
        -------
        dict
        """
        test_result = self.test_client.update(name)
        self.assertEqual(type(test_result),type(expected)) 
    
    @parametrize("name,dict",[
        (name,dict),
        (None,[],dict),
        ("","",dict),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_delete(self,name,expected):
        """test the `delete` method which accepts the following arguments:
        
        Parameters
        ----------
        name : str

        Returns
        -------
        dict
        """
        test_result = self.test_client.delete(name)
        self.assertEqual(type(test_result),type(expected)) 
    
    def tearDown(self):
        pass
        
if __name__ == "__main__":
    unittest.main()
        