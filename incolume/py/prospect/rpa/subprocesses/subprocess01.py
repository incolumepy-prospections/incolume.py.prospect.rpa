"""Tratativa para execução de subprocessos."""
import logging
import subprocess

__author__ = "@britodfbr"  # pragma: no cover


def tratativa01():
    """Run it."""
    return subprocess.call("ls")


def tratativa02():
    """Run it."""
    return subprocess.call(["ls", "-lha"])


def tratativa03():
    """Run it."""
    return subprocess.check_call(["false"])


def tratativa04():
    """Run it."""
    return subprocess.call("ls -lha", shell=True)


def tratativa05():
    """Run it."""
    return subprocess.Popen("ls -lah", shell=True)


def tratativa06():
    """Run it."""
    return subprocess.Popen(
        "ls -lah", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )


def run():
    """Run it."""
    # tratativa01()
    # tratativa02()
    # tratativa03()
    for x in ["tratativa{:02}".format(x) for x in range(1, 10)]:
        try:
            func = eval(x)
            print(f"--- {func.__name__} ---")
            print(f"{func.__doc__}")
            print("-------------------------")
            print(func())
            print("---")
        except subprocess.CalledProcessError as e:
            logging.error("%s: %s", x, e)
        except NameError as e:
            logging.error(e)


if __name__ == "__main__":  # pragma: no cover
    run()
