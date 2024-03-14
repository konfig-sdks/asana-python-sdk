# coding: utf-8

"""
    Asana

    This is the interface for interacting with the [Asana Platform](https://developers.asana.com). Our API reference is generated from our [OpenAPI spec](https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml).

    The version of the OpenAPI document: 1.0
    Created by: https://asana.com/support
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from asana_python_sdk.type.custom_field_setting_response import CustomFieldSettingResponse
from asana_python_sdk.type.next_page import NextPage

class RequiredCustomFieldSettingsGetProjectCustomFieldSettingsResponse(TypedDict):
    pass

class OptionalCustomFieldSettingsGetProjectCustomFieldSettingsResponse(TypedDict, total=False):
    data: typing.List[CustomFieldSettingResponse]

    next_page: NextPage

class CustomFieldSettingsGetProjectCustomFieldSettingsResponse(RequiredCustomFieldSettingsGetProjectCustomFieldSettingsResponse, OptionalCustomFieldSettingsGetProjectCustomFieldSettingsResponse):
    pass
