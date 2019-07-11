import unittest

from tests.lib.client import get_client


class TestGpaOrdersUnloadsList(unittest.TestCase):
    """Tests for the gpa_orders.unloads.list endpoint."""

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

    def test_unloads_list(self):
        """Retrieves unloads from the system"""

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

        self.client.gpa_orders.unloads.create(unload_request_model)

        found = self.client.gpa_orders.unloads.list()

        self.assertGreaterEqual(len(found), 1, 'No unloads were found')
