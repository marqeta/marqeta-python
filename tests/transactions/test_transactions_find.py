import unittest

from tests.lib.client import get_client
from faker import Faker
from tests.lib.simulate import Simulate
from tests.lib.card_products import CardProducts


class TestTransactionsFind(unittest.TestCase):
    """Tests for the transactions.find endpoint."""

    @classmethod
    def setUpClass(cls):
        """Setup for all the tests in this class."""

        cls.card_product = CardProducts().create()

    def setUp(self):
        """Setup each test."""

        self.client = get_client()
        self.fake = Faker()
        self.sim = Simulate()

    def verify_transaction_model(self, response, verify):
        """

        Verifies a transaction model matches the expected values.

        Parameters:
        response (TransactionModel): The response to verify.

        verify (Dictionary): The values that should be in the response.

        """

        # Verify the correct class is being tested
        actual = response.__class__.__name__
        expected = "TransactionModel"

        self.assertEqual(actual, expected, "Unexpected response found")

        # Verify the expected attributes are defined
        expected_attributes = [
            "type",
            "state",
            "token",
            "user_token",
            "acting_user_token",
            "card_token",
            "gpa",
            "duration",
            "created_time",
            "user_transaction_time",
            "settlement_date",
            "request_amount",
            "amount",
            "currency_code",
            "response",
            "network",
            "acquirer_fee_amount",
            "acquirer",
            "user",
            "card",
            "card_acceptor",
        ]

        for attribute in expected_attributes:
            with self.subTest(f"{attribute} is not defined"):
                self.assertIsNotNone(getattr(response, attribute))

        # Verify values match expected values
        match_attributes = list(verify.keys())

        for attribute in match_attributes:
            with self.subTest(f"{attribute} does not match the expected value"):
                self.assertEqual(getattr(response, attribute), verify[attribute])

    def get_merchant(self):
        """Returns a new merchant."""

        merchant_model = {"name": self.fake.company()}

        return self.client.merchants.create(merchant_model)

    def get_card_product(self):
        """Returns a new card product."""

        return self.card_product

    def test_transactions_find(self):
        """Tests finding a transaction."""

        merchant = self.get_merchant()

        user = self.client.users.create({})

        card_product = self.get_card_product()

        card_request = {
            "card_product_token": card_product.token,
            "user_token": user.token,
        }

        card = self.client.cards.create(card_request)

        auth_request_model = {
            "card_token": card.token,
            "amount": 100.0,
            "mid": merchant.token,
        }

        transaction = self.sim.authorization(auth_request_model)

        transaction_token = transaction["transaction"]["token"]

        found = self.client.transactions.find(transaction_token)

        verify = {
            "type": "authorization",
            "user_token": user.token,
            "acting_user_token": user.token,
            "card_token": card.token,
            "request_amount": auth_request_model["amount"],
            "amount": auth_request_model["amount"],
        }

        self.verify_transaction_model(found, verify)
