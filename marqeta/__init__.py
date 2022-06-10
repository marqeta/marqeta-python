"""

marqeta-python

The Marqeta Python library provides access to the Marqeta platform Core API.

This library is released as a Beta. If you find anything that needs fixing or can be improved,
please create an issue on GitHub.

**Version:** v0.1.0

**Author:** Marqeta, Inc.

**Copyright:** (c) 2019 Marqeta, Inc.

**License:** MIT

**Location:** <https://github.com/marqeta/marqeta-python>

Documentation
For complete reference documentation, see the Marqeta Core API Reference.

***Installation***

Requirements: Python 3.7+
Dependencies : Requests
Install from PyPi using pip, a package manager for Python.
pip install marqeta

*** Code Example ***
Initial setup:

from marqeta import Client

base_url = "https://shared-sandbox-api.marqeta.com" application_token = "user42291540313074" access_token = "xxx"

client = Client(base_url, application_token, access_token)

Making requests:

options = {

# Paging
"count": 5,
"start_index": 0,

# Sorting
"sort_by": "-lastModifiedTime",

# Filtering and expansion
"fields": ["field_1", "field_2"],
"expand": "user"
} client.get("cards", params=options)

body = { # Consult API reference }

client.post("cards", params=body)

body = { # Consult API reference }

client.put("cards", params=body)

"""
import sys
import json
import requests
from requests.exceptions import RequestException
from marqeta.version import __version__
from marqeta.errors import MarqetaError
from marqeta.resources.users import UsersCollection
from marqeta.resources.card_products import CardProductsCollection
from marqeta.resources.cards import CardsCollection
from marqeta.resources.gpa_orders import GpaOrdersCollection
from marqeta.resources.funding_sources import FundingSourcesCollection
from marqeta.resources.businesses import BusinessesCollection
from marqeta.resources.accepted_countries import AcceptedCountriesCollection
from marqeta.resources.account_holder_groups import AccountHolderGroupsCollection
from marqeta.resources.digital_wallet_tokens import DigitalWalletTokensCollection
from marqeta.resources.auth_controls import AuthControlsCollection
from marqeta.resources.auto_reloads import AutoReloadsCollection
from marqeta.resources.kyc import KycCollection
from marqeta.resources.balances import BalancesCollection
from marqeta.resources.msa_orders import MsaOrdersCollection
from marqeta.resources.offer_orders import OfferOrdersCollection
from marqeta.resources.bulk_issuances import BulkIssuancesCollection
from marqeta.resources.chargebacks import ChargebacksCollection
from marqeta.resources.commando_modes import CommandoModesCollection
from marqeta.resources.direct_deposits import DirectDepositsCollection
from marqeta.resources.fees import FeesCollection
from marqeta.resources.fee_transfers import FeeTransfersCollection
from marqeta.resources.mcc_groups import MccGroupsCollection
from marqeta.resources.merchants import MerchantsCollection
from marqeta.resources.program_transfers import ProgramTransfersCollection
from marqeta.resources.real_time_fee_groups import RealTimeFeeGroupsCollection
from marqeta.resources.transactions import TransactionsCollection
from marqeta.resources.velocity_controls import VelocityControlsCollection
from marqeta.resources.webhooks import WebhooksCollection
from marqeta.resources.push_to_cards import PushToCardsCollection
from marqeta.resources.pins import PinsCollection
from marqeta.response_models.ping_response import PingResponse
from marqeta.response_models.echo_ping_response import EchoPingResponse

headers = {
    "content-type": "application/json",
    "User-Agent": "marqeta-python/{} (Python {})".format(
        __version__, sys.version.split(" ")[0]
    ),
}

"""
Copyright (c) 2019 Marqeta, Inc.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


class Client(object):
    """
    Initializes the Marqeta Client
     base_url: Url to access
     application_token: authentication token for application
     access_token: authentication token for access

    Returns:
     Marqeta Client Object

    """

    DEFAULT_TIMEOUT = None

    def __init__(
        self,
        base_url=None,
        application_token=None,
        access_token=None,
        timeout=DEFAULT_TIMEOUT,
    ):

        self.base_url = base_url
        self.application_token = application_token
        self.access_token = access_token
        self.timeout = timeout
        objects = self._objects_container()
        self.users = objects["users"]()
        self.businesses = objects["businesses"]()
        self.card_products = objects["card_products"]()
        self.cards = objects["cards"]()
        self.funding_sources = objects["funding_sources"]()
        self.gpa_orders = objects["gpa_orders"]()
        self.accepted_countries = objects["accepted_countries"]()
        self.account_holder_groups = objects["account_holder_groups"]()
        self.auth_controls = objects["auth_controls"]()
        self.auto_reloads = objects["auto_reloads"]()
        self.kyc = objects["kyc"]()
        self.balances = objects["balances"]()
        self.msa_orders = objects["msa_orders"]()
        self.offer_orders = objects["offer_orders"]()
        self.digital_wallet_tokens = objects["digital_wallet_tokens"]()
        self.velocity_controls = objects["velocity_controls"]()
        self.mcc_groups = objects["mcc_groups"]()
        self.transactions = objects["transactions"]()
        self.chargebacks = objects["chargebacks"]()
        self.fee_transfers = objects["fee_transfers"]()
        self.program_transfers = objects["program_transfers"]()
        self.fees = objects["fees"]()
        self.direct_deposits = objects["direct_deposits"]()
        self.webhooks = objects["webhooks"]()
        self.merchants = objects["merchants"]()
        self.commando_modes = objects["commando_modes"]()
        self.bulk_issuances = objects["bulk_issuances"]()
        self.real_time_fee_groups = objects["real_time_fee_groups"]()
        self.push_to_cards = objects["push_to_cards"]()
        self.pins = objects["pins"]()

    def get(self, endpoint, query_params=None):
        """
        Gets the response for the requested endpoint
        :param endpoint:
        :param query_params:
        :return: json response and response status code
        """
        response = requests.get(
            url=self.base_url + endpoint,
            auth=(self.application_token, self.access_token),
            headers=headers,
            params=query_params,
            timeout=self.timeout,
        )

        if response.status_code >= 400:
            response = response.json()
            if "error_code" not in response:
                raise MarqetaError(error_message=response["error_message"])
            else:
                raise MarqetaError(
                    error_code=response["error_code"],
                    error_message=response["error_message"],
                )
        return response.json(), response.status_code

    def put(self, endpoint, data):
        """
        Updates the data for the endpoint
        :param endpoint:
        :param data:
        :return:json response and response status code
        """

        response = requests.put(
            url=self.base_url + endpoint,
            auth=(self.application_token, self.access_token),
            headers=headers,
            timeout=self.timeout,
            data=json.dumps(data),
        )
        if response.status_code >= 400:
            response = response.json()
            if "error_code" not in response:
                raise MarqetaError(error_message=response["error_message"])
            else:
                raise MarqetaError(
                    error_code=response["error_code"],
                    error_message=response["error_message"],
                )
        return response.json(), response.status_code

    def post(self, endpoint, data=None, query_params=None):
        """
        Creates the property for the requested endpoint
        :param endpoint:
        :param data:
        :param query_params: json response and response status code
        :return:
        """
        response = requests.post(
            url=self.base_url + endpoint,
            auth=(self.application_token, self.access_token),
            headers=headers,
            timeout=self.timeout,
            params=query_params,
            data=json.dumps(data),
        )
        if response.status_code >= 400:
            response = response.json()
            if "error_code" not in response:
                raise MarqetaError(error_message=response["error_message"])
            else:
                raise MarqetaError(
                    error_code=response["error_code"],
                    error_message=response["error_message"],
                )
        return response.json(), response.status_code

    def delete(self, endpoint):
        """
        Deletes the requested endpoint(For future use)
        :param endpoint:
        :return: json response and response status code
        """
        response = requests.delete(
            url=self.base_url + endpoint,
            auth=(self.application_token, self.access_token),
            headers=headers,
            timeout=self.timeout,
        )
        if response.status_code >= 400:
            response = response.json()
            if "error_code" not in response:
                raise MarqetaError(error_message=response["error_message"])
            else:
                raise MarqetaError(
                    error_code=response["error_code"],
                    error_message=response["error_message"],
                )
        return (response.json(), response.status_code)

    def ping(self, **kwargs):
        """
        ping validates the marqeta server
        :param kwargs:
        :return: PingResponse object or EchoPingResponse response
        """
        if kwargs:
            data = {key: kwargs[key] for key in kwargs}
            return EchoPingResponse(self.post("ping", data)[0])
        return PingResponse(self.get("ping")[0])

    def _objects_container(self):
        """
        Call subclasses via function to allow passing parent namespace to subclasses.
        :return: dict with objects references
        """

        _parent_class = self

        class UsersWrapper(UsersCollection):
            def __init__(self):
                self._parent_class = _parent_class
                super(UsersWrapper, self).__init__(_parent_class)

        class CardProductWrapper(CardProductsCollection):
            def __init__(self):
                self._parent_class = _parent_class
                super(CardProductWrapper, self).__init__(_parent_class)

        class CardsWrapper(CardsCollection):
            def __init__(self):
                self._parent_class = _parent_class
                super(CardsWrapper, self).__init__(_parent_class)

        class GpaOrderWrapper(GpaOrdersCollection):
            def __init__(self):
                self._parent_class = _parent_class
                super(GpaOrderWrapper, self).__init__(_parent_class)

        class FundingWrapper(FundingSourcesCollection):
            def __init__(self):
                self._parent_class = _parent_class
                super(FundingWrapper, self).__init__(_parent_class)

        class BusinessWrapper(BusinessesCollection):
            def __init__(self):
                self._parent_class = _parent_class
                super(BusinessWrapper, self).__init__(_parent_class)

        class AcceptedCountriesWrapper(AcceptedCountriesCollection):
            def __init__(self):
                self._parent_class = _parent_class
                super(AcceptedCountriesWrapper, self).__init__(_parent_class)

        class AccountHolderWrapper(AccountHolderGroupsCollection):
            def __init__(self):
                self._parent_class = _parent_class
                super(AccountHolderWrapper, self).__init__(_parent_class)

        class AuthControlsWrapper(AuthControlsCollection):
            def __init__(self):
                self._parent_class = _parent_class
                super(AuthControlsWrapper, self).__init__(_parent_class)

        class AutoreloadWrapper(AutoReloadsCollection):
            def __init__(self):
                self._parent_class = _parent_class
                super(AutoreloadWrapper, self).__init__(_parent_class)

        class KycWrapper(KycCollection):
            def __init__(self):
                self._parent_class = _parent_class
                super(KycWrapper, self).__init__(_parent_class)

        class BalancesTokenWrapper(BalancesCollection):
            def __init__(self):
                self._parent_class = _parent_class
                super(BalancesTokenWrapper, self).__init__(_parent_class)

        class MsaOrdersWrapper(MsaOrdersCollection):
            def __init__(self):
                self._parent_class = _parent_class
                super(MsaOrdersWrapper, self).__init__(_parent_class)

        class OfferOrderWrapper(OfferOrdersCollection):
            def __init__(self):
                self._parent_class = _parent_class
                super(OfferOrderWrapper, self).__init__(_parent_class)

        class DigitalWrapper(DigitalWalletTokensCollection):
            def __init__(self):
                self._parent_class = _parent_class
                super(DigitalWrapper, self).__init__(_parent_class)

        class VelocityWrapper(VelocityControlsCollection):
            def __init__(self):
                self._parent_class = _parent_class
                super(VelocityWrapper, self).__init__(_parent_class)

        class MccWrapper(MccGroupsCollection):
            def __init__(self):
                self._parent_class = _parent_class
                super(MccWrapper, self).__init__(_parent_class)

        class TransactionWrapper(TransactionsCollection):
            def __init__(self):
                self._parent_class = _parent_class
                super(TransactionWrapper, self).__init__(_parent_class)

        class ChargebackWrapper(ChargebacksCollection):
            def __init__(self):
                self._parent_class = _parent_class
                super(ChargebackWrapper, self).__init__(_parent_class)

        class FeeTransferWrapper(FeeTransfersCollection):
            def __init__(self):
                self._parent_class = _parent_class
                super(FeeTransferWrapper, self).__init__(_parent_class)

        class ProgramTransferWrapper(ProgramTransfersCollection):
            def __init__(self):
                self._parent_class = _parent_class
                super(ProgramTransferWrapper, self).__init__(_parent_class)

        class FeesWrapper(FeesCollection):
            def __init__(self):
                self._parent_class = _parent_class
                super(FeesWrapper, self).__init__(_parent_class)

        class DirectDepositWrapper(DirectDepositsCollection):
            def __init__(self):
                self._parent_class = _parent_class
                super(DirectDepositWrapper, self).__init__(_parent_class)

        class WebhookWrapper(WebhooksCollection):
            def __init__(self):
                self._parent_class = _parent_class
                super(WebhookWrapper, self).__init__(_parent_class)

        class MerchantsWrapper(MerchantsCollection):
            def __init__(self):
                self._parent_class = _parent_class
                super(MerchantsWrapper, self).__init__(_parent_class)

        class CommandoModesWrapper(CommandoModesCollection):
            def __init__(self):
                self._parent_class = _parent_class
                super(CommandoModesWrapper, self).__init__(_parent_class)

        class RealtimeFeeGroupWrapper(RealTimeFeeGroupsCollection):
            def __init__(self):
                self._parent_class = _parent_class
                super(RealtimeFeeGroupWrapper, self).__init__(_parent_class)

        class BulkIssuancesWrapper(BulkIssuancesCollection):
            def __init__(self):
                self._parent_class = _parent_class
                super(BulkIssuancesWrapper, self).__init__(_parent_class)

        class PushToCardsWrapper(PushToCardsCollection):
            def __init__(self):
                self._parent_class = _parent_class
                super(PushToCardsWrapper, self).__init__(_parent_class)

        class PinsWrapper(PinsCollection):
            def __init__(self):
                self._parent_class = _parent_class
                super(PinsWrapper, self).__init__(_parent_class)

        return {
            "users": UsersWrapper,
            "card_products": CardProductWrapper,
            "cards": CardsWrapper,
            "gpa_orders": GpaOrderWrapper,
            "funding_sources": FundingWrapper,
            "businesses": BusinessWrapper,
            "accepted_countries": AcceptedCountriesWrapper,
            "account_holder_groups": AccountHolderWrapper,
            "auth_controls": AuthControlsWrapper,
            "auto_reloads": AutoreloadWrapper,
            "kyc": KycWrapper,
            "balances": BalancesTokenWrapper,
            "msa_orders": MsaOrdersWrapper,
            "offer_orders": OfferOrderWrapper,
            "digital_wallet_tokens": DigitalWrapper,
            "velocity_controls": VelocityWrapper,
            "mcc_groups": MccWrapper,
            "transactions": TransactionWrapper,
            "chargebacks": ChargebackWrapper,
            "fee_transfers": FeeTransferWrapper,
            "program_transfers": ProgramTransferWrapper,
            "fees": FeesWrapper,
            "direct_deposits": DirectDepositWrapper,
            "webhooks": WebhookWrapper,
            "merchants": MerchantsWrapper,
            "real_time_fee_groups": RealtimeFeeGroupWrapper,
            "commando_modes": CommandoModesWrapper,
            "bulk_issuances": BulkIssuancesWrapper,
            "push_to_cards": PushToCardsWrapper,
            "pins": PinsWrapper,
        }

    def __repr__(self):
        return "<Marqeta.__init__.Client>"
