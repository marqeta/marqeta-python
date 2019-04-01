from datetime import datetime, date
import json


class AchReturn(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def amount(self):
        return self.json_response.get('amount', None)

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
        return self.json_response.get('orderId', None)

    @property
    def reasonCode(self):
        return self.json_response.get('reasonCode', None)

    @property
    def directDeposit(self):
        return self.json_response.get('directDeposit', None)

    @property
    def achType(self):
        return self.json_response.get('achType', None)

    def __repr__(self):
        return '<Marqeta.response_models.ach_return.AchReturn>' + self.__str__()
