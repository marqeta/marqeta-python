import unittest

from tests.lib.client import get_client
from tests.lib.card_products import CardProducts


class TestCardsTransitionsList(unittest.TestCase):
    """Tests for the card_transitions.list endpoint."""

    @classmethod
    def setUpClass(cls):
        """Setup for all the tests in this class."""

        cls.card_product = CardProducts().create()

    def setUp(self):
        """Setup each test."""

        self.client = get_client()

    def get_new_card(self):
        """Returns a new card."""

        user = self.client.users.create({})

        card_request = {
            "card_product_token": self.card_product.token,
            "user_token": user.token
        }

        return self.client.cards.create(card_request)

    def activate_card(self, card_token):
        """Activates a card."""
        transition_body = {
            "card_token": card_token,
            "channel": 'API',
            "state": "ACTIVE"
        }

        return self.client.cards(card_token).transitions.create(transition_body)

    def test_transitions_list_new(self):
        """Lists the transitions for a new card."""

        card = self.get_new_card()

        transitions = self.client.cards(card.token).transitions.list()

        self.assertIsNotNone(transitions, 'Transitions list is None')

        self.assertEqual(len(transitions), 1,
                         'Transitions list has incorrect number of entries')

        self.assertEqual(
            transitions[0].state, 'UNACTIVATED', 'State does not match expected value')

    def test_transitions_list_two(self):
        """Lists the transitions for a card with two transitions."""

        card = self.get_new_card()

        self.activate_card(card.token)

        transitions = self.client.cards(card.token).transitions.list()

        self.assertIsNotNone(transitions, 'Transitions list is None')

        self.assertEqual(len(transitions), 2,
                         'Transitions list has incorrect number of entries')

        if (transitions[0].state == 'UNACTIVATED'):
            self.assertEqual(
                transitions[1].state, 'ACTIVE', 'Transition has an unexpected state')
        elif (transitions[1].state == 'UNACTIVATED'):
            self.assertEqual(
                transitions[0].state, 'ACTIVE', 'Transition has an unexpected state')
        else:
            self.assertFail('None of the transitions has an expected state')
