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
from asana_python_sdk.paths.goals_goal_gid_set_metric_current_value import post
from asana_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestGoalsGoalGidSetMetricCurrentValue(ApiTestMixin, unittest.TestCase):
    """
    GoalsGoalGidSetMetricCurrentValue unit test stubs
        Update a goal metric
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200






if __name__ == '__main__':
    unittest.main()
