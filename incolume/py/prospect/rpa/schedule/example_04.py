"""Run it."""
from inspect import stack

from rocketry import Rocketry
from rocketry.conds import daily, minutely, monthly, weekly

app = Rocketry()


@app.task("minutely after 10")
def restrictives0():
    """Restrictives 0.

    Executa após segundo 10 de cada minuto.
    """
    print(f"Ran {stack()[0][3]}.")


@app.task("hourly after 10:17")
def restrictives1():
    """Run it.

    Executa após  10'17"  de cada hora.
    """
    print(f"Ran {stack()[0][3]}.")


@app.task("hourly after 10:16:08")
def restrictives2():
    """Run it.

    Executa após  10'16"08 milisec de cada hora.
    """
    print(f"Ran {stack()[0][3]}.")


@app.task(minutely.after("10"))
def restrictives3():
    """Run it.

    Executa após segundo 10 de cada minuto.
    """
    print(f"Ran {stack()[0][3]}.")


@app.task(minutely.before("10"))
def restrictives4():
    """Run it.

    Executa antes do segundo 10 de cada minuto.
    """
    print(f"Ran {stack()[0][3]}.")


@app.task(minutely.between("10", "50"))
def restrictives5():
    """Run it.

    Executa entre o segundo 10 e 50 de cada minuto.
    """
    print(f"Ran {stack()[0][3]}.")


@app.task("daily after 23")
def restrictives6():
    """Run it.

    Executa todo dia após 23h.
    """
    print(f"Ran {stack()[0][3]}.")


@app.task(daily.after("23"))
def restrictives7():
    """Run it.

    Executa todo dia após 23h.
    """
    print(f"Ran {stack()[0][3]}.")


@app.task("daily between 00:00 and 00:01")
def restrictives8():
    """Run it.

    Executa todo dia entre o 00:00h e 00:01h.
    """
    print(f"Ran {stack()[0][3]}.")


@app.task(daily.between("00:00", "00:01"))
def restrictives9():
    """Run it.

    Executa todo dia entre o 00:00h e 00:01h.
    """
    print(f"Ran {stack()[0][3]}.")


@app.task("weekly between Monday and Friday")
def testrictives10():
    """Run it.

    Executa semanalmente entre segunda e sexta
    """
    print(f"Ran {stack()[0][3]}.")


@app.task("weekly on Monday")
def testrictives11():
    """Run it.

    Executa semanalmente toda segunda
    """
    print(f"Ran {stack()[0][3]}.")


@app.task(weekly.on("Monday"))
def testrictives12():
    """Run it.

    Executa semanalmente toda segunda
    """
    print(f"Ran {stack()[0][3]}.")


@app.task("monthly starting 8rd")
def testrictives13():
    """Run it.

    Executa mensalmente após dia 8
    """
    print(f"Ran {stack()[0][3]}.")


@app.task(monthly.starting("8rd"))
def testrictives14():
    """Run it.

    Executa mensalmente após dia 8
    """
    print(f"Ran {stack()[0][3]}.")


if __name__ == "__main__":  # pragma: no cover
    app.run()
