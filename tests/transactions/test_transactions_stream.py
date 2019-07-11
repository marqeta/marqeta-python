import unittest

from tests.lib.client import get_client
from faker import Faker
from tests.lib.simulate import Simulate
from tests.lib.card_products import CardProducts


class TestTransactionsStream(unittest.TestCase):
    """Tests the transactions.stream endpoint."""

    @classmethod
    def setUpClass(cls):
        cls.client = get_client()
        cls.fake = Faker()
        cls.sim = Simulate()
        cls.card_product = CardProducts().create()
        cls.generate_authorizations(20)

    @classmethod
    def generate_authorizations(cls, num):
        """Generates the specified number of authorizations."""

        merchant = cls.get_merchant()

        user = cls.client.users.create({})

        card_product = cls.get_card_product()

        card_request = {
            "card_product_token": card_product.token,
            "user_token": user.token
        }

        card = cls.client.cards.create(card_request)

        auth_request_model = {
            "card_token": card.token,
            "amount": 100.0,
            "mid": merchant.token
        }

        for _ in range(num):
            cls.sim.authorization(auth_request_model)

    @classmethod
    def get_merchant(cls):
        """Returns a new merchant."""

        merchant_model = {
            "name": cls.fake.company()
        }

        return cls.client.merchants.create(merchant_model)

    @classmethod
    def get_card_product(cls):
        """Returns a new card product."""

        return cls.card_product

    def test_transactions_stream(self):
        """Tests the transactions stream endpoint."""

        params = {
            "state": "ALL",
        }

        record_limit = 10
        transaction_num = 0
        last_token = None

        for transaction in self.client.transactions.stream(params=params):
            transaction_num += 1

            with self.subTest(f'Transaction {transaction_num} is the same as the previous transaction'):
                self.assertNotEqual(last_token, transaction.token)

            last_token = transaction.token

            if (transaction_num >= record_limit):
                break

        self.assertGreater(transaction_num, 0,
                           'Stream did not return any transactions')
