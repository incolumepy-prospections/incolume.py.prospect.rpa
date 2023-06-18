from inspect import stack
from random import randint

from rocketry import Rocketry
from rocketry.args import Return
from rocketry.conds import after_success, every

app = Rocketry()


@app.task(every("3s"))
def task_a():
    """Run {stack()[0][3]}
    Return value.
    """
    return randint(1, 10)


@app.task(every("1s"))
def task_b():
    """Run {stack()[0][3]}
    Return value.
    """
    return randint(1, 10)


@app.task(after_success(task_b))
def task_02(tres=Return(task_a), todo=Return(task_b)):
    """Run {stack()[0][3]}
    Recebe o parametro da task_01.
    """
    print(f"Ran {stack()[0][3]}: {tres=} {todo=}")


if __name__ == "__main__":  # pragma: no cover
    app.run()
