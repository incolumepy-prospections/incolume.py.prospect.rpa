"""Examples RPA with playwright."""

import asyncio
import time
import datetime as dt
from playwright.async_api import async_playwright
from playwright.sync_api import sync_playwright
from incolume.py.prospect.rpa.gui.screen7 import screen7
from incolume.py.prospect.rpa.gui.screen8 import screen8


def sketch01():
    """Syncrono example."""
    with sync_playwright() as pw_instance:
        browser = pw_instance.chromium.launch()
        page = browser.new_page()
        page.goto("http://playwright.dev")
        print(page.title())
        browser.close()


async def sketch02():
    """Asyncrono example."""
    async with async_playwright() as pw_instance:
        browser = await pw_instance.chromium.launch()
        page = await browser.new_page()
        await page.goto("http://playwright.dev")
        print(await page.title())
        await browser.close()


def sketch03():
    """Screenshot example."""
    with sync_playwright() as pw_instance:
        browser = pw_instance.webkit.launch(headless=False, slow_mo=50)
        page = browser.new_page()
        page.goto("http://whatsmyuseragent.org/")
        page.screenshot(path="example.png")
        browser.close()


def automation1(url: str = "") -> None:
    """Automação para agendamento de sala com playwright."""
    url = (
        url
        or r"https://intranetsispr2.presidencia.gov.br/" r"reservapr/login.php"
    )
    info_login = screen7()
    with sync_playwright() as pw_instance:
        browser = pw_instance.webkit.launch(headless=False, slow_mo=50)
        page = browser.new_page()
        page.goto(url)
        time.sleep(7)
        page.screenshot(path="example.png")
        page.fill('xpath=//*[@id="email-login"]', info_login.get('username'))
        time.sleep(1)
        page.locator('xpath=/html/body/div[1]/div[2]/div[2]/button').click()
        page.fill('xpath=//*[@id="senha"]', info_login.get('password'))
        time.sleep(5)
        # browser.close()


def automation2(date: dt.datetime = None,
                date_format: str = '%d/%m/%Y', url: str = "") -> None:
    """Automação para agendamento de sala com playwright."""
    date = date or dt.datetime.now()
    url = (
        url
        or r"https://intranetsispr2.presidencia.gov.br/reservapr/login.php"
    )
    info_login = screen8()
    with sync_playwright() as pw_instance:
        browser = pw_instance.webkit.launch(headless=False, slow_mo=50)
        page = browser.new_page()
        page.goto(url)
        time.sleep(7)
        page.screenshot(path="example.png")
        page.fill('xpath=//*[@id="txt_login"]', info_login.get('username'))
        page.fill('xpath=//*[@id="txt_senha"]', info_login.get('password'))
        page.locator('xpath=//*[@id="form-signin"]/button').click()
        page.locator('xpath=//*[@id="form-pesquisa-disponibilidade"]'
                     '/div/div[3]/div/div[1]/div/label[2]/input').click()

        time.sleep(1)
        page.fill('xpath=//*[@id="txt_dat_inicio"]',
                  date.strftime(date_format))
        time.sleep(5)
        # browser.close()


def run():
    """Run it.."""
    # sketch01()
    # asyncio.run(sketch02())
    # sketch03()
    # print(f"{dir()}")
    # automation1(url="https://portalhashtag.com/login")
    automation2()


if __name__ == "__main__":
    run()
