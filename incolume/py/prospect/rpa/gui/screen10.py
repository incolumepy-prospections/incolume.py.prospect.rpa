"""Modulo de Tratativa."""
import logging

from PySimpleGUI import PySimpleGUI as sg


def screen10():
    """Run screen10."""
    sg.theme("Reddit")
    # sg.theme('DarkBlue')
    layout = [
        [sg.Text("usuário"), sg.Input(key="username")],
        [sg.Text("  senha"), sg.Input(key="password", password_char="*")],
        [sg.Checkbox("Lembrar usuário", key="fix")],
        [sg.Button("Login")],
    ]
    # eventos, valores = None, None
    janela = sg.Window("Autentication", layout)

    while 1:
        eventos, valores = janela.read()
        if eventos == sg.WINDOW_CLOSED:
            break
        if eventos == "Login":
            logging.debug(valores)
            break
    janela.close()
    return valores


if __name__ == "__main__":
    print(screen10())
