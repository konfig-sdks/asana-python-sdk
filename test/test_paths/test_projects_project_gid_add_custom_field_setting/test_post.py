# coding: utf-8

"""
    Asana

    This is the interface for interacting with the [Asana Platform](https://developers.asana.com). Our API reference is generated from our [OpenAPI spec] (https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml).

    The version of the OpenAPI document: 1.0
    Created by: https://asana.com/support
"""

import unittest
from unittest.mock import patch

import urllib3

import asana_python_sdk
from asana_python_sdk.paths.projects_project_gid_add_custom_field_setting import post
from asana_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestProjectsProjectGidAddCustomFieldSetting(ApiTestMixin, unittest.TestCase):
    """
    ProjectsProjectGidAddCustomFieldSetting unit test stubs
        Add a custom field to a project
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200






if __name__ == '__main__':
    unittest.main()
