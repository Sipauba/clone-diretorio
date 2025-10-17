from tkinter import Entry, Frame, Label, Button, SOLID
from function_path import *

def frame_entry_original (root):
    frame_entry_original = Frame(root,
                               relief = SOLID,
                               bd = 1)
    frame_entry_original.pack(anchor='w', pady=(0,0), padx=(0,0))

    label_original = Label(frame_entry_original, text='ORIGINAL', font=('Arial', 9))
    label_original.grid(row=0, column=0, pady=(0,0), padx=(0,0), sticky='w')

    global entry_original
    entry_original = Entry(frame_entry_original, width=20)
    entry_original.grid(row=0, column=1, padx=(0,0), sticky='w')

    button_original = Button(frame_entry_original, text='Procurar', width=10, height=1, bg='silver',command=lambda:function_path(entry_original))
    button_original.grid(row=0, column=2, padx=(2,0))

    return entry_original

