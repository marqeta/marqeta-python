from datetime import datetime
from marqeta.response_models.gpa import Gpa
from marqeta.response_models.msa import Msa

class OrderScope(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def gpa(self):
        if 'gpa' in self.json_response:
            return Gpa(self.json_response['gpa'])

    @property
    def msa(self):
        if 'msa' in self.json_response:
            return Msa(self.json_response['msa'])

