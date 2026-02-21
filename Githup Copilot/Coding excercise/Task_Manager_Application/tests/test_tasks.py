import os
import tempfile
import unittest
import importlib.util
from pathlib import Path


# Load TaskManager from the sibling tasks.py file by filepath to avoid package import issues
tests_dir = Path(__file__).resolve().parent
tasks_path = (tests_dir / '..' / 'tasks.py').resolve()
spec = importlib.util.spec_from_file_location('tasks', str(tasks_path))
tasks_mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tasks_mod)
TaskManager = tasks_mod.TaskManager


class TaskManagerTests(unittest.TestCase):
    def setUp(self):
        # create a temporary file path for storage
        fd, self.path = tempfile.mkstemp(suffix=".json")
        os.close(fd)
        # ensure empty file
        with open(self.path, 'w', encoding='utf-8') as f:
            f.write('[]')
        # instantiate manager with that storage
        self.m = TaskManager(storage_path=self.path)

    def tearDown(self):
        try:
            os.remove(self.path)
        except OSError:
            pass

    def test_add_and_list(self):
        t = self.m.add_task('Buy milk')
        tasks = self.m.list_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0].title, 'Buy milk')
        self.assertFalse(tasks[0].completed)

    def test_delete(self):
        t = self.m.add_task('Task to delete')
        removed = self.m.delete_task(t.id)
        self.assertEqual(removed.id, t.id)
        self.assertEqual(len(self.m.list_tasks()), 0)
        with self.assertRaises(KeyError):
            self.m.delete_task('non-existent')

    def test_complete(self):
        t = self.m.add_task('Do homework')
        self.assertFalse(t.completed)
        updated = self.m.complete_task(t.id)
        self.assertTrue(updated.completed)
        # completing again is allowed and idempotent
        updated2 = self.m.complete_task(t.id)
        self.assertTrue(updated2.completed)
        with self.assertRaises(KeyError):
            self.m.complete_task('no-id')

    def test_persistence(self):
        t = self.m.add_task('Persist me')
        # create a new manager instance pointed at same storage
        m2 = TaskManager(storage_path=self.path)
        all_titles = [x.title for x in m2.list_tasks()]
        self.assertIn('Persist me', all_titles)


if __name__ == '__main__':
    unittest.main()
