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


class TaskDuplicateRequest(BaseModel):
    # The name of the new task.
    name: typing.Optional[str] = Field(None, alias='name')

    # A comma-separated list of fields that will be duplicated to the new task. ##### Fields - assignee - attachments - dates - dependencies - followers - notes - parent - projects - subtasks - tags
    include: typing.Optional[str] = Field(None, alias='include')
    class Config:
        arbitrary_types_allowed = True
