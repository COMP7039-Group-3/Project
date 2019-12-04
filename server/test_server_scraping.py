
import server
import unittest
import json
import requests
import getSummaries

from unittest import mock


def mock_get_html_from_fake(root_url):
    return '<html></html>'


def try_object_matches_appropriate_format(res):
    json_res = json.loads(res.data)[0]
    url_content = json_res['urls'][0]
    return 'section' in json_res and 'urls' in json_res and 'article' in url_content and 'article_words' in url_content and 'summary' in url_content and 'summary_words' in url_content and 'title' in url_content and 'url' in url_content


class TestServerScraping(unittest.TestCase):
    """
    User Story: 001
    Obtain news from a news source or website
    """

    def setUp(self):
        server.app.testing = True
        self.app = server.app.test_client()

    def test_server_should_connect_and_obtain_results(self):
        """
        TC01	Verify that the application connects to the news source and obtain results
        """
        res = self.app.get('/api/bbc')
        # Assert response is 200
        self.assertEqual(res.status, '200 OK')

        # Assert object has the correct format
        self.assertTrue(try_object_matches_appropriate_format(res))
        

    def test_server_should_return_error_if_cannot_connect(self):
        """
        TC02	Verify that the application throws an error if a connection was not possible to obtain
        """
        res = self.app.get('/api/fakenews')
        self.assertEqual(res.status, '404 NOT FOUND')

    # @mock.patch('getSummaries.get_html_from_source', side_effect=mock_get_html_from_fake)
    def test_server_should_return_empty_if_source_is_empty(self):
        """
        TC03	Verify that the application displays an empty collection when no information is present at the source
        """
        # # Mock getSummaries call
        # getSummaries._mock = getSummaries.get_html_from_source
        # getSummaries.get_html_from_source = mock_get_html_from_fake

        # # Execute the query
        # res = self.app.get('/api/bbc')

        # # Undo the mock
        # # getSummaries.get_html_from_source = getSummaries._mock
        # # delattr(getSummaries, '_mock')

        # print(json.loads(res.data))
        # # Response should be 200 OK
        # self.assertEqual(res.status, '200 OK')

        # # Content should be empty
        # json_res = json.loads(res.data)[0]
        # print(json_res)
        # self.assertEqual(json_res["urls"], [])

    def test_different_sources_provide_different_results(self):
        """
        TC04	Verify that different sources provide different information.
        """
        resbbc = self.app.get('/api/bbc')
        self.assertEqual(resbbc.status, '200 OK')

        # TODO: Uncomment and put appropriate url here
        
        # resother = self.app.get('/api/the-guardian')
        # self.assertEqual(resother.status, '200 OK')
        # self.assertNotEqual(resbbc.data, resother.data)

    def test_different_sources_provide_same_format(self):
        """
        TC05	Verify that for each source the information provided still maintains the same form
        """
        # TODO: Uncomment and put the appropriate endpoint here

        # resother = self.app.get('/api/the-guardian')
        # self.assertEqual(resother.status, '200 OK')
        # self.assertTrue(try_object_matches_appropriate_format(resother))


if __name__ == '__main__':
    unittest.main()
