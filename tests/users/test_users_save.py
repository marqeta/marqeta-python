import unittest

from marqeta.errors import MarqetaError
from tests.lib.client import get_client


class TestUsersSave(unittest.TestCase):
    """Tests for the users.save endpoint."""

    @classmethod
    def setUpClass(cls):
        """Setup for all the tests in the class."""

        cls.client = get_client()

    def verify_saved_user(self, response, verify):
        """

        Verifies a saved user record.

        Parameters:
        response (CardHolderModel): The API response to verify.

        verify (Dictionary): The values that should be in the response.

        """

        # Verify the correct class is being tested
        actual = response.__class__.__name__
        expected = 'CardHolderModel'

        self.assertEqual(actual, expected, 'Unexpected response found')

        # Verify the expected attributes are defined
        expected_attributes = [
            'token',
            'active',
            'first_name',
            'last_name',
            'uses_parent_account',
            'corporate_card_holder',
            'created_time',
            'last_modified_time',
            'metadata',
            'account_holder_group_token',
            'status'
        ]

        for attribute in expected_attributes:
            with self.subTest(f'{attribute} is not defined'):
                self.assertIsNotNone(getattr(response, attribute))

        # Verify values match expected values
        match_attributes = list(verify.keys())

        for attribute in match_attributes:
            expected = verify[attribute]

            # ssn is masked by default
            if attribute == 'ssn':
                expected = '___________'

            with self.subTest(f'{attribute} does not match the expected value'):
                self.assertEqual(getattr(response, attribute), expected)

    def test_save(self):
        """Updates a user who exists."""

        user = self.client.users.create({})

        update_params = {'first_name': 'Mary', 'last_name': 'Shepard'}

        updated = self.client.users.save(user.token, update_params)

        self.verify_saved_user(updated, update_params)

    # Tries to update a user who doesn't exist
    def test_save_nonexist(self):
        update_params = {'first_name': 'Mary', 'last_name': 'Shepard'}

        with self.assertRaises(MarqetaError):
            self.client.users.save('Does not exist', update_params)
