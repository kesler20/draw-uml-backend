from _base import BaseReader
from dataclasses import dataclass

@dataclass
class TestBuilder(BaseReader):

    def build_initial_import(self):
        return '''
import unittest
import {}

print("Testing:" + {}.__doc__)
        '''.format(self.source.class_name, self.source.class_name)

    def build_class_name(self) -> str:
        comment = f"'''{self.source.description}'''"
        return '''

class Test_{}(unittest.TestCase):        
    {}
        '''.format(self.source.class_name, comment)

    def construct_set_up(self):
        class_name = self.source.class_name
        props = [*self.source.properties, *self.source.fields]

        if len(props) == 0:
            setUp = f'''
    def setUp(self):
        self.test_client = {class_name}()'''

        else:

            setUp = f'''
    def setUp(self):
        self.test_client = {class_name}(
            {props[0]},'''

        if len(props) > 1:
            for property in props[1:]:
                property_line = f'''
            {property},'''

                setUp += property_line
                if props.index(property) == len(props) - 1:
                    setUp += '''
        )'''

        return setUp

    def construct_function_io(self, function_name: str, function_arguments: str, function_result_type: str) -> str:
        '''
        This function takes the function names, 
        arguments and the type of the result of the function
        and it returns a function which can be used to test the function
        with the following inputs: 
            - correct values
            - invalid values
            - edge cases
            - invalid types
        and it will check in each case if the type of the result is as expected

        ---
        Params:
        - function_name : the name of the function to be tested
        - function_arguments : the arguments of the function to be tested
        - function_result_type : the type of the result of the function being tested

        ---
        Returns:
        - function_test : a doc string which can be used to test the function passed
        '''
        if function_result_type == "None":
            asserting_result_type_line = ""
        else:
            asserting_result_type_line = f'''
        # assert that the type returned by the method is correct
        self.assertEqual(type(test_result),type({function_result_type}))'''
        return f'''
    def test_io_{function_name}(self):
        """
        test the {function_name} method which accepts the following arguments:
        
        ---
        Params:
        {function_arguments}

        ---
        Returns:
        - {function_result_type}
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

        test_result = self.test_client.{function_name}(*correct_input)
        self.assertEqual(test_result,correct_output[0])
        {asserting_result_type_line} 

        test_result = self.test_client.{function_name}(*edge_case_input)
        self.assertEqual(test_result,edge_case_output[0])
        {asserting_result_type_line}

        test_result = self.test_client.{function_name}(*invalid_types_input)
        self.assertEqual(test_result,invalid_types_output[0]) 
        {asserting_result_type_line}

        test_result = self.test_client.{function_name}(*invalid_values_input)
        self.assertEqual(test_result,invalid_values_output[0]) 
        {asserting_result_type_line}
    '''

    def construct_function_side_effects(self, function_name: str, function_arguments: str, function_result_type: str) -> str:
        '''
        This function takes the function names, 
        arguments and the type of the result of the function
        and it returns a function which can be used to test the side effects of the functions

        ---
        Params:
        - function_name : the name of the function to be tested
        - function_arguments : the arguments of the function to be tested

        ---
        Returns:
        - function_test : a doc string which can be used to test the function passed
        '''
        return f'''
    def test_side_effects_{function_name}(self):
        """
        test the {function_name} method which accepts the following arguments:
        
        ---
        Params:
        {function_arguments}

        ---
        Returns:
        - {function_result_type}
        """
        # array of arguments which are expected by the method which causes the side effect under test
        side_effect_input = []
        # array containing the expected correct result of the side effect
        side_effect_output = []

        # cause a side effect to test
        test_result = self.test_client.{function_name}(*side_effect_input)

        # test that the side effect is expected
        test_result = self.test_client.{function_name}()
        self.assertEqual(test_result,side_effect_output[0])
    '''

    def construct_js_test_function(self):
        return r'''
    // testing with correct input
    test('method_description, testing with correct input', () => {
        // array of arguments which are expected by the method being tested
        const correct_input = [];
        // array containing the expected correct result of the function call
        const correct_output = [];

        expect(method_signature(...correct_input)).toBe(correct_output[0]);
        expect(typeof method_signature(...correct_input)).toBe(method_result_type)
    });

    // testing edge cases
    test('method_description, testing edge cases', () => {
        // array of arguments representing
        // a potential edge case where the method might be used
        const edge_case_input = [];
        // array containing the expected result of the function call
        const edge_case_output = [];

        expect(method_signature(...edge_case_input)).toBe(edge_case_output[0]);
        expect(typeof method_signature(...edge_case_input)).toBe(method_result_type)
    });

    // testing invalid types
    test('method_description, testing invalid types', () => {
        // array of arguments containing an invalid type 
        const invalid_types_input = [];
        // array containing the result of the function call
        const invalid_types_output = [];

        expect(method_signature(...invalid_types_input)).toBe(invalid_types_output[0]);
        expect(typeof method_signature(...invalid_types_input)).toBe(method_result_type)
    });

    // testing invalid inputs
    test('method_description, testing invalid inputs', () => {
        // array of arguments containing an invalid value 
        const invalid_values_input = [];
        // array containing the result of the function call
        const invalid_values_output = [];
        
        expect(method_signature(...invalid_values_input)).toBe(invalid_values_output[0]);
        expect(typeof method_signature(...invalid_values_input)).toBe(method_result_type)
    });
    '''

    def build_tearDown(self):
        return '''
    def tearDown(self):
        pass
        '''

    def build_main_function_call(self):
        return '''
if __name__ == "__main__":
    unittest.main()
        '''