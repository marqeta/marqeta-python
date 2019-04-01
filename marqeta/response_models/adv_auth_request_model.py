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
        return self.json_response.get('mti', None)

    @property
    def network(self):
        return self.json_response.get('network', None)

    @property
    def sub_network(self):
        return self.json_response.get('sub_network', None)

    @property
    def is_router_simulator(self):
        return self.json_response.get('is_router_simulator', None)

    @property
    def network_reference_id(self):
        return self.json_response.get('network_reference_id', None)

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
        return self.json_response.get('stan', None)

    @property
    def rrn(self):
        return self.json_response.get('rrn', None)

    @property
    def processing_code(self):
        return self.json_response.get('processing_code', None)

    @property
    def function_code(self):
        return self.json_response.get('function_code', None)

    @property
    def reason_code(self):
        return self.json_response.get('reason_code', None)

    @property
    def acquirer_reference_id(self):
        return self.json_response.get('acquirer_reference_id', None)

    @property
    def forwarding_institution_id(self):
        return self.json_response.get('forwarding_institution_id', None)

    @property
    def local_transaction_amount(self):
        return self.json_response.get('local_transaction_amount', None)

    @property
    def local_currency_code(self):
        return self.json_response.get('local_currency_code', None)

    @property
    def settlement_amount(self):
        return self.json_response.get('settlement_amount', None)

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
    def settlement_currency_code(self):
        return self.json_response.get('settlement_currency_code', None)

    @property
    def approval_code(self):
        return self.json_response.get('approval_code', None)

    @property
    def network_response(self):
        return self.json_response.get('network_response', None)

    @property
    def stan_padding_length(self):
        return self.json_response.get('stan_padding_length', None)

    @property
    def card_token(self):
        return self.json_response.get('card_token', None)

    @property
    def amount(self):
        return self.json_response.get('amount', None)

    @property
    def cash_back_amount(self):
        return self.json_response.get('cash_back_amount', None)

    @property
    def mid(self):
        return self.json_response.get('mid', None)

    @property
    def pin(self):
        return self.json_response.get('pin', None)

    @property
    def pos_pan_entry_mode(self):
        return self.json_response.get('pos_pan_entry_mode', None)

    @property
    def acquirer_fee_amount(self):
        return self.json_response.get('acquirer_fee_amount', None)

    @property
    def stip_reason_code(self):
        return self.json_response.get('stip_reason_code', None)

    @property
    def is_recurring(self):
        return self.json_response.get('is_recurring', None)

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
        return self.json_response.get('raw_iso_fields', None)

    @property
    def cavv_result_code(self):
        return self.json_response.get('cavv_result_code', None)

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

        return self.json_response.get('is_stip_approval', None)

    def __repr__(self):
        return '<Marqeta.response_models.adv_auth_request_model.AdvAuthRequestModel>' + self.__str__()
