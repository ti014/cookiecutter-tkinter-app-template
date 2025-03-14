import tkinter as tk

class MainWindow(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("{{cookiecutter.project_name}}")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Chào mừng đến với {{cookiecutter.project_name}}!")
        self.label.pack(pady=20)