from datetime import datetime

class Carrier(object):

    def __init__(self, json_response):
        self.json_response = json_response

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

