"""Examples."""
from rocketry import Rocketry

app = Rocketry()


@app.task("every 1 second")
def a_cada_segundo():
    """Run it."""
    print("a cada segundo")


@app.task("every 10 seconds")
def a_cada_10_segundos():
    """Run it."""
    print("a cada 10 segundos")


@app.task("every 2s")
def a_cada_2_segundos():
    """Run it."""
    print("a cada 2 segundos")


@app.task("every 1 hour")
def a_cada_hora():
    """Run it."""
    print("a cada hora")


@app.task("every 2d")
def a_cada_2_dias():
    """Run it."""
    print("a cada 2 dias")


if __name__ == "__main__":  # pragma: no cover
    app.run()
