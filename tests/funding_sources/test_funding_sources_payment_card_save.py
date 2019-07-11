import unittest

from tests.lib.client import get_client
from tests.lib.funding_sources import FundingSources
from tests.lib.funding_source_verifications import verify_payment_card_response_model
from marqeta.errors import MarqetaError


class TestFundingSourcesPaymentCardSave(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Setup for all tests in the class."""

        cls.client = get_client()
        cls.token_update_request = {
            "exp_date": "0424"
        }

    def test_payment_card_save_user(self):
        """Updates a payment card for a user."""

        payment_card = FundingSources.get_user_payment_card()

        updated = self.client.funding_sources.payment_card.save(
            payment_card.token, self.token_update_request)

        verify = FundingSources.get_funding_source_verify(payment_card)
        verify["exp_date"] = self.token_update_request["exp_date"]

        verify_payment_card_response_model(self, updated, verify)

    def test_payment_card_save_business(self):
        """Updates a payment card for a business."""

        payment_card = FundingSources.get_business_payment_card()

        updated = self.client.funding_sources.payment_card.save(
            payment_card.token, self.token_update_request)

        verify = FundingSources.get_funding_source_verify(payment_card)
        verify["exp_date"] = self.token_update_request["exp_date"]

        verify_payment_card_response_model(self, updated, verify)

    def test_payment_card_save_error_token(self):
        """Tests error handling when a bad payment card token is passed."""

        with self.assertRaises(MarqetaError):
            self.client.funding_sources.payment_card.save(
                'Not a payment card token', self.token_update_request)

    def test_payment_card_save_error_request(self):
        """Tests error handling when a bad update request is passed."""

        payment_card = FundingSources.get_user_payment_card()

        with self.assertRaises(MarqetaError):
            self.client.funding_sources.payment_card.save(
                payment_card.token, {})
