import unittest
from test_class import MQTTClient
    

class Test_MQTTClient(unittest.TestCase):

  def setUp(self):
    self.test_client = MQTTClient()

  def test_io_clientID(self):
    """
    test the clientID method which accepts the following arguments:
    
    ---
    Params:
    self

    ---
    Returns:
    -  str
    """
    # array of arguments which are expected by the method being tested
    correct_input = []
    # array containing the expected correct result of the function call
    correct_output = []

    # array of arguments representing
    # a potential edge case where the method might be used
    edge_case_input = []
    # array containing the expected result of the function call
    edge_case_output = []

    # array of arguments containing an invalid type 
    invalid_types_input = []
    # array containing the result of the function call
    invalid_types_output = []

    # array of arguments containing an invalid value 
    invalid_values_input = []
    # array containing the result of the function call
    invalid_values_output = []

    test_result = self.test_client.clientID(*correct_input)
    self.assertEqual(test_result,correct_output[0])
    
    # assert that the type returned by the method is correct
    self.assertEqual(type(test_result),type( str)) 

    test_result = self.test_client.clientID(*edge_case_input)
    self.assertEqual(test_result,edge_case_output[0])
    
    # assert that the type returned by the method is correct
    self.assertEqual(type(test_result),type( str))

    test_result = self.test_client.clientID(*invalid_types_input)
    self.assertEqual(test_result,invalid_types_output[0]) 
    
    # assert that the type returned by the method is correct
    self.assertEqual(type(test_result),type( str))

    test_result = self.test_client.clientID(*invalid_values_input)
    self.assertEqual(test_result,invalid_values_output[0]) 
    
    # assert that the type returned by the method is correct
    self.assertEqual(type(test_result),type( str))

  def test_io__generate_clientID(self):
    """
    test the _generate_clientID method which accepts the following arguments:
    
    ---
    Params:
    length: int = 8

    ---
    Returns:
    -  str
    """
    # array of arguments which are expected by the method being tested
    correct_input = []
    # array containing the expected correct result of the function call
    correct_output = []

    # array of arguments representing
    # a potential edge case where the method might be used
    edge_case_input = []
    # array containing the expected result of the function call
    edge_case_output = []

    # array of arguments containing an invalid type 
    invalid_types_input = []
    # array containing the result of the function call
    invalid_types_output = []

    # array of arguments containing an invalid value 
    invalid_values_input = []
    # array containing the result of the function call
    invalid_values_output = []

    test_result = self.test_client._generate_clientID(*correct_input)
    self.assertEqual(test_result,correct_output[0])
    
    # assert that the type returned by the method is correct
    self.assertEqual(type(test_result),type( str)) 

    test_result = self.test_client._generate_clientID(*edge_case_input)
    self.assertEqual(test_result,edge_case_output[0])
    
    # assert that the type returned by the method is correct
    self.assertEqual(type(test_result),type( str))

    test_result = self.test_client._generate_clientID(*invalid_types_input)
    self.assertEqual(test_result,invalid_types_output[0]) 
    
    # assert that the type returned by the method is correct
    self.assertEqual(type(test_result),type( str))

    test_result = self.test_client._generate_clientID(*invalid_values_input)
    self.assertEqual(test_result,invalid_values_output[0]) 
    
    # assert that the type returned by the method is correct
    self.assertEqual(type(test_result),type( str))

  def test_io__connect_client(self):
    """
    test the _connect_client method which accepts the following arguments:
    
    ---
    Params:
    self

    ---
    Returns:
    -  None
    """
    # array of arguments which are expected by the method being tested
    correct_input = []
    # array containing the expected correct result of the function call
    correct_output = []

    # array of arguments representing
    # a potential edge case where the method might be used
    edge_case_input = []
    # array containing the expected result of the function call
    edge_case_output = []

    # array of arguments containing an invalid type 
    invalid_types_input = []
    # array containing the result of the function call
    invalid_types_output = []

    # array of arguments containing an invalid value 
    invalid_values_input = []
    # array containing the result of the function call
    invalid_values_output = []

    test_result = self.test_client._connect_client(*correct_input)
    self.assertEqual(test_result,correct_output[0])
    
    # assert that the type returned by the method is correct
    self.assertEqual(type(test_result),type( None)) 

    test_result = self.test_client._connect_client(*edge_case_input)
    self.assertEqual(test_result,edge_case_output[0])
    
    # assert that the type returned by the method is correct
    self.assertEqual(type(test_result),type( None))

    test_result = self.test_client._connect_client(*invalid_types_input)
    self.assertEqual(test_result,invalid_types_output[0]) 
    
    # assert that the type returned by the method is correct
    self.assertEqual(type(test_result),type( None))

    test_result = self.test_client._connect_client(*invalid_values_input)
    self.assertEqual(test_result,invalid_values_output[0]) 
    
    # assert that the type returned by the method is correct
    self.assertEqual(type(test_result),type( None))

  def test_io__tear_down(self):
    """
    test the _tear_down method which accepts the following arguments:
    
    ---
    Params:
    *topics

    ---
    Returns:
    -  None
    """
    # array of arguments which are expected by the method being tested
    correct_input = []
    # array containing the expected correct result of the function call
    correct_output = []

    # array of arguments representing
    # a potential edge case where the method might be used
    edge_case_input = []
    # array containing the expected result of the function call
    edge_case_output = []

    # array of arguments containing an invalid type 
    invalid_types_input = []
    # array containing the result of the function call
    invalid_types_output = []

    # array of arguments containing an invalid value 
    invalid_values_input = []
    # array containing the result of the function call
    invalid_values_output = []

    test_result = self.test_client._tear_down(*correct_input)
    self.assertEqual(test_result,correct_output[0])
    
    # assert that the type returned by the method is correct
    self.assertEqual(type(test_result),type( None)) 

    test_result = self.test_client._tear_down(*edge_case_input)
    self.assertEqual(test_result,edge_case_output[0])
    
    # assert that the type returned by the method is correct
    self.assertEqual(type(test_result),type( None))

    test_result = self.test_client._tear_down(*invalid_types_input)
    self.assertEqual(test_result,invalid_types_output[0]) 
    
    # assert that the type returned by the method is correct
    self.assertEqual(type(test_result),type( None))

    test_result = self.test_client._tear_down(*invalid_values_input)
    self.assertEqual(test_result,invalid_values_output[0]) 
    
    # assert that the type returned by the method is correct
    self.assertEqual(type(test_result),type( None))

  def test_io_publish_data(self):
    """
    test the publish_data method which accepts the following arguments:
    
    ---
    Params:
    topic: str, payload: str, quos: Optional[int] = 0

    ---
    Returns:
    -  None
    """
    # array of arguments which are expected by the method being tested
    correct_input = []
    # array containing the expected correct result of the function call
    correct_output = []

    # array of arguments representing
    # a potential edge case where the method might be used
    edge_case_input = []
    # array containing the expected result of the function call
    edge_case_output = []

    # array of arguments containing an invalid type 
    invalid_types_input = []
    # array containing the result of the function call
    invalid_types_output = []

    # array of arguments containing an invalid value 
    invalid_values_input = []
    # array containing the result of the function call
    invalid_values_output = []

    test_result = self.test_client.publish_data(*correct_input)
    self.assertEqual(test_result,correct_output[0])
    
    # assert that the type returned by the method is correct
    self.assertEqual(type(test_result),type( None)) 

    test_result = self.test_client.publish_data(*edge_case_input)
    self.assertEqual(test_result,edge_case_output[0])
    
    # assert that the type returned by the method is correct
    self.assertEqual(type(test_result),type( None))

    test_result = self.test_client.publish_data(*invalid_types_input)
    self.assertEqual(test_result,invalid_types_output[0]) 
    
    # assert that the type returned by the method is correct
    self.assertEqual(type(test_result),type( None))

    test_result = self.test_client.publish_data(*invalid_values_input)
    self.assertEqual(test_result,invalid_values_output[0]) 
    
    # assert that the type returned by the method is correct
    self.assertEqual(type(test_result),type( None))

  def test_io_subscribe_to_topic(self):
    """
    test the subscribe_to_topic method which accepts the following arguments:
    
    ---
    Params:
    topic: str, custom_callback, quos: Optional[int] = 1

    ---
    Returns:
    -  None
    """
    # array of arguments which are expected by the method being tested
    correct_input = []
    # array containing the expected correct result of the function call
    correct_output = []

    # array of arguments representing
    # a potential edge case where the method might be used
    edge_case_input = []
    # array containing the expected result of the function call
    edge_case_output = []

    # array of arguments containing an invalid type 
    invalid_types_input = []
    # array containing the result of the function call
    invalid_types_output = []

    # array of arguments containing an invalid value 
    invalid_values_input = []
    # array containing the result of the function call
    invalid_values_output = []

    test_result = self.test_client.subscribe_to_topic(*correct_input)
    self.assertEqual(test_result,correct_output[0])
    
    # assert that the type returned by the method is correct
    self.assertEqual(type(test_result),type( None)) 

    test_result = self.test_client.subscribe_to_topic(*edge_case_input)
    self.assertEqual(test_result,edge_case_output[0])
    
    # assert that the type returned by the method is correct
    self.assertEqual(type(test_result),type( None))

    test_result = self.test_client.subscribe_to_topic(*invalid_types_input)
    self.assertEqual(test_result,invalid_types_output[0]) 
    
    # assert that the type returned by the method is correct
    self.assertEqual(type(test_result),type( None))

    test_result = self.test_client.subscribe_to_topic(*invalid_values_input)
    self.assertEqual(test_result,invalid_values_output[0]) 
    
    # assert that the type returned by the method is correct
    self.assertEqual(type(test_result),type( None))


if __name__ == '__main__':
    unittest.main()