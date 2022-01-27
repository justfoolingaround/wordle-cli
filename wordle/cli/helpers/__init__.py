import rich
from rich.rule import Rule

MESSAGES = {
    0: '[green bold]Magnificient![/green bold]',
    20: '[green]Splendid![/]',
    40: '[cyan bold]Sweet![/cyan bold]',
    60: '[cyan]Not bad![/]',
    80: '[cyan]Phew~[/]',
}

def play(client):

    console = rich.console.Console()
    console.print(Rule("WORDLE.py"))

    completed = False

    while (not completed) and client.max_attempt > (client.attempt_count):
        word = console.input("[i]Your[/] guess:").lower()

        while (word not in client.all_words) or len(word) != len(client.word):            
            if len(word) != len(client.word):
                console.print("[red bold]The word size mismatches with the [green]WORDLE[/green]'s word size, try again.[/]")
            else:
                console.print("[red bold]Could not find the word in the word list, try again.[/]")
            
            word = console.input("[i]Your[/] guess:").lower()

        completed = client.play(word)
        client.rich_print()

    if completed:
        for threshold, message in MESSAGES.items():
            if threshold >= (client.attempt_count / client.max_attempt) * 100:
                return console.print("You did it, you found [green]{}[/] in {} tries! {}".format(client.word, client.attempt_count, message))
        
    else:
        return console.print("Oops, max tries exceeded, the word was [green bold]{}[/green bold]!".format(client.word))
