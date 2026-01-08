# Quickstart Guide: Console Todo App

## Getting Started

1. Ensure you have Python 3.13+ installed
2. Navigate to the project directory
3. Run the application:

```bash
python -m src.main
```

## Basic Commands

### Add a Todo
```
> add My first todo item
Added todo: 'My first todo item' with ID 1
```

### View Todos
```
> list
Todo List:
  [O] 1: My first todo item
```

### Complete a Todo
```
> complete 1
Marked todo 1 as complete: 'My first todo item'
```

### Update a Todo
```
> update 1 Updated todo description
Updated todo 1: 'Updated todo description'
```

### Delete a Todo
```
> delete 1
Deleted todo with ID 1
```

### Get Help
```
> help

Todo App Help:
  add <description>     - Add a new todo item
  list                 - List all todo items
  complete <id>        - Mark a todo as complete
  update <id> <title>  - Update a todo's title
  delete <id>          - Delete a todo item
  help                 - Show this help message
  quit                 - Exit the application
```

### Exit the Application
```
> quit
Goodbye!
```

## Example Workflow

Here's a complete example of using the application:

```
Welcome to the Console Todo App!
Type 'help' for available commands or 'quit' to exit.

> add Learn Python
Added todo: 'Learn Python' with ID 1

> add Build a todo app
Added todo: 'Build a todo app' with ID 2

> list
Todo List:
  [O] 1: Learn Python
  [O] 2: Build a todo app

> complete 1
Marked todo 1 as complete: 'Learn Python'

> list
Todo List:
  [X] 1: Learn Python
  [O] 2: Build a todo app

> quit
Goodbye!
```

That's it! You're ready to use the Console Todo App.