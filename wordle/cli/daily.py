import click

from ..client import WordleClient
from .helpers import play


@click.command('daily')
def __wordle_daily__():
    return play(WordleClient.word_of_the_day())
