import unittest

from marqeta.errors import MarqetaError
from tests.lib.client import get_client


class TestUsersFind(unittest.TestCase):
    """Tests for the users.find endpoint."""

    @classmethod
    def setUpClass(cls):
        """Set up for all the tests in the class."""
        cls.client = get_client()

    def strip_deposit_account(self, user_record):
        """
        Converts a user record to a dictionary and removes the deposit account section.

        Parameters:
        user_record (UserRecord): The user to convert.

        Returns:
        Dictionary: The user record with the deposit account section removed.

        """

        user_dict = dict(user_record.__dict__)

        del user_dict["json_response"]["deposit_account"]

        return user_dict

    def test_find_user_exists(self):
        """Retrieve an existing user."""

        user = self.client.users.create({})

        self.assertIsNotNone(user.token, "User token was not found")

        found = self.client.users.find(user.token)

        # Deposit account will not be in the found object
        user_dict = self.strip_deposit_account(user)

        self.assertEqual(found.__dict__, user_dict, "Correct user was not found")

    def test_find_user_doesnt_exist(self):
        """Retrieve a user that does not exist."""

        with self.assertRaises(MarqetaError):
            self.client.users.find("Does not exist")
