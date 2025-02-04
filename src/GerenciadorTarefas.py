from Tarefa import tarefa

def arquivoExiste(nomeArquivo):
    try:
        with open(nomeArquivo, 'r'):
            return True
    except FileNotFoundError:
        return False

def criarArquivo(nomeArquivo):
    try:
        with open(nomeArquivo, 'w') as arquivo:
            arquivo.write('')
    except IOError:
        print(f"Erro ao criar o arquivo '{nomeArquivo}'.")

class gerenciadorTarefas:
    def __init__(self, arquivo):
        self.arquivo = arquivo
        self.tarefas = []
        if not arquivoExiste(arquivo):
            criarArquivo(arquivo)
        self.carregarTarefas()

    def carregarTarefas(self):
        try:
            with open(self.arquivo, 'r') as arquivoTarefas:
                for linha in arquivoTarefas:
                    nome, descricao, concluida = linha.strip().split('|')
                    tarefaObj = tarefa(nome, descricao)
                    tarefaObj.concluida = concluida == 'True'
                    self.tarefas.append(tarefaObj)
        except FileNotFoundError:
            print(f"O arquivo '{self.arquivo}' não foi encontrado.")

    def salvarTarefas(self):
        try:
            with open(self.arquivo, 'w') as arquivoTarefas:
                for tarefaObj in self.tarefas:
                    arquivoTarefas.write(f"{tarefaObj.nome}|{tarefaObj.descricao}|{tarefaObj.concluida}\n")
        except IOError:
            print(f"Erro ao salvar as tarefas no arquivo '{self.arquivo}'.")

    def adicionarTarefa(self, nome, descricao):
        self.tarefas.append(tarefa(nome, descricao))
        self.salvarTarefas()

    def excluirTarefa(self, indice):
        if 0 <= indice < len(self.tarefas):
            del self.tarefas[indice]
            self.salvarTarefas()

    def marcarConcluida(self, indice):
        if 0 <= indice < len(self.tarefas):
            self.tarefas[indice].marcarConcluida()
            self.salvarTarefas()
