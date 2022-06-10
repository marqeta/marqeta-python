import unittest
from tests.lib.client import get_client
from tests.lib.card_products import CardProducts


class TestCardsList(unittest.TestCase):
    """Holds the tests for the cards.list endpoint."""

    @classmethod
    def setUpClass(cls):
        """Setup for all the tests in this class."""

        cls.card_product = CardProducts().create()

    def setUp(self):
        """Setup each test."""

        self.client = get_client()

    def test_card_list_positive(self):
        """
        Tests that the card.list endpoint can return results.

        Can not assume only one card will be returned.
        Do not have control over the numbers assigned to cards.

        """

        user = self.client.users.create({})

        card_request = {
            "card_product_token": self.card_product.token,
            "user_token": user.token,
        }

        card = self.client.cards.create(card_request)

        list_cards = self.client.cards.list(card.last_four)

        self.assertTrue(len(list_cards) >= 1, "No cards were returned")

        for list_card in list_cards:
            with self.subTest("List contains card with incorrect last four"):
                self.assertEqual(card.last_four, list_card.last_four)

    def test_card_list_negative(self):
        """Tests when there are no entries in the cards.list"""

        list_cards = self.client.cards.list("AAAA")

        self.assertEqual(len(list_cards), 0, "List returned the wrong number of cards")

    def test_card_list_limit(self):
        """Tests the limit parameter for the card list."""

        limit = 5
        list_cards = self.client.cards.list("1234", limit=limit)

        self.assertLessEqual(len(list_cards), limit, "Page size limit was exceeded")
