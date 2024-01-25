filepath = "todos.txt"
def get_todos(filepath = "todos.txt"):
    with open(filepath, "r") as old_file:
        todos_old = old_file.readlines()
    return todos_old

def new_todos(todos,filepath="todos.txt"):
    with open(filepath, 'w') as new_file:
        new_todos = new_file.writelines(todos)
    return new_todos


if __name__ == "__main__":
    print("Called from the main program")