# Task Manager

A simple command-line task management application written in Python that helps you keep track of your to-do items.

## Features

- **Add tasks** - Create new tasks and add them to your list
- **View tasks** - Display all your current tasks with numbering
- **Edit tasks** - Modify existing tasks
- **Remove tasks** - Delete tasks you no longer need
- **Mark tasks complete** - Mark tasks as completed without removing them
- **Persistent storage** - All tasks are automatically saved to `taskm.json` and loaded when you restart the program

## Requirements

- Python 3.x

## How to Run

1. Open a terminal in the project directory
2. Run the following command:

```bash
python Taskmanager.py
```

Or for unbuffered output:

```bash
python -u Taskmanager.py
```

## How to Use

When you start the program, you'll be presented with a menu of options:

```
Press 'A' to add a task, 'E' to edit a task, 'R' to remove a task, 'V' to view all tasks, 'M' to mark a task as complete, or 'Q' to quit:
```

### Available Commands

| Command | Action |
|---------|--------|
| **A** | Add a new task to your list |
| **E** | Edit an existing task by its number |
| **R** | Remove a task from your list |
| **V** | View all your current tasks |
| **M** | Mark a task as complete |
| **Q** | Quit the application |

### Example Workflow

1. Start the program: `python Taskmanager.py`
2. Press `A` to add a task
3. Enter your task description (e.g., "Buy groceries")
4. Press `V` to view all tasks
5. Press `M` to mark a task as complete
6. Press `Q` to quit

## Data Storage

All tasks are automatically saved to `taskm.json` in JSON format. This file is:
- Created automatically when you add your first task
- Updated every time you make changes (add, edit, remove, mark complete)
- Loaded when the program starts, so your tasks persist between sessions

You can view your tasks by opening `taskm.json` in any text editor.

## Example taskm.json

```json
[
  "Buy groceries",
  "Call mom (Completed)",
  "Finish project report"
]
```

---

**Enjoy organizing your tasks!**
