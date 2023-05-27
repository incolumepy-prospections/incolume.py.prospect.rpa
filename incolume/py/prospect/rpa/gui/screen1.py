"""Modelo de janela com TKInter."""

import logging
import tkinter
from functools import partial

__author__ = "@britodfbr"  # pragma: no cover
janela = tkinter.Tk()
janela.geometry("500x300")


def click(msg: str):
    logging.debug(msg)
    print(msg)


texto = tkinter.Label(janela, text="Login")
texto.pack(padx=10, pady=10)

button = tkinter.Button(janela, text="Login", command=partial(click, "ok"))
button.pack(padx=10, pady=10)

janela.mainloop()
