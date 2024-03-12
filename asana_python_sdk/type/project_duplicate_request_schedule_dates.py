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


class RequiredProjectDuplicateRequestScheduleDates(TypedDict):
    # Determines if the auto-shifted dates should skip weekends.
    should_skip_weekends: bool

class OptionalProjectDuplicateRequestScheduleDates(TypedDict, total=False):
    # Sets the last due date in the duplicated project to the given date. The rest of the due dates will be offset by the same amount as the due dates in the original project.
    due_on: str

    # Sets the first start date in the duplicated project to the given date. The rest of the start dates will be offset by the same amount as the start dates in the original project.
    start_on: str

class ProjectDuplicateRequestScheduleDates(RequiredProjectDuplicateRequestScheduleDates, OptionalProjectDuplicateRequestScheduleDates):
    pass
