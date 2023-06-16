from inspect import stack

from rocketry import Rocketry

app = Rocketry()


@app.task("every 1s", execution="async")
async def task_01():
    f"""Run {stack()[0][3]}
    Executa de modo assincrono.
    """
    print(f"Ran {stack()[0][3]}.")


@app.task("every 1s", execution="thread")
def task_02():
    f"""Run {stack()[0][3]}
    Executa vinculado ao thread separada.
    """
    print(f"Ran {stack()[0][3]}.")


@app.task("every 1s", execution="process")
def task_03():
    f"""Run {stack()[0][3]}
    Executa vinculado ao processo separado.
    """
    print(f"Ran {stack()[0][3]}.")


@app.task("every 1s")
def task_04():
    f"""Run {stack()[0][3]}
    Executa vinculado ao processo/thread principal.
    """
    print(f"Ran {stack()[0][3]}.")


if __name__ == "__main__":  # pragma: no cover
    app.run()
