
class Validator:

    def validate(self, event, window):
        title = window['__TITLE__'].get()
        description = window['__DESC__'].get()




    def _validate_title(self, title):
        if len(title) == 0:
            pass
