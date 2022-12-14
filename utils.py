
def convert_chars_to_string(chars: 'list[str]'):
    '''
    Take a list of characters and converts appends them to an empty string

    ---
    Params:
    - chars : list of characters i.e. ["c","a", "r"]

    ---
    Returns:
    - string: a string i.e. "car" 
    '''
    new_string = ''
    for char in chars:
        new_string += char
    return new_string

def find_substring(string: str, sub_string: str):
    '''
    Uses the string.index() built in method, however
    if the sub-string is not found it returns -1 rather than rasing a ValueError

    ---
    Params:
    - string : the initial string which should contain the substring
    - sub_string : the string that we our looking for in the string

    ---
    Returns: 
    - index: an integer which is -1 if no substring was found'''
    try:
        return string.index(sub_string)
    except ValueError as err:
        return -1

def replace_with_string(raw_string: str, list_of_strings_to_replace: 'list[str]', strings_to_replace_with: str):
    '''
    Replaces a list of unwanted string with a string

    ---
    Params:
    - raw_string : initial string to modify
    - list_of_strings_to_replace : an array containing all the strings that need to be replaced
    - strings_to_replace_with : a string which will replace all the strings in the list_of_strings_to_replace array

    ---
    Returns:
    - clean_string : the initial string with the replaced strings
    '''
    clean_string = ""
    for string in list_of_strings_to_replace:
        clean_string = raw_string.replace(string, strings_to_replace_with)
        raw_string = clean_string
    return clean_string

def convert_file_content_into_list(filename: str):
    '''
    Reads the specified filename and it returns a list containing each lines of the file
    and it removes "\ n" within each line

    ---
    Params:
    - filename: the path of the file containing the items of the list

    ---
    Returns:
    - final _list : a list of strings containing each line of the file'''
    final_list = []
    with open(filename, "r") as f:
        for string in f.readlines():
            final_list.append(string.replace("\n", ""))
    return final_list

def construct_set_up(class_name: str, props: 'list[str]'):
    '''
    takes the name of the class and its properties and builds a setUp method
    for its test class

    ---
    Params:
    - class_name : the name of hte class being tested
    - props : a list of properties of the class being tested

    ---
    Returns:
    - setUp : the setUp method as a doc string
    '''
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

def remove_substring_from_string_list(raw_sample_list: 'list[str]', sub_string_to_remove: str, separator: str):
    '''
    Removes all the instances of a sub-strings from a list of strings.

    ---
    Params:
    - raw_sample_list: a list of strings
    - sub_string_to_remove: a sub-string which will be searched over all the strings within the raw_sample_list
    - separator : a string which indicates when a string within the raw_sample_list should be split

    ---
    Returns:
    - clean_sample_list : a copy of the raw_sample_list which do not contain any instance of the sub-string specified

    '''
    clean_sample_list: 'list[str]' = []
    for name in raw_sample_list:
        clean_name = ""
        raw_name_list = name.split(separator)
        for char in raw_name_list:
            if find_substring(char, sub_string_to_remove) != -1:
                pass
            else:
                clean_name += char
        clean_sample_list.append(clean_name)

    return clean_sample_list

def construct_function_io(function_name: str, function_arguments: str, function_result_type: str) -> str:
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

def construct_function_side_effects(function_name: str, function_arguments: str, function_result_type: str) -> str:
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

def construct_js_test_function():
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