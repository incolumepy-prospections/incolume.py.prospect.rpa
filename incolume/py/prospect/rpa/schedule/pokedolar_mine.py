"""Pokedolar from https://github.com/dunossauro/
live-de-python/blob/main/codigo/Live214/pokedolar.py"""

import logging
from datetime import date
from os import makedirs
from pathlib import Path
from random import randint

from httpx import get, stream
from rocketry import Rocketry
from rocketry.args import Arg, Return
from rocketry.conds import after_fail, after_finish, after_success

# handler = logging.StreamHandler()
# handler.setLevel(logging.DEBUG)
# task_logger = logging.getLogger('rocketry.task')
# task_logger.addHandler(handler)


API = "https://pokeapi.co/api/v2/pokemon"
DOLAR = (
    "https://economia.awesomeapi.com.br/json/daily/USD-BRL/"
    "?start_date={}&end_date={}"
)

app = Rocketry()


@app.param("dater")
def random_date_generator() -> str:
    """Generate random date."""
    day = randint(1, 29)
    month = randint(1, 12)
    year = randint(2019, 2021)
    # day, month, year = 2, 6, 2021
    random_date = date(day=day, month=month, year=year)
    logging.debug(random_date)
    formated_date = random_date.strftime("%Y%m%d")
    logging.debug(formated_date)
    return formated_date


@app.param("date")
def date_today() -> str:
    today = date.today()
    logging.debug(today)
    formated_date = today.strftime("%Y%m%d")
    logging.debug(formated_date)
    return formated_date


@app.task("every 5s", name="Pega cotação do dolar")
def get_dolar(date=Arg("dater")) -> str:
    # def get_dolar(date=Arg('date')) -> str:
    logging.debug(date)
    response = get(DOLAR.format(date, date)).json()[0]["high"]
    logging.debug(f"{response.status_code=}")
    return response.replace(".", "")[:3]


@app.task(after_fail(get_dolar))
def get_dolar_fail(date=Arg("date")):
    # Envia um email para o Maykon
    print(f"Erro no dia {date}")
    print("Enviando email para responsável..")


@app.task(after_success(get_dolar))
def get_pokemon_json(number=Return(get_dolar)):
    response = get(f"{API}/{number}").json()
    return response


@app.task(after_success(get_pokemon_json))
def get_pokemon_sprite_url(poke_json=Return(get_pokemon_json)):
    return (poke_json["sprites"]["front_default"], poke_json["name"])


@app.task(after_success(get_pokemon_sprite_url))
def download_sprite(
    poke_data=Return(get_pokemon_sprite_url),
    poke_numer=Return(get_dolar),
    download=Arg("download"),
):
    url, name = poke_data
    file = Path(f"{poke_numer}_{name}.png")
    if not download:
        return file
    with open(file, "wb") as download_file:
        with stream("GET", url) as s:
            for chunk in s.iter_bytes():
                download_file.write(chunk)
    return file


@app.task(after_finish(download_sprite))
def move_sprite(path: Path = Return(download_sprite)):
    makedirs("sprites", exist_ok=True)
    pasta = Path("sprites")
    path.rename(pasta / path)


@app.param("download")
def download(val=Return(get_dolar)):
    pasta: Path = Path("sprites")
    sprites: list[Path] | None = None
    try:
        sprites = list(pasta.glob("*.png"))
    except Exception:
        pasta.mkdir(exist_ok=True, parents=True)
        sprites = []

    for sprite in sprites:
        if sprite.as_posix().startswith(val):
            print(f"{val=} é repetido")
            return False
    else:
        return True


app.run()
