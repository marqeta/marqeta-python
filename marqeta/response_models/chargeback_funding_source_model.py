from datetime import datetime, date
from marqeta.response_models.funding_source_model import FundingSourceModel
from marqeta.response_models import datetime_object
import json
import re


class ChargebackFundingSourceModel(FundingSourceModel):
    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def name(self):
        return self.json_response.get("name", None)

    @property
    def credit(self):
        return self.json_response.get("credit", None)

    def __repr__(self):
        return (
            "<Marqeta.response_models.chargeback_funding_source_model.ChargebackFundingSourceModel>"
            + self.__str__()
        )
