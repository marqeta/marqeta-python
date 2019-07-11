import unittest

from tests.lib.client import get_client
from tests.lib.card_products import CardProducts
from marqeta.errors import MarqetaError


class TestCardsFindByBarcode(unittest.TestCase):
    """Tests for the card.find_by_barcode endpoint"""

    @classmethod
    def setUpClass(cls):
        """Setup for all the tests in this class."""
        cls.card_product = CardProducts().create()

    def setUp(self):
        """Setup each test."""

        self.client = get_client()

    def test_find_by_barcode_positive(self):
        """Test behavior when find_by_barcode should return a result."""

        user = self.client.users.create({})

        card_request = {
            "card_product_token": self.card_product.token,
            "user_token": user.token
        }

        card = self.client.cards.create(card_request)

        card_found = self.client.cards.find_by_barcode(card.barcode)

        self.assertEqual(card_found.barcode, card.barcode,
                         'Incorrect card returned by find')

    def test_find_by_barcode_negative(self):
        """Test behavior when find_by_barcode should not return a result"""

        with self.assertRaises(MarqetaError):
            self.client.cards.find_by_barcode('Not a barcode')
