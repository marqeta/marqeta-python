from datetime import datetime, date
from marqeta.response_models import datetime_object
import json
import re


class OriginalDataElements(object):
    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def mti(self):
        return self.json_response.get("mti", None)

    @property
    def stan(self):
        return self.json_response.get("stan", None)

    @property
    def transmission_time(self):
        return self.json_response.get("transmission_time", None)

    @property
    def acquiring_institution_id(self):
        return self.json_response.get("acquiring_institution_id", None)

    @property
    def network_reference_id(self):
        return self.json_response.get("network_reference_id", None)

    @property
    def forwarding_institution_id(self):
        return self.json_response.get("forwarding_institution_id", None)

    @property
    def transaction_token(self):
        return self.json_response.get("transaction_token", None)

    def __repr__(self):
        return (
            "<Marqeta.response_models.original_data_elements.OriginalDataElements>"
            + self.__str__()
        )
