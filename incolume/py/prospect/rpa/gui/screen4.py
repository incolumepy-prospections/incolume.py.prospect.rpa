"""Modelo de caixa de dialogo simples com TKInter."""

import tkinter.simpledialog
import logging

__author__ = "@britodfbr"  # pragma: no cover
senha = tkinter.simpledialog.askstring("Password", "Enter password:", show='*')

logging.debug(senha)
print(senha)
