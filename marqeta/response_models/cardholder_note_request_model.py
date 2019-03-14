from datetime import datetime, date
import json

class CardholderNoteRequestModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'token' : self.token,
           'description' : self.description,
           'created_by' : self.created_by,
           'created_by_user_role' : self.created_by_user_role,
           'private' : self.private,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

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

    def __repr__(self):
         return '<Marqeta.response_models.cardholder_note_request_model.CardholderNoteRequestModel>'