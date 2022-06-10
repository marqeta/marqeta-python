import unittest

from tests.lib.client import get_client
from tests.lib.card_products import CardProducts
from tests.lib.card_transition_response import verify_card_transition_response
from tests.lib.utilities import Utilities


class TestCardsTransitionsCreate(unittest.TestCase):
    """Tests for the cards.transitions.create endpoint."""

    @classmethod
    def setUpClass(cls):
        """Setup for all the tests in this class."""

        cls.client = get_client()

        card_product = CardProducts().create()

        user = cls.client.users.create({})

        card_request = {
            "card_product_token": card_product.token,
            "user_token": user.token,
        }

        cls.card = cls.client.cards.create(card_request)

        cls.transition_body = {"card_token": cls.card.token, "channel": "API"}

    def get_default_transition_values(self):
        """Returns default transition values."""

        return {
            "fulfillment_status": "ISSUED",
            "validations": {
                "user": {"birth_date": False, "phone": False, "ssn": False}
            },
            "expiration": Utilities().get_card_expiration(),
            "pin_is_set": False,
            "user": {"metadata": {}},
            "card": {"metadata": {}},
        }

    def get_expected_values(self):
        """Returns the default expected values."""

        return {**self.get_default_transition_values(), **self.transition_body}

    def test_transition_create_api_active(self):
        """Tests transition to ACTIVE state."""

        self.transition_body["state"] = "ACTIVE"

        transition = self.client.cards(self.card.token).transitions.create(
            self.transition_body
        )

        verify_card_transition_response(self, transition, self.get_expected_values())

    def test_transition_create_api_suspended(self):
        """Tests transition to SUSPENDED state."""

        # Activate the card
        self.transition_body["state"] = "ACTIVE"

        self.client.cards(self.card.token).transitions.create(self.transition_body)

        # Suspend the card
        self.transition_body["state"] = "SUSPENDED"

        transition = self.client.cards(self.card.token).transitions.create(
            self.transition_body
        )

        verify_card_transition_response(self, transition, self.get_expected_values())

    def test_transition_create_api_terminated(self):
        """Tests transition to TERMINATED state."""

        self.transition_body["state"] = "TERMINATED"

        transition = self.client.cards(self.card.token).transitions.create(
            self.transition_body
        )

        verify_card_transition_response(self, transition, self.get_expected_values())
