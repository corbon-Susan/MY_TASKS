
# @title 2. To-Do List Application
"""
 A to-do list application is a practical project that
 helps users manage tasks efficiently. This application allows
 users to add, remove, and view tasks while keeping track of
 completed and pending activities. Learning to build a to-do
 list enhances understanding of data structures, file
 handling, and basic user interaction in Python.
 This project will cover step-by-step implementation of a to
 do list application, user input handling, list operations, and
 file handling for persistent storage.
 Key Concepts of To-Do List in Python
 Basic List Operations:-Adding tasks-Removing tasks-Marking tasks as complete-Displaying tasks-User Input Handling:-Using input() function-Handling invalid inputs
 File Handling:-Storing tasks in a text file-Retrieving saved tasks on program
 restart
 Functions in Python:-Defining functions for task management-Calling functions with user inputs
 """
Tasks=[]
def add_task (task):
    Tasks.append(task)
    print(f'Task"{task}" added!')

def remove_task(task):
    if task in Tasks:
        Tasks.remove(task)
        for index, task in enumerate(Tasks, 1):
            print(f'{index}. {task}')
    else:
        print("No tasks in your list")

def view_tasks():
    if Tasks:
        print("Your Tasks:")
        for index, task in enumerate(Tasks, 1):  # Start numbering from 1
            print(f'{index}. {task}')
    else:
        print(" No tasks in your list")

while True:
    print("\nOption: 1. Add Task   2.  Remove Task  3. View Tasks   4. Exit")
    Choice = input (" Enter your choice: ")
    if Choice == '1':
        task = input(" Enter task: ")
        add_task(task)
    elif Choice == '2':
        task = input ( " Enter task to remove: ")
        remove_task(task)
    elif Choice =='3':
        view_tasks()
    elif Choice == '4':
        print ("Existing program, have a productive day")
    else:     
        print("Invalid choice! Please select a valid option.")
        break


from pathlib import Path
workspace =Path ("to do list")
workspace.mkdir(exist_ok =True)
file_path = workspace/"To_do_list.txt"
file_path