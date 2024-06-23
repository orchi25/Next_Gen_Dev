import json
import os

todo = 'tasks.json'

def load_tasks():
    if os.path.exists(todo):
        with open(todo, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(todo, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks, description):
    tasks.append({
        'description': description,
        'completed': False
    })

def update_task(tasks, index, description):
    if 0 <= index < len(tasks):
        tasks[index]['description'] = description

def complete_task(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index]['completed'] = True

def delete_task(tasks, index):
    if 0 <= index < len(tasks):
        tasks.pop(index)

def list_tasks(tasks):
    for i, task in enumerate(tasks):
        status = '✓' if task['completed'] else '✗'
        print(f"{i + 1}. {status} {task['description']}")

def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List:")
        list_tasks(tasks)
        print("\nOptions:")
        print("1. Add task")
        print("2. Update task")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            description = input("Enter task description: ")
            add_task(tasks, description)
        elif choice == '2':
            index = int(input("Enter task number to update: ")) - 1
            description = input("Enter new description: ")
            update_task(tasks, index, description)
        elif choice == '3':
            index = int(input("Enter task number to complete: ")) - 1
            complete_task(tasks, index)
        elif choice == '4':
            index = int(input("Enter task number to delete: ")) - 1
            delete_task(tasks, index)
        elif choice == '5':
            break
        else:
            print("Invalid option. Please try again.")
        
        save_tasks(tasks)

if __name__ == "__main__":
    main()
