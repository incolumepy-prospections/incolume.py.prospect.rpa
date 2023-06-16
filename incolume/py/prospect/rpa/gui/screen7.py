"""Modelo de janela com CustomTKInter."""

import logging

import customtkinter as ctk  # type: ignore

__author__ = "@britodfbr"  # pragma: no cover


def screen7():
    """Screen gui for username and password."""
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")
    janela7 = ctk.CTk()
    janela7.title("Authentication")
    janela7.geometry("500x300")
    username, pwd, cbox = None, None, None
    logging.debug(f"{username=}, {pwd=}, {cbox=}")

    def on_click():
        """Run handler events."""
        janela7.username, janela7.pwd, janela7.cbox = (
            login7.get(),
            pwd6.get(),
            checkbox.get(),
        )
        values = f"{janela7.username}, {janela7.pwd}, {janela7.cbox}"
        logging.debug(values)
        print(values)
        janela7.quit()

    texto7 = ctk.CTkLabel(janela7, text="Informações para Login")
    texto7.pack(padx=10, pady=10)

    login7 = ctk.CTkEntry(janela7, placeholder_text="Digite teu Login")
    login7.pack(padx=10, pady=10)

    pwd6 = ctk.CTkEntry(janela7, placeholder_text="Digite tua senha", show="*")
    pwd6.pack(padx=10, pady=10)

    checkbox = ctk.CTkCheckBox(janela7, text="Lembrar usuário")
    checkbox.pack(padx=10, pady=10)

    button = ctk.CTkButton(janela7, text="Login", command=on_click)
    button.pack(padx=10, pady=10)

    janela7.mainloop()
    return {
        "username": janela7.username,
        "password": janela7.pwd,
        "fix": janela7.cbox,
    }


if __name__ == "__main__":  # pragma: no cover
    print(screen7())
