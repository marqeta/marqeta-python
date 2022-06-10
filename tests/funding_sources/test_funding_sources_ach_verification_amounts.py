import unittest

from tests.lib.client import get_client
from tests.lib.funding_sources import FundingSources
from marqeta.errors import MarqetaError


class TestFundingSourcesAchVerificationAmounts(unittest.TestCase):
    """Tests for the funding_sources.ach.verification_amounts endpoint."""

    @classmethod
    def setUpClass(cls):
        """Setup for each test in the class."""

        cls.client = get_client()

    def test_ach_verification_amounts_user(self):
        """Retrieves the verification amounts for a user funding source."""

        funding_source = FundingSources.get_user_ach_funding_source()

        amounts = self.client.funding_sources.ach(
            funding_source.token
        ).verification_amounts()

        with self.subTest("First verification amount not within expected range"):
            self.assertTrue(0 < amounts.verify_amount1 < 1)

        with self.subTest("Second verification amount not within expected range"):
            self.assertTrue(0 < amounts.verify_amount2 < 1)

    def test_ach_verification_amounts_fail(self):
        """Tests behavior when can not get verification amounts"""

        with self.assertRaises(MarqetaError):
            self.client.funding_sources.ach(
                "Not a funding source token"
            ).verification_amounts()
