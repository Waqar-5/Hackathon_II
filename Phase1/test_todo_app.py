"""
Simple test script to verify the todo application functionality.
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

from src.services.todo_service import TodoService
from src.interfaces.cli_interface import CLIInterface
from src.models.todo import Todo

def test_todo_functionality():
    """Test the core functionality of the todo application."""
    print("Testing Todo Application Functionality...")

    # Create service and interface
    todo_service = TodoService()
    cli_interface = CLIInterface(todo_service)

    # Test 1: Add a todo
    result = cli_interface.add_todo("Test todo item")
    print(f"Add todo: {result}")
    assert "Added todo" in result

    # Test 2: List todos
    result = cli_interface.list_todos()
    print(f"List todos: {result}")
    assert "Test todo item" in result

    # Test 3: Add another todo
    result = cli_interface.add_todo("Second todo item")
    print(f"Add second todo: {result}")
    assert "Added todo" in result

    # Test 4: List all todos
    result = cli_interface.list_todos()
    print(f"List all todos: {result}")
    assert "Test todo item" in result
    assert "Second todo item" in result

    # Test 5: Complete a todo
    result = cli_interface.complete_todo("1")
    print(f"Complete todo 1: {result}")
    assert "marked todo 1 as complete" in result.lower()

    # Test 6: List todos to see completion status
    result = cli_interface.list_todos()
    print(f"List todos after completion: {result}")
    assert "[X]" in result  # Should show completed status with X for completed items

    # Test 7: Update a todo
    result = cli_interface.update_todo(["2", "Updated todo description"])
    print(f"Update todo 2: {result}")
    assert "updated todo 2" in result.lower()

    # Test 8: Delete a todo
    result = cli_interface.delete_todo("1")
    print(f"Delete todo 1: {result}")
    assert "deleted todo with id 1" in result.lower()

    # Test 9: List todos to confirm deletion
    result = cli_interface.list_todos()
    print(f"List todos after deletion: {result}")
    assert "todo with id 1" not in result.lower()
    assert "Updated todo description" in result

    # Test 10: Error handling - try to complete non-existent todo
    result = cli_interface.complete_todo("999")
    print(f"Try to complete non-existent todo: {result}")
    assert "not found" in result.lower()

    print("\nAll tests passed! The todo application is working correctly.")

if __name__ == "__main__":
    test_todo_functionality()