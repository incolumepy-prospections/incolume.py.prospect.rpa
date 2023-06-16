import asyncio
import datetime as dt
import logging

from playwright.async_api import async_playwright
from PySimpleGUI import PySimpleGUI as sg
from rocketry import Rocketry
from rocketry.args import Return
from rocketry.conds import daily

scheduling = Rocketry()


@scheduling.param()
async def screen():
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


async def action_web(
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
    with async_playwright() as pw_instance:
        browser = await pw_instance.webkit.launch(headless=hidden, slow_mo=50)
        page = await browser.new_page()
        await page.wait_for_timeout(3000)
        await page.goto(url)
        await page.screenshot(path="capture0.png")
        asyncio.sleep(1)
        await page.fill('xpath=//*[@id="txt_login"]', username)
        await page.fill('xpath=//*[@id="txt_senha"]', password)
        await page.screenshot(path="capture1.png")

        # Botão login
        await page.locator('xpath=//*[@id="form-signin"]/button').click()
        asyncio.sleep(1)

        # tipo de espaço
        await page.locator(
            'xpath=//*[@id="form-pesquisa-disponibilidade"]'
            "/div/div[3]/div/div[1]/div/label[2]/input"
        ).click()
        # datas
        await page.locator('xpath=//*[@id="txt_dat_inicio"]').click()
        await page.keyboard.type(date.strftime(date_format))
        await page.keyboard.press("Tab")
        await page.keyboard.type(date.strftime(date_format))
        await page.keyboard.press("Tab")

        # horários
        # page.locator('xpath=//*[@id="txt_hor_inicio"]')
        await page.keyboard.type("0800")
        await page.keyboard.press("Tab")

        # page.locator('xpath=//*[@id="txt_hor_fim"]')
        await page.keyboard.type("1800")

        # Quantia de Participantes
        await page.fill('xpath=//*[@id="txt_num_participantes"]', "45")

        # Secretário
        await page.locator(
            'xpath=//*[@id="form-pesquisa-disponibilidade"]'
            "/div/div[3]/div/div[5]"
            "/div/div[5]/div/label/input"
        ).click()

        # Pesquisar
        await page.locator(
            'xpath=//*[@id="form-pesquisa-disponibilidade"]'
            "/div/div[2]/button[2]"
        ).click()

        # Reserva
        await page.locator(
            'xpath=//*[@id="carregaEspacosAba1"]'
            "/ul/li[3]/div/div[2]/div/div[3]/button"
        ).click()

        # tipo de evento
        await page.select_option("select#txt_cod_tipo_evento", label="Curso")

        # Descrição do Evento
        await page.fill(
            'xpath=//*[@id="txt_dsc_evento"]', "Programa de Intercâmbio SAJ"
        )

        # Ativos
        await page.locator(
            "xpath=/html/body/div[1]/section[2]/form/div/div[2]/div/"
            "div[2]/div[1]/div[1]/div/div[1]/div/label/input"
        ).click()
        await page.locator(
            "xpath=/html/body/div[1]/section[2]/form/div/div[2]/div/"
            "div[2]/div[1]/div[1]/div/div[2]/div/label/input"
        ).click()
        await page.locator(
            "xpath=/html/body/div[1]/section[2]/form/div/div[2]/div/"
            "div[2]/div[1]/div[1]/div/div[3]/div/label/input"
        ).click()
        await page.locator(
            "xpath=/html/body/div[1]/section[2]/form/div/div[2]/div/"
            "div[2]/div[1]/div[1]/div/div[4]/div/label/input"
        ).click()
        await page.locator(
            "xpath=/html/body/div[1]/section[2]/form/div/div[2]/div/"
            "div[2]/div[1]/div[1]/div/div[5]/div/label/input"
        ).click()
        await page.locator(
            "xpath=/html/body/div[1]/section[2]/form/div/div[2]/div/"
            "div[2]/div[1]/div[1]/div/div[6]/div/label/input"
        ).click()
        await page.locator(
            "xpath=/html/body/div[1]/section[2]/form/div/div[2]/div/"
            "div[2]/div[1]/div[1]/div/div[7]/div/label/input"
        ).click()
        # page.locator('xpath=/html/body/div[1]/section[2]/form/div/div[2]/div/'
        #              'div[2]/div[1]/div[1]/div/div[8]/div/label/input').click()
        await page.locator(
            "xpath=/html/body/div[1]/section[2]/form/div/div[2]/div/"
            "div[2]/div[1]/div[1]/div/div[9]/div/label/input"
        ).click()
        await page.locator(
            "xpath=/html/body/div[1]/section[2]/form/div/div[2]"
            "/div/div[2]/div[1]/div[1]/div/div[10]"
            "/div/label/input"
        ).click()
        await page.screenshot(path="capture2.png")

        # Salvar reserva
        await page.locator(
            "xpath=/html/body/div[1]/section[2]" "/form/div/div[3]/button[2]"
        ).click()
        await page.screenshot(path="capture3.png")

        # Confirmar reserva
        await page.fill('xpath=//*[@id="txt_dsc_senha_confirmacao"]', password)
        await page.locator(
            'xpath=//*[@id="myModalBody"]' "/div/div/div/div/button"
        ).click()

        # time.sleep(5)
        await page.screenshot(path="capture4.png")
        await browser.close()


@scheduling.task(daily.at("15:47"))
async def automation(
    reserve_date: str = "",
    delta: dict[str:int] = None,
    date_format: str = "%d%m%Y",
    url: str = "",
    hidden: bool = True,
    info_login=Return(screen),
) -> None:
    """Automação para agendamento de sala com playwright."""
    try:
        date = dt.datetime.strptime(reserve_date, "%d/%m/%Y")
    except ValueError:
        date = None
    print(f"{info_login=}")
    username, password, fix = info_login.values()
    logging.debug(f"{username=}, {fix=}")
    await action_web(
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
    asyncio.run(automation(reserve_date="04/06/2023", hidden=False))


if __name__ == "__main__":
    run()
