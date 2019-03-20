from datetime import datetime, date
from marqeta.response_models.network_fee_model import NetworkFeeModel
from marqeta.response_models.advanced_auth_card_acceptor_model import AdvancedAuthCardAcceptorModel
from marqeta.response_models.transaction_options import TransactionOptions
from marqeta.response_models.original_data_elements import OriginalDataElements
from marqeta.response_models.replacement_amount import ReplacementAmount
from marqeta.response_models.webhook import Webhook
from marqeta.response_models.digital_wallet_token import DigitalWalletToken
from marqeta.response_models.digital_wallet_token_device import DigitalWalletTokenDevice
from marqeta.response_models.digital_wallet_token_wallet_provider import DigitalWalletTokenWalletProvider
from marqeta.response_models.card_options import CardOptions
from marqeta.response_models.advanced_auth_poi import AdvancedAuthPoi
import json

class AdvAuthRequestModel(object):

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
        if 'mti' in self.json_response:
            return self.json_response['mti']

    @property
    def network(self):
        if 'network' in self.json_response:
            return self.json_response['network']

    @property
    def sub_network(self):
        if 'sub_network' in self.json_response:
            return self.json_response['sub_network']

    @property
    def is_router_simulator(self):
        if 'is_router_simulator' in self.json_response:
            return self.json_response['is_router_simulator']

    @property
    def network_reference_id(self):
        if 'network_reference_id' in self.json_response:
            return self.json_response['network_reference_id']

    @property
    def local_transaction_date(self):
        if 'local_transaction_date' in self.json_response:
                return datetime.strptime(self.json_response['local_transaction_date'], '%Y-%m-%d').date()

    @property
    def transaction_date(self):
        if 'transaction_date' in self.json_response:
                return datetime.strptime(self.json_response['transaction_date'], '%Y-%m-%d').date()

    @property
    def settlement_date(self):
        if 'settlement_date' in self.json_response:
                return datetime.strptime(self.json_response['settlement_date'], '%Y-%m-%d').date()

    @property
    def stan(self):
        if 'stan' in self.json_response:
            return self.json_response['stan']

    @property
    def rrn(self):
        if 'rrn' in self.json_response:
            return self.json_response['rrn']

    @property
    def processing_code(self):
        if 'processing_code' in self.json_response:
            return self.json_response['processing_code']

    @property
    def function_code(self):
        if 'function_code' in self.json_response:
            return self.json_response['function_code']

    @property
    def reason_code(self):
        if 'reason_code' in self.json_response:
            return self.json_response['reason_code']

    @property
    def acquirer_reference_id(self):
        if 'acquirer_reference_id' in self.json_response:
            return self.json_response['acquirer_reference_id']

    @property
    def forwarding_institution_id(self):
        if 'forwarding_institution_id' in self.json_response:
            return self.json_response['forwarding_institution_id']

    @property
    def local_transaction_amount(self):
        if 'local_transaction_amount' in self.json_response:
            return self.json_response['local_transaction_amount']

    @property
    def local_currency_code(self):
        if 'local_currency_code' in self.json_response:
            return self.json_response['local_currency_code']

    @property
    def settlement_amount(self):
        if 'settlement_amount' in self.json_response:
            return self.json_response['settlement_amount']

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
    def settlement_currency_code(self):
        if 'settlement_currency_code' in self.json_response:
            return self.json_response['settlement_currency_code']

    @property
    def approval_code(self):
        if 'approval_code' in self.json_response:
            return self.json_response['approval_code']

    @property
    def network_response(self):
        if 'network_response' in self.json_response:
            return self.json_response['network_response']

    @property
    def stan_padding_length(self):
        if 'stan_padding_length' in self.json_response:
            return self.json_response['stan_padding_length']

    @property
    def card_token(self):
        if 'card_token' in self.json_response:
            return self.json_response['card_token']

    @property
    def amount(self):
        if 'amount' in self.json_response:
            return self.json_response['amount']

    @property
    def cash_back_amount(self):
        if 'cash_back_amount' in self.json_response:
            return self.json_response['cash_back_amount']

    @property
    def mid(self):
        if 'mid' in self.json_response:
            return self.json_response['mid']

    @property
    def pin(self):
        if 'pin' in self.json_response:
            return self.json_response['pin']

    @property
    def pos_pan_entry_mode(self):
        if 'pos_pan_entry_mode' in self.json_response:
            return self.json_response['pos_pan_entry_mode']

    @property
    def acquirer_fee_amount(self):
        if 'acquirer_fee_amount' in self.json_response:
            return self.json_response['acquirer_fee_amount']

    @property
    def stip_reason_code(self):
        if 'stip_reason_code' in self.json_response:
            return self.json_response['stip_reason_code']

    @property
    def is_recurring(self):
        if 'is_recurring' in self.json_response:
            return self.json_response['is_recurring']

    @property
    def network_fees(self):
        if 'network_fees' in self.json_response:
            return [NetworkFeeModel(val) for val in self.json_response['network_fees']]

    @property
    def card_acceptor(self):
        if 'card_acceptor' in self.json_response:
            return AdvancedAuthCardAcceptorModel(self.json_response['card_acceptor'])

    @property
    def transaction_options(self):
        if 'transaction_options' in self.json_response:
            return TransactionOptions(self.json_response['transaction_options'])

    @property
    def original_data_elements(self):
        if 'original_data_elements' in self.json_response:
            return OriginalDataElements(self.json_response['original_data_elements'])

    @property
    def replacement_amount(self):
        if 'replacement_amount' in self.json_response:
            return ReplacementAmount(self.json_response['replacement_amount'])

    @property
    def webhook(self):
        if 'webhook' in self.json_response:
            return Webhook(self.json_response['webhook'])

    @property
    def digital_wallet_token(self):
        if 'digital_wallet_token' in self.json_response:
            return DigitalWalletToken(self.json_response['digital_wallet_token'])

    @property
    def digital_wallet_token_device_info(self):
        if 'digital_wallet_token_device_info' in self.json_response:
            return DigitalWalletTokenDevice(self.json_response['digital_wallet_token_device_info'])

    @property
    def digital_wallet_token_wallet_provider_info(self):
        if 'digital_wallet_token_wallet_provider_info' in self.json_response:
            return DigitalWalletTokenWalletProvider(self.json_response['digital_wallet_token_wallet_provider_info'])

    @property
    def raw_iso_fields(self):
        if 'raw_iso_fields' in self.json_response:
            return self.json_response['raw_iso_fields']

    @property
    def cavv_result_code(self):
        if 'cavv_result_code' in self.json_response:
            return self.json_response['cavv_result_code']

    @property
    def card_options(self):
        if 'card_options' in self.json_response:
            return CardOptions(self.json_response['card_options'])

    @property
    def poi(self):
        if 'poi' in self.json_response:
            return AdvancedAuthPoi(self.json_response['poi'])

    @property
    def is_stip_approval(self):
        if 'is_stip_approval' in self.json_response:
            return self.json_response['is_stip_approval']

    def __repr__(self):
         return '<Marqeta.response_models.adv_auth_request_model.AdvAuthRequestModel>'