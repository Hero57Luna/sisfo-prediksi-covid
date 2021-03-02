import os
import pygubu
import tkinter as tk
import tkinter.ttk as ttk
import config as conf

PROJECT_PATH = os.path.dirname(__file__)
PROJECT_UI = os.path.join(PROJECT_PATH, "UI_Tambah_Pengguna.ui")


class TambahPengguna:
    def __init__(self, parent):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        self.mainwindow = builder.get_object('top_level', parent)
        builder.connect_callbacks(self)
        self.input_nama = builder.get_object('input_nama', parent)
        self.input_username = builder.get_object('input_username', parent)
        self.input_password = builder.get_object('input_password', parent)
        self.input_role = builder.get_object('input_role', parent)
        self.input_departement = builder.get_object('input_departement', parent)

    def submit(self):
        config = conf.Config()

        nama = self.input_nama.get()
        username = self.input_username.get()
        password = self.input_password.get()
        role = self.input_role.get()
        departement = self.input_departement.get()

        config.create(nama, username, password, role, departement)


    def run(self):
        self.mainwindow.mainloop()

root = tk.Tk()
app = TambahPengguna(root)
app.run()

