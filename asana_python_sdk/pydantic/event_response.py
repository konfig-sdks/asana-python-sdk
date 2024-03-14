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
from pydantic import BaseModel, Field, RootModel

from asana_python_sdk.pydantic.asana_named_resource import AsanaNamedResource
from asana_python_sdk.pydantic.event_response_change import EventResponseChange
from asana_python_sdk.pydantic.user_compact import UserCompact

class EventResponse(BaseModel):
    user: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='user')

    resource: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='resource')

    # *Deprecated: Refer to the resource_type of the resource.* The type of the resource that generated the event.
    type: typing.Optional[str] = Field(None, alias='type')

    # The type of action taken on the **resource** that triggered the event.  This can be one of `changed`, `added`, `removed`, `deleted`, or `undeleted` depending on the nature of the event.
    action: typing.Optional[str] = Field(None, alias='action')

    parent: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='parent')

    # The timestamp when the event occurred.
    created_at: typing.Optional[datetime] = Field(None, alias='created_at')

    change: typing.Optional[EventResponseChange] = Field(None, alias='change')
    class Config:
        arbitrary_types_allowed = True
