from inspect import stack

from rocketry import Rocketry
from rocketry.args import Arg
from rocketry.conds import every

from incolume.py.prospect.rpa.gui.screen8 import screen8

app = Rocketry()
app.params(**screen8())


@app.task(every("1m"))
def task_a(username=Arg("username"), password=Arg("password")):
    """Run {stack()[0][3]}
    Return value.
    """
    print(username, password)


if __name__ == "__main__":  # pragma: no cover
    app.run()
