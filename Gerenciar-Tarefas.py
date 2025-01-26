import tkinter as tk
from tkinter import messagebox

class TaskManager:
    def __init__(self):
        self.file_name = 'tarefas.txt'
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.file_name, 'r') as file:
                for line in file:
                    name, description = line.strip().split('|')
                    self.tasks.append(Task(name, description))
        except FileNotFoundError:
            with open(self.file_name, 'w'):
                pass

    def save_tasks(self):
        try:
            with open(self.file_name, 'w') as file:
                for task in self.tasks:
                    file.write(f"{task.name}|{task.description}\n")
        except IOError:
            print(f"Erro ao salvar as tarefas no arquivo '{self.file_name}'.")

    def add_task(self, name, description):
        self.tasks.append(Task(name, description))
        self.save_tasks()

    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()
            self.save_tasks()

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            self.save_tasks()


class Task:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.name = ''.join(c + '\u0336' for c in self.name)
        self.description = ''.join(c + '\u0336' for c in self.description)
        self.completed = True


class TaskApp:
    def __init__(self, root):
        self.manager = TaskManager()
        self.root = root
        self.root.title('Gerenciamento de Tarefas')
        self.root.geometry('500x450')
        self.root.config(background="#262A40")
        self.root.resizable(False, False)

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text='Sistema de Gerenciamento', font="Arial 20 bold", bg="#262A40", fg="#F2F2F2").place(x=75, y=15)
        tk.Label(self.root, text='de Tarefas', font="Arial 20 bold", bg="#262A40", fg="#F2F2F2").place(x=180, y=50)

        tk.Button(self.root, text="Adicionar Tarefa", bg="#416CA6", fg="#0E1521", activebackground="#85BFF2",
                  activeforeground="black", font="Arial 12 bold", height=2, width=36, command=self.open_add_task_window).place(x=70, y=115)

        tk.Button(self.root, text='Exibir Tarefas', bg="#416CA6", fg="#0E1521", activebackground="#85BFF2",
                  activeforeground="black", font="Arial 12 bold", height=2, width=36, command=self.open_view_tasks_window).place(x=70, y=195)

        tk.Button(self.root, text='Marcar Como Concluída', bg="#416CA6", fg="#0E1521",
                  font="Arial 12 bold", height=2, width=36, activebackground="#85BFF2",
                  activeforeground="black", command=self.open_mark_completed_window).place(x=70, y=275)

        tk.Button(self.root, text='Excluir Tarefa', bg="#416CA6", fg="#0E1521", font="Arial 12 bold",
                  height=2, width=36, activebackground="#85BFF2", activeforeground="black",
                  command=self.open_delete_task_window).place(x=70, y=355)

    def open_add_task_window(self):
        add_task_window = tk.Toplevel(self.root)
        add_task_window.title('Adicionar Tarefa')
        add_task_window.geometry('300x200')
        add_task_window.config(background="#262A40")

        tk.Label(add_task_window, text='Adicionar nome e', font="Arial 15 bold", bg="#262A40", fg="#F2F2F2").place(x=64, y=10)
        tk.Label(add_task_window, text='descrição da tarefa', font="Arial 15 bold", bg="#262A40", fg="#F2F2F2").place(x=55, y=35)

        name_entry = tk.Entry(add_task_window, width=35)
        name_entry.place(x=45, y=80)
        name_entry.insert(0, 'Nome:')

        desc_entry = tk.Entry(add_task_window, width=35)
        desc_entry.place(x=45, y=110)
        desc_entry.insert(0, 'Descrição:')

        def submit_task():
            name = name_entry.get()
            description = desc_entry.get()
            if name and description:
                self.manager.add_task(name, description)
                messagebox.showinfo('Alerta!', 'Sua tarefa e descrição foram enviados!')
                add_task_window.destroy()
            else:
                messagebox.showerror("Erro", "Por favor, insira um nome e uma descrição para a tarefa.")

        tk.Button(add_task_window, text='Enviar', height=1, width=5, command=submit_task).place(x=125, y=150)

    def open_view_tasks_window(self):
        view_tasks_window = tk.Toplevel(self.root)
        view_tasks_window.title('Exibir Tarefas')
        view_tasks_window.geometry('300x200')
        view_tasks_window.config(background="#262A40")

        if not self.manager.tasks:
            tk.Label(view_tasks_window, text='Nenhuma tarefa foi adicionada ainda.', font="Arial 19 bold",
                     bg="#262A40", fg="#F2F2F2").pack(pady=80)
        else:
            tk.Label(view_tasks_window, text='Tarefas:          Descrição:', bg='#262A40', fg='white',
                     font='Arial 15 bold').place(x=27, y=25)

            tasks_text = '\n'.join([task.name for task in self.manager.tasks])
            desc_text = '\n'.join([task.description for task in self.manager.tasks])

            tk.Label(view_tasks_window, text=tasks_text, bg='#262A40', fg='white', font='Arial 12 bold').place(x=38, y=63)
            tk.Label(view_tasks_window, text=desc_text, bg='#262A40', fg='white', font='Arial 12 bold').place(x=175, y=63)

    def open_mark_completed_window(self):
        mark_completed_window = tk.Toplevel(self.root)
        mark_completed_window.title('Marcar Como Concluída')
        mark_completed_window.geometry('300x200')
        mark_completed_window.config(background="#262A40")

        if not self.manager.tasks:
            tk.Label(mark_completed_window, text='Nenhuma tarefa foi adicionada ainda.', font="Arial 19 bold",
                     bg="#262A40", fg="#F2F2F2").pack(pady=80)
        else:
            tk.Label(mark_completed_window, text='Tarefas:          Descrição:', bg='#262A40', fg='white',
                     font='Arial 15 bold').place(x=27, y=25)

            tasks_text = '\n'.join([task.name for task in self.manager.tasks])
            tk.Label(mark_completed_window, text=tasks_text, bg='#262A40', fg='white', font='Arial 12 bold').place(x=38, y=63)

            entry = tk.Entry(mark_completed_window, width=20)
            entry.place(x=85, y=141)
            entry.insert(0, 'Número da Tarefa:')

            def submit_completion():
                try:
                    index = int(entry.get()) - 1
                    self.manager.mark_task_completed(index)
                    messagebox.showinfo('Alerta!', 'Sua tarefa foi marcada como concluída!')
                    mark_completed_window.destroy()
                except (ValueError, IndexError):
                    messagebox.showerror("Erro", "Por favor, insira um número válido relacionado à tarefa.")

            tk.Button(mark_completed_window, text='Enviar', height=1, width=5, command=submit_completion).place(x=120, y=161)

    def open_delete_task_window(self):
        delete_task_window = tk.Toplevel(self.root)
        delete_task_window.title('Excluir Tarefa')
        delete_task_window.geometry('300x200')
        delete_task_window.config(background="#262A40")

        if not self.manager.tasks:
            tk.Label(delete_task_window, text='Nenhuma tarefa foi adicionada ainda.', font="Arial 19 bold",
                     bg="#262A40", fg="#F2F2F2").pack(pady=80)
        else:
            tk.Label(delete_task_window, text='Tarefas:          Descrição:', bg='#262A40', fg='white',
                     font='Arial 15 bold').place(x=27, y=25)

            tasks_text = '\n'.join([task.name for task in self.manager.tasks])
            tk.Label(delete_task_window, text=tasks_text, bg='#262A40', fg='white', font='Arial 12 bold').place(x=38, y=63)

            entry = tk.Entry(delete_task_window, width=20)
            entry.place(x=85, y=141)
            entry.insert(0, 'Número da Tarefa:')

            def submit_deletion():
                try:
                    index = int(entry.get()) - 1
                    self.manager.delete_task(index)
                    messagebox.showinfo('Alerta!', 'Sua tarefa foi excluída!')
                    delete_task_window.destroy()
                except (ValueError, IndexError):
                    messagebox.showerror("Erro", "Por favor, insira um número válido relacionado à tarefa.")

            tk.Button(delete_task_window, text='Enviar', height=1, width=5, command=submit_deletion).place(x=120, y=161)


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskApp(root)
    root.mainloop()
