from __future__ import absolute_import, division, print_function

from marqeta.errors import MarqetaError
from marqeta.resources.users import UsersCollection
from marqeta.resources.cardproducts import CardProductCollection
from marqeta.resources.cards import CardsCollection
from marqeta.resources.gpa_order import GpaCollection
from marqeta.resources.funding_sources import FundingSourcesCollection
from marqeta.resources.businesses import BusinessesCollection
from marqeta.resources.accepted_countries import AcceptedcountriesCollection
from marqeta.resources.account_holder_groups import AccountholdergroupsCollection
from marqeta.resources.digitalwallettokens import DigitalwallettokensCollection
from marqeta.resources.authcontrols import AuthcontrolsCollection
from marqeta.resources.autoreloads import AutoreloadsCollection
from marqeta.resources.kyc import KycCollection
from marqeta.resources.balances import BalancesTokenCollection
from marqeta.resources.msaorders import MsaordersCollection
from marqeta.resources.offerorders import OfferordersCollection
from marqeta.resources.bulkissuances import BulkissuancesCollection
from marqeta.resources.campaigns import CampaignsCollection
from marqeta.resources.chargebacks import ChargebacksCollection
from marqeta.resources.commandomodes import CommandomodesCollection
from marqeta.resources.directdeposits import DirectdepositsCollection
from marqeta.resources.fees import FeesCollection
from marqeta.resources.feetransfers import FeetransfersCollection
from marqeta.resources.mccgroups import MccgroupsCollection
from marqeta.resources.merchants import MerchantsCollection
from marqeta.resources.offerorders import OfferordersCollection
from marqeta.resources.offers import OffersCollection
from marqeta.resources.programtransfers import ProgramtransfersCollection
from marqeta.resources.realtimefeegroups import RealtimefeegroupsCollection
from marqeta.resources.stores import StoresCollection
from marqeta.resources.transactions import TransactionsCollection
from marqeta.resources.velocitycontrols import VelocitycontrolsCollection
from marqeta.resources.webhooks import WebhooksCollection
from marqeta.resources.pushtocards import PushtocardsCollection
from marqeta.resources.ping import PingCollection
from marqeta.resources.pins import PinsCollection


import requests,json


headers = {'content-type': 'application/json',
            'User-Agent': '"marqeta-python/{} (Python {})".format(__version__)'}

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
        # self.ping = objects['ping']()
        # self.pins = objects['pins']()


    def get(self, endpoint, query_params=None):
        response = requests.get(url=self.base_url + endpoint, auth=(
            self.application_token, self.access_token),
                                headers= headers,
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
        print(endpoint)
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
                                   headers= headers)
        if response.status_code >= 400:
            response = response.json()
            if 'error_code' not in response:
                raise MarqetaError(error_message=response['error_message'])
            else:
                raise MarqetaError(error_code=response['error_code'], error_message=response['error_message'])
        return (
            response.json(), response.status_code)

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

        class GpaWrapper(GpaCollection):

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

        class AcceptedcountriesWrapper(AcceptedcountriesCollection):

            def __init__(self):
                self._parent_class = _parent_class
                super().__init__(_parent_class)

        class AccountHolderWrapper(AccountholdergroupsCollection):

            def __init__(self):
                self._parent_class = _parent_class
                super().__init__(_parent_class)

        class AuthcontrolsWrapper(AuthcontrolsCollection):

            def __init__(self):
                self._parent_class = _parent_class
                super().__init__(_parent_class)

        class AutoreloadWrapper(AutoreloadsCollection):

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

        class MsaordersWrapper(MsaordersCollection):

            def __init__(self):
                self._parent_class = _parent_class
                super().__init__(_parent_class)

        class OfferOrderWrapper(OfferordersCollection):

            def __init__(self):
                self._parent_class = _parent_class
                super().__init__(_parent_class)

        class DigitalWrapper(DigitalwallettokensCollection):

            def __init__(self):
                self._parent_class = _parent_class
                super().__init__(_parent_class)

        class VelocityWrapper(VelocitycontrolsCollection):

            def __init__(self):
                self._parent_class = _parent_class
                super().__init__(_parent_class)

        class MccWrapper(MccgroupsCollection):

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

        class FeeTransferWrapper(FeetransfersCollection):

            def __init__(self):
                self._parent_class = _parent_class
                super().__init__(_parent_class)

        class ProgramTransferWrapper(ProgramtransfersCollection):

            def __init__(self):
                self._parent_class = _parent_class
                super().__init__(_parent_class)

        class FeesWrapper(FeesCollection):

            def __init__(self):
                self._parent_class = _parent_class
                super().__init__(_parent_class)

        class DirectDepositWrapper(DirectdepositsCollection):

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

        class CommandomodesWrapper(CommandomodesCollection):

            def __init__(self):
                self._parent_class = _parent_class
                super().__init__(_parent_class)

        class RealtimeFeeGroupWrapper(RealtimefeegroupsCollection):

            def __init__(self):
                self._parent_class = _parent_class
                super().__init__(_parent_class)

        class OffersWrapper(OffersCollection):

            def __init__(self):
                self._parent_class = _parent_class
                super().__init__(_parent_class)

        class BulkissuancesWrapper(BulkissuancesCollection):

            def __init__(self):
                self._parent_class = _parent_class
                super().__init__(_parent_class)

        class PushtocardsWrapper(PushtocardsCollection):

            def __init__(self):
                self._parent_class = _parent_class
                super().__init__(_parent_class)

        class PingWrapper(PingCollection):

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
                'gpa_orders': GpaWrapper,
                'funding_sources': FundingWrapper,
                'businesses': BusinessWrapper,
                'accepted_countries': AcceptedcountriesWrapper,
                'account_holder_groups': AccountHolderWrapper,
                'auth_controls': AuthcontrolsWrapper,
                'auto_reloads': AutoreloadWrapper,
                'kyc': KycWrapper,
                'balances': BalancesTokenWrapper,
                'msa_orders':MsaordersWrapper,
                'offer_orders': OfferOrderWrapper,
                'digital_wallet_tokens':DigitalWrapper,
                'velocity_controls':VelocityWrapper ,
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
                'commando_modes': CommandomodesWrapper,
                'bulk_issuances': BulkissuancesWrapper,
                'push_to_cards': PushtocardsWrapper,
                'ping': PingWrapper,
                'pins': PinsWrapper

                }

