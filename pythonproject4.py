import tkinter as tk
from tkinter import ttk, messagebox

# Task list
tasks = []

# Add task
def add_task():
    task_name = task_entry.get().strip()
    priority = priority_combobox.get()

    if not task_name:
        messagebox.showwarning("Warning", "Task name cannot be empty.")
        return

    tasks.append({"name": task_name, "priority": priority, "status": "Pending"})
    update_ui()
    task_entry.delete(0, tk.END)
    priority_combobox.set("Low")
    messagebox.showinfo("Success", "Task added successfully!")

# Mark task as completed
def mark_completed():
    selected_item = task_table.focus()
    if not selected_item:
        messagebox.showwarning("Warning", "Please select a task to mark as completed.")
        return

    task_index = task_table.index(selected_item)
    tasks[task_index]["status"] = "Completed"
    update_ui()
    messagebox.showinfo("Success", "Task marked as completed!")

# Delete task
def delete_task():
    selected_item = task_table.focus()
    if not selected_item:
        messagebox.showwarning("Warning", "Please select a task to delete.")
        return

    task_index = task_table.index(selected_item)
    tasks.pop(task_index)
    update_ui()
    messagebox.showinfo("Success", "Task deleted successfully!")

# Update UI
def update_ui():
    for row in task_table.get_children():
        task_table.delete(row)

    for task in tasks:
        task_table.insert('', tk.END, values=(task["name"], task["priority"], task["status"]))

# GUI Setup
root = tk.Tk()
root.title("Task Manager")
root.geometry("600x400")

# Header
header = tk.Label(root, text="📝 Task Manager", font=("Helvetica", 20, "bold"))
header.pack(pady=10)

# Entry Frame
entry_frame = tk.Frame(root)
entry_frame.pack(pady=10)

tk.Label(entry_frame, text="Task Name:").grid(row=0, column=0, padx=5)
task_entry = tk.Entry(entry_frame, width=30)
task_entry.grid(row=0, column=1, padx=5)

tk.Label(entry_frame, text="Priority:").grid(row=0, column=2, padx=5)
priority_combobox = ttk.Combobox(entry_frame, values=["Low", "Medium", "High"], width=10)
priority_combobox.set("Low")
priority_combobox.grid(row=0, column=3, padx=5)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="Add Task", command=add_task)
add_button.grid(row=0, column=0, padx=10)

complete_button = tk.Button(button_frame, text="Mark Completed", command=mark_completed)
complete_button.grid(row=0, column=1, padx=10)

delete_button = tk.Button(button_frame, text="Delete Task", command=delete_task)
delete_button.grid(row=0, column=2, padx=10)

# Task Table
task_table = ttk.Treeview(root, columns=("Name", "Priority", "Status"), show="headings", height=10)
task_table.heading("Name", text="Task Name")
task_table.heading("Priority", text="Priority")
task_table.heading("Status", text="Status")
task_table.pack(pady=10)

# Run the application
root.mainloop()
