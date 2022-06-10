import unittest

from tests.lib.client import get_client
from tests.lib.verifications import verify_user_transition


class TestUsersTransitionsCreate(unittest.TestCase):
    """Tests the users.transitions.create endpoint."""

    @classmethod
    def setUpClass(cls):
        """Setup for each test in the class."""
        cls.client = get_client()
        cls.user = cls.client.users.create({})
        cls.transition_data = {
            "reason_code": "00",
            "reason": "Testing",
            "channel": "SYSTEM",
            "user_token": cls.user.token,
        }

    def test_transitions_create_unverified(self):
        """Transition a user to unverified."""

        self.transition_data["status"] = "UNVERIFIED"

        transition = self.client.users(self.user.token).transitions.create(
            self.transition_data
        )

        verify_user_transition(self, transition, self.transition_data)

    def test_transitions_create_limited(self):
        """Transition a user to limited."""

        self.transition_data["status"] = "LIMITED"

        transition = self.client.users(self.user.token).transitions.create(
            self.transition_data
        )

        verify_user_transition(self, transition, self.transition_data)

    def test_transitions_create_active(self):
        """Transition a user to active."""

        self.transition_data["status"] = "ACTIVE"

        transition = self.client.users(self.user.token).transitions.create(
            self.transition_data
        )

        verify_user_transition(self, transition, self.transition_data)

    def test_transitions_create_suspended(self):
        """Transition a user to suspended."""

        self.transition_data["status"] = "SUSPENDED"

        transition = self.client.users(self.user.token).transitions.create(
            self.transition_data
        )

        verify_user_transition(self, transition, self.transition_data)

    def test_transitions_create_closed(self):
        """Transition a user to closed."""

        self.transition_data["status"] = "CLOSED"

        transition = self.client.users(self.user.token).transitions.create(
            self.transition_data
        )

        verify_user_transition(self, transition, self.transition_data)
