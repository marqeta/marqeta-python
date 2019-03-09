from datetime import datetime

class ReportRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

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
            return datetime.strptime(self.json_response['startDate'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def endDate(self):
        if 'endDate' in self.json_response:
            return datetime.strptime(self.json_response['endDate'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def sendFiles(self):
        if 'sendFiles' in self.json_response:
            return self.json_response['sendFiles']

