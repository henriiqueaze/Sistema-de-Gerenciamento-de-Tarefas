import tkinter as tk
from tkinter import messagebox

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

        botoes = [
            ("Adicionar Tarefa", self.janela_adicionar_tarefa, 115),
            ("Exibir Tarefas", self.janela_exibir_tarefa, 195),
            ("Marcar Como Concluída", self.janela_marcar_concluida, 275),
            ("Excluir Tarefa", self.janela_excluir_tarefa, 355)
        ]

        for texto, comando, y in botoes:
            tk.Button(
                self.janela, text=texto, bg="#416CA6", fg="#0E1521", activebackground="#85BFF2",
                activeforeground="black", font="Arial 12 bold", height=2, width=36, command=comando
            ).place(x=70, y=y)

    def criar_janela_tarefa(self, titulo, placeholder, callback):
        janela = tk.Toplevel(self.janela)
        janela.title(titulo)
        janela.config(background="#262A40")
        janela.geometry('300x200')
        janela.resizable(False, False)

        tk.Label(janela, text='Adicionar nome e', font="Arial 15 bold", bg="#262A40", fg="#F2F2F2").place(x=64, y=10)
        tk.Label(janela, text='descrição da tarefa', font="Arial 15 bold", bg="#262A40", fg="#F2F2F2").place(x=55, y=35)

        campos = {}
        for i, (label, y) in enumerate([(placeholder[0], 80), (placeholder[1], 110)]):
            entry = tk.Entry(janela, width=35, fg="#808080")
            entry.place(x=45, y=y)
            entry.insert(0, label)
            entry.bind("<FocusIn>", lambda e, entry=entry, text=label: self.on_focus_in(entry, text))
            entry.bind("<FocusOut>", lambda e, entry=entry, text=label: self.on_focus_out(entry, text))
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

    def janela_adicionar_tarefa(self):
        self.criar_janela_tarefa(
            'Adicionar Tarefa',
            ('Nome:', 'Descrição:'),
            lambda valores: self.gerenciador.adicionar_tarefa(valores['Nome:'], valores['Descrição:'])
        )

    def janela_exibir_tarefa(self):
        self.exibir_tarefas('Exibir Tarefa')

    def janela_marcar_concluida(self):
        self.exibir_tarefas('Marcar Como Concluída', self.gerenciador.marcar_concluida)

    def janela_excluir_tarefa(self):
        self.exibir_tarefas('Excluir Tarefa', self.gerenciador.excluir_tarefa)

    def exibir_tarefas(self, titulo, callback=None):
        if not self.gerenciador.tarefas:
            messagebox.showinfo('Alerta!', 'Nenhuma tarefa foi adicionada.')
            return

        janela = tk.Toplevel(self.janela)
        janela.title(titulo)
        janela.config(background="#262A40")
        janela.geometry('300x200')
        janela.resizable(False, False)

        tk.Label(janela, text='Tarefas:          Descrição:', bg='#262A40', fg='white', font='Arial 15 bold').place(x=27, y=25)

        tarefas, descricoes = '', ''
        for i, tarefa in enumerate(self.gerenciador.tarefas):
            nome = ''.join(c + '\u0336' for c in tarefa.nome) if tarefa.concluida else tarefa.nome
            descricao = ''.join(c + '\u0336' for c in tarefa.descricao) if tarefa.concluida else tarefa.descricao
            tarefas += f"{i + 1}. {nome}\n"
            descricoes += f"{descricao}\n"

        tk.Label(janela, text=tarefas, bg='#262A40', fg='white', font='Arial 12 bold').place(x=38, y=63)
        tk.Label(janela, text=descricoes, bg='#262A40', fg='white', font='Arial 12 bold').place(x=175, y=63)

        if callback:
            numero_entry = tk.Entry(janela, width=20, fg="#808080")
            numero_entry.place(x=87, y=130)
            numero_entry.insert(0, 'Número da Tarefa:')

            numero_entry.bind("<FocusIn>", lambda e: self.on_focus_in(numero_entry, 'Número da Tarefa:'))
            numero_entry.bind("<FocusOut>", lambda e: self.on_focus_out(numero_entry, 'Número da Tarefa:'))

            def enviar():
                try:
                    indice = int(numero_entry.get()) - 1
                    callback(indice)
                    messagebox.showinfo('Alerta!', 'Operação realizada com sucesso!')
                    janela.destroy()
                except (ValueError, IndexError):
                    messagebox.showerror('Erro', 'Por favor, insira um número válido relacionado à tarefa.')

            tk.Button(
                janela, text='Enviar', bg="#416CA6", fg="#0E1521", activebackground="#85BFF2",
                activeforeground="black", font="Arial 10 bold", height=1, width=15, command=enviar
            ).place(x=85, y=161)

    def on_focus_in(self, entry, placeholder):
        if entry.get() == placeholder:
            entry.delete(0, tk.END)
            entry.config(fg="black")

    def on_focus_out(self, entry, placeholder):
        if entry.get() == "":
            entry.insert(0, placeholder)
            entry.config(fg="#808080")
