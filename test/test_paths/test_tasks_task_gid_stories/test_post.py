# coding: utf-8

"""
    Asana

    This is the interface for interacting with the [Asana Platform](https://developers.asana.com). Our API reference is generated from our [OpenAPI spec](https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml).

    The version of the OpenAPI document: 1.0
    Created by: https://asana.com/support
"""

import unittest
from unittest.mock import patch

import urllib3

import asana_python_sdk
from asana_python_sdk.paths.tasks_task_gid_stories import post
from asana_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestTasksTaskGidStories(ApiTestMixin, unittest.TestCase):
    """
    TasksTaskGidStories unit test stubs
        Create a story on a task
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 201






if __name__ == '__main__':
    unittest.main()
