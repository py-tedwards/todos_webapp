FILEPATH = 'todos.txt'

def read_todos(filepath = FILEPATH):
    """ Open filepath, read through todos list,
    return the list. """
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write todos list with list
    arg passed through. """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
