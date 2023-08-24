#@author Sobomate-Victor Asimiea

import tkinter as tk
from tkinter import *
from tkinter import scrolledtext
from tkinter.ttk import *

def addTask():
    newTask = newTaskEntry.get()
    if newTask:
        todo_list.append({"task": newTask, "status": "pending"})
        newTaskEntry.delete(0, tk.END)
        printList()
        
def printList():
    list_display.delete(1.0, tk.END)
    for idx, entry in enumerate(todo_list, start=1):
        list_display.insert(tk.END, f"{idx}. [{entry['status']}] {entry['task']}\n")
        
def markCompleted():
    entry_number = int(entry_index.get())

    if 1 <= entry_number <= len(todo_list):
        todo_list[entry_number-1]["status"] = "completed"
        printList()
        
def clear():
    global todo_list
    todo_list =  []
    list_display.delete(1.0, tk.END)

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Initialize the list
todo_list = []

# Create widgets
title_label = tk.Label(root, text="To-Do List", font=("Times New Roman", 20, "bold"))
list_display = scrolledtext.ScrolledText(root, height=10, width=40, wrap=tk.WORD)
new_item_label = tk.Label(root, text="Enter new item:", font=("TimesNewRoman", 10))
newTaskEntry = tk.Entry(root)
add_button = tk.Button(root, text="Add Item", command=addTask)
mark_label = tk.Label(root, text="Enter index to mark as completed:", font=("TimesNewRoman", 10))
entry_index = tk.Entry(root)
mark_button = tk.Button(root, text="Mark Completed", command=markCompleted)
clear_button = tk.Button(root, text="Clear List", command=clear)

# Place widgets using grid layout
title_label.grid(row=0, columnspan=2, pady=10)
list_display.grid(row=1, columnspan=2, padx=10, pady=10)
new_item_label.grid(row=3, column=0, padx=10)
newTaskEntry.grid(row=3, column=1, padx=10)
add_button.grid(row=4, column=2)
mark_label.grid(row=6, column=0, padx=10)
entry_index.grid(row=6, column=1, padx=10)
mark_button.grid(row=7, column=1)
clear_button.grid(row=7, column=2)

# Start the main loop
root.mainloop()
