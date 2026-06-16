import os
import tkinter as tk
import keyboard as ky
os.system("cls")

def ok():
    campo.delete(0, tk.END)
    campo.pack()
    confirmar.pack()
def criar():
    texto=campo.get()
    if texto!="":
        for i in range(len(os.listdir())):
            arquivo[i].destroy()
        with open(f"{texto}.py", "w"):
            pass
        listar()
    campo.pack_forget()
    confirmar.pack_forget()
    janela.update()
    
def listar():
    arquivo.append("")
    i=0
    for item in os.listdir():
        arquivo[i]=tk.Label(frame_arquivos, text=item, image=imagem, compound="top", wraplength=80, bg="gray")
        arquivo[i].pack(side="left", padx=5)
        i=i+1
        
janela=tk.Tk()
janela.geometry("500x300")
janela.config(bg="gray")
imagem=tk.PhotoImage(file="teste.png")
mais=tk.PhotoImage(file="mais.png")
arquivo=[""]*len(os.listdir())
botao=tk.Button(janela, command=ok, image=mais, bg="gray", bd=0)
botao.pack(pady=20)
frame_arquivos = tk.Frame(janela, bg="gray")
frame_arquivos.pack()
listar()
campo=tk.Entry(janela)
confirmar=tk.Button(janela, text="OK", command=criar, bg="yellow")
janela.mainloop()
