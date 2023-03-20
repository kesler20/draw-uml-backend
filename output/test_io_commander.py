
import pytest
from commander import Commander

print("Testing:" + Commander.__doc__)
        
    @pytest.mark.parametrize(name,int,[
        (name,int),
        (None,[],int),
        ("","",int),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_run(name):
        """test the `run` method which accepts the following arguments:
        
        Parameters
        ----------
        name : type

        Returns
        -------
        int
        """
        test_result = self.test_client.run(name)
        self.assertEqual(type(test_result),type(int)) 
    
    @pytest.mark.parametrize(n,list,[
        (n,list),
        (None,[],list),
        ("","",list),
    ])
    @pytest.mark.skip(reason="feature not implemented yet")
    def test_io_execute(n):
        """test the `execute` method which accepts the following arguments:
        
        Parameters
        ----------
        n : int

        Returns
        -------
        list
        """
        test_result = self.test_client.execute(n)
        self.assertEqual(type(test_result),type(list)) 
    