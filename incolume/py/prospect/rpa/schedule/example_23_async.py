import asyncio
from inspect import stack

from rocketry import Rocketry
from rocketry.conds import every

app = Rocketry(execution="async")


@app.task(every("1m"))
async def do_things():
    f"""Run {stack()[0][3]}"""
    print(stack()[0][3])


async def main():
    """Launch Rocketry app (and possibly something else)"""
    rocketry_task = asyncio.create_task(app.serve())
    # Start possibly other async apps
    await rocketry_task


if __name__ == "__main__":
    print(asyncio.run(main()))
