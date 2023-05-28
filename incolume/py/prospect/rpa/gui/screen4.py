"""Modelo de caixa de dialogo simples com TKInter."""

import logging
import tkinter.simpledialog

__author__ = "@britodfbr"  # pragma: no cover
senha = tkinter.simpledialog.askstring("Password", "Enter password:", show="*")

logging.debug(senha)
print(senha)
