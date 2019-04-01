from datetime import datetime, date
from marqeta.response_models.gatewaylog import Gatewaylog
import json


class Gatewaylog(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def id(self):
        return self.json_response.get('id', None)

    @property
    def traceNumber(self):
        return self.json_response.get('traceNumber', None)

    @property
    def paymentTypeCode(self):
        return self.json_response.get('paymentTypeCode', None)

    @property
    def achTransactionType(self):
        return self.json_response.get('achTransactionType', None)

    @property
    def memo(self):
        return self.json_response.get('memo', None)

    @property
    def gatewayVersion(self):
        return self.json_response.get('gatewayVersion', None)

    @property
    def gatewayResponse(self):
        return self.json_response.get('gatewayResponse', None)

    @property
    def timedOut(self):
        return self.json_response.get('timedOut', None)

    @property
    def deal_Id(self):
        return self.json_response.get('deal_Id', None)

    @property
    def order_Id(self):
        return self.json_response.get('order_Id', None)

    @property
    def request_method(self):
        return self.json_response.get('request_method', None)

    @property
    def response_code(self):
        return self.json_response.get('response_code', None)

    @property
    def response_subcode(self):
        return self.json_response.get('response_subcode', None)

    @property
    def response_reasoncode(self):
        return self.json_response.get('response_reasoncode', None)

    @property
    def response_message(self):
        return self.json_response.get('response_message', None)

    @property
    def status(self):
        return self.json_response.get('status', None)

    @property
    def fraud_avs(self):
        return self.json_response.get('fraud_avs', None)

    @property
    def fraud_auth(self):
        return self.json_response.get('fraud_auth', None)

    @property
    def fraud_cvv(self):
        return self.json_response.get('fraud_cvv', None)

    @property
    def gateway_transactionId(self):
        return self.json_response.get('gateway_transactionId', None)

    @property
    def original_gateway(self):
        if 'original_gateway' in self.json_response:
            return Gatewaylog(self.json_response['original_gateway'])

    @property
    def amount(self):
        return self.json_response.get('amount', None)

    @property
    def duplicate(self):
        return self.json_response.get('duplicate', None)

    @property
    def post_date(self):
        if 'post_date' in self.json_response:
            return datetime.strptime(self.json_response['post_date'], '%Y-%m-%d').date()

    @property
    def response_time(self):
        if 'response_time' in self.json_response:
            return datetime.strptime(self.json_response['response_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def api_duration(self):
        return self.json_response.get('api_duration', None)

    @property
    def gateway_duration(self):
        return self.json_response.get('gateway_duration', None)

    @property
    def ach_status(self):
        return self.json_response.get('ach_status', None)

    @property
    def created(self):
        if 'created' in self.json_response:
            return datetime.strptime(self.json_response['created'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def modified(self):
        if 'modified' in self.json_response:
            return datetime.strptime(self.json_response['modified'], '%Y-%m-%d').date()

    def __repr__(self):
        return '<Marqeta.response_models.gatewaylog.Gatewaylog>' + self.__str__()
