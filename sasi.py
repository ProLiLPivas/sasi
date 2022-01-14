import os
from typing import List

"""
S.A.S.I.
    S - same
    A - apps
    S - structure
    I - interface
"""

class File:

    def __init__(self, name):
        self.name = name
        self.path = ''
        self.level = 1
        self.text = ''

    def with_text(self, text):
        self.text += text
        return self

    def with_imports(self):
        ...

    def with_class(self):
        ...

    def create(self, path):
        with open(path + '/' + self.name, 'w') as f: f.write(self.text)

    def view(self, res='', level=0, sep='|____'):
        res += f"{'|   ' * (level - 1) }{sep} {self.name} \n"
        return res


class Folder:

    def __init__(self, name, is_package=False):
        self.name = name
        self.path = ''
        self.is_package = is_package
        self.folders = []
        self.files: List[File] = []

    def folder(self, folder):
        folder.path = self.path + self.name
        self.folders.append(folder)
        return self

    def file(self, file: File):
        file.path = self.path
        self.files.append(file)
        return self

    def create(self, path=os.getcwd()):
        new_path = path + '/' + self.name
        os.mkdir(new_path)
        for folder in self.folders:
            folder.create(new_path)
        for file in self.files:
            file.create(new_path)
        if self.is_package:
            self.__create_init(new_path)

    def __create_init(self, path):
        init_file = File('__init__.py')
        for file in self.files:
            init_file.with_text(f"from {file.name.replace('.py', '')} import *\n")
        init_file.create(path)

    def view(self, res='', level=0, sep='|____'):
        if level == 0:
            res += f'[ {self.name.upper()} ]\n'
        else:
            res += f"{'|   ' * (level - 1)}{sep} {self.name} \n"

        for folder in self.folders:
            res = folder.view(res, level+1)
        for file in self.files:
            res = file.view(res, level+1)
            if self.is_package: res+= f"{'|   ' * (level - 1)}{sep}__init__.py\n"
        return res

class App:

    def __init__(self, name):

        root_folder = ''

def crate_example():
