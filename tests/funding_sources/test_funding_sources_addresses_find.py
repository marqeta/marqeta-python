import unittest

from tests.lib.client import get_client
from tests.lib.address_verifications import verify_card_holder_address_response
from tests.lib.funding_sources import FundingSources
from marqeta.errors import MarqetaError


class TestFundingSourcesAddressesFind(unittest.TestCase):
    """Tests for the funding_sources.addresses.find endpoint."""

    @classmethod
    def setUpClass(cls):
        """Setup for each test in the class."""

        cls.client = get_client()

    def get_address_expected(self, address):
        """

        Turns a CardholderAddressResponse object into a dictionary of expected values.

        Parameters:
        address (CardHolderAddressResponse): The response to convert.

        """

        address_expected = address.__dict__['json_response']

        del address_expected['created_time']
        del address_expected['last_modified_time']

        return address_expected

    def test_funding_sources_addresses_find_user(self):
        """Finds a user address."""

        address = FundingSources.get_user_card_holder_address()

        found = self.client.funding_sources.addresses.find(address.token)

        verify_card_holder_address_response(
            self, found, self.get_address_expected(address))

    def test_funding_sources_addresses_find_business(self):
        """Finds a business address."""

        address = FundingSources.get_business_card_holder_address()

        found = self.client.funding_sources.addresses.find(address.token)

        verify_card_holder_address_response(
            self, found, self.get_address_expected(address))

    def test_funding_sources_addresses_find_invalid_token(self):
        """Tries a find with a token that does not map to an address."""

        with self.assertRaises(MarqetaError):
            self.client.funding_sources.addresses.find('Not an address token')
