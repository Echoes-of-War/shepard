import subprocess
import os
from os.path import join

class Compiler:
    def __init__(self, nwnsc, srcDir, tempDir, libDir):
        self.nwnsc = nwnsc
        self.srcDir = srcDir
        self.tempDir = tempDir
        self.libDir = libDir

    def compile(self, file):
        outfile = os.path.splitext(file)[0] + '.ncs'
        p = subprocess.Popen([self.nwnsc, '-qw', '-n', self.libDir, '-r', join(self.tempDir, outfile), '-i', self.srcDir, join(self.srcDir, file)])
        p.wait()