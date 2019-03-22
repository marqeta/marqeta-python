import sys
import json
import requests
from marqeta.version import __version__
from marqeta.errors import MarqetaError
from marqeta.resources.users import UsersCollection
from marqeta.resources.cardproducts import CardProductCollection
from marqeta.resources.cards import CardsCollection
from marqeta.resources.gpaorder import GpaOrderCollection
from marqeta.resources.fundingsources import FundingSourcesCollection
from marqeta.resources.businesses import BusinessesCollection
from marqeta.resources.acceptedcountries import AcceptedCountriesCollection
from marqeta.resources.accountholdergroups import AccountHolderGroupsCollection
from marqeta.resources.digitalwallettokens import DigitalWalletTokensCollection
from marqeta.resources.authcontrols import AuthControlsCollection
from marqeta.resources.autoreloads import AutoReloadsCollection
from marqeta.resources.kyc import KycCollection
from marqeta.resources.balances import BalancesTokenCollection
from marqeta.resources.msaorders import MsaOrdersCollection
from marqeta.resources.offerorders import OfferOrdersCollection
from marqeta.resources.bulkissuances import BulkIssuancesCollection
from marqeta.resources.campaigns import CampaignsCollection
from marqeta.resources.chargebacks import ChargebacksCollection
from marqeta.resources.commandomodes import CommandoModesCollection
from marqeta.resources.directdeposits import DirectDepositsCollection
from marqeta.resources.fees import FeesCollection
from marqeta.resources.feetransfers import FeeTransfersCollection
from marqeta.resources.mccgroups import MccGroupsCollection
from marqeta.resources.merchants import MerchantsCollection
from marqeta.resources.offerorders import OfferOrdersCollection
from marqeta.resources.offers import OffersCollection
from marqeta.resources.programtransfers import ProgramTransfersCollection
from marqeta.resources.realtimefeegroups import RealTimeFeeGroupsCollection
from marqeta.resources.stores import StoresCollection
from marqeta.resources.transactions import TransactionsCollection
from marqeta.resources.velocitycontrols import VelocityControlsCollection
from marqeta.resources.webhooks import WebhooksCollection
from marqeta.resources.pushtocards import PushToCardsCollection
from marqeta.resources.pins import PinsCollection
from marqeta.response_models.ping_response import PingResponse
from marqeta.response_models.echo_ping_response import EchoPingResponse

headers = {'content-type': 'application/json',
           'User-Agent': 'marqeta-python/{} (Python {})'.format(__version__, sys.version.split(' ')[0])}


class Client(object):

    def __init__(self, base_url=None, application_token=None, access_token=None):
        self.base_url = base_url
        self.application_token = application_token
        self.access_token = access_token
        objects = self._objects_container()
        self.users = objects['users']()
        self.businesses = objects['businesses']()
        self.card_products = objects['card_products']()
        self.cards = objects['cards']()
        self.funding_sources = objects['funding_sources']()
        self.gpa_orders = objects['gpa_orders']()
        self.accepted_countries = objects['accepted_countries']()
        self.account_holder_groups = objects['account_holder_groups']()
        self.auth_controls = objects['auth_controls']()
        self.auto_reloads = objects['auto_reloads']()
        self.kyc = objects['kyc']()
        self.balances = objects['balances']()
        self.msa_orders = objects['msa_orders']()
        self.offer_orders = objects['offer_orders']()
        self.digital_wallet_tokens = objects['digital_wallet_tokens']()
        self.velocity_controls = objects['velocity_controls']()
        self.mcc_groups = objects['mcc_groups']()
        self.transactions = objects['transactions']()
        self.chargebacks = objects['chargebacks']()
        self.fee_transfers = objects['fee_transfers']()
        self.program_transfers = objects['program_transfers']()
        self.fees = objects['fees']()
        self.direct_deposits = objects['direct_deposits']()
        self.webhooks = objects['webhooks']()
        self.merchants = objects['merchants']()
        self.stores = objects['stores']()
        self.campaigns = objects['campaigns']()
        self.offers = objects['offers']()
        self.commando_modes = objects['commando_modes']()
        self.bulk_issuances = objects['bulk_issuances']()
        self.real_time_fee_groups = objects['real_time_fee_groups']()
        self.push_to_cards = objects['push_to_cards']()
        self.pins = objects['pins']()

    def get(self, endpoint, query_params=None):
        response = requests.get(url=self.base_url + endpoint, auth=(
            self.application_token, self.access_token),
                                headers=headers,
                                params=query_params)
        if response.status_code >= 400:
            response = response.json()
            if 'error_code' not in response:
                raise MarqetaError(error_message=response['error_message'])
            else:
                raise MarqetaError(error_code=response['error_code'], error_message=response['error_message'])
        return response.json(), response.status_code

    def put(self, endpoint, data):
        response = requests.put(url=self.base_url + endpoint, auth=(
            self.application_token, self.access_token),
                                headers=headers,
                                data=json.dumps(data))
        if response.status_code >= 400:
            response = response.json()
            if 'error_code' not in response:
                raise MarqetaError(error_message=response['error_message'])
            else:
                raise MarqetaError(error_code=response['error_code'], error_message=response['error_message'])
        return response.json(), response.status_code

    def post(self, endpoint, data=None, query_params=None):
        response = requests.post(url=self.base_url + endpoint, auth=(
            self.application_token, self.access_token),
                                 headers=headers,
                                 params=query_params,
                                 data=json.dumps(data))
        if response.status_code >= 400:
            response = response.json()
            if 'error_code' not in response:
                raise MarqetaError(error_message=response['error_message'])
            else:
                raise MarqetaError(error_code=response['error_code'], error_message=response['error_message'])
        return response.json(), response.status_code

    def delete(self, endpoint):
        response = requests.delete(url=self.base_url + endpoint, auth=(
            self.application_token, self.access_token),
                                   headers=headers)
        if response.status_code >= 400:
            response = response.json()
            if 'error_code' not in response:
                raise MarqetaError(error_message=response['error_message'])
            else:
                raise MarqetaError(error_code=response['error_code'], error_message=response['error_message'])
        return (
            response.json(), response.status_code)

    def ping(self, **kwargs):
        if kwargs:
            data = {key: kwargs[key] for key in kwargs}
            return EchoPingResponse(self.post('ping', data)[0])
        return PingResponse(self.get('ping')[0])

    def _objects_container(self):
        """
        Call subclasses via function to allow passing parent namespace to subclasses.

        Returns the dict with objects references.
        """
        _parent_class = self

        class UsersWrapper(UsersCollection):

            def __init__(self):
                self._parent_class = _parent_class
                super().__init__(_parent_class)

        class CardProductWrapper(CardProductCollection):

            def __init__(self):
                self._parent_class = _parent_class
                super().__init__(_parent_class)

        class CardsWrapper(CardsCollection):

            def __init__(self):
                self._parent_class = _parent_class
                super().__init__(_parent_class)

        class GpaOrderWrapper(GpaOrderCollection):

            def __init__(self):
                self._parent_class = _parent_class
                super().__init__(_parent_class)

        class FundingWrapper(FundingSourcesCollection):

            def __init__(self):
                self._parent_class = _parent_class
                super().__init__(_parent_class)

        class BusinessWrapper(BusinessesCollection):

            def __init__(self):
                self._parent_class = _parent_class
                super().__init__(_parent_class)

        class AcceptedCountriesWrapper(AcceptedCountriesCollection):

            def __init__(self):
                self._parent_class = _parent_class
                super().__init__(_parent_class)

        class AccountHolderWrapper(AccountHolderGroupsCollection):

            def __init__(self):
                self._parent_class = _parent_class
                super().__init__(_parent_class)

        class AuthControlsWrapper(AuthControlsCollection):

            def __init__(self):
                self._parent_class = _parent_class
                super().__init__(_parent_class)

        class AutoreloadWrapper(AutoReloadsCollection):

            def __init__(self):
                self._parent_class = _parent_class
                super().__init__(_parent_class)

        class KycWrapper(KycCollection):

            def __init__(self):
                self._parent_class = _parent_class
                super().__init__(_parent_class)

        class BalancesTokenWrapper(BalancesTokenCollection):

            def __init__(self):
                self._parent_class = _parent_class
                super().__init__(_parent_class)

        class MsaOrdersWrapper(MsaOrdersCollection):

            def __init__(self):
                self._parent_class = _parent_class
                super().__init__(_parent_class)

        class OfferOrderWrapper(OfferOrdersCollection):

            def __init__(self):
                self._parent_class = _parent_class
                super().__init__(_parent_class)

        class DigitalWrapper(DigitalWalletTokensCollection):

            def __init__(self):
                self._parent_class = _parent_class
                super().__init__(_parent_class)

        class VelocityWrapper(VelocityControlsCollection):

            def __init__(self):
                self._parent_class = _parent_class
                super().__init__(_parent_class)

        class MccWrapper(MccGroupsCollection):

            def __init__(self):
                self._parent_class = _parent_class
                super().__init__(_parent_class)

        class TransactionWrapper(TransactionsCollection):

            def __init__(self):
                self._parent_class = _parent_class
                super().__init__(_parent_class)

        class ChargebackWrapper(ChargebacksCollection):

            def __init__(self):
                self._parent_class = _parent_class
                super().__init__(_parent_class)

        class FeeTransferWrapper(FeeTransfersCollection):

            def __init__(self):
                self._parent_class = _parent_class
                super().__init__(_parent_class)

        class ProgramTransferWrapper(ProgramTransfersCollection):

            def __init__(self):
                self._parent_class = _parent_class
                super().__init__(_parent_class)

        class FeesWrapper(FeesCollection):

            def __init__(self):
                self._parent_class = _parent_class
                super().__init__(_parent_class)

        class DirectDepositWrapper(DirectDepositsCollection):

            def __init__(self):
                self._parent_class = _parent_class
                super().__init__(_parent_class)

        class WebhookWrapper(WebhooksCollection):

            def __init__(self):
                self._parent_class = _parent_class
                super().__init__(_parent_class)

        class MerchantsWrapper(MerchantsCollection):

            def __init__(self):
                self._parent_class = _parent_class
                super().__init__(_parent_class)

        class StoresWrapper(StoresCollection):

            def __init__(self):
                self._parent_class = _parent_class
                super().__init__(_parent_class)

        class CampaignsWrapper(CampaignsCollection):

            def __init__(self):
                self._parent_class = _parent_class
                super().__init__(_parent_class)

        class CommandoModesWrapper(CommandoModesCollection):

            def __init__(self):
                self._parent_class = _parent_class
                super().__init__(_parent_class)

        class RealtimeFeeGroupWrapper(RealTimeFeeGroupsCollection):

            def __init__(self):
                self._parent_class = _parent_class
                super().__init__(_parent_class)

        class OffersWrapper(OffersCollection):

            def __init__(self):
                self._parent_class = _parent_class
                super().__init__(_parent_class)

        class BulkIssuancesWrapper(BulkIssuancesCollection):

            def __init__(self):
                self._parent_class = _parent_class
                super().__init__(_parent_class)

        class PushToCardsWrapper(PushToCardsCollection):

            def __init__(self):
                self._parent_class = _parent_class
                super().__init__(_parent_class)

        class PinsWrapper(PinsCollection):

            def __init__(self):
                self._parent_class = _parent_class
                super().__init__(_parent_class)

        return {'users': UsersWrapper,
                'card_products': CardProductWrapper,
                'cards': CardsWrapper,
                'gpa_orders': GpaOrderWrapper,
                'funding_sources': FundingWrapper,
                'businesses': BusinessWrapper,
                'accepted_countries': AcceptedCountriesWrapper,
                'account_holder_groups': AccountHolderWrapper,
                'auth_controls': AuthControlsWrapper,
                'auto_reloads': AutoreloadWrapper,
                'kyc': KycWrapper,
                'balances': BalancesTokenWrapper,
                'msa_orders': MsaOrdersWrapper,
                'offer_orders': OfferOrderWrapper,
                'digital_wallet_tokens': DigitalWrapper,
                'velocity_controls': VelocityWrapper,
                'mcc_groups': MccWrapper,
                'transactions': TransactionWrapper,
                'chargebacks': ChargebackWrapper,
                'fee_transfers': FeeTransferWrapper,
                'program_transfers': ProgramTransferWrapper,
                'fees': FeesWrapper,
                'direct_deposits': DirectDepositWrapper,
                'webhooks': WebhookWrapper,
                'merchants': MerchantsWrapper,
                'stores': StoresWrapper,
                'campaigns': CampaignsWrapper,
                'offers': OffersWrapper,
                'real_time_fee_groups': RealtimeFeeGroupWrapper,
                'commando_modes': CommandoModesWrapper,
                'bulk_issuances': BulkIssuancesWrapper,
                'push_to_cards': PushToCardsWrapper,
                'pins': PinsWrapper

                }
