import unittest

from tests.lib.client import get_client
from tests.lib.funding_sources import FundingSources
from tests.lib.ach_response_model import verify_ach_response_model
from marqeta.errors import MarqetaError


class TestFundingSourcesAchFind(unittest.TestCase):
    """Tests for the funding_sources.ach.find endpoint."""

    @classmethod
    def setUpClass(cls):
        """Setup each test."""

        cls.client = get_client()

    def test_ach_find_success_user(self):
        """Tests successful find of an user ach funding source."""

        funding_source = FundingSources.get_user_ach_funding_source()

        found = self.client.funding_sources.ach.find(funding_source.token)

        verify_ach_response_model(self, found, funding_source.__dict__)

    def test_ach_find_success_business(self):
        """Tests successful find of a business ach funding source."""

        funding_source = FundingSources.get_business_ach_funding_source()

        found = self.client.funding_sources.ach.find(funding_source.token)

        verify_ach_response_model(self, found, funding_source.__dict__)

    def test_ach_find_fail(self):
        """Tests unsuccessful find of an ach funding source."""

        with self.assertRaises(MarqetaError):
            self.client.funding_sources.ach.find("Not a funding source token")
