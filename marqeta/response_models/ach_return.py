from datetime import datetime, date
import json

class AchReturn(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'amount' : self.amount,
           'date' : self.date,
           'dateInitiated' : self.dateInitiated,
           'orderId' : self.orderId,
           'reasonCode' : self.reasonCode,
           'directDeposit' : self.directDeposit,
           'achType' : self.achType,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def amount(self):
        if 'amount' in self.json_response:
            return self.json_response['amount']

    @property
    def date(self):
        if 'date' in self.json_response:
                return datetime.strptime(self.json_response['date'], '%Y-%m-%d').date()

    @property
    def dateInitiated(self):
        if 'dateInitiated' in self.json_response:
                return datetime.strptime(self.json_response['dateInitiated'], '%Y-%m-%d').date()

    @property
    def orderId(self):
        if 'orderId' in self.json_response:
            return self.json_response['orderId']

    @property
    def reasonCode(self):
        if 'reasonCode' in self.json_response:
            return self.json_response['reasonCode']

    @property
    def directDeposit(self):
        if 'directDeposit' in self.json_response:
            return self.json_response['directDeposit']

    @property
    def achType(self):
        if 'achType' in self.json_response:
            return self.json_response['achType']

    def __repr__(self):
         return '<Marqeta.response_models.ach_return.AchReturn>'