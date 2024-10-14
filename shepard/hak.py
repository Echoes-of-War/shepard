import os
import subprocess
import time
import sys
from os.path import join


class HakPacker:
    def __init__(self, targetDir, tempDir, libDir):
        os = 'linux'
        if sys.platform.startswith('win'):
            os = 'win'
        elif sys.platform.startswith('darwin'):
            os = 'macos'

        self.nwn_erf = join(libDir, os, 'nwn_erf')
        # self.nwn_gff = join(libDir, os, 'nwn_gff')
        # self.nwnsc = join(libDir, os, 'nwnsc')
        self.targetDir = targetDir
        # self.tempDir = tempDir
        self.libDir = libDir


    def pack(self, hakPath):
        return
    #     print(f'Packing hak files from {targetDir}')
    #     packTic = time.perf_counter()

    #     for root, subdirs, files in os.walk(targetDir):
    #         for d in subdirs:
                

    #     packToc = time.perf_counter()
    #     print(f'Packed hak files to {hakDir} in {packToc - packTic:0.1f}s')



    def unpack(self, hakPath):
        if not os.path.isdir(hakPath):
            print(f'ERROR - invalid path to hak directory {hakPath}')
            return
        absHak = os.path.abspath(hakPath)

        if not os.path.isdir(self.targetDir):
            print(f'ERROR - invalid path to target directory {self.targetDir}')
            return
        absRaw = os.path.abspath(self.targetDir)

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
                p = subprocess.Popen([self.nwn_erf, '-f', currentHak, '-x'], cwd=targetHakDir, shell=True)
                p.wait()
                print(f'Unpacked to {targetHakDir}')

        unpackToc = time.perf_counter()
        print(f'Unpacked hak files to {absRaw} in {unpackToc - unpackTic:0.1f}s')

