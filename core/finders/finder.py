from abc import abstractmethod, ABC


class Finder:



    @abstractmethod
    def find(self, audio_name='default'):
        pass

    @abstractmethod
    def find_all(self, path):
        pass