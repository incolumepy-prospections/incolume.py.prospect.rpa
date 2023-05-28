"""Modelo de janela com CustomTKInter."""

import logging
from functools import partial

import customtkinter as ctk  # type: ignore

__author__ = "@britodfbr"  # pragma: no cover
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
janela = ctk.CTk()
janela.geometry("500x300")


def on_click(*args, **kwargs):
    """Run handler events."""
    logging.debug("%s %s", args, kwargs)
    print(args, kwargs)


texto3 = ctk.CTkLabel(janela, text="Login")
texto3.pack(padx=10, pady=10)

login3 = ctk.CTkEntry(janela, placeholder_text="Digite teu Login")
login3.pack(padx=10, pady=10)

pwd3 = ctk.CTkEntry(janela, placeholder_text="Digite tua senha", show="*")
pwd3.pack(padx=10, pady=10)

checkbox3 = ctk.CTkCheckBox(janela, text="...")
checkbox3.pack(padx=10, pady=10)

button3 = ctk.CTkButton(
    janela,
    text="Login",
    command=partial(on_click, login3.get(), pwd3.get(), checkbox3.get()),
)
button3.pack(padx=10, pady=10)

janela.mainloop()
