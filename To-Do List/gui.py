import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a to-do", key="new_todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(
    values=functions.get_todos(), key="todos", enable_events=True, size=[45, 10]
)
edit_button = sg.Button("Edit")

window = sg.Window(
    "To-Do App",
    layout=[[label], [input_box, add_button], [list_box, edit_button]],
    font=("Helvetica", 20),
)

while True:
    event, values = window.read()
    print(event)
    print(values)

    match event:
        case "Add":
            todos = functions.add_todos(values["new_todo"])
            todo_list = functions.get_todos()

            window["todos"].update(values=todo_list)
        case "Edit":
            todo_list = functions.get_todos()
            idx = todo_list.index(values["todos"][0])
            todo_list[idx] = values["new_todo"] + "\n"
            functions.edit_todos(todo_list)

            window["todos"].update(values=todo_list)
        case "todos":
            # case occurs when clicking in Listbox
            window["new_todo"].update(value=values["todos"][0])

        case sg.WIN_CLOSED:
            break

window.close()
