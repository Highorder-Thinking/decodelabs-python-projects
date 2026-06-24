# ============================================
# DecodeLabs - Project 1: To-Do List
# ============================================

my_tasks = []  # The in-memory database (volatile container)
task_id_counter = 1  # Auto-incrementing primary key (like SQL)


def add_task(task_name):
    """Add a new task to the list (INSERT INTO)"""
    global task_id_counter
    task = {
        "id": task_id_counter,   # Dictionary 'id' -> Primary Key
        "task": task_name         # Dictionary 'task' -> Column Value
    }
    my_tasks.append(task)         # list.append(row) -> INSERT INTO
    task_id_counter += 1
    print(f"  ✅ Task added: '{task_name}'")


def view_tasks():
    """Display all tasks (SELECT * FROM)"""
    if not my_tasks:
        print("  📭 No tasks yet. Add some tasks first!")
        return
    print("\n  📋 Your To-Do List:")
    print("  " + "-" * 30)
    for index, task in enumerate(my_tasks, start=1):   # enumerate() - professional way
        print(f"  {index}. {task['task']}")
    print("  " + "-" * 30)


def main():
    """Main engine — follows the IPO model (Input → Process → Output)"""
    print("=" * 40)
    print("  DecodeLabs To-Do List App")
    print("=" * 40)

    while True:
        print("\n  Menu:")
        print("  1. Add Task")
        print("  2. Remove Task")
        print("  3. View Tasks")
        print("  4. Exit")

        choice = input("\n  Enter your choice (1/2/3/4): ").strip()

        if choice == "1":
            task_name = input("  Enter task: ").strip()
            if task_name:
                add_task(task_name)
            else:
                print("  ⚠️  Task cannot be empty.")
                print("  Please enter a valid task name.")
        elif choice == "2":
            if not my_tasks:
                print("  📭 No tasks to remove. Add some tasks first!")
                continue
            view_tasks()
            try:
                task_number = int(input("  Enter task number to remove: ").strip())
                if 1 <= task_number <= len(my_tasks):
                    removed_task = my_tasks.pop(task_number - 1)
                    print(f"  🗑️ Task removed: '{removed_task['task']}'")
                else:
                    print("  ❌ Invalid task number.")
            except ValueError:
                print("  ❌ Please enter a valid number.")        

        elif choice == "3":
            view_tasks()

        elif choice == "4":
            print("\n  Thank you for using the To-Do List App!")
            print("  Remember to stay productive and organized.")
            print("  👋 Goodbye! Keep Doing.\n")
            break

        else:
            print("  ❌ Invalid choice. Enter 1, 2, 3 or 4.")



if __name__ == "__main__":   # Gatekeeper — professional Python entry point
    main()