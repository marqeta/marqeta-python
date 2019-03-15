from datetime import datetime, date
import json

class OriginalDataElements(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'mti' : self.mti,
           'stan' : self.stan,
           'transmission_time' : self.transmission_time,
           'acquiring_institution_id' : self.acquiring_institution_id,
           'network_reference_id' : self.network_reference_id,
           'forwarding_institution_id' : self.forwarding_institution_id,
           'transaction_token' : self.transaction_token,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def mti(self):
        if 'mti' in self.json_response:
            return self.json_response['mti']

    @property
    def stan(self):
        if 'stan' in self.json_response:
            return self.json_response['stan']

    @property
    def transmission_time(self):
        if 'transmission_time' in self.json_response:
            return self.json_response['transmission_time']

    @property
    def acquiring_institution_id(self):
        if 'acquiring_institution_id' in self.json_response:
            return self.json_response['acquiring_institution_id']

    @property
    def network_reference_id(self):
        if 'network_reference_id' in self.json_response:
            return self.json_response['network_reference_id']

    @property
    def forwarding_institution_id(self):
        if 'forwarding_institution_id' in self.json_response:
            return self.json_response['forwarding_institution_id']

    @property
    def transaction_token(self):
        if 'transaction_token' in self.json_response:
            return self.json_response['transaction_token']

    def __repr__(self):
         return '<Marqeta.response_models.original_data_elements.OriginalDataElements>'