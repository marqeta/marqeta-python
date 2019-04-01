from datetime import datetime, date
import json


class DigitalWalletTokenDevice(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def device_type(self):
        return self.json_response.get('device_type', None)

    @property
    def device_lang_code(self):
        return self.json_response.get('device_lang_code', None)

    @property
    def device_id(self):
        return self.json_response.get('device_id', None)

    @property
    def device_number(self):
        return self.json_response.get('device_number', None)

    @property
    def device_name(self):
        return self.json_response.get('device_name', None)

    @property
    def device_location(self):
        return self.json_response.get('device_location', None)

    @property
    def device_ip_address(self):
        return self.json_response.get('device_ip_address', None)

    def __repr__(self):
        return '<Marqeta.response_models.digital_wallet_token_device.DigitalWalletTokenDevice>' + self.__str__()
