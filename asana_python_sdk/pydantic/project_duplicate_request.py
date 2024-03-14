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

from asana_python_sdk.pydantic.project_duplicate_request_schedule_dates import ProjectDuplicateRequestScheduleDates

class ProjectDuplicateRequest(BaseModel):
    # The name of the new project.
    name: str = Field(alias='name')

    # Sets the team of the new project. If team is not defined, the new project will be in the same team as the the original project.
    team: typing.Optional[str] = Field(None, alias='team')

    # A comma-separated list of elements that will be duplicated to the new project. Tasks are always included. ##### Fields - allocations - forms - members - notes - task_assignee - task_attachments - task_dates - task_dependencies - task_followers - task_notes - task_projects - task_subtasks - task_tags
    include: typing.Optional[str] = Field(None, alias='include')

    schedule_dates: typing.Optional[ProjectDuplicateRequestScheduleDates] = Field(None, alias='schedule_dates')
    class Config:
        arbitrary_types_allowed = True
