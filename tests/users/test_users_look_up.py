import unittest
import time

from tests.lib.client import get_client


class TestUsersLookUp(unittest.TestCase):
    """Tests for the users.look_up endpoint."""

    def setUp(self):
        """Setup each test."""

        self.client = get_client()

    def test_look_up_success_ssn(self):
        """Successful lookup by ssn."""

        ssn = str(int(time.time() % 1000000000))
        masked_ssn = "___________"

        client_options = {"ssn": ssn}

        user = self.client.users.create(client_options)

        self.assertIsNotNone(user.token, "User token is not defined")

        results = self.client.users.look_up(client_options)

        self.assertGreaterEqual(len(results), 1, "Look up returned no results")

        for result in results:
            with self.subTest("Results contain incorrect search value"):
                self.assertEqual(result.ssn, masked_ssn)

    def test_look_up_fail_ssn(self):
        """Unsuccessful lookup by ssn."""
        client = get_client()

        search_options = {"ssn": "abcdefghi"}

        results = client.users.look_up(search_options)

        self.assertEqual(
            len(results), 0, "Look up returned the wrong number of results"
        )

    def test_look_up_success_dda(self):
        """Test successful lookup by dda."""

        user = self.client.users.create({})

        search_options = {"dda": user.deposit_account.account_number}

        results = self.client.users.look_up(search_options)

        self.assertGreaterEqual(len(results), 1, "Look up returned no results")

        for result in results:
            with self.subTest("Results contain incorrect search value"):
                self.assertEqual(result.token, user.token)

    def test_look_up_fail_dda(self):
        """Test unsuccessful lookup by dda."""

        dda = "search_" + str(int(time.time() % 1000000000))

        search_options = {"dda": dda}

        results = self.client.users.look_up(search_options)

        self.assertEqual(
            len(results), 0, "Look up returned the wrong number of results"
        )

    def test_look_up_success_first_name(self):
        """Tests successful lookup by first name."""

        first_name = "John" + str(int(time.time() % 1000000000))

        client_options = {"first_name": first_name}

        self.client.users.create(client_options)

        results = self.client.users.look_up(client_options)

        self.assertEqual(
            len(results), 1, "Look up returned the wrong number of results"
        )

        self.assertEqual(
            results[0].first_name, first_name, "Results contain incorrect search value"
        )

    def test_look_up_fail_first_name(self):
        """Tests failed lookup by first name."""

        search_options = {
            "first_name": "Fake first name" + str(int(time.time() % 1000000000))
        }

        results = self.client.users.look_up(search_options)

        self.assertEqual(
            len(results), 0, "Look up returned the wrong number of results"
        )

    def test_look_up_success_last_name(self):
        """Test successful lookup by last name."""

        last_name = "Smith" + str(int(time.time() % 1000000000))

        client_options = {"last_name": last_name}

        self.client.users.create(client_options)

        results = self.client.users.look_up(client_options)

        self.assertEqual(
            len(results), 1, "Look up returned the wrong number of results"
        )

        self.assertEqual(
            results[0].last_name, last_name, "Results contain incorrect search value"
        )

    def test_look_up_fail_last_name(self):
        """Test failed lookup by last name."""

        search_options = {
            "last_name": "Fake last name" + str(int(time.time() % 1000000000))
        }

        results = self.client.users.look_up(search_options)

        self.assertEqual(
            len(results), 0, "Look up returned the wrong number of results"
        )

    def test_look_up_success_phone(self):
        """Test successful lookup by phone."""

        phone = str(int(time.time()))

        client_options = {"phone": phone}

        self.client.users.create(client_options)

        results = self.client.users.look_up(client_options)

        self.assertGreaterEqual(len(results), 1, "Look up returned no results")

        for result in results:
            with self.subTest("Results contain incorrect search value"):
                self.assertEqual(result.phone, phone)

    def test_look_up_fail_phone(self):
        search_options = {"phone": "Not a phone number"}

        results = self.client.users.look_up(search_options)

        self.assertEqual(
            len(results), 0, "Look up returned the wrong number of results"
        )

    def test_look_up_success_email(self):
        """Test successful lookup by email."""

        email = "mail0_" + str(int(time.time())) + "@marqeta.qe"

        client_options = {"email": email}

        self.client.users.create(client_options)

        results = self.client.users.look_up(client_options)

        self.assertEqual(
            len(results), 1, "Look up returned the wrong number of results"
        )

        self.assertEqual(
            results[0].email, email, "Results contain incorrect search value"
        )

    def test_look_up_fail_email(self):
        """Test failed lookup by email."""

        search_options = {"email": "not an email"}

        results = self.client.users.look_up(search_options)

        self.assertEqual(
            len(results), 0, "Look up returned the wrong number of results"
        )

    def test_look_up_success_two_parameters(self):
        """Test successful lookup by two parameters."""

        email = "mail1_" + str(int(time.time())) + "@marqeta.qe"
        first_name = "John" + str(int(time.time() % 1000000000))

        client_options = {"email": email, "first_name": first_name}

        self.client.users.create(client_options)

        results = self.client.users.look_up(client_options)

        self.assertEqual(
            len(results), 1, "Look up returned the wrong number of results"
        )

        self.assertEqual(
            results[0].email, email, "Results contain incorrect search value"
        )
        self.assertEqual(
            results[0].first_name, first_name, "Results contain incorrect search value"
        )

    def test_look_up_fail_two_parameters(self):
        """Test failed lookup by two parameters."""

        email = "fail2_" + str(int(time.time())) + "@marqeta.qe"
        first_name = "Doctor" + str(int(time.time() % 1000000000))

        search_options = {"email": email, "first_name": first_name}

        results = self.client.users.look_up(search_options)

        self.assertEqual(
            len(results), 0, "Look up returned the wrong number of results"
        )
