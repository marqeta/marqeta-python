from datetime import datetime, date
from marqeta.response_models import datetime_object
import json
import re

class CardholderNoteRequestModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def token(self):
        return self.json_response.get('token', None)


    @property
    def description(self):
        return self.json_response.get('description', None)


    @property
    def created_by(self):
        return self.json_response.get('created_by', None)


    @property
    def created_by_user_role(self):
        return self.json_response.get('created_by_user_role', None)


    @property
    def private(self):
        return self.json_response.get('private', None)

    def __repr__(self):
         return '<Marqeta.response_models.cardholder_note_request_model.CardholderNoteRequestModel>' + self.__str__()
