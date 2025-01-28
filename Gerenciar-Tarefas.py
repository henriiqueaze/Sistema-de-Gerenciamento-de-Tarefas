import tkinter as tk
from tkinter import messagebox

class Tarefa:
    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao
        self.concluida = False

    def marcar_concluida(self):
        self.concluida = True

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

class InterfaceTarefa:
    def __init__(self, gerenciador):
        self.gerenciador = gerenciador
        self.janela = tk.Tk()
        self.janela.title('Gerenciamento de Tarefas')
        self.janela.geometry('500x450')
        self.janela.config(background="#262A40")
        self.janela.resizable(False, False)
        self.configurar_interface()
        self.janela.mainloop()

    def configurar_interface(self):
        titulo = tk.Label(self.janela, text='Sistema de Gerenciamento', font="Arial 20 bold", bg="#262A40", fg="#F2F2F2")
        titulo.place(x=75, y=15)
        titulo1 = tk.Label(self.janela, text='de Tarefas', font="Arial 20 bold", bg="#262A40", fg="#F2F2F2")
        titulo1.place(x=180, y=50)

        botao_adicionar = tk.Button(self.janela, text="Adicionar Tarefa", bg="#416CA6", fg="#0E1521", activebackground="#85BFF2",
                                     activeforeground="black", font="Arial 12 bold", height=2, width=36, command=self.janela_adicionar_tarefa)
        botao_adicionar.place(x=70, y=115)

        botao_exibir = tk.Button(self.janela, text='Exibir Tarefas', bg="#416CA6", fg="#0E1521", activebackground="#85BFF2",
                                  activeforeground="black", font="Arial 12 bold", height=2, width=36, command=self.janela_exibir_tarefa)
        botao_exibir.place(x=70, y=195)

        botao_marcar = tk.Button(self.janela, text='Marcar Como Concluída', bg="#416CA6", fg="#0E1521",
                                  font="Arial 12 bold", height=2, width=36, activebackground="#85BFF2",
                                  activeforeground="black", command=self.janela_marcar_concluida)
        botao_marcar.place(x=70, y=275)

        botao_excluir = tk.Button(self.janela, text='Excluir Tarefa', bg="#416CA6", fg="#0E1521", font="Arial 12 bold",
                                   height=2, width=36, activebackground="#85BFF2", activeforeground="black",
                                   command=self.janela_excluir_tarefa)
        botao_excluir.place(x=70, y=355)

    def on_focus_in(self, entry, placeholder):
        if entry.get() == placeholder:
            entry.delete(0, tk.END)
            entry.config(fg="black")

    def on_focus_out(self, entry, placeholder):
        if entry.get() == "":
            entry.insert(0, placeholder)
            entry.config(fg="#808080")

    def janela_adicionar_tarefa(self):
        janela = tk.Toplevel(self.janela)
        janela.title('Adicionar Tarefa')
        janela.config(background="#262A40")
        janela.geometry('300x200')
        janela.resizable(False, False)

        tk.Label(janela, text='Adicionar nome e', font="Arial 15 bold", bg="#262A40", fg="#F2F2F2").place(x=64, y=10)
        tk.Label(janela, text='descrição da tarefa', font="Arial 15 bold", bg="#262A40", fg="#F2F2F2").place(x=55, y=35)

        nome_entry = tk.Entry(janela, width=35, fg="#808080")
        nome_entry.place(x=45, y=80)
        nome_entry.insert(0, 'Nome:')

        descricao_entry = tk.Entry(janela, width=35, fg="#808080")
        descricao_entry.place(x=45, y=110)
        descricao_entry.insert(0, 'Descrição:')

        nome_entry.bind("<FocusIn>", lambda e: self.on_focus_in(nome_entry, 'Nome:'))
        nome_entry.bind("<FocusOut>", lambda e: self.on_focus_out(nome_entry, 'Nome:'))

        descricao_entry.bind("<FocusIn>", lambda e: self.on_focus_in(descricao_entry, 'Descrição:'))
        descricao_entry.bind("<FocusOut>", lambda e: self.on_focus_out(descricao_entry, 'Descrição:'))

        def enviar():
            nome = nome_entry.get()
            descricao = descricao_entry.get()
            if not nome or nome == 'Nome:' or not descricao or descricao == 'Descrição:':
                messagebox.showerror("Erro", "Por favor, insira um nome e uma descrição para a tarefa.")
                return
            self.gerenciador.adicionar_tarefa(nome, descricao)
            messagebox.showinfo('Alerta!', 'Sua tarefa e descrição foram enviados!')
            janela.destroy()

        tk.Button(janela, text='Enviar', height=1, width=5, command=enviar).place(x=125, y=150)

    def janela_exibir_tarefa(self):
        if not self.gerenciador.tarefas:
            messagebox.showinfo('Alerta!', 'Nenhuma tarefa foi adicionada.')
            return

        janela = tk.Toplevel(self.janela)
        janela.title('Exibir Tarefa')
        janela.config(background="#262A40")
        janela.geometry('300x200')
        janela.resizable(False, False)

        tk.Label(janela, text='Tarefas:          Descrição:', bg='#262A40', fg='white', font='Arial 15 bold').place(x=27, y=25)

        tarefas = ''
        descricoes = ''
        for i, tarefa in enumerate(self.gerenciador.tarefas):
            nome = ''.join(c + '\u0336' for c in tarefa.nome) if tarefa.concluida else tarefa.nome
            descricao = ''.join(c + '\u0336' for c in tarefa.descricao) if tarefa.concluida else tarefa.descricao
            tarefas += f"{i + 1}. {nome}\n"
            descricoes += f"{descricao}\n"

        tk.Label(janela, text=tarefas, bg='#262A40', fg='white', font='Arial 12 bold').place(x=38, y=63)
        tk.Label(janela, text=descricoes, bg='#262A40', fg='white', font='Arial 12 bold').place(x=175, y=63)

    def janela_marcar_concluida(self):
        if not self.gerenciador.tarefas:
            messagebox.showinfo('Alerta!', 'Nenhuma tarefa foi adicionada.')
            return

        janela = tk.Toplevel(self.janela)
        janela.title('Marcar Como Concluída')
        janela.config(background="#262A40")
        janela.geometry('300x200')
        janela.resizable(False, False)

        tk.Label(janela, text='Tarefas:          Descrição:', bg='#262A40', fg='white', font='Arial 15 bold').place(x=27, y=25)

        tarefas = ''
        descricoes = ''
        for i, tarefa in enumerate(self.gerenciador.tarefas):
            nome = ''.join(c + '\u0336' for c in tarefa.nome) if tarefa.concluida else tarefa.nome
            descricao = ''.join(c + '\u0336' for c in tarefa.descricao) if tarefa.concluida else tarefa.descricao
            tarefas += f"{i + 1}. {nome}\n"
            descricoes += f"{descricao}\n"

        tk.Label(janela, text=tarefas, bg='#262A40', fg='white', font='Arial 12 bold').place(x=38, y=63)
        tk.Label(janela, text=descricoes, bg='#262A40', fg='white', font='Arial 12 bold').place(x=175, y=63)

        numero_entry = tk.Entry(janela, width=20, fg="#808080")
        numero_entry.place(x=85, y=141)
        numero_entry.insert(0, 'Número da Tarefa:')

        numero_entry.bind("<FocusIn>", lambda e: self.on_focus_in(numero_entry, 'Número da Tarefa:'))
        numero_entry.bind("<FocusOut>", lambda e: self.on_focus_out(numero_entry, 'Número da Tarefa:'))

        def enviar():
            try:
                indice = int(numero_entry.get()) - 1
                self.gerenciador.marcar_concluida(indice)
                messagebox.showinfo('Alerta!', 'Sua tarefa foi marcada como concluída!')
                janela.destroy()
            except (ValueError, IndexError):
                messagebox.showerror('Erro', 'Por favor, insira um número válido relacionado à tarefa.')

        tk.Button(janela, text='Enviar', height=1, width=5, command=enviar).place(x=120, y=161)

    def janela_excluir_tarefa(self):
        if not self.gerenciador.tarefas:
            messagebox.showinfo('Alerta!', 'Nenhuma tarefa foi adicionada.')
            return

        janela = tk.Toplevel(self.janela)
        janela.title('Excluir Tarefa')
        janela.config(background="#262A40")
        janela.geometry('300x200')
        janela.resizable(False, False)

        tk.Label(janela, text='Tarefas:          Descrição:', bg='#262A40', fg='white', font='Arial 15 bold').place(x=27, y=25)

        tarefas = ''
        descricoes = ''
        for i, tarefa in enumerate(self.gerenciador.tarefas):
            nome = ''.join(c + '\u0336' for c in tarefa.nome) if tarefa.concluida else tarefa.nome
            descricao = ''.join(c + '\u0336' for c in tarefa.descricao) if tarefa.concluida else tarefa.descricao
            tarefas += f"{i + 1}. {nome}\n"
            descricoes += f"{descricao}\n"

        tk.Label(janela, text=tarefas, bg='#262A40', fg='white', font='Arial 12 bold').place(x=38, y=63)
        tk.Label(janela, text=descricoes, bg='#262A40', fg='white', font='Arial 12 bold').place(x=175, y=63)

        numero_entry = tk.Entry(janela, width=20, fg="#808080")
        numero_entry.place(x=85, y=141)
        numero_entry.insert(0, 'Número da Tarefa:')

        numero_entry.bind("<FocusIn>", lambda e: self.on_focus_in(numero_entry, 'Número da Tarefa:'))
        numero_entry.bind("<FocusOut>", lambda e: self.on_focus_out(numero_entry, 'Número da Tarefa:'))

        def enviar():
            try:
                indice = int(numero_entry.get()) - 1
                self.gerenciador.excluir_tarefa(indice)
                messagebox.showinfo('Alerta!', 'Sua tarefa foi excluída com sucesso!')
                janela.destroy()
            except (ValueError, IndexError):
                messagebox.showerror('Erro', 'Por favor, insira um número válido relacionado à tarefa.')

        tk.Button(janela, text='Enviar', height=1, width=5, command=enviar).place(x=120, y=161)

if __name__ == "__main__":
    gerenciador = GerenciadorTarefas("/assets/Tarefas/Tarefas.txt")
    InterfaceTarefa(gerenciador)
