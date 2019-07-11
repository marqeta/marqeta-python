import unittest

from tests.lib.client import get_client
from tests.lib.address_verifications import verify_card_holder_address_response
from tests.lib.funding_sources import FundingSources
from marqeta.errors import MarqetaError


class TestFundingSourcesAddressesListForBusiness(unittest.TestCase):
    """Tests for the funding_sources.addresses.list_for_business endpoint."""

    @classmethod
    def setUpClass(cls):
        """Setup for all tests in the class."""

        cls.client = get_client()

    def test_addresses_list_for_business_one(self):
        """Tests when one funding source address should be returned."""

        business = self.client.businesses.create({})

        address = FundingSources.get_business_card_holder_address(business)

        FundingSources.get_business_payment_card(business)

        addresses = self.client.funding_sources.addresses.list_for_business(
            business.token)

        self.assertEqual(len(addresses), 1,
                         'Incorrect number of addresses returned')

        verify_card_holder_address_response(
            self, addresses[0], address.__dict__)

    def test_addresses_list_for_business_two(self):
        """Tests when two funding source addresses should be returned."""

        business = self.client.businesses.create({})

        address_one = FundingSources.get_card_holder_address_model()

        address_one["business_token"] = business.token

        address_two = {
            "business_token": business.token,
            "first_name": "O",
            "last_name": "PD",
            "address_1": "455 7th St.",
            "city": "Oakland",
            "state": "CA",
            "zip": "94612",
            "country": "USA"
        }

        self.client.funding_sources.addresses.create(address_one)
        self.client.funding_sources.addresses.create(address_two)

        addresses = self.client.funding_sources.addresses.list_for_business(
            business.token)

        self.assertEqual(len(addresses), 2,
                         'Incorrect number of addresses returned')

        if addresses[0].first_name == address_one['first_name']:
            verify_card_holder_address_response(
                self, addresses[0], address_one)
            verify_card_holder_address_response(
                self, addresses[1], address_two)
        else:
            verify_card_holder_address_response(
                self, addresses[1], address_one)
            verify_card_holder_address_response(
                self, addresses[0], address_two)

    def test_addresses_list_for_business_zero(self):
        """Tests when no funding source addresses should be returned."""

        business = self.client.businesses.create({})

        with self.assertRaises(MarqetaError):
            self.client.funding_sources.addresses.list_for_user(business.token)
