import os
import tkinter as tk
os.system("cls")

def criar():
    campo=tk.Entry(janela)
    campo.pack( )
    texto=campo.get()
    if texto!="":
        for i in range(len(os.listdir())):
            arquivo[i].destroy()
        with open(f"{texto}.py", "w"):
            pass
        listar()
    
def listar():
    arquivo.append("")
    i=0
    for item in os.listdir():
        arquivo[i]=tk.Label(janela, text=item)
        arquivo[i].pack(pady=1)
        i=i+1
        
janela=tk.Tk()
janela.geometry("500x300")
janela.config(bg="gray")
arquivo=[""]*len(os.listdir())
botao=tk.Button(janela, text="criar arquivos", command=criar, bg="yellow")
botao.pack(pady=10)
listar()
janela.mainloop()