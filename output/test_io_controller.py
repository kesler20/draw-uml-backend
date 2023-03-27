
import unittest
from controller import Controller
print("Testing:" + Controller.__doc__)
        
class Test_Controller(unittest.TestCase):        
    """This is an interface with the PID controller hardware"""
        
    def setUp(self):
        self.test_client = Controller(
            status
        )
        
    @staticmethod
    @pytest.mark.parametrize("control_value,bool",[
        (control_value,bool),
        (None,[],bool),
        ("","",bool),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_activate(control_value,bool):
        """test the `activate` method which accepts the following arguments:
        
        Parameters
        ----------
        control_value : int

        Returns
        -------
        bool
        """
        test_result = self.test_client.activate(control_value)
        self.assertEqual(type(test_result),type(bool)) 
    
    def tearDown(self):
        pass
        
if __name__ == "__main__":
    unittest.main()
        