import time

import pyautogui


def automation1(url: str = '') -> None:
    """Automação para agendamento de sala com pyautogui."""
    url = url or r'https://intranetsispr2.presidencia.gov.br/' \
                 r'reservapr/login.php'
    #
    pyautogui.alert("Pronto para iniciar a automação?")
    pyautogui.PAUSE = .5

    pyautogui.press("winleft")
    time.sleep(2)
    pyautogui.write("chrome")
    pyautogui.press("enter")

    pyautogui.hotkey("ctrl", "t")
    time.sleep(.8)

    pyautogui.write(url)
    pyautogui.press("enter")
    pyautogui.confirm('Proceda com o login e pressione OK.')

if __name__ == "__main__":  # pragma: no cover
    automation1()


