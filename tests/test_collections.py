import unittest
from unittest import mock
from marqeta.resources.collection import Collection
from marqeta.response_models.user_card_holder_response import UserCardHolderResponse
from marqeta import Client

"""
mock test for the Collection class for the user endpoint 
"""


class CollectionTest(unittest.TestCase):

    data = {"token": "test_token"}

    def setUp(self):
        self.client = Client("", "", "")
        self.collections = Collection(self.client, UserCardHolderResponse)

    @mock.patch(
        "marqeta.resources.collection.Collection._page",
        return_value={
            "is_more": False,
            "count": 5,
            "start_index": 0,
            "data": [{"token": "test_token"}, {}, {}, {}, {}],
        },
    )
    def test_stream(self, mock_data):
        count = 0
        user_stream = []
        user_stream_sort_by = []
        for user in self.collections.stream():
            if count == 4:
                break
            else:
                user_stream.append(user)
                count += 1
        self.assertTrue(len(user_stream), 4)

        for user in self.collections.stream("email"):
            if count == 4:
                break
            else:
                user_stream_sort_by.append(user)
                count += 1
        self.assertTrue(len(user_stream), 4)
        self.assertNotEqual(user_stream, user_stream_sort_by)
        # checking for the value returned
        self.assertTrue(user_stream[0].token == "test_token")

    """ testting list method for is_more = False """

    @mock.patch(
        "marqeta.resources.collection.Collection.stream",
        return_value=[UserCardHolderResponse(data), UserCardHolderResponse(data)],
    )
    def test_list(self, mock_data):
        user_list = self.collections.list()
        # checking for number of user objects when is_more = False
        self.assertEqual(len(user_list), 2)

    """ testting list method for is_more = True """

    @mock.patch("marqeta.Client.post", return_value=[{"first_name": "test_name"}, 200])
    def test_create(self, mock_data):
        data = {"first_name": "test_name"}
        created_user = self.collections.create(data)
        self.assertEqual(created_user.first_name, data["first_name"])
        self.assertTrue(created_user.first_name == "test_name")

    @mock.patch("marqeta.Client.get", return_value=[{"first_name": "test_name"}, 200])
    def test_find(self, mock_data):
        user = self.collections.find("token")
        self.assertEqual(user.first_name, "test_name")
        self.assertTrue(user.first_name == "test_name")

    @mock.patch(
        "marqeta.Client.put", return_value=[{"first_name": "test_name_changed"}, 200]
    )
    def test_save(self, mock_data):
        data = {"first_name": "test_name_changed"}
        updated_user = self.collections.save("token", data)
        self.assertEqual(updated_user.first_name, data["first_name"])
        self.assertTrue(updated_user.first_name == "test_name_changed")


if __name__ == "__main__":
    unittest.main()
