class MarqetaError(Exception):

    def __init__(self, code, message):
        self.message = message
        self.code = code

    def __str__(self):
        return 'MarqetaError:' + self.message +'\nError Code:' + self.code

    def __repr__(self):
        return '{ Error :'+self.message +',code: '+   self.code +'}'