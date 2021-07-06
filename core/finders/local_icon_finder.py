import os

from core.finders.finder import Finder


class LocalIconFinder(Finder):
    __instance = None

    def __init__(self):
        if not LocalIconFinder.__instance:
            print(" __init__ method called..")
            self.path = 'core/ui/static/icons/'
            self.icon_list = []
            os.chdir(self.path)
        else:
            print("Instance already created:", self.getInstance())

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = LocalIconFinder()
        return cls.__instance



    def find_all(self):
        files = os.walk('.')
        files = self.get_filenames_from_directory(files=files)
        self.icon_list = files

    def get_filenames_from_directory(self, files) -> list:
        result = []
        for dirpath, dirnames, filenames in os.walk("."):
            for filename in filenames:
                result.append(filename.split('.')[0])
        return result

    def get_icon_file_by_name(self, name):
        for o in os.walk('.'):
            print(o)