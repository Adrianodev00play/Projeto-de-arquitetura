import os
import tkinter as tk
import sys
import shutil

#função que exclui todos os registros do arquivo de texto
def excluir_registros():
    global registro
    with open("Registros.txt", "w"):
        pass

#função que muda o valor da variável "pasta_atual" para o caminho da pasta anterior
def voltar_pasta():
    global pasta_atual
    limpar_arquivos_da_tela()
    pasta_atual = os.path.dirname(pasta_atual)
    listar(2, 2)

#função que cria o botão de voltar para a pasta anterior
def botao_de_voltar():
    rf=tk.Button(janela, text="voltar", image=botao_voltar, bd=0, bg="#2e2d2d", command=lambda: (voltar_pasta(), rf.destroy()))
    rf.place(x=10, y=10)

#função que verifica se é um diretório ao clicar duas vezes, se for um arquivo python não faz nada, se for um diretório, limpa os arquivos na tela, muda o caminho da pasta atual e verifica: se a pasta atual for diferente da pasta raiz, exibe um botão pra voltar pra pasta anterior
def mudar_pasta(event, item):
    global search
    global buscar
    global cancelar
    global pasta_atual
    global pesquisa
    li=0
    if item.endswith(".py"):
        li=li
    else:
        limpar_arquivos_da_tela()
        pasta_atual=os.path.join(pasta_atual, item)
        listar(2, 2)
        if pasta_atual!=".":
            botao_de_voltar()
    pesquisa.pack_forget()
    pesquisa.pack(before=frame_arquivos, pady=10)
    search.pack_forget()
    buscar.pack_forget()
    cancelar.pack_forget()

#função que cria um novo campo digitável somente para pesquisa, cria também os botões "cancelar" e "OK(ok usado exclusivamente para o campo de pesquisa)"
def campo_pesquisa():
    global search
    global cancelar
    global buscar
    search=tk.Entry(janela)
    pesquisa.pack_forget()
    search.pack(before=frame_arquivos)

    #ao clicar nesse botão de cancelar irá limpar todos os arquivos na tela
    cancelar=tk.Button(janela, text="cancelar", image=botao_cancelar, bd=0, bg="#2e2d2d", command=lambda:(search.pack_forget(), cancelar.pack_forget(), pesquisa.pack(before=frame_arquivos), buscar.pack_forget(), limpar_arquivos_da_tela(), listar(2, 2)))
    cancelar.pack(before=frame_arquivos)
    buscar=tk.Button(janela, text="Ok", bg="#2e2d2d", image=botao_ok, bd=0, command=lambda:(limpar_arquivos_da_tela(), listar(1, search.get())))
    buscar.pack(before=frame_arquivos)

#função que fecha todas as janelas abertas
def fechar_todas_janelas():
    janela.destroy()
    edit.destroy()
    nova_janela.destroy()

#função que renomeia arquivos, pega o nome do arquivo através do parâmetro [antigo], depois pega o novo nome a ser renomeado que está no campo digitável, verifica se o o arquivo é um arquivo python ou diretório, renomeia esse arquivo, adiciona ao vetor de logs tal operação, limpa os arquivos na tela e chama a função listar
def renomear_update_arquivo(antigo):
    texto=campo.get()
    if antigo.endswith(".py"):
        os.rename(os.path.join(pasta_atual, antigo), os.path.join(pasta_atual, f"{texto}.py"))
        logs.append(f"renomeou um arquivo chamado [{antigo}] para [{texto}.py]")
    else:
        os.rename(os.path.join(pasta_atual, antigo), os.path.join(pasta_atual, texto))
        logs.append(f"renomeou uma pasta chamada [{antigo}] para [{texto}]")
    limpar_arquivos_da_tela()
    listar(2, 2)
    edit.destroy()
    search.pack_forget()
    cancelar.pack_forget()
    buscar.pack_forget()
    pesquisa.pack(before=frame_arquivos)
    campo.pack_forget()
    confirmar.pack_forget()

#função que garante que quando o usuário desiste de criar algum arquivo e acaba fechando a janela clicando no "X", o valor da variável "pasta" passe a valer 0 novamente
def valor_pasta_0():
    global pasta
    pasta=0
    nova_janela.destroy()

#função que cria a janela de edição e cria também os botões de "apagar" e "renomear"
def janela_edicao(evento, nome):
    global edit
    edit=tk.Toplevel()
    x=(edit.winfo_screenwidth()//2)-(200//2)
    y=(edit.winfo_screenheight()//2)-(100//2)
    edit.geometry(f"{200}x{100}+{x}+{y}")
    edit.config(bg="gray")
    apagar=tk.Button(edit, image=botao_excluir, bg="gray", bd=0, command=lambda:apagar_arquivos(1, nome))
    apagar.pack()
    renomear=tk.Button(edit, text="renomear", bg="gray", bd=0, image=botao_renomear, command=lambda:(criar_campo_digitavel(edit, renomear_update_arquivo, nome), renomear.pack_forget(), apagar.pack_forget()))
    renomear.pack()
    edit.mainloop()

#função que cria o campo digitável que pode ser usada na criação de arquivos e também para renomear arquivos e cria também o botão "OK" que pode ser usado para criar ou renomear um arquivo
#OBS:Essa função pode fazer duas coisas: ao ser usado para criar arquivos, o parâmetro [tipo] vai receber o valor "nova_janela", o parâmetro [funcao] recebe "criar_um_novo_arquivo" e o parâmetro [nome] recebe um valor qualquer porque no momento nao vai ser usado. Já ao ser usado para renomear arquivos, o parâmetro [tipo] recebe o valor "edit", o parâmetro [funcao] recebe "renomear_update_arquivo" e o parâmetro [nome] recebe o nome do arquivo a ser renomeado
def criar_campo_digitavel(tipo, funcao, nome):
    global campo
    global confirmar
    campo=tk.Entry(tipo)
    campo.pack(pady=10)
    confirmar=tk.Button(tipo, text="OK", bg="gray", image=botao_ok, bd=0, command=lambda:funcao(nome), fg="white")
    confirmar.pack()
    campo.delete(0, tk.END)

#função que recebe o nome do arquivo a ser apagado, limpa oa arquivos da tela, verifica se o arquivo é um arquivo python ou um diretório, apagando assim o respectivo arquivo. Também adiciona uma mensagem ao vetor de logs para registrar tal operação, e depois lista os arquivos novamente
def apagar_arquivos(event, texto):
    limpar_arquivos_da_tela()
    if texto.endswith(".py"):
        os.remove(os.path.join(pasta_atual, texto))
        logs.append(f"apagou um arquivo chamado: {texto}")
    else:
        shutil.rmtree(os.path.join(pasta_atual, texto))
        logs.append(f"apagou uma pasta chamada: {texto}")
    listar(2, 2)
    edit.destroy()
    search.pack_forget()
    cancelar.pack_forget()
    buscar.pack_forget()
    pesquisa.pack(before=frame_arquivos)

#função que verifica o arquivo selecionado usando a variável "pasta" como referência, se o valor de "pasta" for igual a 1 o programa cria uma pasta, se for diferente de 1 o programa já entende que o arquivo selecionado é um arquivo python e ja cria ele, e depois faz a listagem de arquivos novamente
def verificar_o_arquivo_selecionado(texto):
    if pasta==1:
        os.mkdir(os.path.join(pasta_atual, texto))
        logs.append(f"criou uma pasta chamada: {texto}")
    else:
        with open(os.path.join(pasta_atual, f"{texto}.py"), "w"):
            pass
        logs.append(f"criou um arquivo chamado: {texto}.py")
        print(f"criou {texto}.py")
    listar(2, 2)

#função que limpa todos os arquivos da tela
def limpar_arquivos_da_tela():
    for i in range(len(os.listdir(pasta_atual))):
            if arquivo[i]!="":
                arquivo[i].master.destroy()

#função que recebe um arquivo verifica se ele é um arquivo ou diretório e aplica sua devida imagem de fundo
def verificar_arquivo_e_adiciona_imagem(item, i):
    if item.endswith(".py"):
        arquivo[i].config(image=imagem)
    else:
        arquivo[i].config(image=diretorio)

#funcão que cria os arquivos e adiciona ao vetor de arquivos, cria também as caixas onde os arquivos seram exibidos
def criar_arquivos_e_adicionar_ao_vetor(linha, coluna, i, item):
    caixa = tk.Frame(frame_arquivos, width=120, height=140, bg="#2e2d2d")
    caixa.grid(row=linha, column=coluna, padx=10, pady=10)
    caixa.grid_propagate(False)
    arquivo[i] = tk.Button(caixa, text=item, compound="top", wraplength=100, bg="#2e2d2d", fg="white", font=("Segoe UI Variable Small Semibol", 10), bd=0)
    arquivo[i].bind("<Double-Button-1>", lambda event: (mudar_pasta(event, item)))
    arquivo[i].bind("<Button-3>", lambda event: janela_edicao(event, item))

#função que aponta os caminhos corretos das imagens caso o arquivo seja compilado para um executável
def caminho(relativo):
    base = getattr(sys, "_MEIPASS", os.path.abspath("."))
    return os.path.join(base, relativo)
os.system("cls")

#função que recebe o identificador vinda da funcao "abrir_janela_criação_arquivo()" e abre um campo digitável para o nome do arquivo ou pasta
def selecao_de_arquivo(identificador):
    global pasta
    global campo
    global confirmar

    #se o identificador for igual a 1, o valor da variável global "pasta" passa a ser 1, que vai ser usada mais tarde
    if identificador==1:
        pasta=1
    criar_campo_digitavel(nova_janela, criar_um_novo_arquivo, 1)

#função que cria a janela de criação de arquivos e os botões "criar pasta" e "criar arquivos"
def abrir_janela_criação_arquivo():
    global criar_pasta
    global criar_arquivo
    global nova_janela
    nova_janela=tk.Toplevel()
    nova_janela.config(bg="gray")
    x=(nova_janela.winfo_screenwidth()//2)-(200//2)
    y=(nova_janela.winfo_screenheight()//2)-(100//2)
    nova_janela.geometry(f"{200}x{100}+{x}+{y}")

    #ao clicar no botao criar pasta envia o parâmetro 1 para uma funcão responsável por identificar a opção selecionada
    criar_pasta = tk.Button(nova_janela, text="Pasta", image=botao_pasta, bg="gray", bd=0, command=lambda: (selecao_de_arquivo(1), criar_arquivo.pack_forget(), criar_pasta.pack_forget()))
    criar_pasta=criar_pasta
    criar_pasta.pack(pady=10)

    #ao ser clicado envia o parâmetro 2 para uma funcão responsável por identificar a opção selecionada
    criar_arquivo = tk.Button(nova_janela, text="Arquivo", image=botao_arquivo, bg="gray", bd=0,  command=lambda: (selecao_de_arquivo(2), criar_arquivo.pack_forget(), criar_pasta.pack_forget()))
    criar_arquivo.pack()
    nova_janela.protocol("WM_DELETE_WINDOW", valor_pasta_0)
    nova_janela.mainloop()

#função que pega o texto do campo digitável no mode de criação de arquivos, verifica se o texto é vazio, se for vazio nao faz nada, se tiver algum conteúdo ela limpa todos os arquivos da tela, e verifica qual foi o arquivo que você selecionou, por ultimo, muda o valor de pasta novamente para 0
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

#função que lista todos os arquivos presentes na pasta, adiciona esses arquivos em um vetor de arquivos, verifica o tipo de arquivo e coloca sua devida imagem de fundo, exibe esses arquivos no layout e organiza o sistema de grid, ela também serve para exibir somente os arquivos das pesquisas
def listar(filtro, nome):
    arquivo.append("")
    i = 0
    linha = 0
    coluna = 0
    for item in os.listdir(pasta_atual):
        if os.path.isdir(item) or item.endswith(".py"):
            if item!="projeto_arquitetura.py" and item!="arquivos_do_sistema" and item!="Registros.txt" and item!="" :
                criar_arquivos_e_adicionar_ao_vetor(linha, coluna, i, item)
                verificar_arquivo_e_adiciona_imagem(item, i)
                if filtro==1:
                    if arquivo[i]["text"]==f"{nome}.py" or arquivo[i]["text"]==nome:
                        arquivo[i].pack(expand=True)
                        coluna += 1
                        if coluna == 11:
                            coluna = 0
                            linha += 1
                else:        
                    arquivo[i].pack(expand=True)
                    coluna += 1
                    if coluna == 11:
                        coluna = 0
                        linha += 1
                i += 1
            else:
                continue

#===Escopo principal===

#cria a janela principal do gerenciador de arquivos
janela=tk.Tk()
x=(janela.winfo_screenwidth()//2)-(800//2)
y=(janela.winfo_screenheight()//2)-(600//2)
janela.geometry(f"{800}x{600}+{x}+{y}")
janela.config(bg="#2e2d2d")

#variáveis usada para armazenar a foto do fundo dos arquivos
imagem = tk.PhotoImage(file=caminho("arquivos_do_sistema/teste.png"))
mais = tk.PhotoImage(file=caminho("arquivos_do_sistema/mais.png"))
diretorio = tk.PhotoImage(file=caminho("arquivos_do_sistema/pasta.png"))
botao_pasta=tk.PhotoImage(file=caminho("arquivos_do_sistema/nome_pasta.png"))
botao_arquivo=tk.PhotoImage(file=caminho("arquivos_do_sistema/nome_arquivo.png"))
botao_excluir=tk.PhotoImage(file=caminho("arquivos_do_sistema/nome_excluir.png"))
botao_renomear=tk.PhotoImage(file=caminho("arquivos_do_sistema/nome_renomear.png"))
botao_pesquisa=tk.PhotoImage(file=caminho("arquivos_do_sistema/nome_pesquisa.png"))
botao_cancelar=tk.PhotoImage(file=caminho("arquivos_do_sistema/nome_cancelar.png"))
botao_voltar=tk.PhotoImage(file=caminho("arquivos_do_sistema/nome_voltar.png"))
botao_ok=tk.PhotoImage(file=caminho("arquivos_do_sistema/nome_ok.png"))

#variável usada para apontar o caminho para onde o programma deve "olhar"
pasta_atual="."

#vetor que armazena o nome de todos os arquivos da pasta
arquivo=[""]*len(os.listdir(pasta_atual))

#botão que abre a aba de pesquisa
pesquisa=tk.Button(janela, text="pesquisa", image=botao_pesquisa, bg="#2e2d2d", bd=0, command=campo_pesquisa)
pesquisa.pack(pady=10)
#método usado para organizar os arquivos em linhas 
frame_arquivos = tk.Frame(janela, bg="#2e2d2d")
frame_arquivos.pack(fill="both", expand=True)

#botão que abre a criação de um novo arquivo
botao_criacao=tk.Button(janela, command=abrir_janela_criação_arquivo, image=mais, bg="#2e2d2d", bd=0)
botao_criacao.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)

#chama a função que lista todos os arquivos presentes na pasta
listar(2, "s")

#variável global que é usada para criar a janela de criação de arquivos
nova_janela=None

#variável global que é usada para criar a janela de edição de arquivos
edit=None

#variável global usada para criar o campo para digitar o nome do arquivo
campo=None

#variável global usada para criar o botão "OK" da janela de criação de arquivos e da janela de renomear
confirmar=None

#variável global usada para criar o botao de "criar pasta"
criar_arquivo=None

#variável global usada para criar o botao de "criar pasta"
criar_pasta=None

#variáveis gloais para armazenas os valores d acriação de pasta ou arquivos
pasta=0

#metodo usado para fechar todas as outras janelas ao fechar a janela principal
janela.protocol("WM_DELETE_WINDOW", fechar_todas_janelas)

#variável global usada para criar o campo digitável da busca
search=None

#variável global usada para criar o botão de excluir arquivos ou pastas
cancelar=None

#variável global usada para criar o botão "OK" da busca por arquivos
buscar=None

#vetor que armazena cada interação feita dentro do programa
logs=[]

#botão que apaga todos os registros de operações realizadas, guardadas dentro de um arquivo de texto
apagar_registros = tk.Button(janela, text="Apagar registros", command=excluir_registros)
apagar_registros.place(relx=1.0, rely=0.0, anchor="ne", x=-10, y=10)

#inicializa a janela principal
janela.mainloop()

#limpa o terminal ao fechar o programa
os.system("cls")

#printa no terminal todas as operações realizadas dentro do gerenciador 
print("Registro de Operações:\n")
if logs==[]:
    print("Nenhuma operação realizada")
else:
    for a in logs:
        print(a)

#armazena os arquivos de logs no arquivo de texto
if logs:
    with open("Registros.txt", "r") as arquivo:
        conteudo = arquivo.read()

    with open("Registros.txt", "w") as arquivo:
        arquivo.write("________________________\n")
        for item in logs:
            arquivo.write(item + "\n")
        arquivo.write("\n")
        arquivo.write(conteudo)
