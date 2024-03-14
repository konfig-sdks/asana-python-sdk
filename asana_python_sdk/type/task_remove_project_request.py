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


class RequiredTaskRemoveProjectRequest(TypedDict):
    # The project to remove the task from.
    project: str

class OptionalTaskRemoveProjectRequest(TypedDict, total=False):
    pass

class TaskRemoveProjectRequest(RequiredTaskRemoveProjectRequest, OptionalTaskRemoveProjectRequest):
    pass
