import unittest
import time
import requests

from tests.lib.client import SingletonClient, get_client


class TestGpaOrdersUnloadsCreate(unittest.TestCase):
    """Tests for the gpa_orders_unloads.create endpoint."""

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
            "zip": "94612"
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
            "country": "USA"
        }

    def get_user_ach_request(self, user_token):
        """Returns a ach funding sourde request for a user."""

        # Routing number is for Wells Fargo, CA checking accounts
        return {
            "user_token": user_token,
            "account_number": "12345678901234567",
            "routing_number": "121042882",
            "name_on_account": "Marqeta QE",
            "account_type": "checking"
        }

    def free_ach_funds(self, transaction_token):
        """Makes ach funds available with no wait."""

        """

        Further development on this method is halted until the suite is integrated with Sushi Boat.

        """

        url = f'{SingletonClient.get_base_url()}funding_sources/ach/admin/post/#{transaction_token}'

        headers = {
            "content_type": "application/json",
            "accept": "application/json",
            "auth": "Need to define!!!!"
        }

        requests.post(url, {}, headers)

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
            'token',
            'amount',
            'created_time',
            'last_modified_time',
            'transaction_token',
            'state',
            'response',
            'funding',
            'funding_source_token',
            'funding_source_address_token',
            'original_order_token'
        ]

        for attribute in expected_attributes:
            with self.subTest(f'{attribute} is not defined'):
                self.assertIsNotNone(getattr(response, attribute))

        # Verify values match expected values
        match_attributes = list(verify.keys())

        for attribute in match_attributes:
            with self.subTest(f'{attribute} does not match the expected value'):
                self.assertEqual(getattr(response, attribute),
                                 verify[attribute])

    def test_gpa_orders_unloads_create_payment_card_user(self):
        """Creates a gpa unload for an order funded by a user payment card."""

        user = self.client.users.create({})

        card_request = self.get_user_payment_card_request(user.token)

        payment_card = self.client.funding_sources.payment_card.create(
            card_request)

        address_request = self.get_user_card_holder_address_request(user.token)

        address = self.client.funding_sources.addresses.create(address_request)

        gpa_request = {
            "user_token": user.token,
            "amount": 100.00,
            "currency_code": "USD",
            "funding_source_token": payment_card.token,
            "funding_source_address_token": address.token
        }

        order = self.client.gpa_orders.create(gpa_request)

        unload_request_model = {
            "original_order_token": order.token,
            "amount": 50.00
        }

        gpa_return = self.client.gpa_orders.unloads.create(
            unload_request_model)

        self.verify_gpa_return(gpa_return, unload_request_model)

    def xtest_gpa_orders_unloads_create_ach_user(self):
        """Creates a gpa unload for an order funded by a user ach."""

        """

        This test is disabled.
        Further development on this test is halted until the suite is integrated with Sushi Boat.

        """

        user = self.client.users.create({})

        ach_request = self.get_user_ach_request(user.token)

        ach_source = self.client.funding_sources.ach.create(ach_request)

        amounts = self.client.funding_sources.ach(
            ach_source.token).verification_amounts()

        ach_verification = {
            "verify_amount1": amounts.verify_amount1,
            "verify_amount2": amounts.verify_amount2
        }

        self.client.funding_sources.ach.save(
            ach_source.token, ach_verification)

        gpa_request = {
            "user_token": user.token,
            "amount": 100.00,
            "currency_code": "USD",
            "funding_source_token": ach_source.token
        }

        order = self.client.gpa_orders.create(gpa_request)

        self.free_ach_funds(order.transaction_token)

        unload_request_model = {
            "original_order_token": order.token,
            "amount": 50.00
        }

        gpa_return = self.client.gpa_orders.unloads.create(
            unload_request_model)

        self.verify_gpa_return(gpa_return, unload_request_model)
