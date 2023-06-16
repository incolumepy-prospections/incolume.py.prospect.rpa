import asyncio
import logging
from inspect import stack

from PySimpleGUI import PySimpleGUI as sg
from rocketry import Rocketry
from rocketry.args import Return
from rocketry.conds import every

app = Rocketry(execution="async")


@app.param()
async def screen():
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


@app.task(every("30s"))
async def do_things(info=Return("screen")):
    f"""Run {stack()[0][3]}"""
    print(f"{stack()[0][3]}: {info}")


async def main():
    """Launch Rocketry app (and possibly something else)"""
    rocketry_task = asyncio.create_task(app.serve())
    # Start possibly other async apps
    await rocketry_task


if __name__ == "__main__":
    print(asyncio.run(main()))
