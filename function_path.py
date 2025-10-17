from tkinter import filedialog

def function_path(entry):
    path_original = filedialog.askopenfilename(title="Selecione o caminho da pasta")

    if path_original:
        entry.delete(0,'end')
        entry.insert(0, path_original)
    
    return path_original