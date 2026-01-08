"""
Main entry point for the console todo application.
"""

import sys
import signal
from typing import List
from src.services.todo_service import TodoService
from src.interfaces.cli_interface import CLIInterface


class TodoApp:
    """
    Main application class that manages the todo app lifecycle.
    """
    def __init__(self):
        self.todo_service = TodoService()
        self.cli_interface = CLIInterface(self.todo_service)
        self.running = True

    def handle_signal(self, signum, frame):
        """Handle interrupt signal (Ctrl+C)."""
        print("\nReceived interrupt signal. Exiting...")
        self.running = False

    def parse_command(self, user_input: str) -> List[str]:
        """
        Parse user input into command and arguments, handling quoted strings.

        Args:
            user_input: Raw user input string

        Returns:
            List of command parts
        """
        # Handle quoted strings
        parts = []
        current_part = ""
        in_quotes = False
        i = 0

        while i < len(user_input):
            char = user_input[i]

            if char == '"':
                in_quotes = not in_quotes
            elif char == ' ' and not in_quotes:
                if current_part:
                    parts.append(current_part)
                    current_part = ""
            else:
                current_part += char

            i += 1

        # Add the last part if it exists
        if current_part:
            parts.append(current_part)

        return parts

    def execute_command(self, command_parts: List[str]) -> str:
        """
        Execute a command based on parsed parts.

        Args:
            command_parts: List of command parts [command, arg1, arg2, ...]

        Returns:
            Command execution result as string
        """
        if not command_parts:
            return "Please enter a command. Type 'help' for available commands."

        command = command_parts[0].lower()

        if command == "add":
            if len(command_parts) < 2:
                return "Error: Add command requires a description"
            description = " ".join(command_parts[1:])
            return self.cli_interface.add_todo(description)

        elif command == "list":
            return self.cli_interface.list_todos()

        elif command == "complete":
            if len(command_parts) < 2:
                return "Error: Complete command requires a todo ID"
            return self.cli_interface.complete_todo(command_parts[1])

        elif command == "update":
            if len(command_parts) < 3:
                return "Error: Update command requires ID and new title"
            return self.cli_interface.update_todo(command_parts[1:])

        elif command == "delete":
            if len(command_parts) < 2:
                return "Error: Delete command requires a todo ID"
            return self.cli_interface.delete_todo(command_parts[1])

        elif command == "help":
            return self.cli_interface.show_help()

        elif command in ["quit", "exit"]:
            self.running = False
            return "Goodbye!"

        else:
            return f"Unknown command: {command}. Type 'help' for available commands."

    def run(self):
        """Run the main application loop."""
        print("Welcome to the Console Todo App!")
        print("Type 'help' for available commands or 'quit' to exit.\n")

        # Set up signal handler for graceful shutdown
        signal.signal(signal.SIGINT, self.handle_signal)

        while self.running:
            try:
                user_input = input("> ").strip()

                if not user_input:
                    continue

                command_parts = self.parse_command(user_input)
                result = self.execute_command(command_parts)
                print(result)

            except EOFError:
                # Handle Ctrl+D
                print("\nGoodbye!")
                break
            except KeyboardInterrupt:
                # Handle Ctrl+C (though signal handler should catch this)
                print("\nReceived interrupt signal. Exiting...")
                break


def main():
    """Main entry point."""
    app = TodoApp()
    app.run()


if __name__ == "__main__":
    main()