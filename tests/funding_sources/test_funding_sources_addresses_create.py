import unittest

from tests.lib.client import get_client
from tests.lib.address_verifications import verify_card_holder_address_response
from tests.lib.funding_sources import FundingSources
from marqeta.errors import MarqetaError


class TestFundingSourcesAddressesCreate(unittest.TestCase):
    """Tests for the funding_sources.addresses.create endpoint."""

    @classmethod
    def setUpClass(cls):
        """Setup for all the tests in the class."""

        cls.client = get_client()

    def test_addresses_create_user(self):
        """Create a funding source address for a user."""

        user = self.client.users.create({})

        card_holder_address_model = FundingSources.get_card_holder_address_model()
        card_holder_address_model["user_token"] = user.token

        address = self.client.funding_sources.addresses.create(
            card_holder_address_model)

        verify_card_holder_address_response(
            self, address, card_holder_address_model)

    def test_addresses_create_business(self):
        """Create a funding source address for a business."""

        business = self.client.businesses.create({})

        card_holder_address_model = FundingSources.get_card_holder_address_model()
        card_holder_address_model["business_token"] = business.token

        address = self.client.funding_sources.addresses.create(
            card_holder_address_model)

        verify_card_holder_address_response(
            self, address, card_holder_address_model)

    def test_addresses_create_bad_model(self):
        """Create a funding source with an address model missing required fields."""

        with self.assertRaises(MarqetaError):
            self.client.funding_sources.addresses.create(
                FundingSources.get_card_holder_address_model())
