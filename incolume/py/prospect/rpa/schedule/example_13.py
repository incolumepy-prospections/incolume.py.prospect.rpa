import datetime
from inspect import stack

from rocketry import Rocketry
from rocketry.args import Arg
from rocketry.conds import every

app = Rocketry()


@app.param()
def epoch():
    return datetime.datetime.utcnow().strftime("%s")


@app.task(every("3s"))
def task_a(value=Arg(epoch)):
    f"""Run {stack()[0][3]}
    Return value.
    """
    print(value)


if __name__ == "__main__":  # pragma: no cover
    app.run()
