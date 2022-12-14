import time
from main_test_generator.utils import *

'''
A method consist of a description and a signature
for instance:
sum = ['adds 1 + 2 to equal 3','sum']

will return
test('adds 1 + 2 to equal 3', () => {
  expect(sum(1, 2)).toBe(3);
});
'''

list_of_lines = []
with open(r"test_classes\test_class.js", "r") as f:
    for line in f.readlines():
        list_of_lines.append(line)

comments = []
from_line = 0
to_line = 0
for index, line in enumerate(list_of_lines):
    if find_substring(line, "/**") != -1:
        from_line = index
    if find_substring(line, "*/") != -1:
        to_line = index
        comments.append(
            (list_of_lines[from_line:to_line + 1], list_of_lines[to_line + 1]))

clean_comments = []
for comment in comments:
    if find_substring(comment[1], "localStorage") != -1:
        pass
    elif find_substring(comment[1], "this.") != -1:
        pass
    elif find_substring(comment[1], "let") != -1:
        pass
    elif find_substring(comment[1], "if ") != -1:
        pass
    elif find_substring(comment[1], "export") != -1:
        pass
    else:
        clean_comments.append(comment)

final_comments = []
for comment in clean_comments:
    final_comments.append((comment[0][1].replace(
        "   * ", "").replace("\n", ""), comment[1].split(" ")[2]))

# this is to append the next functions in the final comments array and avoid ovverriding
initial_lines = []
for comment in final_comments:
    # write the template functions to the file
    with open(r"results\test_class_result.js", "w") as f:
        # we need enough placeholders to replace all the functions in the final_comments array
        f.writelines([*initial_lines,construct_js_test_function()])

    # read the template file and replace each variable with the current instance
    with open(r"results\test_class_result.js", "r") as f:
        lines = []
        for line in f.readlines():
            line = line.replace("method_description", comment[0])
            line = line.replace("method_signature", comment[1])
            line = line.replace("method_result_type", "number")
            lines.append(line)
    initial_lines = lines


with open(r"results\test_class_result.js", "w") as f:
    f.writelines(lines)

# # remove the remaining boilerplate code
# with open("test_class_result.js", "r") as f_read:
#     file_content = f_read.readlines()

# with open("test_class_result.js", "w") as f_write:
#     f_write.writelines(file_content[46:])
