import mysql.connector
from mysql.connector import Error
import tkinter as tk
from tkinter import messagebox

def create_connection():
    """ Create a database connection to the MySQL database """
    return mysql.connector.connect(
        host="localhost",
        user="root",   # Replace with your MySQL username
        password="Mahoga@1234",  # Replace with your MySQL password
        database="todo_db"
    )

def add_task():
    """ Add a new task to the tasks table """
    task = task_entry.get()
    status = status_entry.get()
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO tasks (task, status) VALUES (%s, %s)", (task, status))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Task added successfully")
    view_tasks()

def view_tasks():
    """ Fetch all tasks from the tasks table and display in the listbox """
    task_listbox.delete(0, tk.END)
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")
    rows = cur.fetchall()
    conn.close()
    for row in rows:
        task_listbox.insert(tk.END, f"{row[0]} - {row[1]} - {row[2]}")

def delete_task():
    """ Delete the selected task from the tasks table """
    selection = task_listbox.curselection()
    if not selection:
        messagebox.showerror("Error", "No task selected")
        return
    task_id = task_listbox.get(selection)[0]
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM tasks WHERE id=%s", (task_id,))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Task deleted successfully")
    view_tasks()

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Task entry
task_label = tk.Label(root, text="Task:")
task_label.pack()
task_entry = tk.Entry(root)
task_entry.pack()

# Status entry
status_label = tk.Label(root, text="Status:")
status_label.pack()
status_entry = tk.Entry(root)
status_entry.pack()

# Add task button
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

# Task list
task_listbox = tk.Listbox(root, width=50)
task_listbox.pack()

# Delete task button
delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack()

# View tasks initially
view_tasks()

# Run the application
root.mainloop()
