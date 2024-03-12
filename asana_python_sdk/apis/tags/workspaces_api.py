# coding: utf-8

"""
    Asana

    This is the interface for interacting with the [Asana Platform](https://developers.asana.com). Our API reference is generated from our [OpenAPI spec] (https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml).

    The version of the OpenAPI document: 1.0
    Created by: https://asana.com/support
"""

from asana_python_sdk.paths.workspaces_workspace_gid_add_user.post import AddUserToWorkspace
from asana_python_sdk.paths.workspaces_workspace_gid.get import GetWorkspaceRecord
from asana_python_sdk.paths.workspaces.get import ListMultiple
from asana_python_sdk.paths.workspaces_workspace_gid_remove_user.post import RemoveUserFromWorkspace
from asana_python_sdk.paths.workspaces_workspace_gid.put import UpdateWorkspaceRecord
from asana_python_sdk.apis.tags.workspaces_api_raw import WorkspacesApiRaw


class WorkspacesApi(
    AddUserToWorkspace,
    GetWorkspaceRecord,
    ListMultiple,
    RemoveUserFromWorkspace,
    UpdateWorkspaceRecord,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: WorkspacesApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = WorkspacesApiRaw(api_client)
