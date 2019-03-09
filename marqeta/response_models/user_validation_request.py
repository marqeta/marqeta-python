from datetime import datetime

class UserValidationRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def birth_date(self):
        if 'birth_date' in self.json_response:
            return datetime.strptime(self.json_response['birth_date'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def phone(self):
        if 'phone' in self.json_response:
            return self.json_response['phone']

    @property
    def ssn(self):
        if 'ssn' in self.json_response:
            return self.json_response['ssn']

