from datetime import datetime, date
import json

class Device(object):

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
        if 'token' in self.json_response:
            return self.json_response['token']

    @property
    def type(self):
        if 'type' in self.json_response:
            return self.json_response['type']

    @property
    def language_code(self):
        if 'language_code' in self.json_response:
            return self.json_response['language_code']

    @property
    def device_id(self):
        if 'device_id' in self.json_response:
            return self.json_response['device_id']

    @property
    def phone_number(self):
        if 'phone_number' in self.json_response:
            return self.json_response['phone_number']

    @property
    def name(self):
        if 'name' in self.json_response:
            return self.json_response['name']

    @property
    def location(self):
        if 'location' in self.json_response:
            return self.json_response['location']

    @property
    def ip_address(self):
        if 'ip_address' in self.json_response:
            return self.json_response['ip_address']

    def __repr__(self):
         return '<Marqeta.response_models.device.Device>'