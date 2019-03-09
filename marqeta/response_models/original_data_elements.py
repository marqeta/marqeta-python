from datetime import datetime

class OriginalDataElements(object):

    def __init__(self, json_response):
        self.json_response = json_response

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

