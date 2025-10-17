from tkinter import Button

def button_executar(root):
    button_executar = Button(root, text='EXECUTAR', width=15, height=1, bg='silver')
    button_executar.place(x=150, y=150)
    return button_executar
