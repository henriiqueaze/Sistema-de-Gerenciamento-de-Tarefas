import os
from Tarefa import tarefa

def arquivoExiste(nomeArquivo):
    return os.path.isfile(nomeArquivo)

def criarArquivo(nomeArquivo):
    try:
        pasta = os.path.dirname(nomeArquivo)
        if pasta and not os.path.exists(pasta):
            os.makedirs(pasta, exist_ok=True)  
        with open(nomeArquivo, 'w', encoding='utf-8') as f:
            pass
        print(f"Arquivo criado/garantido em: {os.path.abspath(nomeArquivo)}")
        return True
    except Exception as e:
        print(f"Erro ao criar o arquivo '{nomeArquivo}': {e}")
        return False

class gerenciadorTarefas:
    def __init__(self, arquivo):
        self.arquivo = arquivo
        self.tarefas = []
        if not arquivoExiste(arquivo):
            criarArquivo(arquivo)
        self.carregarTarefas()

    def carregarTarefas(self):
        try:
            with open(self.arquivo, 'r', encoding='utf-8') as arquivoTarefas:
                for linha in arquivoTarefas:
                    linha = linha.strip()
                    if not linha:
                        continue 
                    parts = linha.split('|')
                    if len(parts) != 3:
                        print(f"Linha inválida no arquivo (pulando): {linha}")
                        continue
                    nome, descricao, concluida = parts
                    tarefaObj = tarefa(nome, descricao)
                    tarefaObj.concluida = (concluida == 'True')
                    self.tarefas.append(tarefaObj)
        except FileNotFoundError:
            print(f"O arquivo '{self.arquivo}' não foi encontrado.")
        except Exception as e:
            print(f"Erro ao ler o arquivo '{self.arquivo}': {e}")

    def salvarTarefas(self):
        try:
            with open(self.arquivo, 'w', encoding='utf-8') as arquivoTarefas:
                for tarefaObj in self.tarefas:
                    arquivoTarefas.write(f"{tarefaObj.nome}|{tarefaObj.descricao}|{tarefaObj.concluida}\n")
        except IOError as e:
            print(f"Erro ao salvar as tarefas no arquivo '{self.arquivo}': {e}")

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
