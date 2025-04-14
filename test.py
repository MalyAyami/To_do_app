# add
import pytest
from task_manager import TaskManager


def test_add_single_task():
    manager = TaskManager()
    task = manager.add_task("Test task")
    assert task["description"] == "Test task"
    assert task["completed"] is False


def test_add_multiple_tasks():
    manager = TaskManager()
    manager.add_task("Task 1")
    task2 = manager.add_task("Task 2")
    assert task2["id"] == 2


def test_task_ids_are_unique():
    manager = TaskManager()
    ids = [manager.add_task(f"Task {i}")["id"] for i in range(5)]
    assert ids == [1, 2, 3, 4, 5]


def test_task_repr():
    manager = TaskManager()
    manager.add_task("Write report")
    assert repr(manager.tasks[0]) == "[❌] (1) Write report"


# remove

def test_remove_existing_task():
    manager = TaskManager()
    manager.add_task("Test task")
    assert manager.remove_task(1) is True


def test_remove_nonexistent_task():
    manager = TaskManager()
    manager.add_task("Test task")
    assert manager.remove_task(999) is False


def test_remove_from_empty_list():
    manager = TaskManager()
    assert manager.remove_task(1) is False


def test_task_list_after_removal():
    manager = TaskManager()
    manager.add_task("Task to delete")
    manager.remove_task(1)
    assert len(manager.tasks) == 0


# edit

def test_edit_existing_task():
    manager = TaskManager()
    manager.add_task("Old")
    assert manager.edit_task(1, "New") is True
    assert manager.tasks[0].description == "New"


def test_edit_nonexistent_task():
    manager = TaskManager()
    assert manager.edit_task(99, "New Desc") is False


def test_edit_empty_description():
    manager = TaskManager()
    manager.add_task("Fill me")
    manager.edit_task(1, "")
    assert manager.tasks[0].description == ""


def test_edit_keeps_completion_status():
    manager = TaskManager()
    manager.add_task("Edit this")
    manager.complete_task(1)
    manager.edit_task(1, "Edited")
    assert manager.tasks[0].completed is True


# complete

def test_complete_existing_task():
    manager = TaskManager()
    manager.add_task("Do it")
    assert manager.complete_task(1) is True
    assert manager.tasks[0].completed is True


def test_complete_already_completed_task():
    manager = TaskManager()
    manager.add_task("Do it")
    manager.complete_task(1)
    assert manager.complete_task(1) is True


def test_complete_nonexistent_task():
    manager = TaskManager()
    assert manager.complete_task(42) is False


def test_complete_does_not_affect_others():
    manager = TaskManager()
    manager.add_task("Task 1")
    manager.add_task("Task 2")
    manager.complete_task(1)
    assert manager.tasks[1].completed is False


# filter

def test_filter_all_tasks():
    manager = TaskManager()
    manager.add_task("Task 1")
    manager.add_task("Task 2")
    tasks = manager.filter_tasks("all")
    assert len(tasks) == 2


def test_filter_completed_tasks():
    manager = TaskManager()
    manager.add_task("Task 1")
    manager.add_task("Task 2")
    manager.complete_task(2)
    tasks = manager.filter_tasks("done")
    assert len(tasks) == 1
    assert tasks[0]["id"] == 2


def test_filter_pending_tasks():
    manager = TaskManager()
    manager.add_task("Task 1")
    manager.add_task("Task 2")
    manager.complete_task(1)
    tasks = manager.filter_tasks("pending")
    assert len(tasks) == 1
    assert tasks[0]["id"] == 2


def test_filter_invalid_status_returns_all():
    manager = TaskManager()
    manager.add_task("Task 1")
    tasks = manager.filter_tasks("unknown")
    assert len(tasks) == 1