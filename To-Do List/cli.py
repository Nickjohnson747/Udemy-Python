import functions
import time

now = time.strftime("%b %d, %Y, %H:%M:%S")
print(now)
directory = functions.directory

file = open(directory + "/todos.txt", "w")
file.close
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

            todo_list = functions.get_todos()

            for index, item in enumerate(todo_list):
                print(index + 1, "-", item.strip("\n"))

        case "edit":
            try:
                todo_list = functions.get_todos()
                idx_to_edit: int = int(input("Number of todo item to edit: "))

                # we are displaying using 1-based indexing, so need to adjust for that
                todo_list[idx_to_edit - 1] = input("New todo item: ").title() + "\n"

                functions.write_todos(todo_list)

            except ValueError:
                print(
                    "ERROR: You must enter a number for the item you want to change\n"
                )
            except IndexError:
                print("ERROR: That item number is not in the list")
        case "complete":
            try:
                todo_list = functions.get_todos()
                idx_to_remove: int = int(input("Number of completed todo item: "))

                del todo_list[idx_to_remove - 1]

                functions.write_todos(todo_list)

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
