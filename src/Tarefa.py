class tarefa:
    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao
        self.concluida = False

    def marcarConcluida(self):
        self.concluida = True
