import asyncio
from playwright.sync_api import sync_playwright
from playwright.async_api import async_playwright


def sketch01():
    """"""
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("http://playwright.dev")
        print(page.title())
        browser.close()


async def sketch02():
    """"""
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("http://playwright.dev")
        print(await page.title())
        await browser.close()


def sketch03():
    """"""
    with sync_playwright() as p:
        browser = p.webkit.launch(headless=False, slow_mo=50)
        page = browser.new_page()
        page.goto("http://whatsmyuseragent.org/")
        page.screenshot(path="example.png")
        browser.close()


def automation1(url: str = '') -> None:
    """Automação para agendamento de sala com playwright."""

    url = url or r'https://intranetsispr2.presidencia.gov.br/' \
                 r'reservapr/login.php'


def run():
    """run it.."""
    sketch01()
    asyncio.run(sketch02())
    sketch03()
    print('{}'.format(dir()))


if __name__ == '__main__':
    run()
