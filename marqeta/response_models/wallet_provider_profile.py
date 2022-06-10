from datetime import datetime, date
from marqeta.response_models.account import Account
from marqeta.response_models.risk_assessment import RiskAssessment
from marqeta.response_models import datetime_object
import json
import re


class WalletProviderProfile(object):
    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def account(self):
        if "account" in self.json_response:
            return Account(self.json_response["account"])

    @property
    def risk_assessment(self):
        if "risk_assessment" in self.json_response:
            return RiskAssessment(self.json_response["risk_assessment"])

    @property
    def device_score(self):
        return self.json_response.get("device_score", None)

    @property
    def pan_source(self):
        return self.json_response.get("pan_source", None)

    @property
    def reason_code(self):
        return self.json_response.get("reason_code", None)

    @property
    def recommendation_reasons(self):
        return self.json_response.get("recommendation_reasons", None)

    def __repr__(self):
        return (
            "<Marqeta.response_models.wallet_provider_profile.WalletProviderProfile>"
            + self.__str__()
        )
