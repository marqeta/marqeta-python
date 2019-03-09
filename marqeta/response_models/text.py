from datetime import datetime
from marqeta.response_models.text_value import TextValue
from marqeta.response_models.text_value import TextValue

class Text(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def name_line_1(self):
        if 'name_line_1' in self.json_response:
            return TextValue(self.json_response['name_line_1'])

    @property
    def name_line_2(self):
        if 'name_line_2' in self.json_response:
            return TextValue(self.json_response['name_line_2'])

