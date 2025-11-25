import tkinter as tk
from tkinter import Frame, Label, Entry, Button, SOLID, filedialog

def function_path(entry):
    path = filedialog.askdirectory(title="Selecione o caminho da pasta")

    if path:
        entry.delete(0,'end')
        entry.insert(0, path)
    
    return path



root = tk.Tk()
root.title('Clona diretório')
# Esse trecho até o geometry() é um algorítmo que faz a janela iniciar bem no centro da tela, independente a resolução do monitor
largura = 400
altura = 400
largura_screen = root.winfo_screenwidth()
altura_screen = root.winfo_screenheight()
posx = largura_screen/2 - largura/2
posy = altura_screen/2 - altura/2
root.geometry('%dx%d+%d+%d' % (largura, altura, posx, posy))



#---------------------------------
frame_entry_original = Frame(root,
                               relief = SOLID,
                               bd = 1)
frame_entry_original.pack(anchor='w', pady=(0,0), padx=(0,0))

label_original = Label(frame_entry_original, text='ORIGINAL', font=('Arial', 9))
label_original.grid(row=0, column=0, pady=(0,0), padx=(0,0), sticky='w')

#global entry_original
entry_original = Entry(frame_entry_original, width=20)
entry_original.grid(row=0, column=1, padx=(0,0), sticky='w')

button_original = Button(frame_entry_original, text='Procurar', width=10, height=1, bg='silver',command=lambda:function_path(entry_original))
button_original.grid(row=0, column=2, padx=(2,0))

#-------------------------------
frame_entry_clone = Frame(root,
                               relief = SOLID,
                               bd = 1)
frame_entry_clone.pack(anchor='w', pady=(0,0), padx=(0,0))

label_clone = Label(frame_entry_clone, text='CLONE', font=('Arial', 9))
label_clone.grid(row=0, column=0, pady=(0,0), padx=(0,0), sticky='w')

#global entry_clone
entry_clone = Entry(frame_entry_clone, width=20)
entry_clone.grid(row=0, column=1, padx=(0,0), sticky='w')

button_clone = Button(frame_entry_clone, text='Procurar', width=10, height=1, bg='silver', command=lambda:function_path(entry_clone))
button_clone.grid(row=0, column=2, padx=(2,0))

root.mainloop()