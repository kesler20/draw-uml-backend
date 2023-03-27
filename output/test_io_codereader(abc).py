
import unittest
from codereader(abc) import CodeReader(ABC)
print("Testing:" + CodeReader(ABC).__doc__)
        
class Test_CodeReader(ABC)(unittest.TestCase):        
    """"""
        
    def setUp(self):
        self.test_client = CodeReader(ABC)(
            source_code_path
            ,response_code_path
        )
        
    @staticmethod
    @pytest.mark.parametrize(",Path",[
        (,Path),
        (None,[],Path),
        ("","",Path),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_source_code_path(,Path):
        """test the `source_code_path` method which accepts the following arguments:
        
        Parameters
        ----------
        

        Returns
        -------
        Path
        """
        test_result = self.test_client.source_code_path()
        self.assertEqual(type(test_result),type(Path)) 
    
    @staticmethod
    @pytest.mark.parametrize(",Path",[
        (,Path),
        (None,[],Path),
        ("","",Path),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_response_code_path(,Path):
        """test the `response_code_path` method which accepts the following arguments:
        
        Parameters
        ----------
        

        Returns
        -------
        Path
        """
        test_result = self.test_client.response_code_path()
        self.assertEqual(type(test_result),type(Path)) 
    
    @staticmethod
    @pytest.mark.parametrize("path,",[
        (path,),
        (None,[],),
        ("","",),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_set_response_code_path(path,):
        """test the `set_response_code_path` method which accepts the following arguments:
        
        Parameters
        ----------
        path : str

        Returns
        -------
        
        """
        test_result = self.test_client.set_response_code_path(path)
        self.assertEqual(type(test_result),type()) 
    
    @staticmethod
    @pytest.mark.parametrize("path,",[
        (path,),
        (None,[],),
        ("","",),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_set_source_code_path(path,):
        """test the `set_source_code_path` method which accepts the following arguments:
        
        Parameters
        ----------
        path : str

        Returns
        -------
        
        """
        test_result = self.test_client.set_source_code_path(path)
        self.assertEqual(type(test_result),type()) 
    
    @staticmethod
    @pytest.mark.parametrize(",None",[
        (,None),
        (None,[],None),
        ("","",None),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_read(,None):
        """test the `read` method which accepts the following arguments:
        
        Parameters
        ----------
        

        Returns
        -------
        None
        """
        test_result = self.test_client.read()
        self.assertEqual(type(test_result),type(None)) 
    
    def tearDown(self):
        pass
        
if __name__ == "__main__":
    unittest.main()
        