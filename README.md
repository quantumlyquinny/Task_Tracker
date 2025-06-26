# Task_Tracker

A lightweight command-line Task Tracker app built in Python.  
Helps you manage your tasks — add, update, delete, and track their status — using a simple JSON file.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![CLI](https://img.shields.io/badge/Interface-CLI-informational)
![Status](https://img.shields.io/badge/Status-Active-green)

---

## 🚀 Features

- ✅ Add new tasks
- ✏️ Update task titles
- 🗑️ Delete tasks and automatically renumber remaining ones
- 🔄 Mark tasks as `done`, `in progress`, or `not started`
- 📋 List tasks filtered by status
- 💾 Persist tasks in a local `tasks.json` file (auto-created)

---

## 📁 Project Structure

![image](https://github.com/user-attachments/assets/83f7bcf0-8ace-44c0-8ddb-7b43a51d1c26)


---

## 🧑‍💻 Getting Started

### ✅ Requirements
- Python 3.x installed
- No external libraries needed

### ▶️ Run the Application

1. Clone the repository:
```bash
git clone https://github.com/yourusername/task-tracker-cli.git
cd task-tracker-cli

### ✅ Requirements

--- Task Tracker Menu ---
1. Add Task
2. Update Task Title
3. Delete Task and Renumber
4. Mark Task Status
5. List Tasks by Status
6. Exit

## How Data is Stored

Tasks are stored in a local tasks.json file as a dictionary:

json
Copy
Edit
{
  "1": {"title": "Complete assignment", "status": "done"},
  "2": {"title": "Go for a walk", "status": "not started"}



