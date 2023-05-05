import pytest
from parametrize import parametrize
from _test_base import *
from _types import *
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
        
    @parametrize(",Path",[
        (,Path),
        (None,[],Path),
        ("","",Path),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_source_code_path(self,,expected):
        """test the `source_code_path` method which accepts the following arguments:
        
        Parameters
        ----------
        

        Returns
        -------
        Path
        """
        test_result = self.test_client.source_code_path()
        self.assertEqual(type(test_result),type(expected)) 
    
    @parametrize(",Path",[
        (,Path),
        (None,[],Path),
        ("","",Path),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_response_code_path(self,,expected):
        """test the `response_code_path` method which accepts the following arguments:
        
        Parameters
        ----------
        

        Returns
        -------
        Path
        """
        test_result = self.test_client.response_code_path()
        self.assertEqual(type(test_result),type(expected)) 
    
    @parametrize("path,",[
        (path,),
        (None,[],),
        ("","",),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_set_response_code_path(self,path,expected):
        """test the `set_response_code_path` method which accepts the following arguments:
        
        Parameters
        ----------
        path : str

        Returns
        -------
        
        """
        test_result = self.test_client.set_response_code_path(path)
        self.assertEqual(type(test_result),type(expected)) 
    
    @parametrize("path,",[
        (path,),
        (None,[],),
        ("","",),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_set_source_code_path(self,path,expected):
        """test the `set_source_code_path` method which accepts the following arguments:
        
        Parameters
        ----------
        path : str

        Returns
        -------
        
        """
        test_result = self.test_client.set_source_code_path(path)
        self.assertEqual(type(test_result),type(expected)) 
    
    @parametrize(",None",[
        (,None),
        (None,[],None),
        ("","",None),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_read(self,,expected):
        """test the `read` method which accepts the following arguments:
        
        Parameters
        ----------
        

        Returns
        -------
        None
        """
        test_result = self.test_client.read()
        self.assertEqual(type(test_result),type(expected)) 
    
    def tearDown(self):
        pass
        
if __name__ == "__main__":
    unittest.main()
        