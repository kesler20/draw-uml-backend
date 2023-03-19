
import unittest
from computer import Computer

print("Testing:" + Computer.__doc__)
        

class Test_Computer(unittest.TestCase):        
    """Object Description"""
        
    def setUp(self):
        self.test_client = Computer(
            foll
            ,memory
            ,run
        )
        
    @staticmethod
    @pytest.mark.parametrize("param1,param2, expected",[
        ("input1","input2","expected_value1"),
        ("input1a","input2a","expected_value2"),
        ("input1c","input2b","expected_value3"),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_execute(self,*args):
        """
        test the execute method which accepts the following arguments:
        
        Parameters
        ----------
        name : type

        Returns
        -------
          str
        """
        test_result = self.test_client.execute(*args)
        self.assertEqual(test_result,invalid_values_output[0]) 
    
    @staticmethod
    @pytest.mark.parametrize("param1,param2, expected",[
        ("input1","input2","expected_value1"),
        ("input1a","input2a","expected_value2"),
        ("input1c","input2b","expected_value3"),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_foo(self,*args):
        """
        test the foo method which accepts the following arguments:
        
        Parameters
        ----------
        name : type

        Returns
        -------
          list
        """
        test_result = self.test_client.foo(*args)
        self.assertEqual(test_result,invalid_values_output[0]) 
    
    def tearDown(self):
        pass
        
if __name__ == "__main__":
    unittest.main()
        