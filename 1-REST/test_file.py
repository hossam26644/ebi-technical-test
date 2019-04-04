''' gene_suggest testing module'''
import json

import unittest
import main

from configurations import TestConfigurations

app = main.app #The app object
main.initialize_app(app, TestConfigurations) #initialize it


class FlaskTestCase(unittest.TestCase):
    ''' test class for gene-suggest endpoint'''

    client = app.test_client()

    def test_end_point_exists(self):
        ''' Test that end point exists
            request with no arguments should give a bad request 400
        '''
        response = self.client.get('/gene-operations/gene-suggest')
        self.assertEqual(response.status_code, 400)

    def test_get_known_single_result(self):
        ''' Testing with one expected result;
            May fail if database changed.
            Better to combine with testing using a
            testing database that is a static snap
            shot of the database 
        '''
        response = self.client.get(
            "/gene-operations/gene-suggest?species=ailuropoda_melanoleuca&limit=1")
        data = json.loads(response.get_data(as_text=True))
        data = self.get_result_list_from_dict(data["result_list"])
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data, ['5S_rRNA'])

    def test_get_known_multible_results(self):
        ''' Testing with one multible result;
            May fail if database changed.
            Better to combine with testing using a
            testing database that is a static snap
            shot of the database 
        '''
        response = self.client.get(
            "/gene-operations/gene-suggest?query=brc&species=homo_sapiens&limit=5")
        data = json.loads(response.get_data(as_text=True))
        data = self.get_result_list_from_dict(data["result_list"])
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data, ['BRCA1', 'BRCA2', 'BRCC3', 'BRCC3P1'])

    def get_result_list_from_dict(self, dict):
        ''' gets a dictionary result and returns a list '''
        result = []
        for pair in dict:
            result.append(pair["display_label"])
        return result
if __name__ == '__main__':
    unittest.main()
