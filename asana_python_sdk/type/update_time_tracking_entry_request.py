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


class RequiredUpdateTimeTrackingEntryRequest(TypedDict):
    pass

class OptionalUpdateTimeTrackingEntryRequest(TypedDict, total=False):
    # *Optional*. Time in minutes tracked by the entry
    duration_minutes: int

    # *Optional*. The day that this entry is logged on. Defaults to today if no day specified
    entered_on: date

class UpdateTimeTrackingEntryRequest(RequiredUpdateTimeTrackingEntryRequest, OptionalUpdateTimeTrackingEntryRequest):
    pass
