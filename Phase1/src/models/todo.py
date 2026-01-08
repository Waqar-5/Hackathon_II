"""
Todo model class representing a single todo item.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Todo:
    """
    Represents a single todo item with id, title, and completion status.
    """
    id: int
    title: str
    completed: bool = False

    def __post_init__(self):
        """Validate the todo after initialization."""
        if not isinstance(self.id, int) or self.id < 0:
            raise ValueError(f"Todo ID must be a non-negative integer, got {self.id}")

        if not isinstance(self.title, str) or not self.title.strip():
            raise ValueError(f"Todo title must be a non-empty string, got {repr(self.title)}")

        if not isinstance(self.completed, bool):
            raise ValueError(f"Todo completed status must be a boolean, got {self.completed}")

    def mark_completed(self) -> None:
        """Mark the todo as completed."""
        self.completed = True

    def update_title(self, new_title: str) -> None:
        """Update the todo title after validation."""
        if not isinstance(new_title, str) or not new_title.strip():
            raise ValueError(f"Todo title must be a non-empty string, got {repr(new_title)}")

        self.title = new_title.strip()