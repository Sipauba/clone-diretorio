from tkinter import filedialog

def function_path(entry):
    path = filedialog.askdirectory(title="Selecione o caminho da pasta")

    if path:
        entry.delete(0,'end')
        entry.insert(0, path)
    
    return path