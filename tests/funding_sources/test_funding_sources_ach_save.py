import unittest

from tests.lib.client import get_client
from tests.lib.funding_sources import FundingSources
from tests.lib.ach_response_model import verify_ach_response_model
from marqeta.errors import MarqetaError


class TestFundingSourcesAchSave(unittest.TestCase):
    """Tests for the funding_sources.ach.save endpoint."""

    @classmethod
    def setUpClass(cls):
        """Setup for each test in the class."""

        cls.client = get_client()

    def get_funding_source_verify(self, funding_source):
        """Returns a dictionary to compare against a funding source."""

        verify = funding_source.__dict__['json_response']

        del verify['created_time']
        del verify['last_modified_time']
        del verify['date_sent_for_verification']

        return verify

    def test_ach_save_success(self):
        """Verifies the ach account with the correct verification amounts."""

        funding_source = FundingSources.get_user_ach_funding_source()

        amounts = self.client.funding_sources.ach(
            funding_source.token).verification_amounts()

        ach_verification = {
            "verify_amount1": amounts.verify_amount1,
            "verify_amount2": amounts.verify_amount2
        }

        result = self.client.funding_sources.ach.save(
            funding_source.token, ach_verification)

        verify = self.get_funding_source_verify(funding_source)

        verify['verification_status'] = 'ACH_VERIFIED'
        verify['active'] = True

        verify_ach_response_model(self, result, verify)

    def test_ach_save_fail(self):
        """Tries to verify the ach account with incorrect verification amounts."""

        funding_source = FundingSources.get_user_ach_funding_source()

        amounts = self.client.funding_sources.ach(
            funding_source.token).verification_amounts()

        ach_verification = {
            "verify_amount1": amounts.verify_amount1 + 0.01,
            "verify_amount2": amounts.verify_amount2 + 0.01
        }

        with self.assertRaises(MarqetaError):
            self.client.funding_sources.ach.save(
                funding_source.token, ach_verification)

    def test_ach_save_unknown_source(self):
        """Verifies behavior when the funding source cannot be found."""

        ach_verification = {
            "verify_amount1": 0.01,
            "verify_amount2": 0.01
        }

        with self.assertRaises(MarqetaError):
            self.client.funding_sources.ach.save(
                'Not a funding source token', ach_verification)
