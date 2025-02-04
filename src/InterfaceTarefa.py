import tkinter as tk
from tkinter import messagebox

class interfaceTarefa:
    def __init__(self, gerenciador):
        self.gerenciador = gerenciador
        self.janela = tk.Tk()
        self.janela.title('Gerenciamento de Tarefas')
        self.janela.geometry('500x450')
        self.janela.config(background="#262A40")
        self.janela.resizable(False, False)
        self.configurarInterface()
        self.janela.mainloop()

    def configurarInterface(self):
        titulo = tk.Label(self.janela, text='Sistema de Gerenciamento', font="Arial 20 bold", bg="#262A40", fg="#F2F2F2")
        titulo.place(x=75, y=15)
        titulo1 = tk.Label(self.janela, text='de Tarefas', font="Arial 20 bold", bg="#262A40", fg="#F2F2F2")
        titulo1.place(x=180, y=50)

        botoes = [
            ("Adicionar Tarefa", self.janelaAdicionarTarefa, 115),
            ("Exibir Tarefas", self.janelaExibirTarefa, 195),
            ("Marcar Como Concluída", self.janelaMarcarConcluida, 275),
            ("Excluir Tarefa", self.janelaExcluirTarefa, 355)
        ]

        for texto, comando, yPos in botoes:
            tk.Button(
                self.janela, text=texto, bg="#416CA6", fg="#0E1521", activebackground="#85BFF2",
                activeforeground="black", font="Arial 12 bold", height=2, width=36, command=comando
            ).place(x=70, y=yPos)

    def criarJanelaTarefa(self, titulo, placeholder, callback):
        janela = tk.Toplevel(self.janela)
        janela.title(titulo)
        janela.config(background="#262A40")
        janela.geometry('300x200')
        janela.resizable(False, False)

        tk.Label(janela, text='Adicionar nome e', font="Arial 15 bold", bg="#262A40", fg="#F2F2F2").place(x=64, y=10)
        tk.Label(janela, text='descrição da tarefa', font="Arial 15 bold", bg="#262A40", fg="#F2F2F2").place(x=55, y=35)

        campos = {}
        for i, (label, yPos) in enumerate([(placeholder[0], 80), (placeholder[1], 110)]):
            entry = tk.Entry(janela, width=35, fg="#808080")
            entry.place(x=45, y=yPos)
            entry.insert(0, label)
            entry.bind("<FocusIn>", lambda e, entry=entry, text=label: self.onFocusIn(entry, text))
            entry.bind("<FocusOut>", lambda e, entry=entry, text=label: self.onFocusOut(entry, text))
            campos[label] = entry

        def enviar():
            valores = {k: v.get() for k, v in campos.items()}
            if any(valores[k] == k for k in valores):
                messagebox.showerror("Erro", "Por favor, preencha todos os campos corretamente.")
                return
            callback(valores)
            messagebox.showinfo('Alerta!', 'Operação realizada com sucesso!')
            janela.destroy()

        tk.Button(
            janela, text='Enviar', bg="#416CA6", fg="#0E1521", activebackground="#85BFF2",
            activeforeground="black", font="Arial 10 bold", height=1, width=15, command=enviar
        ).place(x=85, y=150)

    def janelaAdicionarTarefa(self):
        self.criarJanelaTarefa(
            'Adicionar Tarefa',
            ('Nome:', 'Descrição:'),
            lambda valores: self.gerenciador.adicionarTarefa(valores['Nome:'], valores['Descrição:'])
        )

    def janelaExibirTarefa(self):
        self.exibirTarefas('Exibir Tarefa')

    def janelaMarcarConcluida(self):
        self.exibirTarefas('Marcar Como Concluída', self.gerenciador.marcarConcluida)

    def janelaExcluirTarefa(self):
        self.exibirTarefas('Excluir Tarefa', self.gerenciador.excluirTarefa)

    def exibirTarefas(self, titulo, callback=None):
        if not self.gerenciador.tarefas:
            messagebox.showinfo('Alerta!', 'Nenhuma tarefa foi adicionada.')
            return

        janela = tk.Toplevel(self.janela)
        janela.title(titulo)
        janela.config(background="#262A40")
        janela.geometry('300x200')
        janela.resizable(False, False)

        tk.Label(janela, text='Tarefas:          Descrição:', bg='#262A40', fg='white', font='Arial 15 bold').place(x=27, y=25)

        tarefasText = ''
        descricoesText = ''
        for i, tarefaObj in enumerate(self.gerenciador.tarefas):
            nomeText = ''.join(c + '\u0336' for c in tarefaObj.nome) if tarefaObj.concluida else tarefaObj.nome
            descricaoText = ''.join(c + '\u0336' for c in tarefaObj.descricao) if tarefaObj.concluida else tarefaObj.descricao
            tarefasText += f"{i + 1}. {nomeText}\n"
            descricoesText += f"{descricaoText}\n"

        tk.Label(janela, text=tarefasText, bg='#262A40', fg='white', font='Arial 12 bold').place(x=38, y=63)
        tk.Label(janela, text=descricoesText, bg='#262A40', fg='white', font='Arial 12 bold').place(x=175, y=63)

        if callback:
            numeroEntry = tk.Entry(janela, width=20, fg="#808080")
            numeroEntry.place(x=87, y=130)
            numeroEntry.insert(0, 'Número da Tarefa:')

            numeroEntry.bind("<FocusIn>", lambda e: self.onFocusIn(numeroEntry, 'Número da Tarefa:'))
            numeroEntry.bind("<FocusOut>", lambda e: self.onFocusOut(numeroEntry, 'Número da Tarefa:'))

            def enviar():
                try:
                    indice = int(numeroEntry.get()) - 1
                    callback(indice)
                    messagebox.showinfo('Alerta!', 'Operação realizada com sucesso!')
                    janela.destroy()
                except (ValueError, IndexError):
                    messagebox.showerror('Erro', 'Por favor, insira um número válido relacionado à tarefa.')

            tk.Button(
                janela, text='Enviar', bg="#416CA6", fg="#0E1521", activebackground="#85BFF2",
                activeforeground="black", font="Arial 10 bold", height=1, width=15, command=enviar
            ).place(x=85, y=161)

    def onFocusIn(self, entry, placeholder):
        if entry.get() == placeholder:
            entry.delete(0, tk.END)
            entry.config(fg="black")

    def onFocusOut(self, entry, placeholder):
        if entry.get() == "":
            entry.insert(0, placeholder)
            entry.config(fg="#808080")
