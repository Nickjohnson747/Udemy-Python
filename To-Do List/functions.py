import os

directory: str = os.path.dirname(os.path.abspath(__file__))

# creates file when imported instead of based on which file you run (CLI or GUI)
file = open(directory + "/todos.txt", "a")
file.close()


# use a instead of w filemode so we don't have to re-write the entire file when adding 1 item
def add_todos(todo: str) -> None:
    with open(directory + "/todos.txt", "a") as todo_file:
        todo_file.writelines(todo.title() + "\n")


def get_todos() -> list:
    with open(directory + "/todos.txt", "r") as todo_file:
        todo_list = todo_file.readlines()

    return todo_list


def edit_todos(todo_list: str) -> None:
    with open(directory + "/todos.txt", "w") as todo_file:
        todo_file.writelines(todo_list)
