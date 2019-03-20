from datetime import datetime, date
import json

class ReportRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def partner(self):
        if 'partner' in self.json_response:
            return self.json_response['partner']

    @property
    def report(self):
        if 'report' in self.json_response:
            return self.json_response['report']

    @property
    def startDate(self):
        if 'startDate' in self.json_response:
                return datetime.strptime(self.json_response['startDate'], '%Y-%m-%d').date()

    @property
    def endDate(self):
        if 'endDate' in self.json_response:
                return datetime.strptime(self.json_response['endDate'], '%Y-%m-%d').date()

    @property
    def sendFiles(self):
        if 'sendFiles' in self.json_response:
            return self.json_response['sendFiles']

    def __repr__(self):
         return '<Marqeta.response_models.report_request.ReportRequest>'