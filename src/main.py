from GerenciadorTarefas import GerenciadorTarefas
from InterfaceTarefa import InterfaceTarefa

if __name__ == "__main__":
    gerenciador = GerenciadorTarefas("assets/Tarefas/Tarefas.txt")
    InterfaceTarefa(gerenciador)
