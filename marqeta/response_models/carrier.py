from datetime import datetime, date
import json

class Carrier(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'template_id' : self.template_id,
           'logo_file' : self.logo_file,
           'logo_thumbnail_file' : self.logo_thumbnail_file,
           'message_file' : self.message_file,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def template_id(self):
        if 'template_id' in self.json_response:
            return self.json_response['template_id']

    @property
    def logo_file(self):
        if 'logo_file' in self.json_response:
            return self.json_response['logo_file']

    @property
    def logo_thumbnail_file(self):
        if 'logo_thumbnail_file' in self.json_response:
            return self.json_response['logo_thumbnail_file']

    @property
    def message_file(self):
        if 'message_file' in self.json_response:
            return self.json_response['message_file']

    def __repr__(self):
         return '<Marqeta.response_models.carrier.Carrier>'