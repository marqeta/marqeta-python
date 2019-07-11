import unittest

from tests.lib.client import get_client
from tests.lib.business_card_holder_model import verify_business_card_holder_model
from marqeta.errors import MarqetaError


class TestBusinessesLookUp(unittest.TestCase):
    """Tests for the businesses.look_up endpoint."""

    @classmethod
    def setUpClass(cls):
        """Setup for each test in the class."""

        cls.client = get_client()

    def test_businesses_look_up_success(self):
        """Tests a successful look up."""

        business = self.client.businesses.create({})

        account_number = business.deposit_account.account_number

        found = self.client.businesses.look_up({"dda": account_number})

        verify = {
            'token': business.token,
            'account_holder_group_token': business.account_holder_group_token,
            'active': business.active,
            'metadata': business.metadata
        }

        verify_business_card_holder_model(self, found, verify)

    def test_businesses_look_up_fail(self):
        """Tests a failed look up."""

        with self.assertRaises(MarqetaError):
            self.client.businesses.look_up({"dda": "Not an account number"})
