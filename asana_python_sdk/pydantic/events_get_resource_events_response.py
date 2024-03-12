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

from asana_python_sdk.pydantic.event_response import EventResponse

class EventsGetResourceEventsResponse(BaseModel):
    data: typing.Optional[typing.List[EventResponse]] = Field(None, alias='data')

    # A sync token to be used with the next call to the /events endpoint.
    sync: typing.Optional[str] = Field(None, alias='sync')

    # Indicates whether there are more events to pull.
    has_more: typing.Optional[bool] = Field(None, alias='has_more')
    class Config:
        arbitrary_types_allowed = True
