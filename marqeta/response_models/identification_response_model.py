from datetime import datetime

class IdentificationResponseModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def type(self):
        if 'type' in self.json_response:
            return self.json_response['type']

    @property
    def value(self):
        if 'value' in self.json_response:
            return self.json_response['value']

    @property
    def expiration_date(self):
        if 'expiration_date' in self.json_response:
            return datetime.strptime(self.json_response['expiration_date'], '%Y-%m-%d').date()

