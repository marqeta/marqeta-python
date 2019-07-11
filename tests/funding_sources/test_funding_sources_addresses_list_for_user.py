import unittest

from tests.lib.client import get_client
from tests.lib.address_verifications import verify_card_holder_address_response
from tests.lib.funding_sources import FundingSources
from marqeta.errors import MarqetaError


class TestFundingSourcesAddressesListForUser(unittest.TestCase):
    """Tests for the funding_sources.addresses.list_for_user endpoint."""

    @classmethod
    def setUpClass(cls):
        """Setup for all tests in the class."""

        cls.client = get_client()

    def setUp(self):
        """Setup for each test in the class."""

        self.user = self.client.users.create({})

    def create_card_product(self):
        """Creates a card product."""

        product_details = {
            "name": "Simple Date Card Product",
            "start_date": "2019-02-01",
            "config": {
                "fulfillment": {
                    "payment_instrument": "VIRTUAL_PAN"
                }
            }
        }

        return self.client.card_products.create(product_details)

    def create_card(self, card_product, user):
        """Creates a card."""

        card_request = {
            "card_product_token": card_product.token,
            "user_token": user.token
        }

        return self.client.cards.create(card_request)

    def test_addresses_list_for_user_one(self):
        """Tests when one funding source address should be returned."""

        card_holder_address_model = FundingSources.get_card_holder_address_model()

        card_holder_address_model["user_token"] = self.user.token

        self.client.funding_sources.addresses.create(card_holder_address_model)

        self.create_card(self.create_card_product(), self.user)

        addresses = self.client.funding_sources.addresses.list_for_user(
            self.user.token)

        self.assertEqual(len(addresses), 1,
                         'Unexpected number of addresses retrieved')

        verify_card_holder_address_response(
            self, addresses[0], card_holder_address_model)

        with self.subTest('Address defined is not the default'):
            self.assertTrue(addresses[0].is_default_address)

    def test_addresses_list_for_user_two(self):
        """Tests when two funding source addresses should be returned."""

        card_holder_address_one = FundingSources.get_card_holder_address_model()

        card_holder_address_one["user_token"] = self.user.token

        card_holder_address_two = {
            "user_token": self.user.token,
            "first_name": "O",
            "last_name": "PD",
            "address_1": "455 7th St.",
            "city": "Oakland",
            "state": "CA",
            "zip": "94612",
            "country": "USA"
        }

        self.client.funding_sources.addresses.create(card_holder_address_one)
        self.client.funding_sources.addresses.create(card_holder_address_two)

        addresses = self.client.funding_sources.addresses.list_for_user(
            self.user.token)

        self.assertEqual(len(addresses), 2,
                         'Unexpected number of addresses retrieved')

        if addresses[0].first_name == card_holder_address_one['first_name']:
            verify_card_holder_address_response(
                self, addresses[0], card_holder_address_one)
            verify_card_holder_address_response(
                self, addresses[1], card_holder_address_two)
        else:
            verify_card_holder_address_response(
                self, addresses[1], card_holder_address_one)
            verify_card_holder_address_response(
                self, addresses[0], card_holder_address_two)

    def test_addresses_list_for_user_zero(self):
        """Tests when no funding source addresses should be returned."""

        user = self.client.users.create({})

        with self.assertRaises(MarqetaError):
            self.client.funding_sources.addresses.list_for_user(user.token)
