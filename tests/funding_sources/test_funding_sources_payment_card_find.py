import unittest

from tests.lib.client import get_client
from tests.lib.funding_sources import FundingSources
from tests.lib.funding_source_verifications import verify_payment_card_response_model
from marqeta.errors import MarqetaError


class TestFundingSourcesPaymentCardFind(unittest.TestCase):
    """Tests for the funding_sources_payment_card_find endpoint."""

    @classmethod
    def setUpClass(cls):
        """Setup for all tests in the class."""

        cls.client = get_client()

    def test_payment_card_find_success(self):
        """Verifies find returns the correct payment card."""

        payment_card = FundingSources.get_user_payment_card()

        found = self.client.funding_sources.payment_card.find(payment_card.token)

        expected = FundingSources.get_funding_source_verify(payment_card)

        verify_payment_card_response_model(self, found, expected)

    def test_payment_card_find_fail(self):
        """Tests error handling when payment card is not found."""

        with self.assertRaises(MarqetaError):
            self.client.funding_sources.payment_card.find("Not a payment card token")
