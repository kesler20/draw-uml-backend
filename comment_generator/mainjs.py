

with open("test_file.js", "r") as f:
    content = f.readlines()

with open("any_symbol.txt", "r") as f:
    any_symbol = f.readlines()[0]


def doc_generator(func_params, func_signature, func_result):
    if func_params == "" or func_signature == "" or func_result == "":
        return ""
    else:
        return f'''
/**
 * {func_signature}
 * 
 * @param {any_symbol} {func_params} 
 * @returns {func_result}
 */
'''


with open("result_file.js", "w") as f:
    func_params = ""
    func_signature = ""
    func_result = ""
    for line in content:
        if line.endswith(") => {"):
            func_params = line.split(")")[0].split("(")[1].split(",")
            func_signature = line.split("const ")[1].split(" = (")[0]
        if line.startswith("  return "):
            func_result = line.replace("  return ", "").replace("\n", "")

        f.write(doc_generator(func_params, func_signature, func_result))
        f.write(line)
