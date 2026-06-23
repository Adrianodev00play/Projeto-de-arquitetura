import os
import tkinter as tk
import sys
import os

def caminho(relativo):
    base = getattr(sys, "_MEIPASS", os.path.abspath("."))
    return os.path.join(base, relativo)
os.system("cls")

#função que confirma a criação de um novo arquivo
def ok(a):
    global pasta
    global campo
    global confirmar
    if a==1:
        pasta=1
    criar_arquivo.pack_forget()
    criar_pasta.pack_forget()
    campo=tk.Entry(asd)
    campo.pack(pady=10)
    confirmar=tk.Button(asd, text="OK", command=criar, bg="blue", fg="white")
    confirmar.pack()
    campo.delete(0, tk.END)

#função que escolhe o tipo de arquivo
def file():
    global criar_pasta
    global criar_arquivo
    global asd
    asd=tk.Toplevel()
    asd.config(bg="gray")
    x=(asd.winfo_screenwidth()//2)-(200//2)
    y=(asd.winfo_screenheight()//2)-(100//2)
    asd.geometry(f"{200}x{100}+{x}+{y}")
    criar_pasta=tk.Button(asd, text="Pasta", command=lambda:ok(1))
    criar_pasta=criar_pasta
    criar_pasta.pack(pady=10)
    criar_arquivo=tk.Button(asd, text="Arquivo", command=lambda:ok(2))
    criar_arquivo.pack()
    asd.mainloop()

def criar():
    global pasta
    texto=campo.get()
    if texto!="":
        for i in range(len(os.listdir())):
            arquivo[i].destroy()
        if pasta==1:
            os.mkdir(texto)
        else:
            with open(f"{texto}.py", "w"):
                pass
        listar()
    campo.pack_forget()
    confirmar.pack_forget()
    asd.destroy()
    pasta=0

#função que lista todos os arquivos presentes na pasta
def listar():
    arquivo.append("")

    i = 0
    linha = 0
    coluna = 0

    for item in os.listdir():

        caixa = tk.Frame(
            frame_arquivos,
            width=120,
            height=140,
            bg="#2e2d2d"
        )
        caixa.grid(row=linha, column=coluna, padx=10, pady=10)
        caixa.grid_propagate(False)

        arquivo[i] = tk.Label(
            caixa,
            text=item,
            compound="top",
            wraplength=100,
            bg="#2e2d2d",
            fg="white",
            font=("Segoe UI Variable Small Semibol", 10)
        )

        if item.endswith(".py"):
            arquivo[i].config(image=imagem)
        else:
            arquivo[i].config(image=diretorio)

        arquivo[i].pack(expand=True)

        coluna += 1

        if coluna == 6:
            coluna = 0
            linha += 1

        
        i += 1
#cria a janela principal
janela=tk.Tk()
janela.geometry("500x300")
janela.config(bg="#2e2d2d")

#variáveis usada para armazenar a foto do fundo dos arquivos
imagem = tk.PhotoImage(file=caminho("arquivos_do_sistema/teste.png"))
mais = tk.PhotoImage(file=caminho("arquivos_do_sistema/mais.png"))
diretorio = tk.PhotoImage(file=caminho("arquivos_do_sistema/pasta.png"))

#vetor que armazena o nome de todos os arquivos da pasta
arquivo=[""]*len(os.listdir())

#botão que abre a criação de um novo arquivo
botao=tk.Button(janela, command=file, image=mais, bg="#2e2d2d", bd=0)
botao.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)

#método usado para organizar os arquivos em linhas 
frame_arquivos = tk.Frame(janela, bg="#2e2d2d")
frame_arquivos.pack()

#chama a função que lista todos os arquivos presentes na pasta
listar()

asd=None

#campo para digitar o nome do arquivo
campo=None
confirmar=None

#variável para definir a criação de pastas ou arquivos
criar_arquivo=None
criar_pasta=None

#variáveis gloais para armazenas os valores d acriação de pasta ou arquivos
pasta=0
arquivo_py=0

janela.mainloop()
