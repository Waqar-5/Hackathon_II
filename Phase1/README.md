# Console Todo App

A simple command-line todo application built with Python.

## Features

- Add new todo items
- View all todo items with completion status
- Mark todo items as complete
- Update todo item descriptions
- Delete todo items
- Graceful shutdown with Ctrl+C support

## Prerequisites

- Python 3.13 or higher

## Installation

1. Clone or download the repository
2. Navigate to the project directory
3. The application can be run directly with Python

## Usage

Run the application:

```bash
python -m src.main
```

Once the application is running, you can use the following commands:

- `add <description>` - Add a new todo item
- `list` - List all todo items
- `complete <id>` - Mark a todo as complete
- `update <id> <new description>` - Update a todo's description
- `delete <id>` - Delete a todo item
- `help` - Show help information
- `quit` or `exit` - Exit the application

### Example Session

```
> add Buy groceries
Added todo: 'Buy groceries' with ID 1

> add Clean the house
Added todo: 'Clean the house' with ID 2

> list
Todo List:
  [O] 1: Buy groceries
  [O] 2: Clean the house

> complete 1
Marked todo 1 as complete: 'Buy groceries'

> list
Todo List:
  [X] 1: Buy groceries
  [O] 2: Clean the house

> quit
Goodbye!
```

## Architecture

The application follows a clean architecture pattern:

- `src/models/todo.py` - Data model for todo items
- `src/services/todo_service.py` - Business logic for todo operations
- `src/interfaces/cli_interface.py` - CLI command handlers
- `src/main.py` - Main application loop and entry point

## Testing

Run the test suite:

```bash
python test_todo_app.py
```

## License

MIT