from GerenciadorTarefas import gerenciadorTarefas
from InterfaceTarefa import interfaceTarefa

if __name__ == "__main__":
    gerenciador = gerenciadorTarefas("assets/Tarefas/Tarefas.txt")
    interfaceTarefa(gerenciador)
