import unittest
from unittest import mock
from marqeta.users import UsersCollection
from marqeta import Client


class UsersCollectionTest(unittest.TestCase):

    def setUp(self):
        self.client = Client('','','')
        self.users_collection = UsersCollection(self.client)

    ''' method for mocking the marqeta.client.get method'''

    class MockUserResource(object):

        def __init__(self,**kwargs):
            self.response = kwargs['data']

    @mock.patch('marqeta.Client.post', return_value = [{'first_name': 'test_name'}, 200])
    def test_create(self, mock_data):
        data = {'first_name': 'test_name'}
        created_user = self.users_collection.create(data)
        self.assertEqual(created_user.response, data)
        self.assertTrue(created_user.first_name == 'test_name')

    @mock.patch('marqeta.Client.get', return_value=[{'first_name': 'test_name'}, 200])
    def test_find(self, mock_data):
        user = self.users_collection.find('token')
        self.assertEqual(user.response, {'first_name': 'test_name'})
        self.assertTrue(user.first_name == 'test_name')

    @mock.patch('marqeta.Client.put', return_value=[{'first_name': 'test_name_changed'}, 200])
    def test_save(self, mock_data):
        data = {'first_name': 'test_name_changed'}
        updated_user = self.users_collection.save('token',data)
        self.assertEqual(updated_user.response, data)
        self.assertTrue(updated_user.first_name == 'test_name_changed')

    ''' testting list method for is_more = False '''

    @mock.patch('marqeta.users.UsersCollection._page', return_value={'is_more':False,'count': 5, 'start_index': 0,
                                                                     'data': [{'token':'test_token'}, {}, {}, {}, {}]})
    def test_list(self, mock_data):
        user_list = self.users_collection.list()
        user_list_sort_by = self.users_collection.list('email')
        self.assertEqual(len(user_list), 5)   # checking for number of user objects when is_more = False
        self.assertNotEqual(user_list, user_list_sort_by)
        self.assertTrue(user_list[0].token == 'test_token') # checking for the value returned

    ''' testting list method for is_more = True '''

    @mock.patch('marqeta.users.UsersCollection._page', return_value={'is_more': True, 'count': 5, 'start_index': 0,
                                                                     'data': [{'token': 'test_token'}, {}, {}, {}, {}]})
    def test_list_for_more_pages(self, mock_data):
        user_list = self.users_collection.list()
        user_list_sort_by = self.users_collection.list('email')
        self.assertEqual(len(user_list), 10)  # checking for number of user objects when is_more = True
        self.assertNotEqual(user_list, user_list_sort_by)
        self.assertTrue(user_list[0].token == 'test_token')  # checking for the value returned


if __name__ == '__main__':
    unittest.main()
