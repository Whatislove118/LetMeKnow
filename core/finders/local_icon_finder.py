import os
from copy import copy

from core.finders.finder import Finder
from core.threads.thread_finder import ThreadFinder


class LocalIconFinder(Finder):
    __instance = None

    def __init__(self):
        if not LocalIconFinder.__instance:
            print(" __init__ method called..")
            self.icon_list = []
        else:
            print("Instance already created:", self.getInstance())

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = LocalIconFinder()
        return cls.__instance

    def format_names(self):
        result = copy(self.icon_list)
        for i, icon in enumerate(self.icon_list):
            result[i] = icon.split('/').pop().split('.')[0]
        return result
            

    def find_all(self, path):
        thread_finder = ThreadFinder('Finder icon', path)
        thread_finder.start()
        while thread_finder.is_alive():
            pass
        for i, f in enumerate(thread_finder.files):
            thread_finder.files[i] = path + f + '.png'
        self.icon_list = thread_finder.files



    def get_filenames_from_directory(self, path) -> list:
        result = []
        for dirpath, dirnames, filenames in os.walk(path):
            for filename in filenames:
                result.append(filename.split('.')[0])
        return result

    def find_by_name(self, name, path):
        thread_finder = ThreadFinder('Finder icon', path)
        thread_finder.start()
        print(name)
        while thread_finder.is_alive():
            pass
        print(thread_finder.files)
        for f in thread_finder.files:
            if f == name:
                return path + name + '.png'