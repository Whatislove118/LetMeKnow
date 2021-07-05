class NotValidFinishTimeException(Exception):

    def __init__(self):
        self.txt = "Finish time must be greater than current time"

