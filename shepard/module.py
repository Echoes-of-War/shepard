import subprocess
import os
import time
import multiprocessing
from os.path import join
import shepard.converter as converter
import shepard.compiler as compiler
import shepard.copier as copier


class ModulePacker:
    def __init__(self, os, targetDir, tempDir, libDir):
        self.nwn_erf = join(libDir, os, 'nwn_erf')
        self.nwn_gff = join(libDir, os, 'nwn_gff')
        self.nwnsc = join(libDir, os, 'nwnsc')
        self.targetDir = targetDir
        self.tempDir = tempDir
        self.libDir = libDir

    def unpack(self, modulePath):
        if not os.path.isfile(modulePath):
            print(f'ERROR - invalid path to module {modulePath}')
            return
        absModule = os.path.abspath(modulePath)

        print(f'Unpacking {absModule}')
        unpackTic = time.perf_counter()
        p = subprocess.Popen([self.nwn_erf, '-f', absModule, '-x'], cwd=self.tempDir, shell=True)
        p.wait()
        unpackToc = time.perf_counter()
        print(f'Unpacked module to {self.tempDir} in {unpackToc - unpackTic:0.1f}s')

        gffFiles = []
        scriptFiles = []
        for f in os.listdir(self.tempDir):
            ext = os.path.splitext(f)[1]
            if ext == '.nss':
                scriptFiles.append(f)
            elif ext != '.ncs':
                gffFiles.append(f)

        # Greedily try to use all of the cores except for one
        p = multiprocessing.Pool(multiprocessing.cpu_count() - 1) 

        print('Converting gff files')
        convertTic = time.perf_counter()
        conv = converter.Converter(self.nwn_gff, self.targetDir, self.tempDir)
        p.map(conv.from_gff, gffFiles)
        convertToc = time.perf_counter()
        print(f'Converted gff files in {convertToc - convertTic:0.1f}s')

        print('Copying script files')
        copyTic = time.perf_counter()
        subdir = join(self.targetDir, 'scripts')
        try:
            os.makedirs(subdir)
        except FileExistsError:
            # directory already exists
            pass
        cop = copier.Copier(self.tempDir, subdir)
        p.map(cop.copy, scriptFiles)
        copyToc = time.perf_counter()
        print(f'Copied script files {copyToc - copyTic:0.1f}s')

    def pack(self, modulePath):
        if os.path.isfile(modulePath) or os.path.isdir(modulePath):
            print(f'ERROR - already exists {modulePath}')
            return
        absModule = os.path.abspath(modulePath)

        gffFiles = []
        scriptFiles = []
        for root, subdirs, files in os.walk(self.targetDir):
            for f in files:
                ext = os.path.splitext(f)[1]
                if ext == '.nss':
                    scriptFiles.append(f)
                elif ext != '':
                    gffFiles.append(f)

        # Greedily try to use all of the cores except for one
        p = multiprocessing.Pool(multiprocessing.cpu_count() - 1) 

        print('Compiling scripts')
        compileTic = time.perf_counter()
        comp = compiler.Compiler(self.nwnsc, join(self.targetDir, 'scripts'), self.tempDir, self.libDir)
        p.map(comp.compile, scriptFiles)
        compileToc = time.perf_counter()
        print(f'Compiled scripts in {compileToc - compileTic:0.1f}s')

        print('Converting gff files')
        convertTic = time.perf_counter()
        conv = converter.Converter(self.nwn_gff, self.targetDir, self.tempDir)
        p.map(conv.to_gff, gffFiles)
        convertToc = time.perf_counter()
        print(f'Converted gff files in {convertToc - convertTic:0.1f}s')

        print('Copying script files')
        copyTic = time.perf_counter()
        cop = copier.Copier(join(self.targetDir, 'scripts'), self.tempDir)
        p.map(cop.copy, scriptFiles)
        copyToc = time.perf_counter()
        print(f'Copied script files {copyToc - copyTic:0.1f}s')

        print(f'Packing {absModule}')
        packTic = time.perf_counter()
        p = subprocess.Popen([self.nwn_erf, '-e', 'MOD', '-f', modulePath, '-c', self.tempDir], shell=True)
        p.wait()
        packToc = time.perf_counter()
        print(f'Packed module to {absModule} in {packToc - packTic:0.1f}s')
