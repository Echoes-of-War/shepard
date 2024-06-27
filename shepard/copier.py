import shutil
from os.path import join

class Copier:
    def __init__(self, fromDir, toDir):
        self.fromDir = fromDir
        self.toDir = toDir

    def copy(self, file):
        shutil.copyfile(join(self.fromDir, file), join(self.toDir, file))