"""Modelo de janela com CustomTKInter."""

import logging
from functools import partial

import customtkinter as ctk  # type: ignore

__author__ = "@britodfbr"  # pragma: no cover
janela = ctk.CTk()
janela.geometry("500x300")


def on_click(msg: str):
    """Run handler events."""
    logging.debug(msg)
    print(msg)


texto2 = ctk.CTkLabel(janela, text="Login")
texto2.pack(padx=10, pady=10)

login2 = ctk.CTkEntry(janela, placeholder_text="Digite teu Login")
login2.pack(padx=10, pady=10)

pwd2 = ctk.CTkEntry(janela, placeholder_text="Digite tua senha", show="*")
pwd2.pack(padx=10, pady=10)

button2 = ctk.CTkButton(
    janela, text="Login", command=partial(on_click, f"{login2=}{pwd2=}")
)
button2.pack(padx=10, pady=10)

janela.mainloop()
