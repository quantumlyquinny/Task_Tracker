#Functions for task tracker: Add, Update, Delete; Mark as done/in progress; List tasks that are done/not done/ in progress
import json

#Add Function
def add_task():
    try:
        with open("tasks.json", "r") as f:
            task = json.load(f)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        task = {}

    if task:
        task_counter = max(int(k) for k in task.keys()) + 1
    else:
        task_counter = 1  # ⬅ Start from 1

    new_task = input("Enter your task: ")
    task[str(task_counter)] = {
        "title": new_task,
        "status": "not done"
    }

    with open("tasks.json", "w") as f:
        json.dump(task, f, indent=4)

def update_task(task_id, new_title):
    try:
        with open("tasks.json", "r") as f:
            tasks = json.load(f)
    except (FileNotFoundError, json.decoder.JSONDecodeError):  # ✅ fix the typo
        print("No tasks found.")
        return

    task_id = str(task_id)
    if task_id not in tasks:
        print(f"Task with ID {task_id} does not exist.")
        return

    tasks[task_id]["title"] = new_title

    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=4)

    print(f"Task {task_id} updated successfully.")

def delete_and_renumber(task_id):
    try:
        with open("tasks.json", "r") as f:
            tasks = json.load(f)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        print("No tasks found.")
        return

    task_id = str(task_id)
    if task_id not in tasks:
        print(f"Task {task_id} does not exist.")
        return

    del tasks[task_id]

    new_tasks = {}
    sorted_items = sorted(tasks.items(), key=lambda x: int(x[0]))
    for index, (old_id, task_data) in enumerate(sorted_items):
        new_id = index + 1  # ⬅ Start numbering from 1
        new_tasks[str(new_id)] = task_data

    with open("tasks.json", "w") as f:
        json.dump(new_tasks, f, indent=4)

    print(f"Task {task_id} deleted and tasks renumbered.")

def mark_task(task_id, new_status):
    try:
        with open("tasks.json", "r") as f:
            tasks = json.load(f)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        print("No tasks found.")
        return
    if str(task_id) not in tasks:
        print(f"task with ID{task_id} does not exist")
        return
    tasks[str(task_id)]["status"]=new_status

    with open("tasks.json","w") as f:
        json.dump(tasks, f, indent=4)
    print(f"task {task_id} marked as {new_status}")
    
def lists(status):
    try:
        with open("tasks.json", "r") as f:
            tasks = json.load(f)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        print("No tasks found.")
        return
    task_counter = 0
    found = False
    for task_id, task in tasks.items():
        if task["status"] == status:
            print(f"{task_counter}. {task['title']} (ID: {task_id})")
            task_counter += 1
            found = True

    if not found:
        print(f"No tasks with status '{status}' found.")

def menu():
    while True:
        print("\n--- Task Tracker Menu ---")
        print("1. Add Task")
        print("2. Update Task Title")
        print("3. Delete Task and Renumber")
        print("4. Mark Task Status")
        print("5. List Tasks by Status")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_task()

        elif choice == "2":
            task_id = input("Enter task ID to update: ")
            new_title = input("Enter new task title: ")
            update_task(task_id, new_title)

        elif choice == "3":
            task_id = input("Enter task ID to delete: ")
            delete_and_renumber(task_id)

        elif choice == "4":
            task_id = input("Enter task ID to mark: ")
            new_status = input("Enter new status (done / in progress / not started): ").strip().lower()
            mark_task(task_id, new_status)

        elif choice == "5":
            status = input("Enter status to filter by (done / in progress / not started): ").strip().lower()
            lists(status)

        elif choice == "6":
            print("Exiting Task Tracker.")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the menu
menu()
