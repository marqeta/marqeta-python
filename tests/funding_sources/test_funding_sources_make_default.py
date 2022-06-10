import unittest

from tests.lib.client import get_client
from tests.lib.funding_sources import FundingSources
from tests.lib.funding_source_verifications import verify_payment_card_response_model
from marqeta.errors import MarqetaError


class TestFundingSourcesMakeDefault(unittest.TestCase):
    """Tests the funding_sources.make_default endpoint."""

    @classmethod
    def setUpClass(cls):
        """Setup for all tests in the class."""

        cls.client = get_client()

    def test_make_default_payment_card_user(self):
        """Makes a user payment card the default."""

        user = self.client.users.create({})

        FundingSources.get_user_payment_card(user)
        payment_card_two = FundingSources.get_user_payment_card(user)

        updated = self.client.funding_sources(payment_card_two.token).make_default()

        verify_payment_card_response_model(self, updated, {"is_default_account": True})

    def test_make_default_ach_user(self):
        """Makes a user ach account the default."""

        user = self.client.users.create({})

        FundingSources.get_user_ach_funding_source(user)
        source = FundingSources.get_user_ach_funding_source(user)

        default = self.client.funding_sources(source.token).make_default()

        verify_payment_card_response_model(self, default, {"is_default_account": True})

    def test_make_default_payment_card_business(self):
        """Makes a business payment card the default."""

        business = self.client.businesses.create({})

        FundingSources.get_business_payment_card(business)
        payment_card_two = FundingSources.get_business_payment_card(business)

        updated = self.client.funding_sources(payment_card_two.token).make_default()

        verify_payment_card_response_model(self, updated, {"is_default_account": True})

    def test_make_default_ach_business(self):
        """Makes a business ach account the default."""

        business = self.client.businesses.create({})

        FundingSources.get_business_ach_funding_source(business)
        source = FundingSources.get_business_ach_funding_source(business)

        default = self.client.funding_sources(source.token).make_default()

        verify_payment_card_response_model(self, default, {"is_default_account": True})

    def test_make_default_unknown_source(self):
        """Verifies behavior when the funding source can not be found."""

        with self.assertRaises(MarqetaError):
            self.client.funding_sources("Not a funding source token").make_default()
