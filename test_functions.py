# Test all the relevant cases. 
# TODO: tee setUpClass, jolla luetaan file kertaalleen, ennen kaikkia testimetodeja. 
# HUOM: jos website on alhaalla! Tee mocking: 
# response = requests.get(f'LÄHDE-URL-TÄHÄN')

import unittest
from unittest.mock import patch
from data_get import data_read


class SimpleTest(unittest.TestCase):

    def test_data_read1(self): # TODO: How to fix this to catch FileNotFoundError?
        with self.assertRaises(FileNotFoundError):
            data_read()

    def test_data_read2(self):
        self.assertTrue(type(data_read()) is type(dict()))

    def test_data_read3(self):
        self.assertEqual(data_read()[1959], 315.98)

"""
     def test_download1(self):
        with patch(data_get.requests.get) as mocked_get: # tämä pitäisi importoida tai muuttaa yllä olevat viittaukset muotoon "self.data_read()" tms.
             mocked_get.return_value.ok = True
             mocked_get.return_value.text = 'Success' 
"""

    

if __name__ == '__main__':
    unittest.main()
