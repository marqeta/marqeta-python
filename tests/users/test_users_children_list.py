import unittest

from tests.lib.client import get_client


class TestUsersChildren(unittest.TestCase):
    """Tests for the users.children endpoint."""

    def setUp(self):
        """Setup for each test."""

        self.client = get_client()
        self.parent = self.client.users.create({})

    def strip_deposit_account(self, user_record):
        """

        Converts a user record to a dictionary and removes the deposit account section.

        Parameters:
        user_record (UserRecord): The user to convert.

        Returns:
        Dictionary: The user record with the deposit account section removed.

        """

        user_dict = dict(user_record.__dict__)

        del user_dict['json_response']['deposit_account']

        return user_dict

    def test_children_list_one(self):
        """Retrieves one child."""

        parent_token = self.parent.token
        self.assertIsNotNone(parent_token, 'Can not get parent token')

        child = self.client.users.create({'parent_token': parent_token})

        children = self.client.users(parent_token).children.list()

        self.assertEqual(len(children), 1,
                         'Incorrect number of children returned')

        child_dict = self.strip_deposit_account(child)

        self.assertEqual(
            child_dict, children[0].__dict__, 'Incorrect child found')

    def test_children_list_two(self):
        """Retrieves two children."""

        parent_token = self.parent.token
        self.assertIsNotNone(parent_token, 'Can not get parent token')

        child1 = self.client.users.create({'parent_token': parent_token})
        child2 = self.client.users.create({'parent_token': parent_token})

        children = self.client.users(parent_token).children.list()

        self.assertEqual(len(children), 2,
                         'Incorrect number of children returned')

        # Deposit account will not be in the children found
        child1_dict = self.strip_deposit_account(child1)
        child2_dict = self.strip_deposit_account(child2)

        # Can not assume the notes will be in the order created
        dict1 = children[0].__dict__
        dict2 = children[1].__dict__

        if child1_dict == dict1:
            self.assertEqual(child2_dict, dict2, 'Incorrect child found')
        elif child1_dict == dict2:
            self.assertEqual(child2_dict, dict1, 'Incorrect child found')
        else:
            self.fail('At least one incorrect child was found')

    def test_children_list_none(self):
        """Retrieves no children."""

        parent_token = self.parent.token
        self.assertIsNotNone(parent_token, 'Can not get parent token')

        children = self.client.users(parent_token).children.list()

        self.assertEqual(len(children), 0,
                         'Incorrect number of children returned')
