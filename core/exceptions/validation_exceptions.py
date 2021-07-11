
class TitleValidationException(Exception):

    def __init__(self, msg):
        self.txt = 'Title is too {}'.format(msg)


class DescriptionValidationException(Exception):

    def __init__(self, msg):
        self.txt = 'Description is too {}'.format(msg)

class IconValidationException(Exception):

    def __init__(self):
        self.txt = 'You should choose icon'

class TimeValidationException(Exception):

    def __init__(self):
        self.txt = 'You should choose time delay'

