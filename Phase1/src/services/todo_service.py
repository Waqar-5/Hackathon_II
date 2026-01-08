"""
Todo service class managing todo items in memory.
"""

from typing import List, Optional
from src.models.todo import Todo


class TodoService:
    """
    Service class for managing todo items with in-memory storage.
    """
    def __init__(self):
        self._todos: List[Todo] = []
        self._next_id: int = 1

    def add_todo(self, title: str) -> Todo:
        """
        Add a new todo item with validation.

        Args:
            title: The title/description of the todo item

        Returns:
            The created Todo object

        Raises:
            ValueError: If the title is empty or invalid
        """
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Todo title must be a non-empty string")

        title = title.strip()

        # Create new todo with next available ID
        new_todo = Todo(id=self._next_id, title=title, completed=False)
        self._todos.append(new_todo)

        # Increment next ID for the next todo
        self._next_id += 1

        return new_todo

    def get_all_todos(self) -> List[Todo]:
        """
        Get all todo items.

        Returns:
            List of all todo items
        """
        return self._todos.copy()  # Return a copy to prevent external modification

    def complete_todo(self, todo_id: int) -> Optional[Todo]:
        """
        Mark a todo item as complete.

        Args:
            todo_id: The ID of the todo to mark as complete

        Returns:
            The updated Todo object if found, None otherwise
        """
        if not isinstance(todo_id, int) or todo_id < 1:
            raise ValueError("Todo ID must be a positive integer")

        for todo in self._todos:
            if todo.id == todo_id:
                todo.mark_completed()
                return todo

        return None

    def update_todo(self, todo_id: int, new_title: str) -> Optional[Todo]:
        """
        Update a todo item's title.

        Args:
            todo_id: The ID of the todo to update
            new_title: The new title for the todo

        Returns:
            The updated Todo object if found, None otherwise

        Raises:
            ValueError: If the new title is empty or invalid
        """
        if not isinstance(todo_id, int) or todo_id < 1:
            raise ValueError("Todo ID must be a positive integer")

        if not isinstance(new_title, str) or not new_title.strip():
            raise ValueError("Todo title must be a non-empty string")

        new_title = new_title.strip()

        for todo in self._todos:
            if todo.id == todo_id:
                todo.update_title(new_title)
                return todo

        return None

    def delete_todo(self, todo_id: int) -> bool:
        """
        Delete a todo item.

        Args:
            todo_id: The ID of the todo to delete

        Returns:
            True if the todo was deleted, False if not found
        """
        if not isinstance(todo_id, int) or todo_id < 1:
            raise ValueError("Todo ID must be a positive integer")

        for i, todo in enumerate(self._todos):
            if todo.id == todo_id:
                del self._todos[i]
                return True

        return False