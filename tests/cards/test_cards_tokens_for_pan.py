import unittest

from tests.lib.client import get_client
from tests.lib.card_products import CardProducts
from marqeta.errors import MarqetaError


class TestCardsTokensForPan(unittest.TestCase):
    """Tests for the cards.tokens_for_pan endpoint"""

    @classmethod
    def setUpClass(cls):
        """Setup for all the tests in this class."""

        cls.card_product = CardProducts().create()

    def setUp(self):
        """Setup each test."""

        self.client = get_client()

    def verify_pan_response(self, response, verify):
        """

        Verifies a pan response has the correct values.

        Parameters:

        response (PanResponse): The object to check.

        verify (Dictionary): The values that should be in the response.

        """

        # Verify the expected attributes are defined
        expected_attributes = [
            'created_time',
            'last_modified_time',
            'user_token',
            'card_token'
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

    def test_get_tokens_valid_pan(self):
        """Test retrieving tokens with a valid PAN."""

        user = self.client.users.create({})

        card_request = {
            "card_product_token": self.card_product.token,
            "user_token": user.token
        }

        card_to_find = self.client.cards.create(card_request)

        card_found = self.client.cards.find_show_pan(card_to_find.token)

        self.assertIsNotNone(card_found.pan, 'Card found does not have a PAN')

        tokens = self.client.cards.tokens_for_pan(card_found.pan)

        expected = {
            "user_token": user.token,
            "card_token": card_to_find.token
        }

        self.verify_pan_response(tokens, expected)

    def test_get_tokens_invalid_pan(self):
        """Test retrieving tokens with an invalid PAN."""

        with self.assertRaises(MarqetaError):
            self.client.cards.tokens_for_pan('Not a valid PAN')
