import unittest

from tests.lib.client import get_client
from tests.lib.address_verifications import verify_card_holder_address_response
from tests.lib.funding_sources import FundingSources
from marqeta.errors import MarqetaError


class TestFundingSourcesAddressesSave(unittest.TestCase):
    """Tests for the funding_sources.addresses.save endpoint."""

    @classmethod
    def setUpClass(cls):
        """Setup for all tests in the class."""

        cls.client = get_client()

    def get_address_update(self):
        """Returns a default card holder address update model."""

        return {
            "first_name": "Sparkle",
            "last_name": "Fairy",
            "address_1": "699 Bellevue Ave",
            "city": "Oakland",
            "state": "CA",
            "zip": "94610",
            "country": "USA"
        }

    def test_addresses_save_user(self):
        """Updates the funding source address for a user."""

        address = FundingSources.get_user_card_holder_address()

        updated = self.client.funding_sources.addresses.save(
            address.token, self.get_address_update())

        verify_card_holder_address_response(
            self, updated, self.get_address_update())

    def test_addresses_save_business(self):
        """Updates the funding source address for a business."""

        address = FundingSources.get_business_card_holder_address()

        updated = self.client.funding_sources.addresses.save(
            address.token, self.get_address_update())

        verify_card_holder_address_response(
            self, updated, self.get_address_update())

    def test_addresses_save_bad_token(self):
        """Verifies the behavior is correct when a bad address token is used."""

        with self.assertRaises(MarqetaError):
            self.client.funding_sources.addresses.save(
                'Not an address token', self.get_address_update())
