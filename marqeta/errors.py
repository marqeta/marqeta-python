class MarqetaError(Exception):

    def __init__(self, **kwargs):
        if 'error_message' in kwargs:
            self.message = kwargs['error_message']
        if 'error_code' in kwargs:
            self.code = kwargs['error_code']

    def __str__(self):
        try:
            return self.message + '\nError Code:' + self.code
        except:
            return self.message

    def __repr__(self):
        return '<Marqeta.errors.MarqetaError>'
