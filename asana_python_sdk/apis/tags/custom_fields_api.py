# coding: utf-8

"""
    Asana

    This is the interface for interacting with the [Asana Platform](https://developers.asana.com). Our API reference is generated from our [OpenAPI spec](https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml).

    The version of the OpenAPI document: 1.0
    Created by: https://asana.com/support
"""

from asana_python_sdk.paths.custom_fields_custom_field_gid_enum_options.post import AddEnumOption
from asana_python_sdk.paths.custom_fields.post import CreateNewFieldRecord
from asana_python_sdk.paths.custom_fields_custom_field_gid.delete import DeleteFieldRecord
from asana_python_sdk.paths.custom_fields_custom_field_gid.get import GetMetadata
from asana_python_sdk.paths.workspaces_workspace_gid_custom_fields.get import ListWorkspaceCustomFields
from asana_python_sdk.paths.custom_fields_custom_field_gid_enum_options_insert.post import ReorderEnumOption
from asana_python_sdk.paths.enum_options_enum_option_gid.put import UpdateEnumOption
from asana_python_sdk.paths.custom_fields_custom_field_gid.put import UpdateFieldRecord
from asana_python_sdk.apis.tags.custom_fields_api_raw import CustomFieldsApiRaw


class CustomFieldsApi(
    AddEnumOption,
    CreateNewFieldRecord,
    DeleteFieldRecord,
    GetMetadata,
    ListWorkspaceCustomFields,
    ReorderEnumOption,
    UpdateEnumOption,
    UpdateFieldRecord,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: CustomFieldsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = CustomFieldsApiRaw(api_client)
