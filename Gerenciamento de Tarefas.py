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


def TarefaNaoAdicionada():
    print('Nenhuma tarefa foi adicionada ainda.')
    sleep(1.5)


def Mostrar_Tarefas():
    for numerar, tarefa in enumerate(nome_tarefas):
        print(f'[{numerar + 1}] - {tarefa}')


def menu():
    print('[1] - Adicionar Tarefa\n[2] - Exibir Tarefas\n[3] - Marcar como Concluída\n'
          '[4] - Excluir Tarefa\n[5] - Sair')
    resposta = int(input('Digite sua opção: '))

    while resposta < 1 or resposta > 5:
        print('\033[31mERRO!\033[m Resposta Inválida.')
        sleep(1.5)
        resposta = int(input('Digite sua opção: '))

    return resposta


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
        ver_tarefas = str(input('Deseja ver a descrição de alguma tarefa? [\033[32mS\033[m/\033[31mN\033[m]:'))

        while ver_tarefas not in 'SsNn':
            print('\033[31mERRO!\033[m Resposta Inválida.')
            sleep(1.5)
            ver_tarefas = str(input('Deseja ver a descrição de alguma tarefa? [\033[32mS\033[m/\033[31mN\033[m]:'))

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


def programa():
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


programa()
