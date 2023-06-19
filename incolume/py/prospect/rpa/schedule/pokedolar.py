"""Module Pokedolar.

from https://github.com/dunossauro/live-de-python
/blob/main/codigo/Live214/pokedolar.py
"""

from datetime import date
from os import listdir, makedirs
from pathlib import Path

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
    """Run it."""
    day = 3  # randint(1, 29)
    month = 6  # randint(1, 12)
    year = 2021  # randint(2019, 2021)
    random_date = date.today().replace(day=day, month=month, year=year)
    formated_date = random_date.strftime("%Y%m%d")
    return formated_date


@app.param("date")
def date_today() -> str:
    """Run it."""
    date_today = date.today()
    formated_date = date_today.strftime("%Y%m%d")
    return formated_date


@app.task("every 5s", name="Pega cotação do dolar")
# def get_dolar(date=Arg('dater')) -> str:
def get_dolar(date=Arg("date")) -> str:
    """Run it."""
    response = get(DOLAR.format(date, date)).json()[0]["high"]
    return response.replace(".", "")[:3]


@app.task(after_fail(get_dolar))
def get_dolar_fail(date=Arg("date")):
    """Run it."""
    # Envia um email para o Maykon
    print(f"Erro no dia {date}")
    print("Enviando email para responsável..")


@app.task(after_success(get_dolar))
def get_pokemon_json(number=Return(get_dolar)):
    """Run it."""
    response = get(f"{API}/{number}").json()
    return response


@app.task(after_success(get_pokemon_json))
def get_pokemon_sprite_url(poke_json=Return(get_pokemon_json)):
    """Run it."""
    return (poke_json["sprites"]["front_default"], poke_json["name"])


@app.task(after_success(get_pokemon_sprite_url))
def download_sprite(
    poke_data=Return(get_pokemon_sprite_url),
    poke_numer=Return(get_dolar),
    download=Arg("download"),
):
    """Run it."""
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
    """Run it."""
    makedirs("sprites", exist_ok=True)
    pasta = Path("sprites")
    path.rename(pasta / path)


@app.param("download")
def download(val=Return(get_dolar)):
    """Run it."""
    sprites: list[str] = listdir("sprites")
    for sprite in sprites:
        if sprite.startswith(val):
            print(f"{val=} é repetido")
            return False
    else:
        return True


if __name__ == "__main__":  # pragma: no cover
    app.run()
