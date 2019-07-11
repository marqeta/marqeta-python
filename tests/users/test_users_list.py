import unittest
import time

from tests.lib.client import get_client
from tests.lib.utilities import Utilities
from tests.lib.user_verifications import verify_card_holder_model


class TestUsersList(unittest.TestCase):
    """Tests for the users.list endpoint."""

    @classmethod
    def setUpClass(cls):
        """Setup for all the tests in the test class."""

        cls.client = get_client()
        cls.num_clients_created = 20

        cls.create_test_users()

    @classmethod
    def create_test_users(cls):
        """Creates the users used by tests in this class."""

        create_range = range(cls.num_clients_created)

        for n in create_range:
            cls.client.users.create()
            # Wait a second between creations so we can sort by time
            time.sleep(1)

    @unittest.skipIf(Utilities.on_shared_sandbox(), 'Test should not be run on the shared sandbox')
    def test_users_list_noargs(self):
        """

        Gets users with no arguments.

        Test should not be run on the shared sandbox.  It takes too long to complete.

        """

        users = self.client.users.list()

        self.assertGreaterEqual(len(users), self.num_clients_created,
                                'List returned fewer users than are known to exist')

        for user in users:
            verify_card_holder_model(self, user, {})

    def test_users_list_count(self):
        """Gets users with an upper limit to the number returned."""

        limit = 5

        users = self.client.users.list(limit=limit)

        self.assertEqual(len(users), limit,
                         'List did not return the expected number of users')

        for user in users:
            verify_card_holder_model(self, user, {})

    def test_users_list_sort_last_modified_reverse(self):
        """Gets users sorted by last modified time from newest to oldest."""

        users = self.client.users.list(
            limit=10, params={"sort_by": "-lastModifiedTime"})

        last_modified_times = []

        for user in users:
            verify_card_holder_model(self, user, {})
            last_modified_times.append(user.last_modified_time)

        sorted_times = last_modified_times
        sorted_times.sort(reverse=True)

        self.assertEqual(last_modified_times, sorted_times,
                         'List was not sorted correctly')

    def test_users_list_sort_last_modified(self):
        """Gets users sorted by last modified time from oldest to newest."""

        users = self.client.users.list(
            limit=10, params={"sort_by": "lastModifiedTime"})

        last_modified_times = []

        for user in users:
            verify_card_holder_model(self, user, {})
            last_modified_times.append(user.last_modified_time)

        sorted_times = last_modified_times
        sorted_times.sort()

        self.assertEqual(last_modified_times, sorted_times,
                         'List was not sorted correctly')
