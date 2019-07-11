import unittest
import time

from tests.lib.client import get_client
from marqeta.errors import MarqetaError


class TestCardsMerchantFind(unittest.TestCase):
    """Tests for the cards.find_for_merchant endpoint."""

    def setUp(self):
        """Setup each test."""

        self.client = get_client()

    def get_merchant(self):
        """Creates a unique merchant."""

        merchant_options = {
            "name": "qe_merchant_" + str(int(time.time() % 1000000000))
        }

        return self.client.merchants.create(merchant_options)

    def get_card_product(self):
        """Creates a card product."""

        card_product_options = {
            "name": "Card Create Product",
            "start_date": "2019-02-01",
            "config": {
                "fulfillment": {
                    "payment_instrument": "VIRTUAL_PAN"
                },
                "special": {
                    "merchant_on_boarding": True
                }
            }
        }
        return self.client.card_products.create(card_product_options)

    def verify_card_response(self, response, verify):
        """

        Verifies a card response matches the expected values.

        Parameters:
        response (CardResponse): The response object to verify.

        verify (Dictionary): The values that should be in the response.

        """

        # Verify the expected attributes are defined
        expected_attributes = [
            'created_time',
            'last_modified_time',
            'token',
            'user_token',
            'card_product_token',
            'last_four',
            'pan',
            'expiration',
            'expiration_time',
            'barcode',
            'pin_is_set',
            'state',
            'state_reason',
            'fulfillment_status',
            'instrument_type',
            'expedite',
            'metadata'
        ]

        for attribute in expected_attributes:
            with self.subTest(f'{attribute} is not defined'):
                self.assertIsNotNone(getattr(response, attribute))

        # Verify values match expected values
        match_attributes = list(verify.keys())

        for attribute in match_attributes:
            # funding_source_token is masked for program funding sources
            if attribute == 'funding_source_token':
                continue
            with self.subTest(f'{attribute} does not match the expected value'):
                self.assertEqual(getattr(response, attribute),
                                 verify[attribute])

    def test_cards_merchant_find_success(self):
        """Test finding a merchant card that exists."""

        merchant = self.get_merchant()
        card_product = self.get_card_product()

        merchant_card_options = {
            "card_product_token": card_product.token
        }

        merchant_card = self.client.cards.create_for_merchant(
            merchant.token, merchant_card_options)

        found = self.client.cards.find_for_merchant(merchant.token)

        self.verify_card_response(found, merchant_card.__dict__)

    def test_cards_merchant_find_failure(self):
        """Tests behavior when looking for a merchant card that doesn't exist."""

        with self.assertRaises(MarqetaError):
            self.client.cards.find_for_merchant('Not a merchant token')
