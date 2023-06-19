"""Examples."""
import logging
from inspect import stack

from rocketry import Rocketry
from rocketry.args import FuncArg
from rocketry.conds import every

from incolume.py.prospect.rpa.gui.screen8 import screen8

app = Rocketry()


@app.task(every("1d"))
def task_a(value=FuncArg(screen8)):
    """Run it.

    Return value.
    """
    logging.debug(stack()[0][3])
    print(value)


if __name__ == "__main__":  # pragma: no cover
    app.run()
