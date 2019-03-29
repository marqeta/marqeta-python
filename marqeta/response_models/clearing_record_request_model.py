from datetime import datetime, date
from marqeta.response_models.network_fee_model import NetworkFeeModel
from marqeta.response_models.webhook import Webhook
from marqeta.response_models.money_model import MoneyModel
from marqeta.response_models.money_model import MoneyModel
from marqeta.response_models.card_acceptor_model import CardAcceptorModel
from marqeta.response_models.original_data_elements import OriginalDataElements
import json


class ClearingRecordRequestModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def network_fees(self):

        if 'network_fees' in self.json_response:
            return [NetworkFeeModel(val) for val in self.json_response['network_fees']]

    @property
    def webhook(self):

        if 'webhook' in self.json_response:
            return Webhook(self.json_response['webhook'])

    @property
    def mid(self):

        return self.json_response.get('mid', None)

    @property
    def amount(self):

        return self.json_response.get('amount', None)

    @property
    def replacement_amount(self):

        return self.json_response.get('replacement_amount', None)

    @property
    def cardholder_billing_amount(self):

        return self.json_response.get('cardholder_billing_amount', None)

    @property
    def cardholder_billing_conversion_rate(self):

        return self.json_response.get('cardholder_billing_conversion_rate', None)

    @property
    def cardholder_billing_currency(self):

        return self.json_response.get('cardholder_billing_currency', None)

    @property
    def card_token(self):

        return self.json_response.get('card_token', None)

    @property
    def acquirer_reference_id(self):

        return self.json_response.get('acquirer_reference_id', None)

    @property
    def rrn(self):

        return self.json_response.get('rrn', None)

    @property
    def stan(self):

        return self.json_response.get('stan', None)

    @property
    def processing_code(self):

        return self.json_response.get('processing_code', None)

    @property
    def acquirer_fee(self):

        if 'acquirer_fee' in self.json_response:
            return MoneyModel(self.json_response['acquirer_fee'])

    @property
    def issuer_fee(self):

        if 'issuer_fee' in self.json_response:
            return MoneyModel(self.json_response['issuer_fee'])

    @property
    def function_code(self):

        return self.json_response.get('function_code', None)

    @property
    def reason_code(self):

        return self.json_response.get('reason_code', None)

    @property
    def approval_code(self):

        return self.json_response.get('approval_code', None)

    @property
    def transaction_date(self):

        if 'transaction_date' in self.json_response:
            return datetime.strptime(self.json_response['transaction_date'], '%Y-%m-%d').date()

    @property
    def local_transaction_date(self):

        if 'local_transaction_date' in self.json_response:
            return datetime.strptime(self.json_response['local_transaction_date'], '%Y-%m-%d').date()

    @property
    def settlement_date(self):

        if 'settlement_date' in self.json_response:
            return datetime.strptime(self.json_response['settlement_date'], '%Y-%m-%d').date()

    @property
    def network_reference_id(self):

        return self.json_response.get('network_reference_id', None)

    @property
    def find_original_window_days(self):

        return self.json_response.get('find_original_window_days', None)

    @property
    def batch_number(self):

        return self.json_response.get('batch_number', None)

    @property
    def batch_file_name(self):

        return self.json_response.get('batch_file_name', None)

    @property
    def sequence_number(self):

        return self.json_response.get('sequence_number', None)

    @property
    def network(self):

        return self.json_response.get('network', None)

    @property
    def sub_network(self):

        return self.json_response.get('sub_network', None)

    @property
    def card_acceptor(self):

        if 'card_acceptor' in self.json_response:
            return CardAcceptorModel(self.json_response['card_acceptor'])

    @property
    def currency_code(self):

        return self.json_response.get('currency_code', None)

    @property
    def original_data_elements(self):

        if 'original_data_elements' in self.json_response:
            return OriginalDataElements(self.json_response['original_data_elements'])

    @property
    def preceding_related_transaction_token(self):

        return self.json_response.get('preceding_related_transaction_token', None)

    @property
    def send_expiration_date(self):

        return self.json_response.get('send_expiration_date', None)

    @property
    def simulate_batch_for_clearing_record_hash(self):

        return self.json_response.get('simulate_batch_for_clearing_record_hash', None)

    @property
    def cross_border_indicator(self):

        return self.json_response.get('cross_border_indicator', None)

    @property
    def mti(self):

        return self.json_response.get('mti', None)

    def __repr__(self):
        return '<Marqeta.response_models.clearing_record_request_model.ClearingRecordRequestModel>'
