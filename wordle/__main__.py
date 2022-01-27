import click

from .cli import daily, rnd

commands = {
    "random": rnd.__wordle_random__,
    "daily": daily.__wordle_daily__,
}

__version__ = "0.1"

@click.group(commands=commands)
@click.version_option(__version__, "-v")
def __wordle_cli__():
    pass

if __name__ == "__main__":
    __wordle_cli__()
