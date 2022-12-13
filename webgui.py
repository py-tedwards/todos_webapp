import streamlit as st
import functions

todos = functions.read_todos()
todo_key_int = 0
todo_key_list = []


def add_todo():
    new_todo = st.session_state['add_todo_input']+'\n'
    todos.append(new_todo)
    functions.write_todos(todos)


st.title("Todo App")
st.subheader("List of todos below")
st.write("Designed to increase productivity")

for todo in todos:
    st.checkbox(todo, key=todo_key_int)
    todo_key_list.append(todo_key_int)
    todo_key_int = todo_key_int+1

for todo, todo_key in zip(todos, todo_key_list):
    checkbox = st.session_state[todo_key]
    if checkbox:
        todos.pop(todos.index(todo))
        functions.write_todos(todos)
        del st.session_state[todo_key]
        st.experimental_rerun()


st.text_input(label="_", label_visibility="hidden", placeholder="Add new todo...",
              key='add_todo_input', on_change=add_todo)