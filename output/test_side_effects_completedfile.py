
import unittest
from completedfile import CompletedFile

print("Testing:" + CompletedFile.__doc__)
        

class Test_CompletedFile(unittest.TestCase):        
    '''Object Description'''
        
    def setUp(self):
        self.test_client = CompletedFile(
            coon
        )
        
    def tearDown(self):
        pass
        
if __name__ == "__main__":
    unittest.main()
        