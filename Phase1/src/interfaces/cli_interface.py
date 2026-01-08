"""
CLI interface for the todo application.
"""

from typing import List, Optional
from src.services.todo_service import TodoService
from src.models.todo import Todo


class CLIInterface:
    """
    Command-line interface for the todo application.
    """
    def __init__(self, todo_service: TodoService):
        self.todo_service = todo_service

    def add_todo(self, title: str) -> str:
        """
        Handle the add todo command.

        Args:
            title: The title of the todo to add

        Returns:
            Confirmation message
        """
        try:
            todo = self.todo_service.add_todo(title)
            return f"Added todo: '{todo.title}' with ID {todo.id}"
        except ValueError as e:
            return f"Error: {str(e)}"

    def list_todos(self) -> str:
        """
        Handle the list todos command.

        Returns:
            Formatted string of all todos
        """
        todos = self.todo_service.get_all_todos()

        if not todos:
            return "No todos in the list."

        lines = ["Todo List:"]
        for todo in todos:
            status = "X" if todo.completed else "O"
            lines.append(f"  [{status}] {todo.id}: {todo.title}")

        return "\n".join(lines)

    def complete_todo(self, todo_id_str: str) -> str:
        """
        Handle the complete todo command.

        Args:
            todo_id_str: String representation of the todo ID to complete

        Returns:
            Confirmation or error message
        """
        try:
            todo_id = int(todo_id_str)
        except ValueError:
            return f"Error: Todo ID must be a number, got '{todo_id_str}'"

        if todo_id < 1:
            return f"Error: Todo ID must be a positive number, got {todo_id}"

        todo = self.todo_service.complete_todo(todo_id)

        if todo:
            return f"Marked todo {todo.id} as complete: '{todo.title}'"
        else:
            return f"Error: Todo with ID {todo_id} not found"

    def update_todo(self, args: List[str]) -> str:
        """
        Handle the update todo command.

        Args:
            args: List containing todo ID and new title

        Returns:
            Confirmation or error message
        """
        if len(args) < 2:
            return "Error: Update command requires ID and new title"

        try:
            todo_id = int(args[0])
        except ValueError:
            return f"Error: Todo ID must be a number, got '{args[0]}'"

        new_title = " ".join(args[1:])

        if todo_id < 1:
            return f"Error: Todo ID must be a positive number, got {todo_id}"

        todo = self.todo_service.update_todo(todo_id, new_title)

        if todo:
            return f"Updated todo {todo.id}: '{todo.title}'"
        else:
            return f"Error: Todo with ID {todo_id} not found"

    def delete_todo(self, todo_id_str: str) -> str:
        """
        Handle the delete todo command.

        Args:
            todo_id_str: String representation of the todo ID to delete

        Returns:
            Confirmation or error message
        """
        try:
            todo_id = int(todo_id_str)
        except ValueError:
            return f"Error: Todo ID must be a number, got '{todo_id_str}'"

        if todo_id < 1:
            return f"Error: Todo ID must be a positive number, got {todo_id}"

        deleted = self.todo_service.delete_todo(todo_id)

        if deleted:
            return f"Deleted todo with ID {todo_id}"
        else:
            return f"Error: Todo with ID {todo_id} not found"

    def show_help(self) -> str:
        """
        Show help information.

        Returns:
            Help text
        """
        help_text = help_text = """
📋  Welcome to Your Personal Todo CLI App!

✨ Commands Overview:

  ➕  add <description>       - Add a shiny new todo item
  📝  list                     - Display all your todo treasures
  ✅  complete <id>            - Mark a todo as completed
  ✏️  update <id> <title>     - Edit the title of a todo
  🗑️  delete <id>             - Remove a todo item forever
  ❓  help                     - Show this guide again
  🚪  quit                     - Exit the app safely

💡 Tip: Use the 'list' command frequently to keep track of your progress!
""".strip()

        return help_text