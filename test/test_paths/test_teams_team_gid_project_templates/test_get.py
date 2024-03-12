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
from asana_python_sdk.paths.teams_team_gid_project_templates import get
from asana_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestTeamsTeamGidProjectTemplates(ApiTestMixin, unittest.TestCase):
    """
    TeamsTeamGidProjectTemplates unit test stubs
        Get a team's project templates
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()