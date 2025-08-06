import os

TASK_FILE = "tasks.txt"

def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, "r") as file:
        return [line.strip() for line in file.readlines()]

def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def view_tasks(tasks):
    if not tasks:
        print("✅ Your to-do list is empty!")
    else:
        print("\n📋 Your tasks:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

def add_task(tasks):
    new_task = input("✍️ Enter a new task: ").strip()
    if new_task:
        tasks.append(new_task)
        save_tasks(tasks)
        print("✅ Task added!")
    else:
        print("⚠️ Task can't be empty!")

def remove_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("🗑️ Enter the number of the task to remove: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"✅ Removed task: {removed}")
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

def main():
    tasks = load_tasks()
    while True:
        print("\n===== TO-DO MENU =====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        choice = input("➡️ Choose an option: ").strip()
        
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("👋 Goodbye! Don't forget your tasks!")
            break
        else:
            print("⚠️ Invalid choice. Try again!")

if __name__ == "__main__":
    main()