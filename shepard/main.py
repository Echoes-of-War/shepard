import click
import os
import shepard.module as module
import shepard.hak

libDir = os.path.join(os.path.dirname(__file__), 'ext')
tmpDir = os.path.join(os.path.dirname(__file__), 'tmp')
if not os.path.exists(tmpDir):
   os.makedirs(tmpDir)

@click.group()
def cli():
    pass

@cli.group()
def mod():
    click.echo(f'performing module action')

@cli.command()
@click.option('--src', prompt='directory to pack', help='path to module source directory')
@click.option('--dest', prompt='mod file to create', help='path to the mod file to create, must end in .mod')
def mod_pack(src, dest):
    mod_packer = module.ModulePacker(src, tmpDir, libDir)
    mod_packer.pack(dest)

@cli.command()
@click.option('--src', prompt='mod file to unpack', help='path to the mod file to unpack, must end in .mod')
@click.option('--dest', prompt='directory to unpack to', help='path to module source directory')
def mod_unpack(src, dest):
    mod_packer = module.ModulePacker(dest, tmpDir, libDir)
    mod_packer.unpack(src)

@cli.group()
def hak():
    click.echo(f'performing hak action')

@cli.command()
@click.option('--src', prompt='directory to pack', help='path to raw source directory')
@click.option('--dest', prompt='directory to pack to', help='path to the directory to fill with .hak files')
def hak_pack(src, dest):
    hak_packer = shepard.hak.HakPacker(src, libDir)
    hak_packer.pack(dest)

@cli.command()
@click.option('--src', prompt='directory of unpack', help='path to the directory of .hak files to unpack from')
@click.option('--dest', prompt='directory to unpack to', help='path to the directory unpack raw data into')
def hak_unpack(src, dest):
    hak_packer = shepard.hak.HakPacker(dest, libDir)
    hak_packer.unpack(src)

mod.add_command(mod_pack)
mod.add_command(mod_unpack)

hak.add_command(hak_pack)
hak.add_command(hak_unpack)

cli.add_command(mod)
cli.add_command(hak)

