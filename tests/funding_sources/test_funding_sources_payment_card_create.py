import unittest

from tests.lib.client import get_client
from tests.lib.funding_sources import FundingSources
from tests.lib.funding_source_verifications import verify_payment_card_response_model
from marqeta.errors import MarqetaError


class TestFundingSourcesPaymentCardCreate(unittest.TestCase):
    """Tests for the funding_sources.payment_card.create endpoint."""

    @classmethod
    def setUpClass(cls):
        """Setup for all tests in the class."""

        cls.client = get_client()

    def test_payment_card_create_user(self):
        """Creates a payment card for a user."""

        user = self.client.users.create({})

        payment_card_request = FundingSources.get_payment_card_request()
        payment_card_request["user_token"] = user.token

        payment_card = self.client.funding_sources.payment_card.create(
            payment_card_request
        )

        expected = FundingSources.get_payment_card_verify_values(payment_card_request)

        verify_payment_card_response_model(self, payment_card, expected)

    def test_payment_card_create_business(self):
        """Creates a payment card for a user."""

        business = self.client.businesses.create({})

        payment_card_request = FundingSources.get_payment_card_request()
        payment_card_request["business_token"] = business.token

        payment_card = self.client.funding_sources.payment_card.create(
            payment_card_request
        )

        expected = FundingSources.get_payment_card_verify_values(payment_card_request)

        verify_payment_card_response_model(self, payment_card, expected)

    def test_payment_card_create_bad_request(self):
        """Tests error handling when the card request is missing required data."""

        with self.assertRaises(MarqetaError):
            self.client.funding_sources.payment_card.create({})
