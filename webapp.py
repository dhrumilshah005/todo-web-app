import streamlit as st
import Functions
import time
import datetime

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

now = datetime.datetime.now()
now = now.strftime("%d-%B-%Y %H:%M:%S")
text = st.empty()
st.title("My todo app")
st.write("This minimalist app will be helpful to manage the day-to-day tasks. Check the Checkbox to mark the task as complete")
st.text_input(label="",placeholder="Enter a task",on_change=add_todo,key='new_todo')

for i,j in enumerate(existing_todos):
    checkbox = st.checkbox(j,key=j)
    if checkbox:
        existing_todos.remove(j)
        Functions.new_todos(existing_todos)
        st.rerun()
