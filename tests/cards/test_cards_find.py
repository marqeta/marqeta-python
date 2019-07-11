import unittest

from tests.lib.client import get_client
from tests.lib.card_products import CardProducts
from marqeta.errors import MarqetaError


class TestCardsFind(unittest.TestCase):
    """Tests finding cards."""

    def setUp(self):
        """Setup for each test."""

        self.client = get_client()

    def test_card_find_success(self):
        """Look for a card that exists."""

        card_product = CardProducts().create()

        user = self.client.users.create({})

        card_request = {
            "card_product_token": card_product.token,
            "user_token": user.token
        }

        card = self.client.cards.create(card_request)

        result = self.client.cards.find(card.token)

        with self.subTest('User token does not match expected value'):
            self.assertEqual(result.user_token, user.token)

        with self.subTest('Card product token does not match expected value'):
            self.assertEqual(result.card_product_token, card_product.token)

        with self.subTest('Card token does not match expected value'):
            self.assertEqual(result.token, card.token)

    def test_card_find_fail(self):
        """Look for a card that does not exist."""

        with self.assertRaises(MarqetaError):
            self.client.cards.find('Not a card token')
