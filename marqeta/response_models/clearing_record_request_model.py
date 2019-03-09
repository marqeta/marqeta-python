from datetime import datetime
from marqeta.response_models.network_fee_model import NetworkFeeModel
from marqeta.response_models.webhook import Webhook
from marqeta.response_models.money_model import MoneyModel
from marqeta.response_models.money_model import MoneyModel
from marqeta.response_models.card_acceptor_model import CardAcceptorModel
from marqeta.response_models.original_data_elements import OriginalDataElements

class ClearingRecordRequestModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

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
        if 'mid' in self.json_response:
            return self.json_response['mid']

    @property
    def amount(self):
        if 'amount' in self.json_response:
            return self.json_response['amount']

    @property
    def replacement_amount(self):
        if 'replacement_amount' in self.json_response:
            return self.json_response['replacement_amount']

    @property
    def cardholder_billing_amount(self):
        if 'cardholder_billing_amount' in self.json_response:
            return self.json_response['cardholder_billing_amount']

    @property
    def cardholder_billing_conversion_rate(self):
        if 'cardholder_billing_conversion_rate' in self.json_response:
            return self.json_response['cardholder_billing_conversion_rate']

    @property
    def cardholder_billing_currency(self):
        if 'cardholder_billing_currency' in self.json_response:
            return self.json_response['cardholder_billing_currency']

    @property
    def card_token(self):
        if 'card_token' in self.json_response:
            return self.json_response['card_token']

    @property
    def acquirer_reference_id(self):
        if 'acquirer_reference_id' in self.json_response:
            return self.json_response['acquirer_reference_id']

    @property
    def rrn(self):
        if 'rrn' in self.json_response:
            return self.json_response['rrn']

    @property
    def stan(self):
        if 'stan' in self.json_response:
            return self.json_response['stan']

    @property
    def processing_code(self):
        if 'processing_code' in self.json_response:
            return self.json_response['processing_code']

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
        if 'function_code' in self.json_response:
            return self.json_response['function_code']

    @property
    def reason_code(self):
        if 'reason_code' in self.json_response:
            return self.json_response['reason_code']

    @property
    def approval_code(self):
        if 'approval_code' in self.json_response:
            return self.json_response['approval_code']

    @property
    def transaction_date(self):
        if 'transaction_date' in self.json_response:
            return datetime.strptime(self.json_response['transaction_date'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def local_transaction_date(self):
        if 'local_transaction_date' in self.json_response:
            return datetime.strptime(self.json_response['local_transaction_date'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def settlement_date(self):
        if 'settlement_date' in self.json_response:
            return datetime.strptime(self.json_response['settlement_date'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def network_reference_id(self):
        if 'network_reference_id' in self.json_response:
            return self.json_response['network_reference_id']

    @property
    def find_original_window_days(self):
        if 'find_original_window_days' in self.json_response:
            return self.json_response['find_original_window_days']

    @property
    def batch_number(self):
        if 'batch_number' in self.json_response:
            return self.json_response['batch_number']

    @property
    def batch_file_name(self):
        if 'batch_file_name' in self.json_response:
            return self.json_response['batch_file_name']

    @property
    def sequence_number(self):
        if 'sequence_number' in self.json_response:
            return self.json_response['sequence_number']

    @property
    def network(self):
        if 'network' in self.json_response:
            return self.json_response['network']

    @property
    def sub_network(self):
        if 'sub_network' in self.json_response:
            return self.json_response['sub_network']

    @property
    def card_acceptor(self):
        if 'card_acceptor' in self.json_response:
            return CardAcceptorModel(self.json_response['card_acceptor'])

    @property
    def currency_code(self):
        if 'currency_code' in self.json_response:
            return self.json_response['currency_code']

    @property
    def original_data_elements(self):
        if 'original_data_elements' in self.json_response:
            return OriginalDataElements(self.json_response['original_data_elements'])

    @property
    def preceding_related_transaction_token(self):
        if 'preceding_related_transaction_token' in self.json_response:
            return self.json_response['preceding_related_transaction_token']

    @property
    def send_expiration_date(self):
        if 'send_expiration_date' in self.json_response:
            return self.json_response['send_expiration_date']

    @property
    def simulate_batch_for_clearing_record_hash(self):
        if 'simulate_batch_for_clearing_record_hash' in self.json_response:
            return self.json_response['simulate_batch_for_clearing_record_hash']

    @property
    def cross_border_indicator(self):
        if 'cross_border_indicator' in self.json_response:
            return self.json_response['cross_border_indicator']

    @property
    def mti(self):
        if 'mti' in self.json_response:
            return self.json_response['mti']

