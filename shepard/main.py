import click
import os
import shepard.module as module

libDir = os.path.join(os.path.dirname(__file__), 'ext')
tmpDir = os.path.join(os.path.dirname(__file__), 'tmp')
if not os.path.exists(tmpDir):
   os.makedirs(tmpDir)

@click.group()
def cli():
    pass

@cli.group()
def mod():
    click.echo(f'perform module action {libDir}')

@cli.command()
def hak():
    click.echo(f'perform hak action {libDir}')

@cli.command()
@click.option('--src', prompt='directory to pack', help='path to module source directory')
@click.option('--dest', prompt='mod file to create', help='path to the mod file to create, must end in .mod')
def pack(src, dest):
    mod_packer = module.ModulePacker(src, tmpDir, libDir)
    mod_packer.pack(dest)

@cli.command()
@click.option('--src', prompt='mod file to unpack', help='path to the mod file to unpack, must end in .mod')
@click.option('--dest', prompt='directory to unpack to', help='path to module source directory')
def unpack(src, dest):
    mod_packer = module.ModulePacker(dest, tmpDir, libDir)
    mod_packer.unpack(src)

mod.add_command(pack)
mod.add_command(unpack)

cli.add_command(mod)
cli.add_command(hak)

