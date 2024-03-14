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


class TaskCountResponse(BaseModel):
    # The number of tasks in a project.
    num_tasks: typing.Optional[int] = Field(None, alias='num_tasks')

    # The number of incomplete tasks in a project.
    num_incomplete_tasks: typing.Optional[int] = Field(None, alias='num_incomplete_tasks')

    # The number of completed tasks in a project.
    num_completed_tasks: typing.Optional[int] = Field(None, alias='num_completed_tasks')

    # The number of milestones in a project.
    num_milestones: typing.Optional[int] = Field(None, alias='num_milestones')

    # The number of incomplete milestones in a project.
    num_incomplete_milestones: typing.Optional[int] = Field(None, alias='num_incomplete_milestones')

    # The number of completed milestones in a project.
    num_completed_milestones: typing.Optional[int] = Field(None, alias='num_completed_milestones')
    class Config:
        arbitrary_types_allowed = True
