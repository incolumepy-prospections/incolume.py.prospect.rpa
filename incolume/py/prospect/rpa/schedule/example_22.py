"""Examples."""
import logging
from inspect import stack

from PySimpleGUI import PySimpleGUI as sg
from rocketry import Rocketry
from rocketry.args import Return
from rocketry.conds import daily, every

app = Rocketry()


@app.task(every("1d"))
def screen():
    """Run screen."""
    # sg.theme('Reddit')
    sg.theme("DarkBlue")
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


@app.task(daily.at("11:02"), execution="process")
def task_a(info_login: dict = Return("screen")):
    """Run it.

    Return value.
    """
    logging.debug(stack()[0][3])
    username, password, fix = info_login.values()
    print(username, password, fix)


if __name__ == "__main__":  # pragma: no cover
    app.run()
