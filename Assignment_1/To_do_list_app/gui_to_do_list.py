import tkinter as tk
from tkinter import simpledialog, messagebox
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

class TodoApp:
    def __init__(self, root):
        self.tasks = load_tasks()
        self.root = root
        self.root.title("To-Do List")
        
        self.listbox = tk.Listbox(root, selectmode=tk.SINGLE)
        self.listbox.pack(fill=tk.BOTH, expand=1)
        
        self.update_listbox()
        
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(fill=tk.X)
        
        self.update_button = tk.Button(root, text="Update Task", command=self.update_task)
        self.update_button.pack(fill=tk.X)
        
        self.complete_button = tk.Button(root, text="Complete Task", command=self.complete_task)
        self.complete_button.pack(fill=tk.X)
        
        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(fill=tk.X)
        
        self.save_button = tk.Button(root, text="Save Tasks", command=self.save_tasks)
        self.save_button.pack(fill=tk.X)
    
    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            status = '✓' if task['completed'] else '✗'
            self.listbox.insert(tk.END, f"{status} {task['description']}")
    
    def add_task(self):
        description = simpledialog.askstring("Add Task", "Enter task description:")
        if description:
            add_task(self.tasks, description)
            self.update_listbox()
    
    def update_task(self):
        index = self.listbox.curselection()
        if index:
            description = simpledialog.askstring("Update Task", "Enter new description:")
            if description:
                update_task(self.tasks, index[0], description)
                self.update_listbox()
    
    def complete_task(self):
        index = self.listbox.curselection()
        if index:
            complete_task(self.tasks, index[0])
            self.update_listbox()
    
    def delete_task(self):
        index = self.listbox.curselection()
        if index:
            delete_task(self.tasks, index[0])
            self.update_listbox()
    
    def save_tasks(self):
        save_tasks(self.tasks)
        messagebox.showinfo("Save Tasks", "Tasks saved successfully")

def main():
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
