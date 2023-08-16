#from tkinter import *
#import tkinter.messagebox
import tkinter as tk

window = tk.Tk()
window.title("TO-DO LIST APP")
greet = tk.Label(text="This is my new To-Do list GUI")
greet.pack()
greeting = tk.Text()#text="This is my new To-Do list GUI")
greeting.pack()
window.mainloop()