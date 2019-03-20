from datetime import datetime, date
import json

class Pos(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def pan_entry_mode(self):
        if 'pan_entry_mode' in self.json_response:
            return self.json_response['pan_entry_mode']

    @property
    def pin_entry_mode(self):
        if 'pin_entry_mode' in self.json_response:
            return self.json_response['pin_entry_mode']

    @property
    def terminal_id(self):
        if 'terminal_id' in self.json_response:
            return self.json_response['terminal_id']

    @property
    def terminal_attendance(self):
        if 'terminal_attendance' in self.json_response:
            return self.json_response['terminal_attendance']

    @property
    def terminal_location(self):
        if 'terminal_location' in self.json_response:
            return self.json_response['terminal_location']

    @property
    def card_holder_presence(self):
        if 'card_holder_presence' in self.json_response:
            return self.json_response['card_holder_presence']

    @property
    def cardholder_authentication_method(self):
        if 'cardholder_authentication_method' in self.json_response:
            return self.json_response['cardholder_authentication_method']

    @property
    def card_presence(self):
        if 'card_presence' in self.json_response:
            return self.json_response['card_presence']

    @property
    def terminal_type(self):
        if 'terminal_type' in self.json_response:
            return self.json_response['terminal_type']

    @property
    def card_data_input_capability(self):
        if 'card_data_input_capability' in self.json_response:
            return self.json_response['card_data_input_capability']

    @property
    def country_code(self):
        if 'country_code' in self.json_response:
            return self.json_response['country_code']

    @property
    def zip(self):
        if 'zip' in self.json_response:
            return self.json_response['zip']

    @property
    def partial_approval_capable(self):
        if 'partial_approval_capable' in self.json_response:
            return self.json_response['partial_approval_capable']

    @property
    def purchase_amount_only(self):
        if 'purchase_amount_only' in self.json_response:
            return self.json_response['purchase_amount_only']

    @property
    def is_recurring(self):
        if 'is_recurring' in self.json_response:
            return self.json_response['is_recurring']

    def __repr__(self):
         return '<Marqeta.response_models.pos.Pos>'