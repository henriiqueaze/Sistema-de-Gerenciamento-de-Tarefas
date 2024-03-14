import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from time import sleep

nome_tarefas = list()
descricao_tarefas = list()


def Titulo():
    string = 'Sistema de Gerenciamento de Tarefas'
    tamanho = len(string) + 6
    print('=' * tamanho)
    print(string.center(tamanho))
    print('=' * tamanho)
    sleep(1.5)


def menu():
    print('[1] - Adicionar Tarefa\n[2] - Exibir Tarefas\n[3] - Marcar como Concluída\n'
          '[4] - Excluir Tarefa\n[5] - Sair')
    resposta = int(input('Digite sua opção: '))

    while resposta < 1 or resposta > 5:
        print('\033[31mERRO!\033[m Resposta Inválida.')
        sleep(1.5)
        resposta = int(input('Digite sua opção: '))

    return resposta


def Mostrar_Tarefas():
    for numerar, tarefa in enumerate(nome_tarefas):
        print(f'[{numerar + 1}] - {tarefa}')


def TarefaNaoAdicionada():
    print('Nenhuma tarefa foi adicionada ainda.')
    sleep(1.5)


def AdicionarTarefa():
    nome_tarefas.append(str(input('Digite sua Tarefa: ')))
    descricao_tarefas.append(str(input('Digite uma descrição da sua tarefa: ')))
    print('Tarefa Adicionada!')
    sleep(1.5)


def ExibirTarefas():
    if not nome_tarefas:
        TarefaNaoAdicionada()

    else:
        Mostrar_Tarefas()
        ver_tarefas = str(input('Deseja ver a descrição de alguma tarefa? '))

        while ver_tarefas not in 'SsNn':
            print('\033[31mERRO!\033[m Resposta Inválida.')
            sleep(1.5)
            ver_tarefas = str(input('Deseja ver a descrição de alguma tarefa? '))

        if ver_tarefas in 'Ss':
            resposta = int(input('Qual tarefa você deseja verificar? ')) - 1
            print(descricao_tarefas[resposta])
            sleep(3)

        if ver_tarefas in 'Nn':
            print('Carregando...')
            sleep(1.5)


def MarcarComoConcluida():
    if not nome_tarefas:
        TarefaNaoAdicionada()

    else:
        Mostrar_Tarefas()
        resposta = int(input('Qual tarefa você deseja marcar como concluída? ')) - 1
        nome_tarefas[resposta] = ''.join(c + '\u0336' for c in nome_tarefas[resposta])
        print('Tarefa Concluída!')
        sleep(1.5)


def ExcluirTarefa():
    if not nome_tarefas:
        TarefaNaoAdicionada()

    else:
        Mostrar_Tarefas()
        resposta = int(input('Qual tarefa você deseja \033[31mexcluir\033[m? ')) - 1
        nome_tarefas.pop(resposta)
        descricao_tarefas.pop(resposta)
        print('Tarefa excluída!')
        sleep(1.5)


def Sair():
    resposta = str(input('Tem certeza que deseja sair? [\033[32mS\033[m/\033[31mN\033[m]: '))
    while resposta not in 'SsNn':
        print('\033[31mERRO!\033[m Resposta Inválida.')
        sleep(1.5)
        resposta = str(input('Tem certeza que deseja sair? [\033[32mS\033[m/\033[31mN\033[m]: '))

    if resposta in 'Ss':
        print('Saindo...')
        sleep(1.5)
        print('Volte Sempre!')
        exit()

    if resposta in 'Nn':
        print('Carregando...')
        sleep(1.5)


"""def programa():
    Titulo()

    while True:
        resposta_menu = menu()
        if resposta_menu == 1:
            AdicionarTarefa()

        elif resposta_menu == 2:
            ExibirTarefas()

        elif resposta_menu == 3:
            MarcarComoConcluida()

        elif resposta_menu == 4:
            ExcluirTarefa()

        elif resposta_menu == 5:
            Sair()


programa()"""


# Primeiro Botão - Configurações
def JanelaAdicionarTarefa():
    # Configurações da Janela
    global adicionar_tarefa_janela
    adicionar_tarefa_janela = Tk()
    adicionar_tarefa_janela.title('Adicionar Tarefa')
    adicionar_tarefa_janela.config(background="#262A40")
    adicionar_tarefa_janela.geometry('300x200')
    adicionar_tarefa_janela.resizable(False, False)

    # Adicionando o texto da janela
    adicionar_tarefa_texto1 = Label(adicionar_tarefa_janela, text='Adicionar nome e', font="Arial 15 bold",
                                    bg="#262A40", fg="#F2F2F2")
    adicionar_tarefa_texto2 = Label(adicionar_tarefa_janela, text='descrição da tarefa', font="Arial 15 bold",
                                    bg="#262A40", fg="#F2F2F2")
    adicionar_tarefa_texto1.place(x=64, y=10)
    adicionar_tarefa_texto2.place(x=55, y=35)

    # Escrever a primeira Entry
    global escrever_nome
    escrever_nome = Entry(adicionar_tarefa_janela, width=35)
    escrever_nome.place(x=45, y=80)
    escrever_nome.insert(0, 'Nome:')

    # Escrever a segunda Entry
    global escrever_desc
    escrever_desc = Entry(adicionar_tarefa_janela, width=35)
    escrever_desc.place(x=45, y=110)
    escrever_desc.insert(0, 'Descrição:')

    # Botão enviar
    botao_enviar = Button(adicionar_tarefa_janela, text='Enviar', height=1, width=5, command=Enviar_Tarefa)
    botao_enviar.place(x=125, y=150)


#Envio de Tarefas para as listas e fim da janela
def Enviar_Tarefa():
    enviar_desc = escrever_desc.get()
    enviar_nome = escrever_nome.get()

    if enviar_desc == '' or enviar_nome == '':
        messagebox.showerror("Erro", "Por favor, insira um nome e uma descrição para a tarefa.")
        escrever_nome.focus_force()

    else:
        escrever_nome.delete(0, 'end')
        escrever_desc.delete(0, 'end')

        # Enviando as respostas das Entrys para as listas
        descricao_tarefas.append(enviar_desc)
        nome_tarefas.append(enviar_nome)

        # Alerta da tarefa e exlusão da imagem
        messagebox.showinfo('Alerta!', 'Sua tarefa e descrição foram enviados!')
        escrever_desc.focus_force()
        adicionar_tarefa_janela.destroy()


# Janela de Tarefas Configurações
janela = Tk()
janela.title('Gerenciamento de Tarefas')
janela.geometry('500x450')
janela.config(background="#262A40")
janela.resizable(False, False)

# Texto Inicial
titulo = Label(janela, text='Sistema de Gerenciamento', font="Arial 20 bold", bg="#262A40", fg="#F2F2F2")
titulo.place(x=75, y=15)

titulo1 = Label(janela, text='de Tarefas', font="Arial 20 bold", bg="#262A40", fg="#F2F2F2")
titulo1.place(x=180, y=50)

# Primeiro Botão
adicionar_tarefa_botao = Button(janela, text="Adicionar Tarefa", bg="#416CA6", fg="#0E1521", activebackground="#85BFF2",
                                activeforeground="black", font="Arial 12 bold", height=2, width=36,
                                command=JanelaAdicionarTarefa)
adicionar_tarefa_botao.place(x=70, y=115)

# Segundo Botão
exibir_tarefa_botao = Button(janela, text='Exibir Tarefas', bg="#416CA6", fg="#0E1521", activebackground="#85BFF2",
                             activeforeground="black", font="Arial 12 bold", height=2, width=36, command=ExibirTarefas)
exibir_tarefa_botao.place(x=70, y=195)

# Terceiro Botão
marcar_como_concluida_botao = Button(janela, text='Marcar Como Concluída', bg="#416CA6", fg="#0E1521",
                                     font="Arial 12 bold", height=2, width=36, activebackground="#85BFF2",
                                     activeforeground="black", command=MarcarComoConcluida)
marcar_como_concluida_botao.place(x=70, y=275)

# Quarto Botão
excluir_tarefa_botao = Button(janela, text='Excluir Tarefa', bg="#416CA6", fg="#202336", font="Arial 12 bold", height=2,
                              width=36, activebackground="black", activeforeground="#0D2673", command=ExcluirTarefa)
excluir_tarefa_botao.place(x=70, y=355)

janela.mainloop()
