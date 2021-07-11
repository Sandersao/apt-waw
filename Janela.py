import tkinter as tk


class Janela:
    @staticmethod
    def create(name="No name"):
        Janela.janela = tk.Tk()
        Janela.janela.title(name)
        Janela.scrollbar = tk.Scrollbar(Janela.janela)
        Janela.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    @staticmethod
    def draw():
        Janela.janela.mainloop()

    @staticmethod
    def addLabel(texto):
        label = tk.Label(text=texto)
        label.pack()
