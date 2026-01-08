# Data Model: Console Todo App

**Feature**: 001-console-todo-app
**Created**: 2026-01-08
**Status**: Draft

## Entity Definitions

### Todo Item
Represents a single task in the todo list.

**Attributes:**
- `id` (int): Unique sequential identifier assigned automatically
- `title` (str): The description of the task to be completed
- `completed` (bool): Status indicating whether the task is completed (default: False)

**Validation Rules:**
- `title` must not be empty or contain only whitespace characters
- `id` must be unique within the collection
- `completed` is a boolean value (True/False)

**State Transitions:**
- Initially created with `completed=False`
- Can transition to `completed=True` via completion operation
- Can transition back to `completed=False` via uncompletion operation (if implemented)

### Todo Collection
Manages the collection of Todo items in memory.

**Attributes:**
- `todos` (dict[int, TodoItem]): Dictionary mapping unique IDs to TodoItem objects
- `next_id` (int): Counter tracking the next available ID for assignment

**Operations:**
- Add new todo item to collection
- Retrieve todo item by ID
- Update todo item properties
- Delete todo item by ID
- List all todo items
- Validate ID existence before operations

## Relationships

- Each Todo Collection contains multiple Todo Items
- Each Todo Item belongs to exactly one Todo Collection
- Todo Items are referenced by their unique ID within the collection

## Data Integrity Rules

- No duplicate IDs allowed in the collection
- All operations must validate ID existence before execution
- Empty titles are not permitted when creating or updating
- Invalid ID references must result in appropriate error handling