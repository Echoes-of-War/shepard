import click
import shepard.module as module

config = {}

@click.group()
@click.option('--library', default='lib', help='path to external dependencies')
def cli(library):
    config['library'] = library

@cli.group()
def mod():
    click.echo(f'perform module action {config["library"]}')

@cli.command()
def hak():
    click.echo(f'perform hak action {config["library"]}')

@cli.command()
@click.option('--src', prompt='directory to pack', help='path to module source directory')
@click.option('--dest', prompt='mod file to create', help='path to the mod file to create, must end in .mod')
def pack(src, dest):
    mod_packer = module.ModulePacker('win', src, src, config["library"])
    mod_packer.pack(dest)

@cli.command()
@click.option('--src', prompt='mod file to unpack', help='path to the mod file to unpack, must end in .mod')
@click.option('--dest', prompt='directory to unpack to', help='path to module source directory')
def unpack(src, dest):
    mod_packer = module.ModulePacker('win', dest, dest, config["library"])
    mod_packer.unpack(src)

mod.add_command(pack)
mod.add_command(unpack)

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
