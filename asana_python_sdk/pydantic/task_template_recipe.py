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
from pydantic import BaseModel, Field, RootModel

from asana_python_sdk.pydantic.attachment_compact import AttachmentCompact
from asana_python_sdk.pydantic.custom_field_compact import CustomFieldCompact
from asana_python_sdk.pydantic.project_compact import ProjectCompact
from asana_python_sdk.pydantic.task_template_recipe_compact import TaskTemplateRecipeCompact
from asana_python_sdk.pydantic.user_compact import UserCompact

TaskTemplateRecipe = typing.Union[TaskTemplateRecipeCompact,typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]
