''' gene_suggest testing module'''
import json

import unittest
import main.application as main

from configurations import TestConfigurations

app = main.app #The app object
main.initialize_app(app, TestConfigurations) #initialize it


class FlaskTestCase(unittest.TestCase):
    ''' test class for gene-suggest endpoint'''

    client = app.test_client()

    def test_end_point_exists(self):
        ''' Test that end point exists, response code is not 404
            request with no arguments should give a bad request 400
        '''
        response = self.client.get('/gene_operations/gene_suggest')
        self.assertNotEqual(response.status_code ,404)

    def test_expected_response(self):
        ''' Test that end point exists, response code is not 404
            request with no arguments should give a bad request 400
        '''
        query = "brc"
        species = "homo_sapiens"
        limit = 10
        response = self.client.get(
            "/gene_operations/gene_suggest?query={}&species={}&limit={}".format(
                                                                        query,
                                                                        species,
                                                                        limit))
        data = json.loads(response.get_data(as_text=True))
        data = self.get_result_list_from_dict(data["result_list"]) #extract response as list
        sorted_data = sorted(data) #note: case sensitive, gene names are upper case
        self.assertEqual(response.status_code, 200) #test response code
        self.assertEqual(data, sorted_data) #Test response list is in order
        self.assertLessEqual(len(data),limit) #test length of response is smaller than or equal the limit


    def get_result_list_from_dict(self, dict):
        ''' gets a dictionary result and returns a list '''
        result = []
        for pair in dict:
            result.append(pair["display_label"])
        return result


if __name__ == '__main__':
    unittest.main()
