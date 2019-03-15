from datetime import datetime, date
import json

class DigitalWalletTokenDevice(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'device_type' : self.device_type,
           'device_lang_code' : self.device_lang_code,
           'device_id' : self.device_id,
           'device_number' : self.device_number,
           'device_name' : self.device_name,
           'device_location' : self.device_location,
           'device_ip_address' : self.device_ip_address,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def device_type(self):
        if 'device_type' in self.json_response:
            return self.json_response['device_type']

    @property
    def device_lang_code(self):
        if 'device_lang_code' in self.json_response:
            return self.json_response['device_lang_code']

    @property
    def device_id(self):
        if 'device_id' in self.json_response:
            return self.json_response['device_id']

    @property
    def device_number(self):
        if 'device_number' in self.json_response:
            return self.json_response['device_number']

    @property
    def device_name(self):
        if 'device_name' in self.json_response:
            return self.json_response['device_name']

    @property
    def device_location(self):
        if 'device_location' in self.json_response:
            return self.json_response['device_location']

    @property
    def device_ip_address(self):
        if 'device_ip_address' in self.json_response:
            return self.json_response['device_ip_address']

    def __repr__(self):
         return '<Marqeta.response_models.digital_wallet_token_device.DigitalWalletTokenDevice>'