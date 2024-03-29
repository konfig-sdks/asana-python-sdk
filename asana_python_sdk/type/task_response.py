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

from asana_python_sdk.type.custom_field_response import CustomFieldResponse
from asana_python_sdk.type.project_compact import ProjectCompact
from asana_python_sdk.type.section_compact import SectionCompact
from asana_python_sdk.type.tag_compact import TagCompact
from asana_python_sdk.type.task_base import TaskBase
from asana_python_sdk.type.task_compact import TaskCompact
from asana_python_sdk.type.user_compact import UserCompact
from asana_python_sdk.type.workspace_compact import WorkspaceCompact

TaskResponse = typing.Union[TaskBase,typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]
