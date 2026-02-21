import argparse
import sys
from pathlib import Path

from .tasks import TaskManager


def main(argv=None):
    parser = argparse.ArgumentParser(prog="taskmgr", description="Simple Task Manager")
    parser.add_argument("command", choices=["add", "delete", "complete", "list", "clear"], help="Command")
    parser.add_argument("title_or_id", nargs="?", help="Task title (for add) or id (for delete/complete)")
    parser.add_argument("--storage", help="Path to storage json file")
    args = parser.parse_args(argv)

    storage = args.storage
    if storage:
        storage = Path(storage)
    manager = TaskManager(storage_path=str(storage) if storage else None)

    try:
        if args.command == "add":
            if not args.title_or_id:
                print("Please provide a task title.")
                return 2
            task = manager.add_task(args.title_or_id)
            print(f"Added: {task.id} - {task.title}")
        elif args.command == "delete":
            if not args.title_or_id:
                print("Please provide a task id to delete.")
                return 2
            removed = manager.delete_task(args.title_or_id)
            print(f"Deleted: {removed.id} - {removed.title}")
        elif args.command == "complete":
            if not args.title_or_id:
                print("Please provide a task id to mark completed.")
                return 2
            t = manager.complete_task(args.title_or_id)
            print(f"Completed: {t.id} - {t.title}")
        elif args.command == "list":
            tasks = manager.list_tasks()
            if not tasks:
                print("No tasks.")
            for t in tasks:
                status = "✔" if t.completed else " "
                print(f"[{status}] {t.id} - {t.title}")
        elif args.command == "clear":
            manager.clear_all()
            print("All tasks cleared.")
    except KeyError as e:
        print(e)
        return 3
    except ValueError as e:
        print(e)
        return 4
    except RuntimeError as e:
        print(e)
        return 5
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
