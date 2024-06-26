import click

@click.group()
def cli():
    pass

@cli.command()
def mod():
    click.echo('perform module action')

@cli.command()
def hak():
    click.echo('perform hak action')

cli.add_command(mod)
cli.add_command(hak)

# @click.command()
# @click.option('--count', default=1, help='Number of greetings.')
# @click.option('--name', prompt='Your name',
#               help='The person to greet.')
# def hello(count, name):
#     """Simple program that greets NAME for a total of COUNT times."""
#     for x in range(count):
#         click.echo(f"Hello {name}!")

if __name__ == '__main__':
    cli()