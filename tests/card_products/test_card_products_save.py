import unittest

from tests.lib.client import get_client
from tests.lib.card_products import CardProducts
from marqeta.errors import MarqetaError


class TestCardProductsSave(unittest.TestCase):
    """Tests for the card_products.save endpoint."""

    @classmethod
    def setUpClass(cls):
        """Setup for all tests in the class."""
        cls.card_products = CardProducts()

    def setUp(self):
        """Setup each test."""

        self.client = get_client()

    def test_card_products_save_name(self):
        """Updates the card product name."""

        card_product = self.card_products.create()

        update_options = {
            "name": "Updated card product name"
        }

        updated = self.client.card_products.save(
            card_product.token, update_options)

        self.assertEqual(updated.name, update_options['name'])

    def test_card_products_save_nothing(self):
        """Verifies behavior is correct when no update options are specified."""

        card_product = self.card_products.create()

        updated = self.client.card_products.save(card_product.token, {})

        self.assertEqual(updated.name, card_product.name)

    def test_card_products_save_not_found(self):
        """Verifies behavior is correct when the card product is not found."""

        with self.assertRaises(MarqetaError):
            self.client.card_products.save('Not a card product token', {})
