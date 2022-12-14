
with open("test_file.py", "r") as f:
    content = f.readlines()


def doc_params_generator(*args):
    final_args = ""
    args = [arg for arg in args[0]]
    for index, arg in enumerate(args):
        if index % 2 != 0:
            pass
        else:
            try:
                final_args += f'''
  - {args[index]} : {args[index + 1]}'''
            except IndexError:
                pass

    return final_args


def doc_generator(*args):
    func_signature = args[0]
    result_type = args[-1]
    return f'''
  """
  {func_signature}

  ---
  Params:{doc_params_generator(args[1:-1])}

  ---
  Returns:
  - val : {result_type} 
  """  

'''


def class_doc_params_generator(*args):
    final_args = ""
    for index, arg in enumerate(args):
        if index % 2 != 0:
            pass
        else:
            try:
                final_args += f'''
    - {args[index]} : {args[index + 1]}'''
            except IndexError:
                pass

    return final_args


def class_doc_generator(*args):
    func_signature = args[0]
    result_type = args[-1]
    return f'''
    """
    {func_signature}

    ---
    Params:{class_doc_params_generator(args[1:-1])}

    ---
    Returns:
    - val : {result_type} 
    """  

'''


def return_signature(line: str):
    return line.split("(")[0].replace("def ", "")


def return_result_type(line: str):
    return line.split("->")[1].replace(":", "").replace("\n", "").replace(" ", "")


def return_params(line: str):
    line = line.split("(")[1]
    line = line.split(")")[0]
    line = [line.replace(" ", "") for line in line.split(":")]
    final_line = []
    for line in [param.split(",") for param in line]:
        if type(line) == str:
            final_line.append(line)
        else:
            for param in line:
                final_line.append(param)
    return final_line


with open("result_file.py", "w") as f:
    for line in content:
        if line.startswith("def"):
            parsed_line = [return_signature(line), *return_params(
                line), return_result_type(line)]
            f.write(line.replace("\n", ""))
            f.write(doc_generator(*parsed_line))
        elif line.startswith("  def"):
            f.write(line.replace("\n", ""))
            f.write(class_doc_generator(*parsed_line))
        else:
            f.write(line)
