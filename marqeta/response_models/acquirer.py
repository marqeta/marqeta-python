from datetime import datetime, date
import json

class Acquirer(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'institution_country' : self.institution_country,
           'network_international_id' : self.network_international_id,
           'institution_id_code' : self.institution_id_code,
           'retrieval_reference_number' : self.retrieval_reference_number,
           'system_trace_audit_number' : self.system_trace_audit_number,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def institution_country(self):
        if 'institution_country' in self.json_response:
            return self.json_response['institution_country']

    @property
    def network_international_id(self):
        if 'network_international_id' in self.json_response:
            return self.json_response['network_international_id']

    @property
    def institution_id_code(self):
        if 'institution_id_code' in self.json_response:
            return self.json_response['institution_id_code']

    @property
    def retrieval_reference_number(self):
        if 'retrieval_reference_number' in self.json_response:
            return self.json_response['retrieval_reference_number']

    @property
    def system_trace_audit_number(self):
        if 'system_trace_audit_number' in self.json_response:
            return self.json_response['system_trace_audit_number']

    def __repr__(self):
         return '<Marqeta.response_models.acquirer.Acquirer>'