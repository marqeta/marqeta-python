import unittest

from tests.lib.client import get_client
from faker import Faker
from tests.lib.simulate import Simulate
from tests.lib.card_products import CardProducts


class TestTransactionsPage(unittest.TestCase):
    """Tests for the transactions.page endpoint."""

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
            "user_token": user.token,
        }

        card = cls.client.cards.create(card_request)

        auth_request_model = {
            "card_token": card.token,
            "amount": 100.0,
            "mid": merchant.token,
        }

        for _ in range(num):
            cls.sim.authorization(auth_request_model)

    @classmethod
    def get_merchant(cls):
        """Returns a new merchant."""

        merchant_model = {"name": cls.fake.company()}

        return cls.client.merchants.create(merchant_model)

    @classmethod
    def get_card_product(cls):
        """Returns a new card product."""

        return cls.card_product

    def verify_transaction_page(self, response, start, count, more):
        """

        Verifies a transaction page response.

        Parameters:
        response (Dictionary): The response to verify.

        start (Integer): The starting index.

        count (Integer): The maximum number of entries per page.

        more (Boolean): Whether there is more data to retrieve.

        """

        with self.subTest("Count has unexpected value"):
            if more:
                self.assertEqual(response["count"], count)
            else:
                self.assertLessEqual(response["count"], count)

        with self.subTest("Start index has unexpected value"):
            self.assertEqual(response["start_index"], start)

        with self.subTest("End index has unexpected value"):
            end_index = start + count - 1
            self.assertEqual(response["end_index"], end_index)

        with self.subTest("Is more has unexpected value"):
            self.assertEqual(response["is_more"], more)

        with self.subTest("Unexpected number of page records found"):
            if response["is_more"]:
                self.assertEqual(len(response["data"]), count)
            else:
                self.assertLessEqual(len(response["data"]), count)

        for record in response["data"]:
            with self.subTest("Invalid model found in response"):
                actual = record.__class__.__name__
                expected = "TransactionModel"

                self.assertEqual(actual, expected)

    def test_transactions_page_one(self):
        """Tests retrieving the first page of transactions."""

        start_index = 0
        count = 5

        params = {"state": "ALL"}

        page = self.client.transactions.page(
            start_index=start_index, count=count, params=params
        )

        self.verify_transaction_page(page, start_index, count, True)

    def test_transactions_page_two(self):
        """Tests retrieving the second page of transactions."""

        start_index = 5
        count = 5

        params = {"state": "ALL"}

        page = self.client.transactions.page(
            start_index=start_index, count=count, params=params
        )

        self.verify_transaction_page(page, start_index, count, True)
