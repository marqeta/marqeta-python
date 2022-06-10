from datetime import datetime, date
from marqeta.response_models import datetime_object
import json
import re


class BillPaymentCompletionRequest(object):
    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def network_reference_id(self):
        return self.json_response.get("network_reference_id", None)

    @property
    def original_transaction_token(self):
        return self.json_response.get("original_transaction_token", None)

    def __repr__(self):
        return (
            "<Marqeta.response_models.bill_payment_completion_request.BillPaymentCompletionRequest>"
            + self.__str__()
        )
