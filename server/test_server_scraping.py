
import server
import unittest
import json
from unittest.mock import Mock, patch

class TestServerScraping(unittest.TestCase):
    """
    User Story: 001
    Obtain news from a news source or website

    TC03	Verify that the application displays an empty collection when no information is present at the source
    TC04	Verify that different sources provide different information.
    TC05	Verify that for each source the information provided still maintains the same form

    """
    def setUp(self):
        server.app.testing = True
        self.app = server.app.test_client()

    def test_server_should_connect_and_obtain_results(self):
        """
        TC01	Verify that the application connects to the news source and obtain results
        """
        res = self.app.get('/api/bbc')
        self.assertEqual(res.status, '200 OK')
        json_res = json.loads(res.data)[0]
        self.assertTrue('section' in json_res)
        self.assertTrue( 'urls' in json_res)
        # self.assertEqual( json_res['urls'], "test")
        url_content = json_res['urls'][0]
        self.assertTrue( 'article' in url_content)
        self.assertTrue( 'article_words' in url_content)
        self.assertTrue( 'summary' in url_content)
        self.assertTrue( 'summary_words' in url_content)
        self.assertTrue( 'title' in url_content)
        self.assertTrue( 'url' in url_content)

        
    def test_server_should_return_error_if_cannot_connect(self):
        """
        TC02	Verify that the application throws an error if a connection was not possible to obtain
        """
        res = self.app.get('/api/fakenews')
        self.assertEqual(res.status, '404 NOT FOUND')

if __name__ == '__main__':
    unittest.main()