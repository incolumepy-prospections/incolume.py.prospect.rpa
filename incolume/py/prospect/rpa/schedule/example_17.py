"""Modulo de Tratativa."""
from rocketry import Rocketry
from rocketry.args import Return
from rocketry.conds import after_success, daily

app = Rocketry()


@app.task(daily)
def do_first():
    """Return hello."""
    return "Hello World"


@app.task(after_success(do_first))
def do_second(arg=Return(do_first)):
    """Run do_second."""
    print(arg)


if __name__ == "__main__":
    app.run()
