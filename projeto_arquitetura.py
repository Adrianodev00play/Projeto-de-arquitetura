import os
import tkinter as tk
import sys
import shutil

def voltar_pasta():
    global pasta_atual
    limpar_arquivos_da_tela()
    pasta_atual = os.path.dirname(pasta_atual)
    listar()

def botao_voltar():
    rf=tk.Button(janela, text="voltar", command=lambda: (voltar_pasta(), rf.destroy()))
    rf.place(x=10, y=10)
def mudar_pasta(event, item):
    global pasta_atual
    li=0
    if item.endswith(".py"):
        li=li
    else:
        limpar_arquivos_da_tela()
        pasta_atual=os.path.join(pasta_atual, item)
        listar()
        print(pasta_atual)
        if pasta_atual!=".":
            botao_voltar()
def exibir_arquivos(i):
    limpar_arquivos_da_tela()
    arquivo[i].pack(expand=True)
    
def encontar_arquivo_busca(nome):
    limpar_arquivos_da_tela()
    arquivo.append("")
    i = 0
    linha = 0
    coluna = 0
    for item in os.listdir(pasta_atual):
        if item!="projeto_arquitetura.py" and item!="arquivos_do_sistema":
            criar_arquivos_e_adicionar_ao_vetor(linha, coluna, i, item)
            verificar_arquivo_e_adiciona_imagem(item, i)
            if arquivo[i]["text"]==f"{nome}.py":
                arquivo[i].pack(expand=True)

            if arquivo[i]["text"]==nome:
                arquivo[i].pack(expand=True)
            coluna += 1
            if coluna == 6:
                coluna = 0
                linha += 1
            i += 1
    
def campo_pesquisa():
    global search
    global cancelar
    global buscar
    search=tk.Entry(janela)
    pesquisa.pack_forget()
    search.pack(before=frame_arquivos)
    cancelar=tk.Button(janela, text="cancelar", command=lambda:(search.pack_forget(), cancelar.pack_forget(), pesquisa.pack(before=frame_arquivos), buscar.pack_forget(), limpar_arquivos_da_tela(), listar()))
    cancelar.pack(before=frame_arquivos)
    buscar=tk.Button(janela, text="Ok", command=lambda:encontar_arquivo_busca(search.get()))
    buscar.pack(before=frame_arquivos)

def fechar_todas_janelas():
    janela.destroy()
    edit.destroy()
    nova_janela.destroy()

def renomear_update_arquivo(antigo):
    texto=campo.get()
    if antigo.endswith(".py"):
        os.rename(os.path.join(pasta_atual, antigo), os.path.join(pasta_atual, f"{texto}.py"))
        logs.append(f"renomeou um arquivo chamado [{antigo}] para [{texto}.py]")
    else:
        os.rename(os.path.join(pasta_atual, antigo), os.path.join(pasta_atual, texto))
        logs.append(f"renomeou uma pasta chamada [{antigo}] para [{texto}]")
    limpar_arquivos_da_tela()
    listar()
    edit.destroy()
    search.pack_forget()
    cancelar.pack_forget()
    buscar.pack_forget()
    pesquisa.pack(before=frame_arquivos)
    campo.pack_forget()
    confirmar.pack_forget()
def valor_pasta_0():
    global pasta
    pasta=0
    nova_janela.destroy()
def janela_edicao(evento, nome):
    global edit
    edit=tk.Tk()
    x=(edit.winfo_screenwidth()//2)-(200//2)
    y=(edit.winfo_screenheight()//2)-(100//2)
    edit.geometry(f"{200}x{100}+{x}+{y}")
    apagar=tk.Button(edit, text="apagar", command=lambda:apagar_arquivos(1, nome))
    apagar.pack()
    renomear=tk.Button(edit, text="renomear", command=lambda:(criar_campo_digitavel(edit, renomear_update_arquivo, nome), renomear.pack_forget(), apagar.pack_forget()))
    renomear.pack()
    edit.mainloop()

def criar_campo_digitavel(tipo, funcao, nome):
    global campo
    global confirmar
    
    campo=tk.Entry(tipo)
    campo.pack(pady=10)
    confirmar=tk.Button(tipo, text="OK", command=lambda:funcao(nome), bg="blue", fg="white")
    confirmar.pack()
    campo.delete(0, tk.END)

def apagar_arquivos(event, texto):
    limpar_arquivos_da_tela()
    if texto.endswith(".py"):
        os.remove(os.path.join(pasta_atual, texto))
        logs.append(f"apagou um arquivo chamado: {texto}")
    else:
        shutil.rmtree(os.path.join(pasta_atual, texto))
        logs.append(f"apagou uma pasta chamada: {texto}")
    listar()
    edit.destroy()
    search.pack_forget()
    cancelar.pack_forget()
    buscar.pack_forget()
    pesquisa.pack(before=frame_arquivos)

def verificar_o_arquivo_selecionado(texto):
    if pasta==1:
        os.mkdir(os.path.join(pasta_atual, texto))
        logs.append(f"criou uma pasta chamada {texto}")
    else:
        with open(os.path.join(pasta_atual, f"{texto}.py"), "w"):
            pass
        logs.append(f"criou um arquivo chamado {texto}.py")
        print(f"criou {texto}.py")
    listar()
def limpar_arquivos_da_tela():
    for i in range(len(os.listdir(pasta_atual))):
            if arquivo[i]!="":
                arquivo[i].pack_forget()
    
def verificar_arquivo_e_adiciona_imagem(item, i):
    if item.endswith(".py"):
        arquivo[i].config(image=imagem)
    else:
        arquivo[i].config(image=diretorio)

def criar_arquivos_e_adicionar_ao_vetor(linha, coluna, i, item):
    caixa = tk.Frame(frame_arquivos, width=120, height=140, bg="#2e2d2d")
    caixa.grid(row=linha, column=coluna, padx=10, pady=10)
    caixa.grid_propagate(False)
    arquivo[i] = tk.Button(caixa, text=item, compound="top", wraplength=100, bg="#2e2d2d", fg="white", font=("Segoe UI Variable Small Semibol", 10), bd=0)
    arquivo[i].bind("<Double-Button-1>", lambda event: mudar_pasta(event, item))
    arquivo[i].bind("<Button-3>", lambda event: janela_edicao(event, item))



def caminho(relativo):
    base = getattr(sys, "_MEIPASS", os.path.abspath("."))
    return os.path.join(base, relativo)
os.system("cls")


#função que confirma a criação de um novo arquivo
def selecao_de_arquivo(identificador):
    global pasta
    global campo
    global confirmar
    if identificador==1:
        pasta=1
    criar_campo_digitavel(nova_janela, criar_um_novo_arquivo, 1)    
#função que escolhe o tipo de arquivo
def abrir_janela_ciação_arquivo():
    global criar_pasta
    global criar_arquivo
    global nova_janela
    nova_janela=tk.Toplevel()
    nova_janela.config(bg="gray")
    x=(nova_janela.winfo_screenwidth()//2)-(200//2)
    y=(nova_janela.winfo_screenheight()//2)-(100//2)
    nova_janela.geometry(f"{200}x{100}+{x}+{y}")
    criar_pasta = tk.Button(nova_janela, text="Pasta", command=lambda: (selecao_de_arquivo(1), criar_arquivo.pack_forget(), criar_pasta.pack_forget()))
    criar_pasta=criar_pasta
    criar_pasta.pack(pady=10)
    criar_arquivo = tk.Button(nova_janela, text="Arquivo", command=lambda: (selecao_de_arquivo(2), criar_arquivo.pack_forget(), criar_pasta.pack_forget()))
    criar_arquivo.pack()
    nova_janela.protocol("WM_DELETE_WINDOW", valor_pasta_0)
    nova_janela.mainloop()

def criar_um_novo_arquivo(a):
    global pasta
    texto=campo.get()
    if texto!="":
        limpar_arquivos_da_tela()
        verificar_o_arquivo_selecionado(texto)
    campo.pack_forget()
    confirmar.pack_forget()
    nova_janela.destroy()
    pasta=0

#função que lista todos os arquivos presentes na pasta
def listar():
    arquivo.append("")
    i = 0
    linha = 0
    coluna = 0
    for item in os.listdir(pasta_atual):
        if item!="projeto_arquitetura.py" and item!="arquivos_do_sistema":
            criar_arquivos_e_adicionar_ao_vetor(linha, coluna, i, item)
            verificar_arquivo_e_adiciona_imagem(item, i)
            arquivo[i].pack(expand=True)
            coluna += 1
            if coluna == 11:
                coluna = 0
                linha += 1
            i += 1
        else:
            continue


#cria a janela principal
janela=tk.Tk()
x=(janela.winfo_screenwidth()//2)-(800//2)
y=(janela.winfo_screenheight()//2)-(600//2)
janela.geometry(f"{800}x{600}+{x}+{y}")
janela.config(bg="#2e2d2d")

#variáveis usada para armazenar a foto do fundo dos arquivos
imagem = tk.PhotoImage(file=caminho("arquivos_do_sistema/teste.png"))
mais = tk.PhotoImage(file=caminho("arquivos_do_sistema/mais.png"))
diretorio = tk.PhotoImage(file=caminho("arquivos_do_sistema/pasta.png"))
pasta_atual="."
#vetor que armazena o nome de todos os arquivos da pasta
arquivo=[""]*len(os.listdir(pasta_atual))
pesquisa=tk.Button(janela, text="pesquisa", command=campo_pesquisa)
pesquisa.pack(pady=1)
#método usado para organizar os arquivos em linhas 
frame_arquivos = tk.Frame(janela, bg="#2e2d2d")
frame_arquivos.pack(fill="both", expand=True)
#botão que abre a criação de um novo arquivo
botao_criacao=tk.Button(janela, command=abrir_janela_ciação_arquivo, image=mais, bg="#2e2d2d", bd=0)
botao_criacao.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)
#chama a função que lista todos os arquivos presentes na pasta
listar()

nova_janela=None
edit=None

#campo para digitar o nome do arquivo
campo=None
confirmar=None

#variável para definir a criação de pastas ou arquivos, que seram transformadas em botões
criar_arquivo=None
criar_pasta=None

#variáveis gloais para armazenas os valores d acriação de pasta ou arquivos
pasta=0
arquivo_py=0
janela.protocol("WM_DELETE_WINDOW", fechar_todas_janelas)
search=None
cancelar=None
buscar=None

logs=[]
janela.mainloop()
os.system("cls")
print("Registro de Operações:")
if logs==[]:
    print("Nenhuma operação realizada")
else:
    for a in logs:
        print(a)
