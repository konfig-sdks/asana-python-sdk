# coding: utf-8

"""
    Asana

    This is the interface for interacting with the [Asana Platform](https://developers.asana.com). Our API reference is generated from our [OpenAPI spec] (https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml).

    The version of the OpenAPI document: 1.0
    Created by: https://asana.com/support
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING


class RequiredTaskAddProjectRequest(TypedDict):
    # The project to add the task to.
    project: str

class OptionalTaskAddProjectRequest(TypedDict, total=False):
    # A task in the project to insert the task after, or `null` to insert at the beginning of the list.
    insert_after: typing.Optional[str]

    # A task in the project to insert the task before, or `null` to insert at the end of the list.
    insert_before: typing.Optional[str]

    # A section in the project to insert the task into. The task will be inserted at the bottom of the section.
    section: typing.Optional[str]

class TaskAddProjectRequest(RequiredTaskAddProjectRequest, OptionalTaskAddProjectRequest):
    pass
