import os
import subprocess
import yaml
import sys
import time
from os.path import join
from pathlib import Path

# usage is:
#     python hak_packer.py pack
#     python hak_packer.py unpack


def main():
    command = str(sys.argv[1])

    config = yaml.safe_load(open("packer_settings.yaml"))
    # targetDir = 'target'

    print(f'Command is to {str(sys.argv[1])}')
    # if not os.path.isdir(targetDir):
    #     os.mkdir(targetDir)
    #     return
    
    if command == 'pack':
        pack()
    elif command == 'unpack':
        unpack(Path(config['hak']['from']), Path(config['hak']['to']))
    else:
        print('ERROR - unrecognized command. Use pack or unpack.')
    # clean up

    print(f'{command} complete')



def pack(hakPath):
    return
#     print(f'Packing hak files from {targetDir}')
#     packTic = time.perf_counter()

#     for root, subdirs, files in os.walk(targetDir):
#         for d in subdirs:
            

#     packToc = time.perf_counter()
#     print(f'Packed hak files to {hakDir} in {packToc - packTic:0.1f}s')



def unpack(hakPath, rawPath):
    if not os.path.isdir(hakPath):
        print(f'ERROR - invalid path to hak directory {hakPath}')
        return
    absHak = os.path.abspath(hakPath)

    if not os.path.isdir(rawPath):
        print(f'ERROR - invalid path to hak directory {rawPath}')
        return
    absRaw = os.path.abspath(rawPath)

    print(f'Unpacking hak files from {absHak}')
    unpackTic = time.perf_counter()
    
    for root, subdirs, files in os.walk(hakPath):
        for f in files:
            currentHak = join(absHak, f)
            targetHakDir = join(absRaw, os.path.splitext(f)[0])
            try:
                os.makedirs(targetHakDir)
            except FileExistsError:
                # directory already exists
                pass
            print(f'Unpacking {currentHak}')
            p = subprocess.Popen(["nwn_erf", '-f', currentHak, '-x'], cwd=targetHakDir)
            p.wait()
            print(f'Unpacked to {targetHakDir}')

    unpackToc = time.perf_counter()
    print(f'Unpacked hak files to {absRaw} in {unpackToc - unpackTic:0.1f}s')


if __name__ == "__main__":
    main()