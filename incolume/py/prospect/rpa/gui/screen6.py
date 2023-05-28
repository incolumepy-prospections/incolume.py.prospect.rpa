"""Modelo de janela com CustomTKInter."""

import logging

import customtkinter as ctk  # type: ignore

__author__ = "@britodfbr"  # pragma: no cover


def screen6():
    """Screen gui for username and password."""
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")
    janela6 = ctk.CTk()
    janela6.title("Authentication")
    janela6.geometry("500x300")

    def on_click():
        """Run handler events."""
        values = f"{login6.get()}, {pwd6.get()}, {checkbox.get()}"
        logging.debug(values)
        print(values)

    texto6 = ctk.CTkLabel(janela6, text="Informações para Login")
    texto6.pack(padx=10, pady=10)

    login6 = ctk.CTkEntry(janela6, placeholder_text="Digite teu Login")
    login6.pack(padx=10, pady=10)

    pwd6 = ctk.CTkEntry(janela6, placeholder_text="Digite tua senha", show="*")
    pwd6.pack(padx=10, pady=10)

    checkbox = ctk.CTkCheckBox(janela6, text="Lembrar usuário")
    checkbox.pack(padx=10, pady=10)

    button = ctk.CTkButton(janela6, text="Login", command=on_click)
    button.pack(padx=10, pady=10)

    janela6.mainloop()


if __name__ == "__main__":  # pragma: no cover
    screen6()
