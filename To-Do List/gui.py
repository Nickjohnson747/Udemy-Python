import functions
import FreeSimpleGUI as sg
import time

clock = sg.Text("", key="clock")
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a to-do", key="new_todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(
    values=functions.get_todos(), key="todos", enable_events=True, size=[45, 10]
)
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window(
    "To-Do App",
    layout=[
        [clock],
        [label],
        [input_box, add_button],
        [list_box, edit_button, complete_button],
        [exit_button],
    ],
    font=("Helvetica", 20),
)

while True:
    event, values = window.read(timeout=10)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    # print(event)
    # print(values)

    match event:
        case "Add":
            added_todo = functions.add_todos(values["new_todo"])
            todo_list = functions.get_todos()

            window["todos"].update(values=todo_list)

        case "Edit":
            try:
                todo_list = functions.get_todos()
                idx_to_edit = todo_list.index(values["todos"][0])

                # Have to strip new line from list_box and re-add so values don't write onto wrong lines
                todo_list[idx_to_edit] = values["new_todo".strip("\n")] + "\n"
                functions.edit_todos(todo_list)

                window["todos"].update(values=todo_list)
            except IndexError as e:
                sg.popup("Please select an item first", font=("Helvetica", 20))
        case "Complete":
            try:
                todo_list = functions.get_todos()
                completed_todo = values["todos"][0]
                todo_list.remove(completed_todo)
                functions.edit_todos(todo_list)

                window["todos"].update(values=todo_list)
            except IndexError as e:
                sg.popup("Please select an item first", font=("Helvetica", 20))
        case "Exit":
            break

        # case occurs when clicking in Listbox
        case "todos":

            window["new_todo"].update(value=values["todos"][0])

        case sg.WIN_CLOSED:
            # Occurs on hitting 'x' button in gui
            break

window.close()
