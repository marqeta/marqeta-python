import unittest

from tests.lib.client import get_client
from faker import Faker
from tests.lib.simulate import Simulate
from tests.lib.card_products import CardProducts


class TestTransactionsList(unittest.TestCase):
    """Tests for the transactions.list endpoint."""

    @classmethod
    def setUpClass(cls):
        """Setup for all the tests in this class."""

        cls.card_product = CardProducts().create()

    def setUp(self):
        """Setup for each test."""

        self.client = get_client()
        self.fake = Faker()
        self.sim = Simulate()

        self.generate_authorizations(10)

    def get_merchant(self):
        """Returns a new merchant."""

        merchant_model = {"name": self.fake.company()}

        return self.client.merchants.create(merchant_model)

    def get_card_product(self):
        """Returns a new card product."""

        return self.card_product

    def generate_authorizations(self, num):
        """Generates the specified number of authorizations."""

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

        for _ in range(num):
            self.sim.authorization(auth_request_model)

    def test_transactions_list_no_args(self):
        """Tests the transactions list with no arguments."""

        transactions = self.client.transactions.list()

        self.assertGreaterEqual(len(transactions), 1, "No transactions found")

    def test_transactions_list_filter_state(self):
        """Tests the transitions list filtered by state."""

        params = {"state": "DECLINED"}

        transactions = self.client.transactions.list(params=params)

        self.assertGreaterEqual(len(transactions), 1, "No transactions found")

        for transaction in transactions:
            with self.subTest("Transaction does not have the correct state"):
                self.assertEqual(params["state"], transaction.state)
