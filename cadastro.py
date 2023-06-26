import tkinter as tk
from tkinter import ttk
import datetime as dt

janela = tk.Tk()

janela.title(' Lupa - Sistema de cadastro de Objetos')

label_descricao = tk.Label(text='Descrição do Objeto')
label_descricao.grid(row=1, column=0, padx=10, pady=10, sticky='nswr', columnspan=4)

janela.mainloop()