
built_in_types = ["str", "None", "float", "dict", "set"
                  "int", "complex", "list", "tuple", "bool"]
typing_types = ["Dict", "List", "Tuple"]


def convert_builtin_to_typing(type):
    if type == 'list':
        return 'List'
    elif type == 'tuple':
        return 'Tuple'
    elif type == 'dict':
        return 'Dict'
    else:
        return type


def convert_typing_to_builtin(type):
    if type == 'List':
        return 'list'
    elif type == 'Tuple':
        return 'tuple'
    elif type == 'Dict':
        return 'dict'
    else:
        return type
