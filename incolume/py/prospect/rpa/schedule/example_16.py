from inspect import stack

from rocketry import Rocketry
from rocketry.args import Arg
from rocketry.conds import every

from incolume.py.prospect.rpa.gui.screen10 import screen10

app = Rocketry()
app.params(**screen10())


@app.task(every("3m"))
def task_a(username=Arg("username"), password=Arg("password")):
    f"""Run {stack()[0][3]}
    Return value.
    """
    print(username, password)


if __name__ == "__main__":  # pragma: no cover
    app.run()
