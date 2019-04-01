from datetime import datetime, date
import json


class Acquirer(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def institution_country(self):
        return self.json_response.get('institution_country', None)

    @property
    def network_international_id(self):
        return self.json_response.get('network_international_id', None)

    @property
    def institution_id_code(self):
        return self.json_response.get('institution_id_code', None)

    @property
    def retrieval_reference_number(self):
        return self.json_response.get('retrieval_reference_number', None)

    @property
    def system_trace_audit_number(self):
        return self.json_response.get('system_trace_audit_number', None)

    def __repr__(self):
        return '<Marqeta.response_models.acquirer.Acquirer>' + self.__str__()
