from frame_entry_clone import entry_clone
from frame_entry_original import entry_original
import shutil
import os
from tkinter import messagebox

def function_copy(path_original, path_clone):

    path_original = entry_original.get()
    path_clone = entry_clone.get()

    if not os.path.exists(path_original):
        messagebox.showerror('Erro','Pasta de origem não existe.')

    if not os.path.exists(path_clone):
        messagebox.showerror('Erro','Pasta de destino não existe.')

    # Se o destino já existir, remove antes de copiar novamente
    if os.path.exists(path_clone):
        shutil.rmtree(path_clone)

    try:
        shutil.copytree(path_original, path_clone)

    except Exception as e:
        messagebox.showerror('Erro', {e})
