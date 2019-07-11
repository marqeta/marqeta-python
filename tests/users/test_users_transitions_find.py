import unittest

from marqeta.errors import MarqetaError
from tests.lib.client import get_client
from tests.lib.verifications import verify_user_transition


class TestUsersTransitionsFind(unittest.TestCase):
    """Test for the users.transitions.find endpoint."""

    @classmethod
    def setUpClass(cls):
        """Setup for all the tests in the class."""

        cls.client = get_client()
        cls.user = cls.client.users.create({})

    def test_transitions_find_exists(self):
        """Find a user transition that exists."""

        transition_data = {
            'status': 'UNVERIFIED',
            'reason_code': '00',
            'reason': 'Testing',
            'channel': 'SYSTEM',
            'user_token': self.user.token
        }

        transition = self.client.users(
            self.user.token).transitions.create(transition_data)

        found_transition = self.client.users(
            self.user.token).transitions.find(transition.token)

        verify_user_transition(self, found_transition, transition_data)

    def test_transitions_find_does_not_exist(self):
        """Look for a user transition that does not exist."""

        with self.assertRaises(MarqetaError):
            self.client.users(self.user.token).transitions.find(
                'Does not exist')
