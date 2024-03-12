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


class RequiredStatusUpdatesDeleteSpecificStatusUpdateResponse(TypedDict):
    pass

class OptionalStatusUpdatesDeleteSpecificStatusUpdateResponse(TypedDict, total=False):
    # An empty object. Some endpoints do not return an object on success. The success is conveyed through a 2-- status code and returning an empty object.
    data: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

class StatusUpdatesDeleteSpecificStatusUpdateResponse(RequiredStatusUpdatesDeleteSpecificStatusUpdateResponse, OptionalStatusUpdatesDeleteSpecificStatusUpdateResponse):
    pass
