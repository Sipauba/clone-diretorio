import tkinter as tk
from frame_entry_original import *
from frame_entry_clone import *
from button_executar import *

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

frame_entry_original(root)

frame_entry_clone(root)

button_executar(root)

root.mainloop()