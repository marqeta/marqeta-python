import unittest

from tests.lib.client import get_client
from tests.lib.funding_sources import FundingSources
from tests.lib.funding_source_verifications import verify_funding_account_response_model
from marqeta.errors import MarqetaError


class TestFundingSourcesListForUser(unittest.TestCase):
    """Tests for the funding_sources.list_for_user endpoint."""

    @classmethod
    def setUpClass(cls):
        """Setup for all tests in the class."""

        cls.client = get_client()

    def setUp(self):
        """Setup for each test in the class."""

        self.user = self.client.users.create({})

    def test_funding_sources_list_for_user_one(self):
        """Tests when one funding source is returned."""

        ach = FundingSources.get_user_ach_funding_source(self.user)

        results = self.client.funding_sources.list_for_user(self.user.token)

        self.assertEqual(
            len(results), 1, "Unexpected number of funding sources returned"
        )

        verify = FundingSources.get_funding_source_verify(ach)

        verify_funding_account_response_model(self, results[0], verify)

    def test_funding_sources_list_for_user_two(self):
        """Tests when two funding sources are returned."""

        ach_one = FundingSources.get_user_ach_funding_source(self.user)
        ach_two = FundingSources.get_user_ach_funding_source(self.user)

        results = self.client.funding_sources.list_for_user(self.user.token)

        self.assertEqual(
            len(results), 2, "Unexpected number of funding sources returned"
        )

        verify_one = FundingSources.get_funding_source_verify(ach_one)
        verify_two = FundingSources.get_funding_source_verify(ach_two)

        if results[0].token == ach_one.token:
            verify_funding_account_response_model(self, results[0], verify_one)
            verify_funding_account_response_model(self, results[1], verify_two)
        else:
            verify_funding_account_response_model(self, results[1], verify_one)
            verify_funding_account_response_model(self, results[0], verify_two)

    def test_funding_sources_list_for_user_zero(self):
        """Tests when no funding sources are returned."""

        with self.assertRaises(MarqetaError):
            self.client.funding_sources.list_for_user(self.user.token)

    def test_funding_sources_list_for_user_unknown(self):
        """Tests when the user is unknown."""

        with self.assertRaises(MarqetaError):
            self.client.funding_sources.list_for_user("Not a user token")
