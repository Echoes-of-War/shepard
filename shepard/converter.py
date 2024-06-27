import subprocess
import os
from os.path import join

class Converter:
    def __init__(self, nwn_gff, srcDir, tempDir):
        self.nwn_gff = nwn_gff
        self.srcDir = srcDir
        self.tempDir = tempDir

    def from_gff(self, file):
        subdir = join(self.srcDir, 'resources', os.path.splitext(file)[1][1:])
        try:
            os.makedirs(subdir)
        except FileExistsError:
            # directory already exists
            pass
        outputJson = file + '.json'
        p = subprocess.Popen([self.nwn_gff, '-i', join(self.tempDir, file), '-o', join(subdir, outputJson), '-p'])
        p.wait()

    def to_gff(self, file):
        subdir = join(self.srcDir, 'resources', os.path.splitext(os.path.splitext(file)[0])[1][1:])
        outputGff = os.path.splitext(file)[0]
        p = subprocess.Popen([self.nwn_gff, '-i', join(subdir, file), '-o', join(self.tempDir, outputGff)])
        p.wait()