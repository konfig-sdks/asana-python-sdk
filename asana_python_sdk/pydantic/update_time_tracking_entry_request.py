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
from pydantic import BaseModel, Field, RootModel


class UpdateTimeTrackingEntryRequest(BaseModel):
    # *Optional*. Time in minutes tracked by the entry
    duration_minutes: typing.Optional[int] = Field(None, alias='duration_minutes')

    # *Optional*. The day that this entry is logged on. Defaults to today if no day specified
    entered_on: typing.Optional[date] = Field(None, alias='entered_on')
    class Config:
        arbitrary_types_allowed = True
