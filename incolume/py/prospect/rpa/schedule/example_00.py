"""Run it."""
from rocketry import Rocketry

app = Rocketry()


@app.task("minutely")
def a_cada_minuto():
    """Run it."""
    print("minuto a minuto")


@app.task("hourly")
def a_cada_hora():
    """Run it."""
    print("toda hora")


@app.task("daily")
def a_cada_dia():
    """Run it."""
    print("todo dia")


@app.task("weekly")
def a_cada_semana():
    """Run it."""
    print("toda semana")


@app.task("monthly")
def a_cada_mes():
    """Run it."""
    print("todo mes")


if __name__ == "__main__":
    app.run()
