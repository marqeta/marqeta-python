from datetime import datetime, date
from marqeta.response_models import datetime_object
import json
import re


class BillPaymentTransactionRequest(object):
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
        return self.json_response.get("amount", None)

    @property
    def currency(self):
        return self.json_response.get("currency", None)

    @property
    def network_reference_id(self):
        return self.json_response.get("network_reference_id", None)

    @property
    def user_token(self):
        return self.json_response.get("user_token", None)

    def __repr__(self):
        return (
            "<Marqeta.response_models.bill_payment_transaction_request.BillPaymentTransactionRequest>"
            + self.__str__()
        )
