import os
from dataclasses import dataclass
try:
    from draw_uml_backend._base import BaseReader, BASE_OUTPUT_RESPONSE_PATH
except ModuleNotFoundError:
    from src.draw_uml_backend._base import BaseReader, BASE_OUTPUT_RESPONSE_PATH


@dataclass
class TestBuilder(BaseReader):
    type_of_test: str
    content: str = ""

    @property
    def test_file(self):
        if self.type_of_test == "io":
            return os.path.join(BASE_OUTPUT_RESPONSE_PATH, "test_io_" + self.source.class_name.lower() + ".py")
        else:
            return os.path.join(BASE_OUTPUT_RESPONSE_PATH, "test_side_effects_" + self.source.class_name.lower() + ".py")

    def add_initial_import(self):
        self.content += '''
import unittest
from {} import {}

print("Testing:" + {}.__doc__)
        '''.format(self.source.class_name.lower(), self.source.class_name, self.source.class_name)
        return self

    def add_class_name(self):
        comment = f"'''{self.source.description}'''"
        self.content += '''

class Test_{}(unittest.TestCase):        
    {}
        '''.format(self.source.class_name, comment)
        if self.type_of_test == "io":
            pass
        else:
            self.content += '''
        Example of how those tests are run
        ---
        given a method ``append_row`` which takes the following arguments
        ```txt
        row: List[List], table_name: str
        ```
        you can cause the side effect (call the method being tested) and then check the endpoints
        ```python
        # array of arguments which are expected by the method which causes the side effect under test
        side_effect_input = [[121],base_table_name]
        # array containing the expected correct result of the side effect
        side_effect_output = [pd.DataFrame([*base_df_values, 121],columns=base_df_cols)]

        # cause a side effect to test
        test_result = self.test_client.append_row(*side_effect_input)

        # test that the side effect is expected
        test_result = self.test_client.get_table(base_table_name)
        self.assertTrue(test_result.equals(side_effect_output[0]))    
        ```
        '''
        return self

    def construct_set_up(self):
        class_name = self.source.class_name
        props = [field[0] for field in self.source.fields] + [prop[0] for prop in self.source.properties]

        if len(props) == 0:
            setUp = f'''
    def setUp(self):
        self.test_client = {class_name}()'''

        else:

            setUp = f'''
    def setUp(self):
        self.test_client = {class_name}(
            {props[0]}'''

        if len(props) >= 1:
            for property in props[1:]:
                property_line = f'''
            ,{property}'''
                setUp += property_line

            setUp += '''
        )
        '''
        self.content += setUp
        return self

    def __construct_function_io(self, function_name: str, function_arguments: str, function_result_type: str):
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
        Parameters:
        - function_name : the name of the function to be tested
        - function_arguments : the arguments of the function to be tested
        - function_result_type : the type of the result of the function being tested

        ---
        Returns:
        - function_test : a doc string which can be used to test the function passed
        '''
        self.content += f'''
    def test_io_{function_name}(self):
        """
        test the {function_name} method which accepts the following arguments:
        
        ---
        Parameters:
        {function_arguments}

        ---
        Returns:
        - {function_result_type}
        """
        # array of arguments which are expected by the method being tested
        correct_input = []
        # array containing the expected correct result of the function call
        correct_output = []

        # array of arguments containing an invalid type 
        invalid_types_input = []
        # array containing the result of the function call
        invalid_types_output = []

        # array of arguments containing an invalid value 
        invalid_values_input = []
        # array containing the result of the function call
        invalid_values_output = []

        test_result = self.test_client.{function_name}(*correct_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,correct_output[0])

        test_result = self.test_client.{function_name}(*edge_case_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,edge_case_output[0])

        test_result = self.test_client.{function_name}(*invalid_types_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_types_output[0]) 

        test_result = self.test_client.{function_name}(*invalid_values_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_values_output[0]) 
    '''

        return self

    def __construct_function_side_effects(self, function_name: str, function_arguments: str, function_result_type: str):
        '''
        This function takes the function names, 
        arguments and the type of the result of the function
        and it returns a function which can be used to test the side effects of the functions

        ---
        Parameters:
        - function_name : the name of the function to be tested
        - function_arguments : the arguments of the function to be tested

        ---
        Returns:
        - function_test : a doc string which can be used to test the function passed
        '''
        self.content += f'''
    def test_side_effects_{function_name}(self):
        """
        test the {function_name} method which accepts the following arguments:
        
        ---
        Parameters:
        {function_arguments}

        ---
        Returns:
        - {function_result_type}
        """
        # array of arguments which are expected by the method which causes the side effect under test
        side_effect_input = []
        # array containing the expected correct result of the method after the side effect
        side_effect_output = []

        # cause a side effect to test
        test_result = self.test_client.{function_name}(*side_effect_input)

        # test that the side effect is expected
        test_result = self.test_client.{function_name}()
        self.assertEqual(test_result,side_effect_output[0])
    '''
        return self

    def add_functions(self):
        if self.type_of_test == "io":
            for method in self.source.methods:
                params = ""
                try:
                    for param in method['params']:
                        if param == method['params'][-1]:
                            params += f"{param[0]} : {param[1]}"
                        else:
                            params += f"{param[0]} : {param[1]}, "
                except IndexError:
                    pass
                self.__construct_function_io(method['signature'], params, method['return_type'])
        else:
            for method in self.source.methods:
                params = ""
                try:
                    for param in method['params']:
                        if param == method['params'][-1]:
                            params += f"{param[0]} : {param[1]}"
                        else:
                            params += f"{param[0]} : {param[1]}, "
                except IndexError:
                    pass
                self.__construct_function_side_effects(method['signature'], params, method['return_type'])
        return self

    def construct_js_test_function(self):
        self.content += r'''
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
        return self

    def add_tearDown(self):
        self.content += '''
    def tearDown(self):
        pass
        '''
        return self

    def add_main_function_call(self):
        self.content += '''
if __name__ == "__main__":
    unittest.main()
        '''
        return self

    def build_test_class(self):
        self.write(self.test_file, self.content)
        return self
