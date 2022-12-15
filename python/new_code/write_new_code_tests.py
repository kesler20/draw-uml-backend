import os
from main_test_generator.utils import *

# initialize starting lines for the test file
test_file_lines = ["import unittest"]

with open(r"test_classes\test_class.py", "r") as f:
    function_names = []
    for line in f.readlines():

        # build the class line string
        if find_substring(line, "class") != -1:
            # get the name of the class being tested
            class_name = convert_chars_to_string(
                convert_chars_to_string(line.split(" ")[1]).split("(")[0])

            # replace its name with Test_classname
            class_line = line.replace(" ", " Test_")

            # make it a child of a unittest.TestCase class
            class_line_chars = class_line.split("(")[0]
            class_line = convert_chars_to_string(
                class_line_chars) + "(unittest.TestCase):"

        # make the setUp string
        if find_substring(line, "def __init__(") != -1:
            # get all the properties from the constructor of the class being tested
            constructor_properties = convert_chars_to_string(
                convert_chars_to_string(line.split("def __init__(")[1]).split(")")[0]).split(",")[1:]

        # rename all the functions to test_functionName
        if find_substring(line, "def ") != -1 and find_substring(line, "def __init__(") == -1:
            function_name_and_body = convert_chars_to_string(
                line.split("def ")[1]).split("(")
            function_name = function_name_and_body[0]
            function_body = convert_chars_to_string(
                function_name_and_body[1].split(")")[0])
            function_body = function_body.replace("self, ", "")
            function_result_type = convert_chars_to_string(line.split(
                "->")[1]).replace("-> ", "").replace(":", "").replace("\n","")
            function_names.append(construct_function_io(
                function_name, function_body, function_result_type))
    
    import_class_line = f'''
from test_class import {class_name}
    '''
    test_file_lines.append(import_class_line)
    test_file_lines.append("\n")
    test_file_lines.append("\n")
    test_file_lines.append(class_line)
    test_file_lines.append("\n")
    test_file_lines.append(construct_set_up(
        class_name, constructor_properties))
    test_file_lines.append("\n")
    for functions in function_names:
        test_file_lines.append(functions)
    test_file_lines.append("\n")
    test_file_lines.append("\n")
    test_file_lines.append("if __name__ == '__main__':\n")
    test_file_lines.append('    unittest.main()')

with open(r"results\test_class_result.py", "w") as f:
    f.writelines(test_file_lines)
