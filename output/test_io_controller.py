import pytest
from parametrize import parametrize
from _test_base import *
from _types import *
import unittest
from controller import Controller
print("Testing:" + Controller.__doc__)
        
class Test_Controller(unittest.TestCase):        
    """This is an interface with the PID controller hardware"""
        
    def setUp(self):
        self.test_client = Controller(
            status
        )
        
    @parametrize("control_value,bool",[
        (control_value,bool),
        (None,[],bool),
        ("","",bool),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_activate(self,control_value,expected):
        """test the `activate` method which accepts the following arguments:
        
        Parameters
        ----------
        control_value : int

        Returns
        -------
        bool
        """
        test_result = self.test_client.activate(control_value)
        self.assertEqual(type(test_result),type(expected)) 
    
    def tearDown(self):
        pass
        
if __name__ == "__main__":
    unittest.main()
        