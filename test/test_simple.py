# coding: utf-8

"""
    Asana

    This is the interface for interacting with the [Asana Platform](https://developers.asana.com). Our API reference is generated from our [OpenAPI spec](https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml).

    The version of the OpenAPI document: 1.0
    Created by: https://asana.com/support
"""

import unittest

import os
from pprint import pprint
from asana_python_sdk import Asana

class TestSimple(unittest.TestCase):
    def setUp(self):
        pass

    def test_client(self):
        asana = Asana(
        
            client_id = 'YOUR_CLIENT_ID',
            client_secret = 'YOUR_CLIENT_SECRET',,
        
            access_token = 'YOUR_BEARER_TOKEN'
        )
        self.assertIsNotNone(asana)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
