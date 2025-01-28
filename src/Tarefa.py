class Tarefa:
    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao
        self.concluida = False

    def marcar_concluida(self):
        self.concluida = True
