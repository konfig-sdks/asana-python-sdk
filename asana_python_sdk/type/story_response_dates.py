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


class RequiredStoryResponseDates(TypedDict):
    pass

class OptionalStoryResponseDates(TypedDict, total=False):
    # The day on which work for this goal begins, or null if the goal has no start date. This takes a date with `YYYY-MM-DD` format, and cannot be set unless there is an accompanying due date.
    start_on: typing.Optional[date]

    # The UTC date and time on which this task is due, or null if the task has no due time. This takes an ISO 8601 date string in UTC and should not be used together with `due_on`.
    due_at: typing.Optional[datetime]

    # The localized day on which this goal is due. This takes a date with format `YYYY-MM-DD`.
    due_on: date

class StoryResponseDates(RequiredStoryResponseDates, OptionalStoryResponseDates):
    pass
