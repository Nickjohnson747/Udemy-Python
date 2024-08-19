import os

directory: str = os.path.dirname(os.path.abspath(__file__))


def write_todos(todo_list: str) -> None:
    with open(directory + "/todos.txt", "w") as todo_file:
        todo_file.writelines(todo_list)


def get_todos() -> list:
    with open(directory + "/todos.txt", "r") as todo_file:
        todo_list = todo_file.readlines()

    return todo_list


while True:
    user_action: str = input("Type add, show, edit, complete, or quit: ").strip()

    match user_action.lower():
        case "add":
            todo: str = input("Todo item: ")
            # todo_list.append(todo.title())

            with open(directory + "/todos.txt", "a") as todo_file:
                todo_file.writelines(todo.title() + "\n")

        # match/case requires bitwise operators
        case "show" | "display":

            todo_list = get_todos()

            for index, item in enumerate(todo_list):
                print(index + 1, "-", item.strip("\n"))

        case "edit":
            try:
                todo_list = get_todos()
                idx_to_edit: int = int(input("Number of todo item to edit: "))

                # we are displaying using 1-based indexing, so need to adjust for that
                todo_list[idx_to_edit - 1] = input("New todo item: ").title() + "\n"

                write_todos(todo_list)

            except ValueError:
                print(
                    "ERROR: You must enter a number for the item you want to change\n"
                )
            except IndexError:
                print("ERROR: That item number is not in the list")
        case "complete":
            try:
                todo_list = get_todos()
                idx_to_remove: int = int(input("Number of completed todo item: "))

                del todo_list[idx_to_remove - 1]

                write_todos(todo_list)

            except ValueError as e:
                print(
                    e,
                    "ERROR: You must enter a number for the item you want to change\n",
                )
            except IndexError as e:
                print(e, "ERROR: That item number is not in the list")

        case "quit":
            print("Exiting...")
            break

        case _:
            print("Unknown command was entered")
