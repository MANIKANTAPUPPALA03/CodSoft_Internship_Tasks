import tkinter as tk
from tkinter import messagebox

def add():
    task=task_entry.get()
    if task:
        task_listbox.insert(tk.END,task)
        task_entry.delete(0,tk.END)
    else:
        messagebox.showwarning("Warning","Task cannot be empty")

def remove():
    try:
        selected=task_listbox.curselection()[0]
        task_listbox.delete(selected)
    except IndexError:
        messagebox.showwarning("Warning","Select a task to remove")

def clear():
    task_listbox.delete(0,tk.END)

root=tk.Tk()
root.title("To do List")

task_entry=tk.Entry(root,width=40)
task_entry.pack(pady=10)

add_b=tk.Button(root,text="Add",command=add)
add_b.pack(pady=5)

remove_b=tk.Button(root,text="Remove",command=remove)
remove_b.pack(pady=5)

clear_b=tk.Button(root,text="Clear",command=clear)
clear_b.pack(pady=5)

task_listbox=tk.Listbox(root,width=50,height=10)
task_listbox.pack(pady=10)
root.mainloop()