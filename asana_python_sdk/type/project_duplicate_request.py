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

from asana_python_sdk.type.project_duplicate_request_schedule_dates import ProjectDuplicateRequestScheduleDates

class RequiredProjectDuplicateRequest(TypedDict):
    # The name of the new project.
    name: str

class OptionalProjectDuplicateRequest(TypedDict, total=False):
    # Sets the team of the new project. If team is not defined, the new project will be in the same team as the the original project.
    team: str

    # A comma-separated list of elements that will be duplicated to the new project. Tasks are always included. ##### Fields - allocations - forms - members - notes - task_assignee - task_attachments - task_dates - task_dependencies - task_followers - task_notes - task_projects - task_subtasks - task_tags
    include: str

    schedule_dates: ProjectDuplicateRequestScheduleDates

class ProjectDuplicateRequest(RequiredProjectDuplicateRequest, OptionalProjectDuplicateRequest):
    pass
