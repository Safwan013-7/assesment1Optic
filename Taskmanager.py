import json
import os

# Configuration
TASKS_FILE = 'taskm.json'

# Load tasks from JSON file
def loadTasks():
    if os.path.exists(TASKS_FILE):
        try:
            with open(TASKS_FILE, 'r') as file:
                return json.load(file)
        except:
            return []
    return []

# Save tasks to JSON file
def saveTasks(all_tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(all_tasks, file, indent=2)

# initial empty list of tasks
tasks = []

#auxiliary functions
def displayTasks(all_tasks):
    print('\nYour tasks:')

    if len(all_tasks) <= 0:
        print("No tasks to display.")
    else:
        for index, task in enumerate(all_tasks):
            print(f"{index + 1}. {task}")

# main function to determine which operation the user wants to perform
def newOperation(all_tasks): 
    operation = input("Press 'A' to add a task, 'E' to edit a task, 'R' to remove a task, 'V' to view all tasks, 'M' to mark a task as complete, or 'Q' to quit: ")

    if operation == 'A':
        addTask(all_tasks)
    elif operation == 'E':
        editTask(all_tasks)
    elif operation == 'R':
        removeTask(all_tasks)
    elif operation == 'V':
        displayTasks(all_tasks)
    elif operation == 'M':
        markTaskComplete(all_tasks)
    elif operation == 'Q':
        return
    else: 
        newOperation(all_tasks)

# function to mark a task as complete by appending " (Completed)" to the end of the task string
def markTaskComplete(all_tasks):
    task_number = input("Enter the number of the task you want to mark as complete: ")
    all_tasks[int(task_number) - 1] += " (Completed)"

    print(f'\nItem {task_number} has been marked as complete.')

    saveTasks(all_tasks)
    displayTasks(all_tasks)
    newOperation(all_tasks)

# function to edit a task by replacing the task string with a new string input by the user
def editTask(all_tasks):
    task_number = input("Enter the number of the task you want to edit: ")

    new_task = input("Edit task: ")
    all_tasks[int(task_number) - 1] = new_task

    print(f'\nItem {task_number} has been edited.')

    saveTasks(all_tasks)
    displayTasks(all_tasks)
    newOperation(all_tasks)

# function to remove a task from the list
def removeTask(all_tasks):
    task_number = (input("Enter the number of the task you want to remove: "))

    all_tasks.remove(all_tasks[int(task_number) - 1])

    print(f'\nItem {task_number} has been removed.')
    
    saveTasks(all_tasks)
    displayTasks(all_tasks)

    newOperation(all_tasks)

# function to add a task to the list and display all tasks after adding the new task
def addTask(all_tasks):
    newtask = input("Add a task: ")
    all_tasks.append(newtask)

    saveTasks(all_tasks)
    for task in all_tasks:
        print(task)


    newOperation(all_tasks)

# Start Application
tasks = loadTasks()
addTask(tasks)