import pytest
from parametrize import parametrize
from _test_base import *
from _types import *
import unittest
from person import Person
print("Testing:" + Person.__doc__)
        
class Test_Person(unittest.TestCase):        
    """This should represent a person in real life"""
        
    def setUp(self):
        self.test_client = Person(
            name
            ,age
        )
        
    @parametrize("last_name,str",[
        (last_name,str),
        (None,[],str),
        ("","",str),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_get_full_name(self,last_name,expected):
        """test the `get_full_name` method which accepts the following arguments:
        
        Parameters
        ----------
        last_name : str

        Returns
        -------
        str
        """
        test_result = self.test_client.get_full_name(last_name)
        self.assertEqual(type(test_result),type(expected)) 
    
    def tearDown(self):
        pass
        
if __name__ == "__main__":
    unittest.main()
        