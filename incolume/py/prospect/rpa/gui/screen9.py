"""Modulo de Tratativa."""
from PySimpleGUI import PySimpleGUI as sg

sg.theme("Reddit")

layout = [
    [sg.Text("usuário"), sg.Input(key="username")],
    [sg.Text("  senha"), sg.Input(key="password", password_char="*")],
    [sg.Checkbox("Lembrar usuário", key="fix")],
    [sg.Button("Login")],
]

janela = sg.Window("Autentication", layout)
while 1:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == "Login":
        print(valores)
        break
