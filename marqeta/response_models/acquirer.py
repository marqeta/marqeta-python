from datetime import datetime

class Acquirer(object):

    def __init__(self, json_response):
        self.json_response = json_response

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

