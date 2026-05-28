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

def markTaskComplete(all_tasks):
    task_number = input("Enter the number of the task you want to mark as complete: ")
    all_tasks[int(task_number) - 1] += " (Completed)"

    print(f'\nItem {task_number} has been marked as complete.')

    displayTasks(all_tasks)
    newOperation(all_tasks)

def editTask(all_tasks):
    task_number = input("Enter the number of the task you want to edit: ")

    new_task = input("Edit task: ")
    all_tasks[int(task_number) - 1] = new_task

    print(f'\nItem {task_number} has been edited.')

    displayTasks(all_tasks)
    newOperation(all_tasks)

def removeTask(all_tasks):
    task_number = (input("Enter the number of the task you want to remove: "))

    all_tasks.remove(all_tasks[int(task_number) - 1])

    print(f'\nItem {task_number} has been removed.')
    
    displayTasks(all_tasks)
    newOperation(all_tasks)

def addTask(all_tasks):
    newtask = input("Add a task: ")
    all_tasks.append(newtask)

    for task in all_tasks:
        print(task)


    newOperation(all_tasks)

# Start Application
addTask(tasks)