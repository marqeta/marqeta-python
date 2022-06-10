from datetime import datetime, date
from marqeta.response_models import datetime_object
import json
import re


class CardholderNoteUpdateRequestModel(object):
    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def description(self):
        return self.json_response.get("description", None)

    def __repr__(self):
        return (
            "<Marqeta.response_models.cardholder_note_update_request_model.CardholderNoteUpdateRequestModel>"
            + self.__str__()
        )
