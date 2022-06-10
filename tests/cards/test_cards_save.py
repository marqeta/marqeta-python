import unittest

from tests.lib.client import get_client
from tests.lib.card_products import CardProducts
from marqeta.errors import MarqetaError


class TestCardsSave(unittest.TestCase):
    """Tests for the cards.save endpoint."""

    @classmethod
    def setUpClass(cls):
        """Setup for all the tests in this class."""

        cls.card_product = CardProducts().create()

    def setUp(self):
        """Setup each test."""

        self.client = get_client()

        user = self.client.users.create({})

        card_request = {
            "card_product_token": self.card_product.token,
            "user_token": user.token,
        }

        self.card = self.client.cards.create(card_request)

    def test_cards_save_metadata(self):
        """Updates the metadata value for a card."""

        card_update_request = {
            "token": self.card.token,
            "metadata": {"prop1": "Red nose"},
        }

        updated_card = self.client.cards.save(self.card.token, card_update_request)

        self.assertIsNotNone(
            updated_card.metadata, "Metadata section not found in updated card"
        )

        self.assertIsNotNone(
            updated_card.metadata["prop1"], "prop1 not found in the metadata"
        )

        self.assertEqual(
            updated_card.metadata["prop1"],
            card_update_request["metadata"]["prop1"],
            "Updated card metadata does not match expected value",
        )

    def test_cards_save_minimum_request(self):
        """Updates a card without specifying any update values."""

        card_update_request = {}

        updated_card = self.client.cards.save(self.card.token, card_update_request)

        self.assertEqual(updated_card.__dict__, self.card.__dict__)

    def test_cards_save_bad_update_request(self):
        """Update a card with a bad card token."""

        card_update_request = {"metadata": {"prop1": "Red nose"}}

        with self.assertRaises(MarqetaError):
            self.client.cards.save("Not a card token", card_update_request)
