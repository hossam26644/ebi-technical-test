''' gene_suggest testing module'''
import json

import unittest
import main

from configurations import TestConfigurations

app = main.app #The app object
main.initialize_app(app, TestConfigurations) #initialize it


class FlaskTestCase(unittest.TestCase):
    ''' test class for gene-suggest endpoint'''

    def test_end_point_exists(self):
        ''' Test that end point exists
            request with no arguments should give a bad request 400
        '''
        client = app.test_client(self)
        response = client.get('/gene-operations/gene-suggest')
        self.assertEqual(response.status_code, 400)


if __name__ == '__main__':
    unittest.main()
