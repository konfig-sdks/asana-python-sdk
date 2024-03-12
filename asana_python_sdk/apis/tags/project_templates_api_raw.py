# coding: utf-8

"""
    Asana

    This is the interface for interacting with the [Asana Platform](https://developers.asana.com). Our API reference is generated from our [OpenAPI spec] (https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml).

    The version of the OpenAPI document: 1.0
    Created by: https://asana.com/support
"""

from asana_python_sdk.paths.project_templates_project_template_gid.delete import DeleteTemplateRecordRaw
from asana_python_sdk.paths.teams_team_gid_project_templates.get import GetAllTemplateRecordsRaw
from asana_python_sdk.paths.project_templates_project_template_gid.get import GetRecordRaw
from asana_python_sdk.paths.project_templates_project_template_gid_instantiate_project.post import InstantiateProjectJobRaw
from asana_python_sdk.paths.project_templates.get import ListMultipleRaw


class ProjectTemplatesApiRaw(
    DeleteTemplateRecordRaw,
    GetAllTemplateRecordsRaw,
    GetRecordRaw,
    InstantiateProjectJobRaw,
    ListMultipleRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass