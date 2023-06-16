from inspect import stack
from random import randint

from rocketry import Rocketry
from rocketry.conds import after_fail, after_finish, after_success, every

app = Rocketry()


@app.task(every("3s"))
def task_01():
    f"""Run {stack()[0][3]}
    Controlar fluxo de tarefas.
    """
    if randint(0, 1):
        raise SyntaxError("Quebrou!")
    print(f"Ran {stack()[0][3]}.")


@app.task(after_success(task_01))
def task_02():
    f"""Run {stack()[0][3]}
    Executa após sucesso da task_01.
    """
    print(f"Ran {stack()[0][3]}: task_01 ran with success.")


@app.task(after_finish(task_01))
def task_04():
    f"""Run {stack()[0][3]}
    Executa ao final do fluxo.
    """
    print(f"Ran {stack()[0][3]}: fluxo finished.")


@app.task(after_fail(task_01))
def task_03():
    f"""Run {stack()[0][3]}
    Executa se houver falha na task_01.
    """
    print(f"Ran {stack()[0][3]}: task_01 do not ran.")


if __name__ == "__main__":  # pragma: no cover
    app.run()
