import tkinter as tk
from tkinter import *
import config as conf
import tkinter.ttk as ttk
import os
import pygubu
import config as conf

PROJECT_PATH = os.path.dirname(__file__)
PROJECT_UI = os.path.join(PROJECT_PATH, "UI_lihat_data.ui")


class TampilkanPengguna:

    def __init__(self, parent):
        config = conf.Config()
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        self.mainwindow = builder.get_object('top_level', parent)
        builder.connect_callbacks(self)
        self.tabelPengguna = builder.get_object('tabel_user', parent)
        self.tabelPengguna['columns'] = ('Nama', 'Username')
        self.tabelPengguna.column('Nama', anchor=tk.CENTER)
        self.tabelPengguna.column('Username', anchor=tk.CENTER)
        self.tabelPengguna.heading('Nama', text='Nama')
        self.tabelPengguna.heading('Username', text='Username')

        hasil = config.read()
        i = 0
        for ro in hasil:
            self.tabelPengguna.insert('', i, text='', values=(ro[0], ro[1]))
            i = i + 1

    def run(self):
        self.mainwindow.mainloop()

root = tk.Tk()
app = TampilkanPengguna(root)
app.run()
