import unittest

from tests.lib.client import get_client
from faker import Faker
from tests.lib.simulate import Simulate
from tests.lib.card_products import CardProducts


class TestTransactionsListForFundingSource(unittest.TestCase):
    """Tests for the transactions.list_for_funding_source endpoint."""

    @classmethod
    def setUpClass(cls):
        """Set up for all the tests in the test class."""
        cls.client = get_client()
        cls.fake = Faker()
        cls.sim = Simulate()
        cls._user = cls.get_user()
        cls._merchant = cls.get_merchant()
        cls._fund_source = cls.get_user_payment_card()
        cls._card_product = CardProducts().create()
        cls._card = cls.get_card()
        cls._address = cls.set_user_address()

        cls._auth_tokens = []

        cls.fund_card()
        cls.activate_card()
        cls.generate_authorizations(10)

    @classmethod
    def get_merchant(cls):
        """Returns a new merchant."""

        merchant_model = {
            "name": cls.fake.company()
        }

        return cls.client.merchants.create(merchant_model)

    @classmethod
    def get_user_payment_card(cls):
        """Creates a user payment card."""

        user = cls._user

        payment_card_request = {
            "user_token": user.token,
            "account_number": "4112344112344113",
            "cvv_number": "123",
            "exp_date": "0323",
            "zip": "94612"
        }

        return cls.client.funding_sources.payment_card.create(payment_card_request)

    @classmethod
    def get_user(cls):
        """Creates a user."""
        return cls.client.users.create({})

    @classmethod
    def get_card_product(cls):
        """Returns a new card product."""

        return cls._card_product

    @classmethod
    def get_card(cls):
        """Returns a card to make transactions with."""

        card_product = cls.get_card_product()

        card_request = {
            "card_product_token": card_product.token,
            "user_token": cls._user.token
        }

        return cls.client.cards.create(card_request)

    @classmethod
    def set_user_address(cls):
        """Defines a funding source address for the user."""

        request = {
            "user_token": cls._user.token,
            "first_name": "Marqeta",
            "last_name": "QE",
            "address_1": "180 Grand Ave.",
            "city": "Oakland",
            "state": "CA",
            "zip": "94612",
            "country": "USA"
        }

        return cls.client.funding_sources.addresses.create(request)

    @classmethod
    def fund_card(cls):
        """Funds the card with the payment card."""

        gpa_request = {
            "user_token": cls._user.token,
            "amount": 10000.00,
            "currency_code": "USD",
            "funding_source_token": cls._fund_source.token,
            "funding_source_address_token": cls._address.token
        }

        cls.client.gpa_orders.create(gpa_request)

    @classmethod
    def activate_card(cls):
        """Activates the user card."""

        transition_body = {
            "card_token": cls._card.token,
            "channel": "API",
            "state": "ACTIVE"
        }

        cls.client.cards(cls._card.token).transitions.create(transition_body)

    @classmethod
    def generate_authorizations(cls, num):
        """Generates the specified number of authorizations."""

        auth_request_model = {
            "card_token": cls._card.token,
            "amount": 100.0,
            "mid": cls._merchant.token
        }

        for _ in range(num):
            authorization = cls.sim.authorization(auth_request_model)
            cls._auth_tokens.append(authorization['transaction']['token'])

    def test_list_for_funding_source(self):
        """Tests the list for funding source endpoint."""

        auth_tokens = self._auth_tokens

        entries = self.client.transactions.list_for_funding_source(
            self._fund_source.token, limit=10)

        for entry in entries:
            with self.subTest('Unexpected authorization found'):
                self.assertIn(entry.token, auth_tokens)
