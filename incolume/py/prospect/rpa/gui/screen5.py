"""Modelo de janela com CustomTKInter."""

import customtkinter as ctk
import logging
from functools import partial

__author__ = "@britodfbr"  # pragma: no cover
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')
janela = ctk.CTk()
janela.title('Authentication')
janela.geometry("500x300")


def click(*args, **kwargs):
    logging.debug('%s %s' % (args, kwargs))
    print(args, kwargs)


texto = ctk.CTkLabel(janela, text='Informações para Login')
texto.pack(padx=10, pady=10)

login = ctk.CTkEntry(janela, placeholder_text='Digite teu Login')
login.pack(padx=10, pady=10)

pwd = ctk.CTkEntry(janela,
                   placeholder_text='Digite tua senha', show='*')
pwd.pack(padx=10, pady=10)

checkbox = ctk.CTkCheckBox(janela, text='...')
checkbox.pack(padx=10, pady=10)

button = ctk.CTkButton(
    janela,
    text='Login',
    command=partial(
        click,
        login.get(),
        pwd.get(),
        checkbox.get()
    )
)
button.pack(padx=10, pady=10)

janela.mainloop()
