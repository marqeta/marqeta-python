import unittest
import re

from tests.lib.client import get_client
from tests.lib.card_products import CardProducts
from marqeta.errors import MarqetaError


class TestCardsFindShowPan(unittest.TestCase):
    """Tests for the cards.find_show_pan endpoint."""

    @classmethod
    def setUpClass(cls):
        """Setup for all the tests in this class."""

        cls.card_product = CardProducts().create()

    def setUp(self):
        """Setup each test."""

        self.client = get_client()

    def test_find_show_pan_positive(self):
        """Tests find that returns a result."""

        user = self.client.users.create({})

        card_request = {
            "card_product_token": self.card_product.token,
            "user_token": user.token,
        }

        card_to_find = self.client.cards.create(card_request)

        card_found = self.client.cards.find_show_pan(card_to_find.token)

        self.assertIsNotNone(card_found.pan, "Card found does not have a PAN")

        pattern = r"\d{16}"

        x = re.compile(pattern)

        self.assertTrue(x.match(card_found.pan), "PAN does not match expected pattern")

    def test_find_show_negative(self):
        """Tests find that does not return a result."""

        with self.assertRaises(MarqetaError):
            self.client.cards.find_show_pan("Not a card token")
