import unittest
import time

from tests.lib.client import get_client
from marqeta.errors import MarqetaError


class TestGpaOrdersUnloadsFind(unittest.TestCase):
    """Tests for the gpa_orders.unloads.find endpoint."""

    def setUp(self):
        """Setup each test."""

        self.client = get_client()

    def get_user_payment_card_request(self, user_token):
        """Returns a payment card request for a user."""

        return {
            "user_token": user_token,
            "account_number": "4112344112344113",
            "cvv_number": "123",
            "exp_date": "0323",
            "zip": "94612",
        }

    def get_user_card_holder_address_request(self, user_token):
        """Returns a payment card address request for a user."""

        return {
            "user_token": user_token,
            "first_name": "Marqeta",
            "last_name": "QE",
            "address_1": "180 Grand Ave.",
            "city": "Oakland",
            "state": "CA",
            "zip": "94612",
            "country": "USA",
        }

    def get_program_name(self):
        """Returns a unique program name."""
        return "qe_program_" + str(int(time.time() % 1000000000))

    def verify_gpa_return(self, response, verify):
        """

        Verifies a GPA return matches the expected values.

        Parameters:
        response (GpaReturns): The GPA return to verify.

        verify (Dictionary): The values that should be in the response.

        """

        # Verify the expected attributes are defined
        expected_attributes = [
            "token",
            "amount",
            "created_time",
            "last_modified_time",
            "transaction_token",
            "state",
            "response",
            "funding",
            "funding_source_token",
            "funding_source_address_token",
            "original_order_token",
        ]

        for attribute in expected_attributes:
            with self.subTest(f"{attribute} is not defined"):
                self.assertIsNotNone(getattr(response, attribute))

        # Verify values match expected values
        match_attributes = list(verify.keys())

        for attribute in match_attributes:
            with self.subTest(f"{attribute} does not match the expected value"):
                self.assertEqual(getattr(response, attribute), verify[attribute])

    def test_gpa_orders_unloads_find_payment_card_user(self):
        """Finds a gpa unload for an order funded by a user payment card."""
        user = self.client.users.create({})

        card_request = self.get_user_payment_card_request(user.token)

        payment_card = self.client.funding_sources.payment_card.create(card_request)

        address_request = self.get_user_card_holder_address_request(user.token)

        address = self.client.funding_sources.addresses.create(address_request)

        gpa_request = {
            "user_token": user.token,
            "amount": 100.00,
            "currency_code": "USD",
            "funding_source_token": payment_card.token,
            "funding_source_address_token": address.token,
        }

        order = self.client.gpa_orders.create(gpa_request)

        unload_request_model = {"original_order_token": order.token, "amount": 50.00}

        gpa_return = self.client.gpa_orders.unloads.create(unload_request_model)

        found = self.client.gpa_orders.unloads.find(gpa_return.token)

        self.verify_gpa_return(found, gpa_return.__dict__)

    def test_gpa_orders_unloads_find_does_not_exist(self):
        """Tries to find an unload that doesn't exist."""

        with self.assertRaises(MarqetaError):
            self.client.gpa_orders.unloads.find("Not an unload token")
