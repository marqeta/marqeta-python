
class MarqetaError(Exception):

    def __init__(self, code, message):
        self.message = message
        self.code = code

    def __str__(self):
        return repr(self.message)









