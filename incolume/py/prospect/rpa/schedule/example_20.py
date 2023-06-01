import datetime
import logging
from rocketry import Rocketry
from rocketry.args import Arg
from rocketry.conds import every, after_success, daily
from inspect import stack
from PySimpleGUI import PySimpleGUI as sg

app = Rocketry()


@app.param()
def screen():
    # sg.theme('Reddit')
    sg.theme('DarkBlue')
    layout = [
        [sg.Text('usuário'), sg.Input(key='username')],
        [sg.Text('  senha'), sg.Input(key='password', password_char='*')],
        [sg.Checkbox('Lembrar usuário', key='fix')],
        [sg.Button('Login')]
    ]
    # eventos, valores = None, None
    janela = sg.Window('Autentication', layout)

    while 1:
        eventos, valores = janela.read()
        if eventos == sg.WINDOW_CLOSED:
            break
        if eventos == 'Login':
            logging.debug(valores)
            break
    janela.close()
    return valores


@app.task(daily.at('10:40'))
def task_a(info_login=Arg('screen')):
    f"""Run {stack()[0][3]}
    Return value.
    """
    username, password, fix = info_login.values()
    print(username, password, fix)


if __name__ == '__main__':  # pragma: no cover
    app.run()
