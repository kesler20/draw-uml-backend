
import unittest
from anotherclass import AnotherClass

print("Testing:" + AnotherClass.__doc__)
        

class Test_AnotherClass(unittest.TestCase):        
    '''Object Description'''
        
    def setUp(self):
        self.test_client = AnotherClass(
            testing
        )
        
    def tearDown(self):
        pass
        
if __name__ == "__main__":
    unittest.main()
        