def add(tasks):
    task = input("Enter task to add: ")
    tasks.append(task)
    print("Task Added!")

def rem(tasks):
    task = input("Enter task to remove: ")
    if task in tasks:
        tasks.remove(task)
        print("Task Removed!")
    else:
        print("Task not found.")

def view(tasks):
    if len(tasks) == 0:
        print("No tasks available.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

tasks = []

while True:
    print("\n-----------")
    print("To-Do List")
    print("-----------")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Exit")
    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        add(tasks)
    elif choice == 2:
        rem(tasks)
    elif choice == 3:
        view(tasks)
    elif choice == 4:
        break
    else:
        print("Invalid choice! Please select a valid option (1-4).")
