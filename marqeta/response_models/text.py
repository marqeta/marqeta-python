from datetime import datetime, date
from marqeta.response_models.text_value import TextValue
from marqeta.response_models.text_value import TextValue
import json


class Text(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def name_line_1(self):

        if 'name_line_1' in self.json_response:
            return TextValue(self.json_response['name_line_1'])

    @property
    def name_line_2(self):

        if 'name_line_2' in self.json_response:
            return TextValue(self.json_response['name_line_2'])

    def __repr__(self):
        return '<Marqeta.response_models.text.Text>'
