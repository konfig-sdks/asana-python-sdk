# coding: utf-8

"""
    Asana

    This is the interface for interacting with the [Asana Platform](https://developers.asana.com). Our API reference is generated from our [OpenAPI spec] (https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml).

    The version of the OpenAPI document: 1.0
    Created by: https://asana.com/support
"""

from asana_python_sdk.paths.custom_fields_custom_field_gid_enum_options.post import AddEnumOptionRaw
from asana_python_sdk.paths.custom_fields.post import CreateNewFieldRecordRaw
from asana_python_sdk.paths.custom_fields_custom_field_gid.delete import DeleteFieldRecordRaw
from asana_python_sdk.paths.custom_fields_custom_field_gid.get import GetMetadataRaw
from asana_python_sdk.paths.workspaces_workspace_gid_custom_fields.get import ListWorkspaceCustomFieldsRaw
from asana_python_sdk.paths.custom_fields_custom_field_gid_enum_options_insert.post import ReorderEnumOptionRaw
from asana_python_sdk.paths.enum_options_enum_option_gid.put import UpdateEnumOptionRaw
from asana_python_sdk.paths.custom_fields_custom_field_gid.put import UpdateFieldRecordRaw


class CustomFieldsApiRaw(
    AddEnumOptionRaw,
    CreateNewFieldRecordRaw,
    DeleteFieldRecordRaw,
    GetMetadataRaw,
    ListWorkspaceCustomFieldsRaw,
    ReorderEnumOptionRaw,
    UpdateEnumOptionRaw,
    UpdateFieldRecordRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass