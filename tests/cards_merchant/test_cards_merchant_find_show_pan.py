import unittest
import time
import re

from tests.lib.client import get_client
from marqeta.errors import MarqetaError


class TestCardsMerchantFindShowPan(unittest.TestCase):
    """Tests for the cards.find_for_merchant_show_pan endpoint."""

    def setUp(self):
        """Setup each test."""

        self.client = get_client()

    def get_merchant(self):
        """Creates a unique merchant."""

        merchant_options = {"name": "qe_merchant_" + str(int(time.time() % 1000000000))}

        return self.client.merchants.create(merchant_options)

    def get_card_product(self):
        """Creates a card product."""

        card_product_options = {
            "name": "Card Create Product",
            "start_date": "2019-02-01",
            "config": {
                "fulfillment": {"payment_instrument": "VIRTUAL_PAN"},
                "special": {"merchant_on_boarding": True},
            },
        }
        return self.client.card_products.create(card_product_options)

    def test_cards_merchant_find_show_pan_success(self):
        """Test showing the whole pan for a merchant card that exists."""

        merchant = self.get_merchant()
        card_product = self.get_card_product()

        merchant_card_options = {"card_product_token": card_product.token}

        self.client.cards.create_for_merchant(merchant.token, merchant_card_options)

        found = self.client.cards.find_for_merchant_show_pan(merchant.token)

        pattern = r"\d{16}"

        x = re.compile(pattern)

        self.assertTrue(
            x.match(found.pan), f"PAN {found.pan} does not match expected pattern"
        )

    def test_cards_merchant_find_show_pan_fail(self):
        """Tests behavior when merchant card is not found."""

        with self.assertRaises(MarqetaError):
            self.client.cards.find_for_merchant_show_pan("Not a merchant token")
