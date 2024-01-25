import streamlit as st
import Functions
import time

existing_todos = Functions.get_todos()
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    existing_todos.append(todo)
    Functions.new_todos(existing_todos)
    time.sleep(0.1)
    st.session_state["new_todo"] =""

def complete_todo(todo):
    existing_todos.remove(todo)
    Functions.new_todos(existing_todos)
    st.rerun()


text = st.empty()
st.title("My todo app")
st.write("This is a minimalist To-do app to track the day-to-day tasks.")
st.text_input(label="",placeholder="Enter a task",on_change=add_todo,key='new_todo')

for i,j in enumerate(existing_todos):
    checkbox = st.checkbox(j,key=j)
    if checkbox:
        existing_todos.remove(j)
        Functions.new_todos(existing_todos)
        st.rerun()
