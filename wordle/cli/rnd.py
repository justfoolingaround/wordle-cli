import click

from ..client import WordleClient
from .helpers import play


@click.command('random')
def __wordle_random__():
    return play(WordleClient.random())
