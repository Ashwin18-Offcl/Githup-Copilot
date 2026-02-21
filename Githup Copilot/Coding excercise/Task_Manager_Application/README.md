# Task Manager Application

Simple CLI Task Manager written in Python.

Features:
- Add a task
- Delete a task
- Mark a task as completed
- Show all tasks

Files:
- `tasks.py` - `Task` dataclass and `TaskManager` with JSON persistence
- `cli.py` - simple CLI wrapper using `argparse`
- `tests/test_tasks.py` - unit tests

Usage examples (PowerShell):

```powershell
# Run CLI from the project root
python -c "import Task_Manager_Application.cli as c; c.main(['add','Buy milk'])"
python -c "import Task_Manager_Application.cli as c; c.main(['list'])"

# Or run module directly if Python package import works in your environment
python -m Task_Manager_Application.cli list

# Use --storage to specify a custom storage file
python -c "import Task_Manager_Application.cli as c; c.main(['add','Read book','--storage','C:/temp/tasks.json'])"
```

Run tests:

```powershell
# From workspace root
python -m unittest discover "Task Manager Application/tests"
```
