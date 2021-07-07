import os
from threading import Thread


class ThreadFinder(Thread):


    def __init__(self, name, path):
        Thread.__init__(self)
        self.name = name
        self.files = []
        self.path = path


    def run(self):
        print('Start thread')
        files = self.get_filenames_from_directory()
        self.files = files


    def get_filenames_from_directory(self) -> list:
        result = []
        for dirpath, dirnames, filenames in os.walk(self.path):
            for filename in filenames:
                result.append(filename.split('.')[0])
        return result
