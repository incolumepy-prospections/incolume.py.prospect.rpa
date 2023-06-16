from rocketry import Rocketry
from rocketry.args import Return
from rocketry.conds import after_success, daily

app = Rocketry()


@app.task(daily)
def do_first():
    return "Hello World"


@app.task(after_success(do_first))
def do_second(arg=Return(do_first)):
    print(arg)


if __name__ == "__main__":
    app.run()
