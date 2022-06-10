from datetime import datetime, date
from marqeta.response_models import datetime_object
import json
import re


class AchVerificationModel(object):
    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def verify_amount1(self):
        return self.json_response.get("verify_amount1", None)

    @property
    def verify_amount2(self):
        return self.json_response.get("verify_amount2", None)

    @property
    def active(self):
        return self.json_response.get("active", None)

    def __repr__(self):
        return (
            "<Marqeta.response_models.ach_verification_model.AchVerificationModel>"
            + self.__str__()
        )
