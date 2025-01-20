import os

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    """Displays the menu options."""
    print("\nTo-Do List Application")
    print("-----------------------")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task as Complete")
    print("6. Exit")

def view_tasks(tasks):
    """Displays all tasks."""
    if not tasks:
        print("\nNo tasks to display.")
    else:
        print("\nTasks:")
        for index, task in enumerate(tasks, 1):
            status = "[Done]" if task['completed'] else "[Pending]"
            print(f"{index}. {task['description']} {status}")

def add_task(tasks):
    """Adds a new task."""
    description = input("\nEnter task description: ")
    tasks.append({"description": description, "completed": False})
    print("Task added successfully!")

def update_task(tasks):
    """Updates an existing task."""
    view_tasks(tasks)
    try:
        task_number = int(input("\nEnter the task number to update: "))
        if 1 <= task_number <= len(tasks):
            new_description = input("Enter the new description: ")
            tasks[task_number - 1]['description'] = new_description
            print("Task updated successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def delete_task(tasks):
    """Deletes a task."""
    view_tasks(tasks)
    try:
        task_number = int(input("\nEnter the task number to delete: "))
        if 1 <= task_number <= len(tasks):
            tasks.pop(task_number - 1)
            print("Task deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def mark_task_as_complete(tasks):
    """Marks a task as complete."""
    view_tasks(tasks)
    try:
        task_number = int(input("\nEnter the task number to mark as complete: "))
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]['completed'] = True
            print("Task marked as complete!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    """Main function to run the To-Do List application."""
    tasks = []

    while True:
        clear_screen()
        display_menu()

        try:
            choice = int(input("\nEnter your choice: "))
            if choice == 1:
                clear_screen()
                view_tasks(tasks)
            elif choice == 2:
                clear_screen()
                add_task(tasks)
            elif choice == 3:
                clear_screen()
                update_task(tasks)
            elif choice == 4:
                clear_screen()
                delete_task(tasks)
            elif choice == 5:
                clear_screen()
                mark_task_as_complete(tasks)
            elif choice == 6:
                print("\nThank you for using the To-Do List application. Goodbye!")
                break
            else:
                print("\nInvalid choice. Please select a valid option.")
        except ValueError:
            print("\nInvalid input. Please enter a number.")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
