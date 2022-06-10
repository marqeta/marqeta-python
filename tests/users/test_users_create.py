import unittest

from tests.lib.client import get_client
from tests.lib.utilities import Utilities
from tests.lib.user_verifications import verify_user_card_holder_response


class TestUsersCreate(unittest.TestCase):
    """Tests for the users.create endpoint."""

    def setUp(self):
        """Setup for each test."""

        self.client = get_client()

    def add_default_user_values(self, user_values):
        """

        Adds the default user values to a record.

        Parameters:
        user_values (Dictionary): The values used to define a user

        Returns:
        Dictionary: The values used to define a user, with unset values set to their defaults.

        """

        defaults = {
            "active": True,
            "uses_parent_account": False,
            "corporate_card_holder": False,
            "metadata": {},
            "account_holder_group_token": "DEFAULT_AHG",
            "status": "ACTIVE",
        }

        return {**defaults, **user_values}

    def verify_user(self, response, verify):
        """

        Verifies a user record.

        Parameters:
        response (UserCardHolderResponse): The API response to verify.

        verify (Dictionary): The values that should be in the response.

        """

        # Verify the correct class is being tested
        actual = response.__class__.__name__
        expected = "UserCardHolderResponse"

        self.assertEqual(actual, expected, "Unexpected response found")

        # Verify the expected attributes are defined
        expected_attributes = [
            "token",
            "active",
            "uses_parent_account",
            "corporate_card_holder",
            "created_time",
            "last_modified_time",
            "metadata",
            "account_holder_group_token",
            "status",
            "deposit_account",
        ]

        for attribute in expected_attributes:
            with self.subTest(f"{attribute} is not defined"):
                self.assertIsNotNone(getattr(response, attribute))

        # Verify values match expected values
        match_attributes = list(verify.keys())

        for attribute in match_attributes:
            expected = verify[attribute]

            # ssn is masked by default
            if attribute == "ssn":
                expected = "___________"

            with self.subTest(f"{attribute} does not match the expected value"):
                self.assertEqual(getattr(response, attribute), expected)

    def test_create_empty_arg(self):
        """Invokes create with an empty object."""

        user_params = {}
        user = self.client.users.create(user_params)

        verify = self.add_default_user_values(user_params)

        self.verify_user(user, verify)

    def test_create_no_arg(self):
        """Invokes create without an argument."""

        user = self.client.users.create()

        verify = self.add_default_user_values({})

        self.verify_user(user, verify)

    def test_create_with_args(self):
        """Invokes create with defined arguments."""

        user_args = {"first_name": "Bob", "last_name": "Builder", "ssn": "123456789"}

        user = self.client.users.create(user_args)

        self.verify_user(user, user_args)

    def test_create_child_user(self):
        """Creates a child user."""

        parent = self.client.users.create({})
        parent_token = parent.token

        self.assertIsNotNone(parent_token, "Could not get token from parent user")

        user_args = {"parent_token": parent_token, "uses_parent_account": True}

        child = self.client.users.create(user_args)

        self.verify_user(child, user_args)

    def test_create_user_passport_expiration_date_formats(self):
        """Creates users using all the passport_expiration_date formats."""

        times = Utilities.get_current_time_all_formats()

        # Last date format being rejected by the API: PS-3891
        del times[-1]

        for time in times:
            user_args = {"passport_expiration_date": time}

            user = self.client.users.create(user_args)

            verify_user_card_holder_response(self, user, user_args)

    def test_create_user_id_card_expiration_date_formats(self):
        """Creates users using all the id_card_expiration_date formats."""

        times = Utilities.get_current_time_all_formats()

        # Last date format being rejected by the API: PS-3891
        del times[-1]

        for time in times:
            user_args = {"id_card_expiration_date": time}

            user = self.client.users.create(user_args)

            verify_user_card_holder_response(self, user, user_args)
