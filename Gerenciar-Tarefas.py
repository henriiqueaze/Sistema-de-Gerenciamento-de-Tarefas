import tkinter as tk
from arquivo import *
from tkinter import messagebox

#Criando o arquivo .txt caso ele não exista
arquivo = 'tarefas.txt'

if not Arquivo_Existe(arquivo):
    Criar_Arquivo(arquivo)

nome_tarefas = []
descricao_tarefas = []

#Carrega as tarefas já existentes do arquivo tarefas.txt
try:
    with open(arquivo, 'r') as arquivo_tarefas:
        for linha in arquivo_tarefas:
            nome, descricao = linha.strip().split('|')
            nome_tarefas.append(nome)
            descricao_tarefas.append(descricao)

except FileNotFoundError:
    print(f"O arquivo '{arquivo}' não foi encontrado.")

#------------><-------------#

#Função para salvar tarefas no arquivo.
def Salvar_Tarefas():
    try:
        with open(arquivo, 'w') as arquivo_tarefas:
            for nome, descricao in zip(nome_tarefas, descricao_tarefas):
                arquivo_tarefas.write(f"{nome}|{descricao}\n")

    except IOError:
        print(f"Erro ao salvar as tarefas no arquivo '{arquivo}'.")

def Enviar_Tarefa():
    enviar_desc = escrever_desc.get()
    enviar_nome = escrever_nome.get()

    #Verificar se os dois campos foram preenchidos.
    if enviar_desc == '' or enviar_nome == '':
        messagebox.showerror("Erro", "Por favor, insira um nome e uma descrição para a tarefa.")
        escrever_nome.focus_force()

    else:
        #Limpando as entradas depois do envio da tarefa.
        escrever_nome.delete(0, 'end')
        escrever_desc.delete(0, 'end')

        #Adicionar tarefa nova nas listas.
        descricao_tarefas.append(enviar_desc)
        nome_tarefas.append(enviar_nome)

        Salvar_Tarefas()

        messagebox.showinfo('Alerta!', 'Sua tarefa e descrição foram enviados!')
        adicionar_tarefa_janela.destroy()

#------------><-------------#

#Função para enviar o número relacionado a tarefa.
def Enviar_Numero():
    global marcar_como_concluida_numero

    #Pegando o número e convertendo para inteiro.
    marcar_numero_str = marcar_como_concluida_numero.get()

    # Verificar se a string não tem nada.
    if not marcar_numero_str:
        messagebox.showerror("Erro", "Por favor, insira um número relacionado à tarefa.")
        marcar_como_concluida_numero.focus_force()
        return

    try:
        marcar_numero = int(marcar_numero_str) - 1

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido relacionado à tarefa.")
        marcar_como_concluida_numero.focus_force()
        return

    #Verificando se o número inserido é um número válido.
    if marcar_numero < 0 or marcar_numero >= len(nome_tarefas):
        messagebox.showerror("Erro", "O número inserido não corresponde a uma tarefa válida.")
        marcar_como_concluida_numero.focus_force()
        return

    #Colocar a tarefa escolhida como marcada na lista de tarefas marcadas como concluídas.
    nome_tarefas[marcar_numero] = ''.join(c + '\u0336' for c in nome_tarefas[marcar_numero])
    descricao_tarefas[marcar_numero] = ''.join(c + '\u0336' for c in descricao_tarefas[marcar_numero])

    #Limpar a entry do número.
    marcar_como_concluida_numero.delete(0, 'end')

    #Mostrar mensagem de sucesso.
    messagebox.showinfo('Alerta!', 'Sua tarefa foi marcada como concluída!')
    marcar_como_concluida_janela.destroy()

#------------><-------------#

#Função para excluir uma tarefa.
def Excluir_Tarefa():
    global excluir_numero

    #Pegando o número inserido e convertendo para inteiro.
    marcar_numero_str = excluir_numero.get()

    #Verificar se nada foi enviado.
    if not marcar_numero_str:
        messagebox.showerror("Erro", "Por favor, insira um número relacionado à tarefa.")
        excluir_numero.focus_force()
        return

    try:
        marcar_numero = int(marcar_numero_str) - 1

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido relacionado à tarefa.")
        excluir_numero.focus_force()
        return

    #Verificar se o número inserido é um número válido.
    if marcar_numero < 0 or marcar_numero >= len(nome_tarefas):
        messagebox.showerror("Erro", "O número inserido não corresponde a uma tarefa válida.")
        excluir_numero.focus_force()
        return

    #Excluir tarefa das listas.
    del (nome_tarefas[marcar_numero], descricao_tarefas[marcar_numero])

    #Limpar entry do número.
    excluir_numero.delete(0, 'end')

    #Exibir mensagem de sucesso.
    messagebox.showinfo('Alerta!', 'Sua tarefa foi excluída!')
    excluir_tarefa_janela.destroy()

#------------><-------------#

#Exibindo uma mensagem caso nenhuma tarefa for adicionada.
def Nenhuma_Tarefa_Adicionada(janela):
    nenhuma_tarefa_adicionada_texto1 = tk.Label(janela, text='Nenhuma tarefa foi', font="Arial 19 bold",
                                                bg="#262A40", fg="#F2F2F2")
    nenhuma_tarefa_adicionada_texto2 = tk.Label(janela, text='adicionada ainda.', font="Arial 19 bold",
                                                bg="#262A40", fg="#F2F2F2")
    nenhuma_tarefa_adicionada_texto1.place(x=35, y=60)
    nenhuma_tarefa_adicionada_texto2.place(x=43, y=100)

#------------><-------------#

#Abrir janela de adicionar tarefa.
def JanelaAdicionarTarefa():
    global adicionar_tarefa_janela, escrever_nome, escrever_desc

    adicionar_tarefa_janela = tk.Toplevel(janela)
    adicionar_tarefa_janela.title('Adicionar Tarefa')
    adicionar_tarefa_janela.config(background="#262A40")
    adicionar_tarefa_janela.geometry('300x200')
    adicionar_tarefa_janela.resizable(False, False)

    #Adicionando o texto da janela.
    adicionar_tarefa_texto1 = tk.Label(adicionar_tarefa_janela, text='Adicionar nome e', font="Arial 15 bold",
                                       bg="#262A40", fg="#F2F2F2")
    adicionar_tarefa_texto2 = tk.Label(adicionar_tarefa_janela, text='descrição da tarefa', font="Arial 15 bold",
                                       bg="#262A40", fg="#F2F2F2")
    adicionar_tarefa_texto1.place(x=64, y=10)
    adicionar_tarefa_texto2.place(x=55, y=35)

    #Escrever a primeira entry.
    escrever_nome = tk.Entry(adicionar_tarefa_janela, width=35)
    escrever_nome.place(x=45, y=80)
    escrever_nome.insert(0, 'Nome:')

    #Escrever a segunda entry.
    escrever_desc = tk.Entry(adicionar_tarefa_janela, width=35)
    escrever_desc.place(x=45, y=110)
    escrever_desc.insert(0, 'Descrição:')

    #Botão enviar.
    botao_enviar = tk.Button(adicionar_tarefa_janela, text='Enviar', height=1, width=5, command=Enviar_Tarefa)
    botao_enviar.place(x=125, y=150)

#------------><-------------#

#Abrir a janela de exibir tarefas.
def JanelaExibirTarefa():
    global exibir_tarefa_janela
    exibir_tarefa_janela = tk.Toplevel(janela)
    exibir_tarefa_janela.title('Exibir Tarefa')
    exibir_tarefa_janela.config(background="#262A40")
    exibir_tarefa_janela.geometry('300x200')
    exibir_tarefa_janela.resizable(False, False)

    if not nome_tarefas and not descricao_tarefas:
        Nenhuma_Tarefa_Adicionada(exibir_tarefa_janela)

    else:
        nomes = tk.Label(exibir_tarefa_janela, text='Tarefas:          Descrição:', bg='#262A40', fg='white',
                         font='Arial 15 bold')
        nomes.place(x=27, y=25)

        #Convertendo os elementos da lista para strings.
        quebra_linha1 = '\n'.join(str(tarefa) for tarefa in nome_tarefas)

        tarefas = tk.Label(exibir_tarefa_janela, text=quebra_linha1, bg='#262A40', fg='white',
                           font='Arial 12 bold')
        tarefas.place(x=38, y=63)

        quebra_linha2 = '\n'.join(descricao_tarefas)
        descricao = tk.Label(exibir_tarefa_janela, text=quebra_linha2, bg='#262A40', fg='white',
                             font='Arial 12 bold')

        descricao.place(x=175, y=63)

#------------><-------------#

#Abrir a janela de marcar tarefa como concluída.
def JanelaMarcarComoConcluida():
    global marcar_como_concluida_numero, marcar_como_concluida_janela
    marcar_como_concluida_janela = tk.Toplevel(janela)
    marcar_como_concluida_janela.title('Marcar Como Concluída')
    marcar_como_concluida_janela.config(background="#262A40")
    marcar_como_concluida_janela.geometry('300x200')
    marcar_como_concluida_janela.resizable(False, False)

    if not nome_tarefas and not descricao_tarefas:
        Nenhuma_Tarefa_Adicionada(marcar_como_concluida_janela)

    else:
        nomes = tk.Label(marcar_como_concluida_janela, text='Tarefas:          Descrição:', bg='#262A40', fg='white',
                         font='Arial 15 bold')
        nomes.place(x=27, y=25)
        quebra_linha1 = '\n'.join(nome_tarefas)
        tarefas = tk.Label(marcar_como_concluida_janela, text=quebra_linha1, bg='#262A40', fg='white',
                           font='Arial 12 bold')
        tarefas.place(x=38, y=63)

        quebra_linha2 = '\n'.join(descricao_tarefas)
        descricao = tk.Label(marcar_como_concluida_janela, text=quebra_linha2, bg='#262A40', fg='white',
                             font='Arial 12 bold')
        descricao.place(x=175, y=63)

        marcar_como_concluida_numero = tk.Entry(marcar_como_concluida_janela, width=20)
        marcar_como_concluida_numero.place(x=85, y=141)
        marcar_como_concluida_numero.insert(0, 'Número da Tarefa:')

        botao_enviar_numero = tk.Button(marcar_como_concluida_janela, text='Enviar', height=1, width=5,
                                        command=Enviar_Numero)
        botao_enviar_numero.place(x=120, y=161)

#------------><-------------#

#Abrir a janela de excluir tarefa.
def JanelaExcluirTarefa():
    global excluir_numero, excluir_tarefa_janela
    excluir_tarefa_janela = tk.Toplevel(janela)
    excluir_tarefa_janela.title('Excluir Tarefa')
    excluir_tarefa_janela.config(background="#262A40")
    excluir_tarefa_janela.geometry('300x200')
    excluir_tarefa_janela.resizable(False, False)

    if not nome_tarefas and not descricao_tarefas:
        Nenhuma_Tarefa_Adicionada(excluir_tarefa_janela)

    else:
        nomes = tk.Label(excluir_tarefa_janela, text='Tarefas:          Descrição:', bg='#262A40',
                         fg='white',
                         font='Arial 15 bold')
        nomes.place(x=27, y=25)
        quebra_linha1 = '\n'.join(nome_tarefas)
        tarefas = tk.Label(excluir_tarefa_janela, text=quebra_linha1, bg='#262A40', fg='white',
                           font='Arial 12 bold')
        tarefas.place(x=38, y=63)

        quebra_linha2 = '\n'.join(descricao_tarefas)
        descricao = tk.Label(excluir_tarefa_janela, text=quebra_linha2, bg='#262A40', fg='white',
                             font='Arial 12 bold')
        descricao.place(x=175, y=63)

        excluir_numero = tk.Entry(excluir_tarefa_janela, width=20)
        excluir_numero.place(x=85, y=141)
        excluir_numero.insert(0, 'Número da Tarefa:')

        botao_excluir_numero = tk.Button(excluir_tarefa_janela, text='Enviar', height=1, width=5,
                                         command=Excluir_Tarefa)
        botao_excluir_numero.place(x=120, y=161)

#------------><-------------#

#Janela principal.
janela = tk.Tk()
janela.title('Gerenciamento de Tarefas')
janela.geometry('500x450')
janela.config(background="#262A40")
janela.resizable(False, False)

#------------><-------------#

#Texto Inicial.
titulo = tk.Label(janela, text='Sistema de Gerenciamento', font="Arial 20 bold", bg="#262A40", fg="#F2F2F2")
titulo.place(x=75, y=15)

titulo1 = tk.Label(janela, text='de Tarefas', font="Arial 20 bold", bg="#262A40", fg="#F2F2F2")
titulo1.place(x=180, y=50)

#------------><-------------#

#Botão adicionar tarefa.
adicionar_tarefa_botao = tk.Button(janela, text="Adicionar Tarefa", bg="#416CA6", fg="#0E1521",
                                   activebackground="#85BFF2",
                                   activeforeground="black", font="Arial 12 bold", height=2, width=36,
                                   command=JanelaAdicionarTarefa)
adicionar_tarefa_botao.place(x=70, y=115)

#Botão exibir tarefas.
exibir_tarefa_botao = tk.Button(janela, text='Exibir Tarefas', bg="#416CA6", fg="#0E1521", activebackground="#85BFF2",
                                activeforeground="black", font="Arial 12 bold", height=2, width=36,
                                command=JanelaExibirTarefa)
exibir_tarefa_botao.place(x=70, y=195)

#Botão marcar tarefa como concluída.
marcar_como_concluida_botao = tk.Button(janela, text='Marcar Como Concluída', bg="#416CA6", fg="#0E1521",
                                        font="Arial 12 bold", height=2, width=36, activebackground="#85BFF2",
                                        activeforeground="black", command=JanelaMarcarComoConcluida)
marcar_como_concluida_botao.place(x=70, y=275)

#Botão excluir tarefa.
excluir_tarefa_botao = tk.Button(janela, text='Excluir Tarefa', bg="#416CA6", fg="#0E1521", font="Arial 12 bold",
                                 height=2,
                                 width=36, activebackground="#85BFF2", activeforeground="black",
                                 command=JanelaExcluirTarefa)
excluir_tarefa_botao.place(x=70, y=355)

janela.mainloop()
