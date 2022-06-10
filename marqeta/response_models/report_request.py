from datetime import datetime, date
from marqeta.response_models import datetime_object
import json
import re


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
        return self.json_response.get("partner", None)

    @property
    def report(self):
        return self.json_response.get("report", None)

    @property
    def startDate(self):
        if "startDate" in self.json_response:
            return datetime_object("startDate", self.json_response)

    @property
    def endDate(self):
        if "endDate" in self.json_response:
            return datetime_object("endDate", self.json_response)

    @property
    def sendFiles(self):
        return self.json_response.get("sendFiles", None)

    def __repr__(self):
        return "<Marqeta.response_models.report_request.ReportRequest>" + self.__str__()
