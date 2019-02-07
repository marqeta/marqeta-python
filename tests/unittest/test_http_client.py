import unittest
import requests
from unittest import mock
from marqeta import Client
from marqeta.errors import MarqetaError

# test methods for get, put , post and delete

class HttpClientTest(unittest.TestCase):
    #Creating client object

    def setUp(self):
        self.client = Client('','test','test')

    def mocked_requests_get(**args):

        response = requests.get("https://www.marqeta.com")
        print('*****mocked response******',response)
        return response


        # class MockResponse:
        #     def __init__(self, json_data, status_code):
        #         self.json = json_data
        #         self.status_code = status_code
        #
        # if args['url'] == 'test_endpoint':
        #     # mock_response = MockResponse({"test_name": "name"}, 200)
        #     # print (mock_response.json)
        #     # print(mock_response.status_code)
        #     return MockResponse({"test_name": "name"}, 200)
        # return MockResponse(None, 400)

    @mock.patch('requests.get',side_effect = mocked_requests_get())
    def test_get_method(self, mock_get):

        # import pdb ;pdb.set_trace()
        response = self.client.get('test_endpoint')
        self.assertTrue(response.ok)
        #self.assertEqual(response.status_code, 200)

        #self.assertRaises(MarqetaError,lambda: print(self.client.get('test_endpoint1','test_query').status_code) )
        # != 200)

        # checking for Exception handling


    '''
    
    @mock.patch('marqeta.Client.post', return_value='200')
    def test_post_method(self, mock_post):
        response = self.client.post('test_endpoint', 'test_data')
        self.assertEqual(response, '200')

        # checking for Exception handling
        self.assertTrue(response != 200, MarqetaError('test_code', 'test_msg'))

    @mock.patch('marqeta.Client.put', return_value='200')
    def test_put_method(self,mock_put):
        response = self.client.put('test_endpoint', 'test_data')
        self.assertEqual(response, '200')

        # checking for Exception handling
        self.assertTrue(response != 200, MarqetaError('test_code', 'test_msg'))

    @mock.patch('marqeta.Client.delete', return_value='200')
    def test_delete_method(self, mock_delete):
        response = self.client.delete('test_endpoint')
        self.assertEqual(response, '200')

        # checking for Exception handling
        self.assertTrue(response != 200, MarqetaError('test_code', 'test_msg'))

'''
if __name__ == '__main__' :
    unittest.main()
