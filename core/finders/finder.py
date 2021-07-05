from abc import abstractmethod, ABC


class Finder:

    path = 'core/ui/static/music/'

    @abstractmethod
    def find(self, audio_name='default'):
        pass

    @abstractmethod
    def find_all(self):
        pass