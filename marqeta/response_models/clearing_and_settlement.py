from datetime import datetime

class ClearingAndSettlement(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def overdraft_destination(self):
        if 'overdraft_destination' in self.json_response:
            return self.json_response['overdraft_destination']

