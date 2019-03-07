class CardMetadata(object):

    def __init__(self, response):
        self.response = response

    @property
    def metadata(self):
        if 'metadata' in self.response:
            return self.response['metadata']



