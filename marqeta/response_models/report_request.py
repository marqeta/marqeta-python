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
        return self.json_response.get('partner', None)

    @property
    def report(self):
        return self.json_response.get('report', None)

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
        return self.json_response.get('sendFiles', None)

    def __repr__(self):
        return '<Marqeta.response_models.report_request.ReportRequest>'
