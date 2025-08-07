# 📝 To-Do List Application

A simple console-based task manager built with Python that provides persistent task storage using file handling.

## ✨ Features

- **Add Tasks**: Create new tasks and add them to your to-do list
- **View Tasks**: Display all tasks with numbered indexing
- **Remove Tasks**: Delete specific tasks by their number
- **Clear All**: Remove all tasks at once (with confirmation)
- **Persistent Storage**: Tasks are automatically saved to and loaded from `tasks.txt`
- **User-Friendly Interface**: Clean console interface with emojis and clear prompts
- **Error Handling**: Robust error handling for file operations and user input

## 🚀 How to Run

1. **Prerequisites**: Python 3.x installed on your system

2. **Clone/Download**: Get the `todo.py` file

3. **Run the application**:
   ```bash
   python todo.py
   ```
   or
   ```bash
   python3 todo.py
   ```

## 🎮 Usage

When you run the application, you'll see a menu with 5 options:

1. **View all tasks** - Shows your current to-do list
2. **Add a new task** - Prompts you to enter a new task
3. **Remove a task** - Lets you delete a task by its number
4. **Clear all tasks** - Removes all tasks (asks for confirmation)
5. **Exit** - Closes the application

## 📁 File Structure

```
project-folder/
├── todo.py          # Main application file
├── tasks.txt        # Auto-generated file for storing tasks
└── README.md        # This file
```

## 🔧 Technical Implementation

### Key Concepts Used:

- **File Handling**: Uses `open()` with context managers (`with` statement)
- **Lists**: Tasks stored in Python list with methods like `append()`, `pop()`
- **String Manipulation**: Uses `.strip()` to clean user input
- **Error Handling**: Try-catch blocks for file operations
- **Object-Oriented Programming**: Organized code using classes

### File Operations:

- **Reading**: Loads existing tasks from `tasks.txt` on startup
- **Writing**: Saves tasks to file after each add/remove operation
- **File Modes**: Uses 'r' for reading and 'w' for writing
- **Error Handling**: Gracefully handles missing files and I/O errors

## 💡 Example Usage

```
🎯 TO-DO LIST MANAGER
==================================================
1. View all tasks
2. Add a new task
3. Remove a task
4. Clear all tasks
5. Exit
--------------------------------------------------
Choose an option (1-5): 2

📝 Enter a new task: Buy groceries
✓ Task added: 'Buy groceries'

Press Enter to continue...
```

## 🛠️ Code Highlights

- **Persistent Storage**: Tasks automatically save to `tasks.txt`
- **Input Validation**: Prevents empty tasks and invalid menu choices
- **User Experience**: Clear feedback messages and formatted output
- **Modular Design**: Well-organized class structure for easy maintenance

## 🚨 Error Handling

The application handles:
- Missing task file (creates new one)
- Invalid task numbers
- Empty task input
- File I/O errors
- Keyboard interrupts (Ctrl+C)

## 📋 Requirements

- Python 3.x
- No external dependencies required
- Works on Windows, macOS, and Linux

---

**Author**: Python Developer Intern  
**Task**: Console-based To-Do List Application  
**Technologies**: Python, File I/O, Lists, String Manipulation