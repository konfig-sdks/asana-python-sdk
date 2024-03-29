# coding: utf-8

"""
    Asana

    This is the interface for interacting with the [Asana Platform](https://developers.asana.com). Our API reference is generated from our [OpenAPI spec](https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml).

    The version of the OpenAPI document: 1.0
    Created by: https://asana.com/support
"""

from asana_python_sdk.paths.projects_project_gid_project_memberships.get import GetCompactRecords
from asana_python_sdk.paths.project_memberships_project_membership_gid.get import GetRecord
from asana_python_sdk.apis.tags.project_memberships_api_raw import ProjectMembershipsApiRaw


class ProjectMembershipsApi(
    GetCompactRecords,
    GetRecord,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: ProjectMembershipsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = ProjectMembershipsApiRaw(api_client)
