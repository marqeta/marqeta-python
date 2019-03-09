from datetime import datetime
from marqeta.response_models.currency_conversion import CurrencyConversion
from marqeta.response_models.response import Response
from marqeta.response_models.merchant_response_model import MerchantResponseModel
from marqeta.response_models.store_response_model import StoreResponseModel
from marqeta.response_models.transaction_card_acceptor import TransactionCardAcceptor
from marqeta.response_models.cardholder_balance import CardholderBalance
from marqeta.response_models.gpa_returns import GpaReturns
from marqeta.response_models.gpa_response import GpaResponse
from marqeta.response_models.program_transfer_response import ProgramTransferResponse
from marqeta.response_models.fee_transfer_response import FeeTransferResponse
from marqeta.response_models.peer_transfer_response import PeerTransferResponse
from marqeta.response_models.msa_order_response import MsaOrderResponse
from marqeta.response_models.msa_returns import MsaReturns
from marqeta.response_models.offer_order_response import OfferOrderResponse
from marqeta.response_models.auto_reload_model import AutoReloadModel
from marqeta.response_models.deposit_deposit_response import DepositDepositResponse
from marqeta.response_models.real_time_fee_group import RealTimeFeeGroup
from marqeta.response_models.fee import Fee
from marqeta.response_models.chargeback_response import ChargebackResponse
from marqeta.response_models.network_fee_model import NetworkFeeModel
from marqeta.response_models.digital_wallet_token import DigitalWalletToken
from marqeta.response_models.cardholder_metadata import CardholderMetadata
from marqeta.response_models.business_metadata import BusinessMetadata
from marqeta.response_models.card_metadata import CardMetadata
from marqeta.response_models.acquirer import Acquirer
from marqeta.response_models.fraud import Fraud
from marqeta.response_models.pos import Pos
from marqeta.response_models.address_verification_model import AddressVerificationModel
from marqeta.response_models.card_security_code_verification import CardSecurityCodeVerification
from marqeta.response_models.transaction_metadata import TransactionMetadata
from marqeta.response_models.user_card_holder_response import UserCardHolderResponse
from marqeta.response_models.cardholder_authentication_data import CardholderAuthenticationData

class TransactionModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def type(self):
        if 'type' in self.json_response:
            return self.json_response['type']

    @property
    def state(self):
        if 'state' in self.json_response:
            return self.json_response['state']

    @property
    def token(self):
        if 'token' in self.json_response:
            return self.json_response['token']

    @property
    def user_token(self):
        if 'user_token' in self.json_response:
            return self.json_response['user_token']

    @property
    def business_token(self):
        if 'business_token' in self.json_response:
            return self.json_response['business_token']

    @property
    def acting_user_token(self):
        if 'acting_user_token' in self.json_response:
            return self.json_response['acting_user_token']

    @property
    def card_token(self):
        if 'card_token' in self.json_response:
            return self.json_response['card_token']

    @property
    def duration(self):
        if 'duration' in self.json_response:
            return self.json_response['duration']

    @property
    def created_time(self):
        if 'created_time' in self.json_response:
            return datetime.strptime(self.json_response['created_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def user_transaction_time(self):
        if 'user_transaction_time' in self.json_response:
            return datetime.strptime(self.json_response['user_transaction_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def settlement_date(self):
        if 'settlement_date' in self.json_response:
            return datetime.strptime(self.json_response['settlement_date'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def request_amount(self):
        if 'request_amount' in self.json_response:
            return self.json_response['request_amount']

    @property
    def amount(self):
        if 'amount' in self.json_response:
            return self.json_response['amount']

    @property
    def currency_conversion(self):
        if 'currency_conversion' in self.json_response:
            return CurrencyConversion(self.json_response['currency_conversion'])

    @property
    def issuerInterchangeAmount(self):
        if 'issuerInterchangeAmount' in self.json_response:
            return self.json_response['issuerInterchangeAmount']

    @property
    def currency_code(self):
        if 'currency_code' in self.json_response:
            return self.json_response['currency_code']

    @property
    def approval_code(self):
        if 'approval_code' in self.json_response:
            return self.json_response['approval_code']

    @property
    def response(self):
        if 'response' in self.json_response:
            return Response(self.json_response['response'])

    @property
    def preceding_related_transaction_token(self):
        if 'preceding_related_transaction_token' in self.json_response:
            return self.json_response['preceding_related_transaction_token']

    @property
    def incremental_authorization_transaction_tokens(self):
        if 'incremental_authorization_transaction_tokens' in self.json_response:
            return self.json_response['incremental_authorization_transaction_tokens']

    @property
    def merchant(self):
        if 'merchant' in self.json_response:
            return MerchantResponseModel(self.json_response['merchant'])

    @property
    def store(self):
        if 'store' in self.json_response:
            return StoreResponseModel(self.json_response['store'])

    @property
    def card_acceptor(self):
        if 'card_acceptor' in self.json_response:
            return TransactionCardAcceptor(self.json_response['card_acceptor'])

    @property
    def gpa(self):
        if 'gpa' in self.json_response:
            return CardholderBalance(self.json_response['gpa'])

    @property
    def gpa_order_unload(self):
        if 'gpa_order_unload' in self.json_response:
            return GpaReturns(self.json_response['gpa_order_unload'])

    @property
    def gpa_order(self):
        if 'gpa_order' in self.json_response:
            return GpaResponse(self.json_response['gpa_order'])

    @property
    def program_transfer(self):
        if 'program_transfer' in self.json_response:
            return ProgramTransferResponse(self.json_response['program_transfer'])

    @property
    def fee_transfer(self):
        if 'fee_transfer' in self.json_response:
            return FeeTransferResponse(self.json_response['fee_transfer'])

    @property
    def peer_transfer(self):
        if 'peer_transfer' in self.json_response:
            return PeerTransferResponse(self.json_response['peer_transfer'])

    @property
    def msa_orders(self):
        if 'msa_orders' in self.json_response:
            return [MsaOrderResponse(val) for val in self.json_response['msa_orders']]

    @property
    def msa_order_unload(self):
        if 'msa_order_unload' in self.json_response:
            return MsaReturns(self.json_response['msa_order_unload'])

    @property
    def offer_orders(self):
        if 'offer_orders' in self.json_response:
            return [OfferOrderResponse(val) for val in self.json_response['offer_orders']]

    @property
    def auto_reload(self):
        if 'auto_reload' in self.json_response:
            return AutoReloadModel(self.json_response['auto_reload'])

    @property
    def direct_deposit(self):
        if 'direct_deposit' in self.json_response:
            return DepositDepositResponse(self.json_response['direct_deposit'])

    @property
    def polarity(self):
        if 'polarity' in self.json_response:
            return self.json_response['polarity']

    @property
    def real_time_fee_group(self):
        if 'real_time_fee_group' in self.json_response:
            return RealTimeFeeGroup(self.json_response['real_time_fee_group'])

    @property
    def fee(self):
        if 'fee' in self.json_response:
            return Fee(self.json_response['fee'])

    @property
    def chargeback(self):
        if 'chargeback' in self.json_response:
            return ChargebackResponse(self.json_response['chargeback'])

    @property
    def network(self):
        if 'network' in self.json_response:
            return self.json_response['network']

    @property
    def subnetwork(self):
        if 'subnetwork' in self.json_response:
            return self.json_response['subnetwork']

    @property
    def acquirer_fee_amount(self):
        if 'acquirer_fee_amount' in self.json_response:
            return self.json_response['acquirer_fee_amount']

    @property
    def fees(self):
        if 'fees' in self.json_response:
            return [NetworkFeeModel(val) for val in self.json_response['fees']]

    @property
    def digital_wallet_token(self):
        if 'digital_wallet_token' in self.json_response:
            return DigitalWalletToken(self.json_response['digital_wallet_token'])

    @property
    def user(self):
        if 'user' in self.json_response:
            return CardholderMetadata(self.json_response['user'])

    @property
    def business(self):
        if 'business' in self.json_response:
            return BusinessMetadata(self.json_response['business'])

    @property
    def card(self):
        if 'card' in self.json_response:
            return CardMetadata(self.json_response['card'])

    @property
    def acquirer(self):
        if 'acquirer' in self.json_response:
            return Acquirer(self.json_response['acquirer'])

    @property
    def fraud(self):
        if 'fraud' in self.json_response:
            return Fraud(self.json_response['fraud'])

    @property
    def pos(self):
        if 'pos' in self.json_response:
            return Pos(self.json_response['pos'])

    @property
    def address_verification(self):
        if 'address_verification' in self.json_response:
            return AddressVerificationModel(self.json_response['address_verification'])

    @property
    def card_security_code_verification(self):
        if 'card_security_code_verification' in self.json_response:
            return CardSecurityCodeVerification(self.json_response['card_security_code_verification'])

    @property
    def transaction_metadata(self):
        if 'transaction_metadata' in self.json_response:
            return TransactionMetadata(self.json_response['transaction_metadata'])

    @property
    def card_holder_model(self):
        if 'card_holder_model' in self.json_response:
            return UserCardHolderResponse(self.json_response['card_holder_model'])

    @property
    def standin_approved_by(self):
        if 'standin_approved_by' in self.json_response:
            return self.json_response['standin_approved_by']

    @property
    def network_reference_id(self):
        if 'network_reference_id' in self.json_response:
            return self.json_response['network_reference_id']

    @property
    def acquirer_reference_id(self):
        if 'acquirer_reference_id' in self.json_response:
            return self.json_response['acquirer_reference_id']

    @property
    def cardholder_authentication_data(self):
        if 'cardholder_authentication_data' in self.json_response:
            return CardholderAuthenticationData(self.json_response['cardholder_authentication_data'])

