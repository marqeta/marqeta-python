import unittest

from tests.lib.client import get_client
from tests.lib.card_products import CardProducts
from tests.lib.card_verifications import verify_card_response


class TestCardsCreate(unittest.TestCase):
    """Tests for the cards.create endpoint."""

    @classmethod
    def setUpClass(cls):
        """Setup for all tests in the class."""

        cls.client = get_client()
        cls.card_product = CardProducts().create()
        cls.user = cls.client.users.create()
        cls.card_request = {
            "card_product_token": cls.card_product.token,
            "user_token": cls.user.token
        }

    def test_create_minimum(self):
        """Minimal card creation test."""

        card = self.client.cards.create(self.card_request)

        expected = {}
        expected.update(self.card_request)
        expected['pin_is_set'] = False
        expected['state'] = 'UNACTIVATED'
        expected['state_reason'] = 'New card'
        expected['fulfillment_status'] = 'ISSUED'
        expected['instrument_type'] = 'VIRTUAL_PAN'
        expected['expedite'] = False
        expected['metadata'] = {}

        verify_card_response(self, card, expected)

    def test_create_show_cvv_true(self):
        """Creates a card and shows the cvv in the response."""

        params = {
            "show_cvv_number": True
        }

        card = self.client.cards.create(self.card_request, params=params)

        verify_card_response(self, card, self.card_request)

        self.assertRegex(
            card.cvv_number, r'\d{3}', 'CVV number did not match expected format')

    def test_create_show_cvv_false(self):
        """Creates a card and doesn't show the cvv in the response."""

        params = {
            "show_cvv_number": False
        }

        card = self.client.cards.create(self.card_request, params=params)

        verify_card_response(self, card, self.card_request)

        self.assertIsNone(
            card.cvv_number, 'CVV number seen in the card response')

    def test_create_show_pan_true(self):
        """Creates a card and shows the entire PAN in the response."""

        params = {
            "show_pan": True
        }

        card = self.client.cards.create(self.card_request, params=params)

        verify_card_response(self, card, self.card_request)

        self.assertRegex(card.pan, r'\d{16}', 'Full PAN was not shown')

    def test_create_show_pan_false(self):
        """Creates a card and shows a masked PAN in the response."""

        params = {
            "show_pan": False
        }

        card = self.client.cards.create(self.card_request, params=params)

        verify_card_response(self, card, self.card_request)

        self.assertRegex(
            card.pan, r'\d{6}_{6}\d{4}', 'Masked PAN was not shown')

    def test_create_show_cvv_and_pan(self):
        """Creates a card and shows both the CVV and full PAN in the response."""

        params = {
            "show_cvv_number": True,
            "show_pan": True
        }

        card = self.client.cards.create(self.card_request, params=params)

        verify_card_response(self, card, self.card_request)

        with self.subTest('CVV number did not match expected format'):
            self.assertRegex(card.cvv_number, r'\d{3}')

        with self.subTest('Full PAN was not shown'):
            self.assertRegex(card.pan, r'\d{16}')
