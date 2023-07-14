import tkinter as tk
from tkinter import messagebox


def add_task():
    task = entry_task.get()
    description = entry_description.get("1.0", tk.END).strip()
    if task:
        listbox.insert(tk.END, task)
        task_descriptions[task] = description
        entry_task.delete(0, tk.END)
        entry_description.delete("1.0", tk.END)
        save_tasks_to_file()
    else:
        messagebox.showwarning("Warning", "Please enter a task.")


def delete_task():
    try:
        index = listbox.curselection()
        task = listbox.get(index)
        del task_descriptions[task]
        listbox.delete(index)
        save_tasks_to_file()
    except:
        messagebox.showwarning("Warning", "Please select a task to delete.")


def view_description(event):
    try:
        index = listbox.curselection()
        task = listbox.get(index)
        description = task_descriptions.get(task, "")
        messagebox.showinfo("Task Description", description)
    except:
        messagebox.showwarning(
            "Warning", "Please select a task to view the description."
        )


def save_tasks_to_file():
    with open("tasks.txt", "w") as file:
        for task, description in task_descriptions.items():
            file.write(f"{task}:{description}\n")


def load_tasks_from_file():
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    task, description = line.split(":", 1)
                    listbox.insert(tk.END, task)
                    task_descriptions[task] = description
    except FileNotFoundError:
        pass


# Create the main window
root = tk.Tk()
root.title("Todo List")

# Create a listbox to display tasks
listbox = tk.Listbox(root, width=50)
listbox.pack(pady=10)

# Create a scrollbar
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Associate the listbox with the scrollbar
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# Create a label for the task entry field
label_task = tk.Label(root, text="Task:")
label_task.pack()

# Create an entry field for adding tasks
entry_task = tk.Entry(root, width=50)
entry_task.pack(pady=5)

# Create a label for the description entry field
label_description = tk.Label(root, text="Description:")
label_description.pack()

# Create a text area for task descriptions
entry_description = tk.Text(root, width=50, height=4)
entry_description.pack(pady=5)

# Create Add Task button
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

# Create Delete Task button
delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

# Dictionary to store task descriptions
task_descriptions = {}

# Load tasks from file
load_tasks_from_file()

# Bind the view_description function to a Double-click event on the listbox
listbox.bind("<Double-Button-1>", view_description)

# Start the main event loop
root.mainloop()
