import unittest

from tests.lib.client import SingletonClient
from tests.lib.card_products import CardProducts
from marqeta.errors import MarqetaError


class TestCardProductsFind(unittest.TestCase):
    """Holds tests for the card_products.find endpoint"""

    @classmethod
    def setUpClass(cls):
        """Setup for all tests in the class."""
        cls.card_products = CardProducts()

    def setUp(self):
        """Setup each test."""

        self.client = SingletonClient.get()

    def test_card_products_find_success(self):
        """Should successfully find a card product."""

        card_product = self.card_products.create()

        found = self.client.card_products.find(card_product.token)

        self.assertIsNotNone(found, "No card products were found")

        with self.subTest("Card returned has wrong token"):
            self.assertEqual(found.token, card_product.token)

        with self.subTest("Card returned has wrong name"):
            self.assertEqual(found.name, card_product.name)

    def test_card_products_find_failure(self):
        """Testing expected behavior when a card product is not found."""

        with self.assertRaises(MarqetaError):
            self.client.card_products.find("Not a card product token")
