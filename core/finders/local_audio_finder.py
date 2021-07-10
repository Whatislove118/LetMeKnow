import os

from core.finders.finder import Finder
from core.threads.thread_finder import ThreadFinder


class LocalAudioFinder(Finder):
    __instance = None
    # __thread_finder = None

    def __init__(self):
        if not LocalAudioFinder.__instance:
            print(" __init__ method called..")
            self.audio_list = []
        else:
            print("Instance already created:", self.getInstance())

    @classmethod
    def getInstance(cls):
        # os.chdir(cls.path)
        if not cls.__instance:
            cls.__instance = LocalAudioFinder()
        return cls.__instance

    def find_by_name(self, name, path):
        thread_finder = ThreadFinder('Finder music', path)
        thread_finder.start()
        print(name)
        while thread_finder.is_alive():
            pass
        print(thread_finder.files)
        for f in thread_finder.files:
            if f == name:
                return path + name + '.wav'


    def find_all(self, path):
        thread_finder = ThreadFinder('Finder music', path)
        thread_finder.start()
        while thread_finder.is_alive():
            pass
        self.audio_list = thread_finder.files

    def get_filenames_from_directory(self, path) -> list:
        result = []
        for dirpath, dirnames, filenames in os.walk(path):
            for filename in filenames:
                result.append(filename.split('.')[0])
        return result

