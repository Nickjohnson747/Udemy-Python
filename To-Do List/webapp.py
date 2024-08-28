import streamlit as st
import functions


def add_todo():
    todo = st.session_state["new_todo"]
    functions.add_todos(todo)


todo_list = functions.get_todos()

st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app helps increase your productivity")
st.caption(
    "Editing text fields is not supported with this library. This webapp will only let you add and remove items"
)

for idx, todo in enumerate(todo_list):
    # create a checkbox item for each item in the todo list
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todo_list.pop(idx)
        functions.edit_todos(todo_list)
        del st.session_state[todo]
        st.rerun()

st.text_input(
    label="a",
    label_visibility="hidden",
    placeholder="Add a new todo...",
    on_change=add_todo,
    key="new_todo",
)
st.caption(
    "You have to manually delete the text in the entry field - no good way to do it with this library automatically"
)

# ==========
# Debug

# st.session_state
