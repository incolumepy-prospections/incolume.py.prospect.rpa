"""Modelo de janela com CustomTKInter."""

import logging

import customtkinter as ctk  # type: ignore

__author__ = "@britodfbr"  # pragma: no cover


def screen8():
    """Screen gui for username and password."""
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")
    janela8 = ctk.CTk()
    janela8.title("Authentication")
    janela8.geometry("500x300")
    username, pwd, cbox = None, None, None
    logging.debug(f"{username=}, {pwd=}, {cbox=}")

    def on_click():
        """Run handler events."""
        janela8.username, janela8.pwd, janela8.cbox = (
            login8.get(),
            pwd8.get(),
            checkbox.get(),
        )
        values = f"{janela8.username}, {janela8.pwd}, {janela8.cbox}"
        logging.debug(values)
        janela8.quit()

    texto7 = ctk.CTkLabel(janela8, text="Informações para Login")
    texto7.pack(padx=10, pady=10)

    login8 = ctk.CTkEntry(janela8, placeholder_text="Digite teu Login")
    login8.pack(padx=10, pady=10)

    pwd8 = ctk.CTkEntry(janela8, placeholder_text="Digite tua senha", show="*")
    pwd8.pack(padx=10, pady=10)

    checkbox = ctk.CTkCheckBox(janela8, text="Lembrar usuário")
    checkbox.pack(padx=10, pady=10)

    button = ctk.CTkButton(janela8, text="Login", command=on_click)
    button.pack(padx=10, pady=10)

    janela8.mainloop()
    return {
        "username": janela8.username,
        "password": janela8.pwd,
        "fix": janela8.cbox,
    }


if __name__ == "__main__":  # pragma: no cover
    print(screen8())
