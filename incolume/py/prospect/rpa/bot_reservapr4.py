import datetime as dt
import logging
import time

from playwright.sync_api import sync_playwright
from PySimpleGUI import PySimpleGUI as sg
from rocketry import Rocketry
from rocketry.args import Arg
from rocketry.conds import daily, every

scheduling = Rocketry()


@scheduling.task(every("1d"))
def screen():
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


def action_web(
    username: str,
    password: str,
    url: str = "",
    date: dt.datetime = None,
    delta: dict[str:int] = None,
    date_format: str = "%d%m%Y",
    hidden: bool = True,
):
    """"""
    url = (
        url or r"https://intranetsispr2.presidencia.gov.br/reservapr/login.php"
    )
    if delta is None:
        delta = {"weeks": 0, "days": 60}
    date = date or dt.datetime.now() + dt.timedelta(**delta)
    logging.debug(f"{username}")
    logging.debug(f"{url}")
    logging.debug(f"{date}")
    logging.debug(f"{delta}")
    logging.debug(f"{date_format}")
    logging.debug(f"{hidden}")
    with sync_playwright() as pw_instance:
        browser = pw_instance.webkit.launch(headless=hidden, slow_mo=50)
        page = browser.new_page()
        page.wait_for_timeout(3000)
        page.goto(url)
        page.screenshot(path="capture0.png")
        time.sleep(1)
        page.fill('xpath=//*[@id="txt_login"]', username)
        page.fill('xpath=//*[@id="txt_senha"]', password)
        page.screenshot(path="capture1.png")

        # Botão login
        page.locator('xpath=//*[@id="form-signin"]/button').click()
        time.sleep(1)

        # tipo de espaço
        page.locator(
            'xpath=//*[@id="form-pesquisa-disponibilidade"]'
            "/div/div[3]/div/div[1]/div/label[2]/input"
        ).click()
        # datas
        page.locator('xpath=//*[@id="txt_dat_inicio"]').click()
        page.keyboard.type(date.strftime(date_format))
        page.keyboard.press("Tab")
        page.keyboard.type(date.strftime(date_format))
        page.keyboard.press("Tab")

        # horários
        # page.locator('xpath=//*[@id="txt_hor_inicio"]')
        page.keyboard.type("0800")
        page.keyboard.press("Tab")

        # page.locator('xpath=//*[@id="txt_hor_fim"]')
        page.keyboard.type("1800")

        # Quantia de Participantes
        page.fill('xpath=//*[@id="txt_num_participantes"]', "45")

        # Secretário
        page.locator(
            'xpath=//*[@id="form-pesquisa-disponibilidade"]'
            "/div/div[3]/div/div[5]"
            "/div/div[5]/div/label/input"
        ).click()

        # Pesquisar
        page.locator(
            'xpath=//*[@id="form-pesquisa-disponibilidade"]'
            "/div/div[2]/button[2]"
        ).click()

        # Reserva
        page.locator(
            'xpath=//*[@id="carregaEspacosAba1"]'
            "/ul/li[3]/div/div[2]/div/div[3]/button"
        ).click()

        # tipo de evento
        page.select_option("select#txt_cod_tipo_evento", label="Curso")

        # Descrição do Evento
        page.fill(
            'xpath=//*[@id="txt_dsc_evento"]', "Programa de Intercâmbio SAJ"
        )

        # Ativos
        page.locator(
            "xpath=/html/body/div[1]/section[2]/form/div/div[2]/div/"
            "div[2]/div[1]/div[1]/div/div[1]/div/label/input"
        ).click()
        page.locator(
            "xpath=/html/body/div[1]/section[2]/form/div/div[2]/div/"
            "div[2]/div[1]/div[1]/div/div[2]/div/label/input"
        ).click()
        page.locator(
            "xpath=/html/body/div[1]/section[2]/form/div/div[2]/div/"
            "div[2]/div[1]/div[1]/div/div[3]/div/label/input"
        ).click()
        page.locator(
            "xpath=/html/body/div[1]/section[2]/form/div/div[2]/div/"
            "div[2]/div[1]/div[1]/div/div[4]/div/label/input"
        ).click()
        page.locator(
            "xpath=/html/body/div[1]/section[2]/form/div/div[2]/div/"
            "div[2]/div[1]/div[1]/div/div[5]/div/label/input"
        ).click()
        page.locator(
            "xpath=/html/body/div[1]/section[2]/form/div/div[2]/div/"
            "div[2]/div[1]/div[1]/div/div[6]/div/label/input"
        ).click()
        page.locator(
            "xpath=/html/body/div[1]/section[2]/form/div/div[2]/div/"
            "div[2]/div[1]/div[1]/div/div[7]/div/label/input"
        ).click()
        # page.locator('xpath=/html/body/div[1]/section[2]/form/div/div[2]/div/'
        #              'div[2]/div[1]/div[1]/div/div[8]/div/label/input').click()
        page.locator(
            "xpath=/html/body/div[1]/section[2]/form/div/div[2]/div/"
            "div[2]/div[1]/div[1]/div/div[9]/div/label/input"
        ).click()
        page.locator(
            "xpath=/html/body/div[1]/section[2]/form/div/div[2]"
            "/div/div[2]/div[1]/div[1]/div/div[10]"
            "/div/label/input"
        ).click()
        page.screenshot(path="capture2.png")

        # Salvar reserva
        page.locator(
            "xpath=/html/body/div[1]/section[2]" "/form/div/div[3]/button[2]"
        ).click()
        page.screenshot(path="capture3.png")

        # Confirmar reserva
        page.fill('xpath=//*[@id="txt_dsc_senha_confirmacao"]', password)
        page.locator(
            'xpath=//*[@id="myModalBody"]' "/div/div/div/div/button"
        ).click()

        # time.sleep(5)
        page.screenshot(path="capture4.png")
        browser.close()


@scheduling.task(daily.at("11:16"))
def automation(
    reserve_date: str = "",
    delta: dict[str:int] = None,
    date_format: str = "%d%m%Y",
    url: str = "",
    hidden: bool = True,
    info_login=Arg(screen),
) -> None:
    """Automação para agendamento de sala com playwright."""
    try:
        date = dt.datetime.strptime(reserve_date, "%d/%m/%Y")
    except ValueError:
        date = None
    username, password, fix = info_login.values()
    logging.debug(f"{username=}, {fix=}")
    action_web(
        username=username,
        password=password,
        url=url,
        date=date,
        date_format=date_format,
        delta=delta,
        hidden=hidden,
    )


def run():
    # automation(hidden=False, delta={'days': 3})
    automation(reserve_date="04/06/2023", hidden=False)


if __name__ == "__main__":
    scheduling.run()
