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


class RequiredTaskSetParentRequest(TypedDict):
    # The new parent of the task, or `null` for no parent.
    parent: str

class OptionalTaskSetParentRequest(TypedDict, total=False):
    # A subtask of the parent to insert the task after, or `null` to insert at the beginning of the list.
    insert_after: str

    # A subtask of the parent to insert the task before, or `null` to insert at the end of the list.
    insert_before: str

class TaskSetParentRequest(RequiredTaskSetParentRequest, OptionalTaskSetParentRequest):
    pass
