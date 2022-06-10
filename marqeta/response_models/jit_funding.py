from datetime import datetime, date
from marqeta.response_models.jit_funding_paymentcard_funding_source import (
    JitFundingPaymentcardFundingSource,
)
from marqeta.response_models.jit_funding_programgateway_funding_source import (
    JitFundingProgramgatewayFundingSource,
)
from marqeta.response_models.jit_funding_program_funding_source import (
    JitFundingProgramFundingSource,
)
from marqeta.response_models import datetime_object
import json
import re


class JitFunding(object):
    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def paymentcard_funding_source(self):
        if "paymentcard_funding_source" in self.json_response:
            return JitFundingPaymentcardFundingSource(
                self.json_response["paymentcard_funding_source"]
            )

    @property
    def programgateway_funding_source(self):
        if "programgateway_funding_source" in self.json_response:
            return JitFundingProgramgatewayFundingSource(
                self.json_response["programgateway_funding_source"]
            )

    @property
    def program_funding_source(self):
        if "program_funding_source" in self.json_response:
            return JitFundingProgramFundingSource(
                self.json_response["program_funding_source"]
            )

    def __repr__(self):
        return "<Marqeta.response_models.jit_funding.JitFunding>" + self.__str__()
