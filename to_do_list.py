
task_list = []


def show_menu():
    menu = """
            1. Add a task
            2. View all tasks
            3. Mark a task as complete
            4. Delete a task
            5. Exit
    """
    return menu


def add_task():
    new_task = input("Add a task: ")
    task_list.append({'TASK': new_task, 'STATUS': '[ ]'})
    return f"'{new_task}' added to the list."


def view_tasks():
    if not task_list:
        return "No tasks found. Your list is empty!"
    
    print("\nVIEW TASKS:")
    for i, task in enumerate(task_list):
        print(f"{i + 1}. {task['STATUS']} {task['TASK']}")
    return ""


def mark_task_as_completed():
    view_tasks()
    if not task_list:
        return "No tasks to mark as complete."
    
    try:
        task_number = int(input("Enter the task number to mark as complete: ")) - 1
        if 0 <= task_number < len(task_list):
            task_list[task_number]['STATUS'] = '[X]'
            return f"Task '{task_list[task_number]['TASK']}' marked as complete."
        else:
            return "Invalid task number."
    except ValueError:
        return "Please enter a valid number."


def delete_task():
    view_tasks()
    if not task_list:
        return "No tasks to delete."
    
    try:
        task_number = int(input("Enter the task number to delete: ")) - 1
        if 0 <= task_number < len(task_list):
            deleted_task = task_list.pop(task_number)
            return f"Task '{deleted_task['TASK']}' deleted."
        else:
            return "Invalid task number."
    except ValueError:
        return "Please enter a valid number."


def handle_user_choice(choice):
    if choice == '1':
        print(add_task())
    elif choice == '2':
        print(view_tasks())
    elif choice == '3':
        print(mark_task_as_completed())
    elif choice == '4':
        print(delete_task())
    elif choice == '5':
        print("Exiting the program. Goodbye!")
        exit()
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")


def main():
    while True:
        print(show_menu())
        choice = input("Enter your choice (1-5): ")
        handle_user_choice(choice)

if __name__ == "__main__":
    main()