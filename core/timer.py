import time
from threading import Thread

from notifypy import Notify


class Timer(Thread):

    def __init__(self, data: dict):
        Thread.__init__(self)
        self.finish_time = data['time']
        self.notify = Notify()
        self.notify.application_name = 'LetMeKnow'
        self.notify.title = data['title']
        self.notify.icon = data['icon']
        self.notify.audio = data['audio']
        self.notify.message = data['description']
        self.delay = data['time']

    def run(self):
        print("Starting doing {}".format(self.notify.title))
        time.sleep(self.delay)
        self.notify.send()









