import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a to-do", key="todo")
add_button = sg.Button("Add")

window = sg.Window(
    "To-Do App", layout=[[label], [input_box, add_button]], font=("Helvetica", 20)
)

while True:
    event, values = window.read()
    print(event)
    print(values)

    match event:
        case "Add":
            todos = functions.add_todos(values["todo"])
        case "Edit":
            pass
        case sg.WIN_CLOSED:
            break

window.close()
