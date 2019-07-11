import unittest

from tests.lib.client import get_client
from tests.lib.funding_sources import FundingSources
from tests.lib.funding_source_verifications import verify_funding_account_response_model
from marqeta.errors import MarqetaError


class TestFundingSourcesListForBusiness(unittest.TestCase):
    """Tests for the funding_sources.list_for_business endpoint."""

    @classmethod
    def setUpClass(cls):
        """Setup each test."""

        cls.client = get_client()

    def test_funding_sources_list_for_business_one(self):
        """Tests when one funding source is returned."""

        business = self.client.businesses.create({})

        ach_source = FundingSources.get_business_ach_funding_source(business)

        results = self.client.funding_sources.list_for_business(business.token)

        self.assertEqual(
            len(results), 1, 'Unexpected number of funding sources returned')

        verify = FundingSources.get_funding_source_verify(ach_source)

        verify_funding_account_response_model(self, results[0], verify)

    def test_funding_sources_list_for_business_two(self):
        """Tests when two funding sources are returned."""

        business = self.client.businesses.create({})

        ach_one = FundingSources.get_business_ach_funding_source(business)
        ach_two = FundingSources.get_business_ach_funding_source(business)

        results = self.client.funding_sources.list_for_business(business.token)

        self.assertEqual(
            len(results), 2, 'Unexpected number of funding sources returned')

        verify_one = FundingSources.get_funding_source_verify(ach_one)
        verify_two = FundingSources.get_funding_source_verify(ach_two)

        if results[0].token == ach_one.token:
            verify_funding_account_response_model(self, results[0], verify_one)
            verify_funding_account_response_model(self, results[1], verify_two)
        else:
            verify_funding_account_response_model(self, results[1], verify_one)
            verify_funding_account_response_model(self, results[0], verify_two)

    def test_funding_sources_list_for_business_zero(self):
        """Tests when no funding sources are returned."""

        business = self.client.businesses.create({})

        with self.assertRaises(MarqetaError):
            self.client.funding_sources.list_for_business(business.token)

    def test_funding_sources_list_for_business_unknown(self):
        """Tests when the business is unknown."""

        with self.assertRaises(MarqetaError):
            self.client.funding_sources.list_for_business(
                'Not a business token')

    def test_funding_sources_list_for_business_filter_type(self):
        """Filters list by type."""

        business = self.client.businesses.create({})

        FundingSources.get_business_ach_funding_source(business)
        card = FundingSources.get_business_payment_card(business)

        results = self.client.funding_sources.list_for_business(
            business.token, params={"type": "paymentcard"})

        self.assertEqual(
            len(results), 1, 'Unexpected number of funding sources returned')

        self.assertEqual(results[0].type, 'paymentcard',
                         'Filter did not return funding source with the correct type')

        verify = FundingSources.get_funding_source_verify(card)

        verify_funding_account_response_model(self, results[0], verify)
