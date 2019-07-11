import unittest

from tests.lib.client import get_client


class TestUsersSsn(unittest.TestCase):
    """Tests for the users.ssn endpoint."""

    @classmethod
    def setUpClass(cls):
        """Setup for each test in the class."""

        cls.client = get_client()

    def test_ssn(self):
        """Retrieves a ssn from a user that has a ssn."""

        full_ssn = '123456789'

        user = self.client.users.create({'ssn': full_ssn})

        ssn = self.client.users(user.token).ssn()

        # Need to specify ssn here - endpoint can retrieve multiple types of ids.
        self.assertEqual(ssn.ssn, full_ssn[5:9], 'Last 4 of SSN was not seen')

    def test_ssn_undefined(self):
        """Retrieves a ssn from a user that does not have a ssn."""

        user = self.client.users.create({})

        ssn = self.client.users(user.token).ssn()

        self.assertIsNone(ssn.ssn, 'Missing SSN not handled properly')

    def test_ssn_full(self):
        """Retrieves a full ssn."""

        full_ssn = '123456789'

        user = self.client.users.create({'ssn': full_ssn})

        ssn = self.client.users(user.token).ssn(full_ssn=True)

        self.assertEqual(ssn.ssn, full_ssn, 'Full SSN was not seen')
