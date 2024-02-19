from time import sleep

nome_tarefa = list()
descricao_tarefa = list()


def title():
    titulo = 'Sistema de Gerenciamento de Tarefas'
    tamanho = len(titulo) + 5
    print('=' * tamanho)
    print(titulo.center(tamanho))
    print('=' * tamanho)
    sleep(1.5)


def programa():
    title()

    while True:
        resposta = int(input('[1] - Adicionar tarefa\n[2] - Exibir tarefas\n[3] - Marcar como concluída\n'
                             '[4] - Excluir tarefa\n[5] - Sair do Programa\n'))

        if resposta == 1:
            nome_tarefa.append(str(input('Digite o nome da tarefa: ')))
            descricao_tarefa.append(str(input('Faça uma descrição sobre a tarefa: ')))
            print('Processando...')
            sleep(1.5)

        if resposta == 2:

            if not nome_tarefa:
                print('Você ainda não adicionou nenhuma tarefa')
                sleep(1.5)

            else:
                for numero, numerar in enumerate(nome_tarefa):
                    print(f'[{numero + 1}] - {numerar}')

                ver_tarefa = int(input('Deseja ver a descrição de que tarefa? ')) - 1
                print('Descrição:')
                print(descricao_tarefa[ver_tarefa])
                sleep(3)

        if resposta == 3:

            if not nome_tarefa:
                print('Você ainda não adicionou nenhuma tarefa')
                sleep(3)

            else:
                for numero, numerar in enumerate(nome_tarefa):
                    print(f'[{numero + 1}] - {numerar}')

                marcar_tarefa = int(input('Qual tarefa você deseja marcar como concluída? ')) - 1
                nome_tarefa[marcar_tarefa] = ''.join(c + '\u0336' for c in nome_tarefa[marcar_tarefa])

                print('Processando...')
                sleep(1)
                print('Tarefa Marcada como Concluída!')
                sleep(1)

        if resposta == 4:

            if not nome_tarefa:
                print('Você ainda não adicionou nenhuma tarefa')
                sleep(1.5)

            else:

                for numero, numerar in enumerate(nome_tarefa):
                    print(f'[{numero + 1}] - {numerar}')

                deletar_tarefa = int(input('Qual tarefa você deseja excluir? ')) - 1
                nome_tarefa.pop(deletar_tarefa)
                descricao_tarefa.pop(deletar_tarefa)
                print('Processando...')
                sleep(1)
                print('Tarefa Excluída!')
                sleep(1)

        if resposta == 5:
            print('Saindo...')
            sleep(1.5)
            break


programa()
