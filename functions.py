def get_todos(filepath="todos.txt"):
    """Read a text file and return a list of
    to-do items"""
    with open("todos.txt", "r") as file_local:
        todos_local = file_local.readlines()

    return todos_local


def write_todos(todos_arg, filepath="todos.txt"):
    """write a to do item list in a text file"""
    with open(filepath, "w") as file:
        file.writelines(todos_arg)

