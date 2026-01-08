# Quickstart Guide: Console Todo App

**Feature**: 001-console-todo-app
**Created**: 2026-01-08

## Getting Started

### Prerequisites
- Python 3.13 or higher
- UV package manager (optional, for dependency management)

### Installation
1. Clone or download the todo application source code
2. Navigate to the project directory
3. (Optional) Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

### Running the Application
Execute the main application file:
```bash
python src/main.py
```

## Basic Usage

Once the application starts, you'll see a command prompt. Available commands:

### Adding a Todo
```bash
add "Buy groceries"
```
Adds a new todo item with the specified description.

### Listing Todos
```bash
list
```
Displays all todo items with their IDs, descriptions, and completion status.

### Marking as Complete
```bash
complete 1
```
Marks the todo item with ID 1 as complete.

### Updating a Todo
```bash
update 1 "Buy groceries and cook dinner"
```
Updates the description of the todo item with ID 1.

### Deleting a Todo
```bash
delete 1
```
Removes the todo item with ID 1 from the list.

### Exiting the Application
```bash
quit
```
Exits the todo application.

## Example Session
```
> add "Buy milk"
Todo added with ID 1: Buy milk

> add "Walk the dog"
Todo added with ID 2: Walk the dog

> list
1. [ ] Buy milk
2. [ ] Walk the dog

> complete 1
Todo 1 marked as complete

> list
1. [x] Buy milk
2. [ ] Walk the dog

> quit
Goodbye!
```

## Troubleshooting

- If you get a "command not recognized" error, ensure you're typing the command correctly
- If you see an "Invalid ID" error, verify the todo item exists before attempting operations
- For empty description errors, ensure all todo items have meaningful content