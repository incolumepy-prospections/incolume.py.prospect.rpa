"""Modelo de janela com CustomTKInter."""

import customtkinter as ctk
import logging
from functools import partial

__author__ = "@britodfbr"  # pragma: no cover
janela = ctk.CTk()
janela.geometry("500x300")


def click(msg: str):
    logging.debug(msg)
    print(msg)


texto = ctk.CTkLabel(janela, text='Login')
texto.pack(padx=10, pady=10)

login = ctk.CTkEntry(janela, placeholder_text='Digite teu Login')
login.pack(padx=10, pady=10)

pwd = ctk.CTkEntry(janela,
                   placeholder_text='Digite tua senha', show='*')
pwd.pack(padx=10, pady=10)

button = ctk.CTkButton(janela, text='Login',
                       command=partial(click, f'{login=}{pwd=}'))
button.pack(padx=10, pady=10)

janela.mainloop()
