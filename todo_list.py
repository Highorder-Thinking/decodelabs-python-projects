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
        print("  2. View Tasks")
        print("  3. Exit")

        choice = input("\n  Enter your choice (1/2/3): ").strip()

        if choice == "1":
            task_name = input("  Enter task: ").strip()
            if task_name:
                add_task(task_name)
            else:
                print("  ⚠️  Task cannot be empty.")

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            print("\n  ⚠️  RAM is volatile — tasks will be lost on exit.")
            print("  👋 Goodbye! Keep building.\n")
            break

        else:
            print("  ❌ Invalid choice. Enter 1, 2, or 3.")


if __name__ == "__main__":   # Gatekeeper — professional Python entry point
    main()
