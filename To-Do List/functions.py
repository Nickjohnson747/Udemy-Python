import os

directory: str = os.path.dirname(os.path.abspath(__file__))


def write_todos(todo_list: str) -> None:
    with open(directory + "/todos.txt", "w") as todo_file:
        todo_file.writelines(todo_list)


def get_todos() -> list:
    with open(directory + "/todos.txt", "r") as todo_file:
        todo_list = todo_file.readlines()

    return todo_list
