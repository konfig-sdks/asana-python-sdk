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

from asana_python_sdk.type.custom_field_compact import CustomFieldCompact
from asana_python_sdk.type.custom_field_setting_response import CustomFieldSettingResponse
from asana_python_sdk.type.portfolio_base import PortfolioBase
from asana_python_sdk.type.project_template_compact import ProjectTemplateCompact
from asana_python_sdk.type.status_update_compact import StatusUpdateCompact
from asana_python_sdk.type.user_compact import UserCompact
from asana_python_sdk.type.workspace_compact import WorkspaceCompact

PortfolioResponse = typing.Union[PortfolioBase,typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]
