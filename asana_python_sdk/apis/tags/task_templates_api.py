# coding: utf-8

"""
    Asana

    This is the interface for interacting with the [Asana Platform](https://developers.asana.com). Our API reference is generated from our [OpenAPI spec] (https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml).

    The version of the OpenAPI document: 1.0
    Created by: https://asana.com/support
"""

from asana_python_sdk.paths.task_templates_task_template_gid.delete import DeleteTaskTemplate
from asana_python_sdk.paths.task_templates_task_template_gid.get import GetSingleTemplate
from asana_python_sdk.paths.task_templates_task_template_gid_instantiate_task.post import InstantiateTaskJob
from asana_python_sdk.paths.task_templates.get import ListMultiple
from asana_python_sdk.apis.tags.task_templates_api_raw import TaskTemplatesApiRaw


class TaskTemplatesApi(
    DeleteTaskTemplate,
    GetSingleTemplate,
    InstantiateTaskJob,
    ListMultiple,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: TaskTemplatesApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = TaskTemplatesApiRaw(api_client)