
import unittest
from operatingsysteminterface import OperatingSystemInterface

print("Testing:" + OperatingSystemInterface.__doc__)
        

class Test_OperatingSystemInterface(unittest.TestCase):        
    """"""
        
    def setUp(self):
        self.test_client = OperatingSystemInterface()
    @staticmethod
    @pytest.mark.parametrize("param1,param2, expected",[
        ("input1","input2","expected_value1"),
        ("input1a","input2a","expected_value2"),
        ("input1c","input2b","expected_value3"),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io___init__(self,*args):
        """
        test the __init__ method which accepts the following arguments:
        
        Parameters
        ----------
        

        Returns
        -------
          None
        """
        test_result = self.test_client.__init__(*args)
        self.assertEqual(test_result,invalid_values_output[0]) 
    
    @staticmethod
    @pytest.mark.parametrize("param1,param2, expected",[
        ("input1","input2","expected_value1"),
        ("input1a","input2a","expected_value2"),
        ("input1c","input2b","expected_value3"),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io___enter__(self,*args):
        """
        test the __enter__ method which accepts the following arguments:
        
        Parameters
        ----------
        

        Returns
        -------
          os
        """
        test_result = self.test_client.__enter__(*args)
        self.assertEqual(test_result,invalid_values_output[0]) 
    
    @staticmethod
    @pytest.mark.parametrize("param1,param2, expected",[
        ("input1","input2","expected_value1"),
        ("input1a","input2a","expected_value2"),
        ("input1c","input2b","expected_value3"),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io___exit__(self,*args):
        """
        test the __exit__ method which accepts the following arguments:
        
        Parameters
        ----------
        

        Returns
        -------
          os
        """
        test_result = self.test_client.__exit__(*args)
        self.assertEqual(test_result,invalid_values_output[0]) 
    
    @staticmethod
    @pytest.mark.parametrize("param1,param2, expected",[
        ("input1","input2","expected_value1"),
        ("input1a","input2a","expected_value2"),
        ("input1c","input2b","expected_value3"),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_gcu(self,*args):
        """
        test the gcu method which accepts the following arguments:
        
        Parameters
        ----------
        

        Returns
        -------
          str
        """
        test_result = self.test_client.gcu(*args)
        self.assertEqual(test_result,invalid_values_output[0]) 
    
    @staticmethod
    @pytest.mark.parametrize("param1,param2, expected",[
        ("input1","input2","expected_value1"),
        ("input1a","input2a","expected_value2"),
        ("input1c","input2b","expected_value3"),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_copy_file_from_folder(self,*args):
        """
        test the copy_file_from_folder method which accepts the following arguments:
        
        Parameters
        ----------
        file : str, source_folder : str="jaguar"

        Returns
        -------
          None
        """
        test_result = self.test_client.copy_file_from_folder(*args)
        self.assertEqual(test_result,invalid_values_output[0]) 
    
    @staticmethod
    @pytest.mark.parametrize("param1,param2, expected",[
        ("input1","input2","expected_value1"),
        ("input1a","input2a","expected_value2"),
        ("input1c","input2b","expected_value3"),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_move_folder_resources(self,*args):
        """
        test the move_folder_resources method which accepts the following arguments:
        
        Parameters
        ----------
        destination_path : str

        Returns
        -------
          None
        """
        test_result = self.test_client.move_folder_resources(*args)
        self.assertEqual(test_result,invalid_values_output[0]) 
    
    @staticmethod
    @pytest.mark.parametrize("param1,param2, expected",[
        ("input1","input2","expected_value1"),
        ("input1a","input2a","expected_value2"),
        ("input1c","input2b","expected_value3"),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_read_word_in_directory(self,*args):
        """
        test the read_word_in_directory method which accepts the following arguments:
        
        Parameters
        ----------
        word : str

        Returns
        -------
          'list[str]'
        """
        test_result = self.test_client.read_word_in_directory(*args)
        self.assertEqual(test_result,invalid_values_output[0]) 
    
    def tearDown(self):
        pass
        
if __name__ == "__main__":
    unittest.main()
        