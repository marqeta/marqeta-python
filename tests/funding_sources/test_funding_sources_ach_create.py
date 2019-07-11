import unittest

from tests.lib.client import get_client
from tests.lib.funding_sources import FundingSources
from tests.lib.ach_response_model import verify_ach_response_model
from marqeta.errors import MarqetaError


class TestFundingSourcesAchCreate(unittest.TestCase):
    """Tests for the funding_sources.ach.create endpoint."""

    @classmethod
    def setUpClass(cls):
        """Setup for all tests in the class."""

        cls.client = get_client()

    def setUp(self):
        """Setup for each test in the class."""

        self.ach_model = FundingSources.get_ach_model()
        self.verify = self.get_basic_verification()

    def get_basic_verification(self):
        """Returns basic verification information."""

        ach_model = self.ach_model

        return {
            "verification_status": "VERIFICATION_PENDING",
            "account_type": ach_model["account_type"],
            "name_on_account": ach_model["name_on_account"]
        }

    def test_ach_create_for_user(self):
        """Creates an ach funding source for a user."""

        user = self.client.users.create({})

        self.ach_model["user_token"] = user.token

        funding_source = self.client.funding_sources.ach.create(self.ach_model)

        self.verify["user_token"] = user.token

        verify_ach_response_model(self, funding_source, self.verify)

    def test_ach_create_for_business(self):
        """Creates an ach funding source for a business."""

        business = self.client.businesses.create({})

        self.ach_model["business_token"] = business.token

        funding_source = self.client.funding_sources.ach.create(self.ach_model)

        self.verify["business_token"] = business.token

        verify_ach_response_model(self, funding_source, self.verify)

    def test_ach_create_failure(self):
        """Tests behavior when ach create fails."""

        with self.assertRaises(MarqetaError):
            self.client.funding_sources.ach.create({})
