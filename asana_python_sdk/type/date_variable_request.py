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


class RequiredDateVariableRequest(TypedDict):
    pass

class OptionalDateVariableRequest(TypedDict, total=False):
    # Globally unique identifier of the date field in the project template. A value of `1` refers to the project start date, while `2` refers to the project due date.
    gid: str

    # The date with which the date variable should be replaced when instantiating a project. This takes a date with `YYYY-MM-DD` format.
    value: typing.Optional[datetime]

class DateVariableRequest(RequiredDateVariableRequest, OptionalDateVariableRequest):
    pass
