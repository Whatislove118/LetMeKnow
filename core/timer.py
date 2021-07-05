from threading import Thread

from notifypy import Notify


class Timer(Thread):

    def __init__(self, finish_time, notify: Notify):
        Thread.__init__(self)
        self.finish_time = finish_time
        self.notify = notify

    def run(self):
        print("Starting doing {}" % self.notify.title)









