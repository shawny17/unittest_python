import requests
import unittest

"""
API test class that utilise Python unittest framework
"""
class APITests(unittest.TestCase):

    # Initial setup for the whole class
    @classmethod
    def setUpClass(cls):
        # URL of the test
        url = 'https://api.tmsandbox.co.nz/v1/Categories/6327/Details.json?catalogue=false'
        # Get response body as JSON
        cls.response = requests.get(url=url).json()

    # TC-1: Verify that Name of response body is equal to 'Carbon credits'
    def test_name_is_valid(self):
        self.assertEqual(self.response['Name'], 'Carbon credits',
                         "FAIL: Name element returns '{}'.".format(self.response['Name']))

    # TC-2: Verify that CanRelist of response body is true
    def test_can_relist_is_valid(self):
        self.assertTrue(self.response['CanRelist'], 
                        "FAIL: CanRelist element returns '{}'.".format(self.response['CanRelist']))

    # TC-3: Verify that Promotions element with Name = "Gallery" has a Description that 
    # contains the text "Good position in category"
    def test_promotion_gallery_contains_value(self):
        for promotion in self.response['Promotions']:
            if promotion['Name'] == 'Gallery':
                self.assertEqual(promotion['Description'], 'Good position in category',
                                 "FAIL: Description element returns '{}'.".format(promotion['Description']))

# Main entry of test
if __name__ == '__main__':
    unittest.main()
 
