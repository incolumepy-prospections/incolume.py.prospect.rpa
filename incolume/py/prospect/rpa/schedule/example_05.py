"""Modulo de Tratativa."""
from inspect import stack

from rocketry import Rocketry

app = Rocketry()


@app.task("every 1s", execution="async")
async def task_01():
    """Run it.

    Executa de modo assincrono.
    """
    print(f"Ran {stack()[0][3]}.")


@app.task("every 1s", execution="thread")
def task_02():
    """Run it.

    Executa vinculado ao thread separada.
    """
    print(f"Ran {stack()[0][3]}.")


@app.task("every 1s", execution="process")
def task_03():
    """Run it.

    Executa vinculado ao processo separado.
    """
    print(f"Ran {stack()[0][3]}.")


@app.task("every 1s")
def task_04():
    """Run it.

    Executa vinculado ao processo/thread principal.
    """
    print(f"Ran {stack()[0][3]}.")


if __name__ == "__main__":  # pragma: no cover
    app.run()
