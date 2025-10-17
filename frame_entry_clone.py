from tkinter import Entry, Frame, Label, Button, SOLID
from function_path import *

def frame_entry_clone (root):
    frame_entry_clone = Frame(root,
                               relief = SOLID,
                               bd = 1)
    frame_entry_clone.pack(anchor='w', pady=(0,0), padx=(0,0))

    label_clone = Label(frame_entry_clone, text='CLONE', font=('Arial', 9))
    label_clone.grid(row=0, column=0, pady=(0,0), padx=(0,0), sticky='w')

    global entry_clone
    entry_clone = Entry(frame_entry_clone, width=20)
    entry_clone.grid(row=0, column=1, padx=(0,0), sticky='w')

    button_clone = Button(frame_entry_clone, text='Procurar', width=10, height=1, bg='silver', command=lambda:function_path(entry_clone))
    button_clone.grid(row=0, column=2, padx=(2,0))

    return entry_clone

