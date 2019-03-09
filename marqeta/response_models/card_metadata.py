class CardMetadata(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def metadata(self):
        if 'metadata' in self.json_response:
            return self.json_response['metadata']

