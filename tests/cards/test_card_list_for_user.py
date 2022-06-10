import unittest
from tests.lib.client import get_client
from tests.lib.card_products import CardProducts


class TestCardListForUser(unittest.TestCase):
    """Tests for the cards.list_for_user endpoint."""

    @classmethod
    def setUpClass(cls):
        """Setup for all tests in the class."""

        cls.card_product = CardProducts().create()

    def setUp(self):
        """Setup each test."""

        self.client = get_client()

        self.user = self.client.users.create({})

    def test_user_one_card(self):
        """Tests list when user has one card."""

        card_product = self.card_product

        card_request = {
            "card_product_token": card_product.token,
            "user_token": self.user.token,
        }

        card = self.client.cards.create(card_request)

        cards = self.client.cards.list_for_user(self.user.token)

        self.assertEqual(len(cards), 1, "Incorrect number of cards returned")

        self.assertEqual(cards[0].token, card.token, "Incorrect card seen in list")

    def test_user_two_cards(self):
        """Tests list when user has multiple cards."""

        card_product = self.card_product

        card_request = {
            "card_product_token": card_product.token,
            "user_token": self.user.token,
        }

        card_one = self.client.cards.create(card_request)
        card_two = self.client.cards.create(card_request)

        cards = self.client.cards.list_for_user(self.user.token)

        self.assertEqual(len(cards), 2, "Incorrect number of cards returned")

        if card_one.token == cards[0].token:
            self.assertEqual(
                card_two.token, cards[1].token, "Incorrect card seen in list"
            )
        elif card_two.token == cards[0].token:
            self.assertEqual(
                card_one.token, cards[1].token, "Incorrect card seen in list"
            )
        else:
            self.fail("Both cards in the list were unexpected")

    def test_user_zero_cards(self):
        """Tests list when user has zero cards"""

        cards = self.client.cards.list_for_user(self.user.token)

        self.assertEqual(len(cards), 0, "Incorrect number of cards returned")
