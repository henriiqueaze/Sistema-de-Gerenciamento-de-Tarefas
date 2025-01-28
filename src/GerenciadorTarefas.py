from Tarefa import Tarefa

def Arquivo_Existe(nome_arquivo):
    try:
        with open(nome_arquivo, 'r'):
            return True
    except FileNotFoundError:
        return False

def Criar_Arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'w') as arquivo:
            arquivo.write('')
    except IOError:
        print(f"Erro ao criar o arquivo '{nome_arquivo}'.")

class GerenciadorTarefas:
    def __init__(self, arquivo):
        self.arquivo = arquivo
        self.tarefas = []
        if not Arquivo_Existe(arquivo):
            Criar_Arquivo(arquivo)
        self.carregar_tarefas()

    def carregar_tarefas(self):
        try:
            with open(self.arquivo, 'r') as arquivo_tarefas:
                for linha in arquivo_tarefas:
                    nome, descricao, concluida = linha.strip().split('|')
                    tarefa = Tarefa(nome, descricao)
                    tarefa.concluida = concluida == 'True'
                    self.tarefas.append(tarefa)
        except FileNotFoundError:
            print(f"O arquivo '{self.arquivo}' não foi encontrado.")

    def salvar_tarefas(self):
        try:
            with open(self.arquivo, 'w') as arquivo_tarefas:
                for tarefa in self.tarefas:
                    arquivo_tarefas.write(f"{tarefa.nome}|{tarefa.descricao}|{tarefa.concluida}\n")
        except IOError:
            print(f"Erro ao salvar as tarefas no arquivo '{self.arquivo}'.")

    def adicionar_tarefa(self, nome, descricao):
        self.tarefas.append(Tarefa(nome, descricao))
        self.salvar_tarefas()

    def excluir_tarefa(self, indice):
        if 0 <= indice < len(self.tarefas):
            del self.tarefas[indice]
            self.salvar_tarefas()

    def marcar_concluida(self, indice):
        if 0 <= indice < len(self.tarefas):
            self.tarefas[indice].marcar_concluida()
            self.salvar_tarefas()
