from datetime import datetime

class CardholderNoteRequestModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def token(self):
        if 'token' in self.json_response:
            return self.json_response['token']

    @property
    def description(self):
        if 'description' in self.json_response:
            return self.json_response['description']

    @property
    def created_by(self):
        if 'created_by' in self.json_response:
            return self.json_response['created_by']

    @property
    def created_by_user_role(self):
        if 'created_by_user_role' in self.json_response:
            return self.json_response['created_by_user_role']

    @property
    def private(self):
        if 'private' in self.json_response:
            return self.json_response['private']

