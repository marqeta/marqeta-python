import unittest

from tests.lib.client import get_client
from tests.lib.verifications import verify_user_transition


class TestUsersTransitionsList(unittest.TestCase):
    """Tests for the users.transitions.list endpoint."""

    @classmethod
    def setUpClass(cls):
        """Setup for all the tests in the class."""
        cls.client = get_client()

    def setUp(self):
        """Setup for each test in the class."""
        self.user = self.client.users.create({})

    def get_user_created_transition(self):
        """Returns the default values for a user created transition."""

        return {
            "status": "ACTIVE",
            "reason_code": "14",
            "reason": "CardHolder creation",
            "channel": "SYSTEM",
        }

    def test_transitions_list_one(self):
        """Retrieve one transition."""

        transition_list = self.client.users(self.user.token).transitions.list()

        self.assertEqual(
            len(transition_list), 1, "Transition list has incorrect number of entries"
        )

        transition_one = transition_list[0]

        verify_user_transition(self, transition_one, self.get_user_created_transition())

    def test_transitions_list_two(self):
        """Retrieve two transitions."""

        transition_data = {
            "status": "SUSPENDED",
            "reason_code": "00",
            "reason": "They did bad things",
            "channel": "FRAUD",
            "user_token": self.user.token,
        }

        self.client.users(self.user.token).transitions.create(transition_data)

        transition_list = self.client.users(self.user.token).transitions.list()

        self.assertEqual(
            len(transition_list), 2, "Transition list has incorrect number of entries"
        )

        transition_one = transition_list[0]

        verify_user_transition(self, transition_one, transition_data)

        transition_two = transition_list[1]

        verify_user_transition(self, transition_two, self.get_user_created_transition())
