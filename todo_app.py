#!/usr/bin/env python3
"""
To-Do List Application
A simple console-based task manager with file persistence
"""

import os
import sys

class TodoApp:
    def __init__(self, filename="tasks.txt"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()
    
    def load_tasks(self):
        """Load tasks from file if it exists"""
        try:
            with open(self.filename, 'r') as file:
                self.tasks = [line.strip() for line in file.readlines() if line.strip()]
        except FileNotFoundError:
            # If file doesn't exist, start with empty task list
            self.tasks = []
            print(f"No existing task file found. Starting fresh!")
    
    def save_tasks(self):
        """Save current tasks to file"""
        try:
            with open(self.filename, 'w') as file:
                for task in self.tasks:
                    file.write(task + '\n')
        except Exception as e:
            print(f"Error saving tasks: {e}")
    
    def add_task(self, task):
        """Add a new task to the list"""
        if task.strip():
            self.tasks.append(task.strip())
            self.save_tasks()
            print(f"✓ Task added: '{task.strip()}'")
        else:
            print("❌ Cannot add empty task!")
    
    def view_tasks(self):
        """Display all tasks with numbers"""
        if not self.tasks:
            print("\n📝 Your to-do list is empty! Add some tasks to get started.")
            return
        
        print(f"\n📋 Your To-Do List ({len(self.tasks)} tasks):")
        print("-" * 40)
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")
        print("-" * 40)
    
    def remove_task(self, task_number):
        """Remove a task by its number"""
        try:
            index = int(task_number) - 1
            if 0 <= index < len(self.tasks):
                removed_task = self.tasks.pop(index)
                self.save_tasks()
                print(f"✓ Removed task: '{removed_task}'")
            else:
                print(f"❌ Invalid task number! Please choose between 1 and {len(self.tasks)}")
        except ValueError:
            print("❌ Please enter a valid number!")
    
    def clear_all_tasks(self):
        """Clear all tasks after confirmation"""
        if not self.tasks:
            print("📝 No tasks to clear!")
            return
        
        confirm = input(f"⚠️  Are you sure you want to delete all {len(self.tasks)} tasks? (y/N): ").lower()
        if confirm == 'y' or confirm == 'yes':
            self.tasks.clear()
            self.save_tasks()
            print("✓ All tasks cleared!")
        else:
            print("❌ Operation cancelled.")
    
    def display_menu(self):
        """Display the main menu"""
        print("\n" + "="*50)
        print("🎯 TO-DO LIST MANAGER")
        print("="*50)
        print("1. View all tasks")
        print("2. Add a new task")
        print("3. Remove a task")
        print("4. Clear all tasks")
        print("5. Exit")
        print("-"*50)
    
    def run(self):
        """Main application loop"""
        print("🎉 Welcome to your To-Do List Manager!")
        
        while True:
            self.display_menu()
            choice = input("Choose an option (1-5): ").strip()
            
            if choice == '1':
                self.view_tasks()
            
            elif choice == '2':
                task = input("\n📝 Enter a new task: ")
                self.add_task(task)
            
            elif choice == '3':
                self.view_tasks()
                if self.tasks:  # Only ask for task number if there are tasks
                    task_num = input("\n🗑️  Enter task number to remove: ")
                    self.remove_task(task_num)
            
            elif choice == '4':
                self.clear_all_tasks()
            
            elif choice == '5':
                print("\n👋 Thanks for using To-Do List Manager! Goodbye!")
                sys.exit(0)
            
            else:
                print("❌ Invalid choice! Please select 1-5.")
            
            # Pause before showing menu again
            input("\nPress Enter to continue...")


def main():
    """Entry point of the application"""
    try:
        app = TodoApp()
        app.run()
    except KeyboardInterrupt:
        print("\n\n👋 Thanks for using To-Do List Manager! Goodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()