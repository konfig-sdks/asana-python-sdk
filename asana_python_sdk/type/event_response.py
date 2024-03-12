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

from asana_python_sdk.type.asana_named_resource import AsanaNamedResource
from asana_python_sdk.type.event_response_change import EventResponseChange
from asana_python_sdk.type.user_compact import UserCompact

class RequiredEventResponse(TypedDict):
    pass

class OptionalEventResponse(TypedDict, total=False):
    user: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    resource: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    # *Deprecated: Refer to the resource_type of the resource.* The type of the resource that generated the event.
    type: str

    # The type of action taken on the **resource** that triggered the event.  This can be one of `changed`, `added`, `removed`, `deleted`, or `undeleted` depending on the nature of the event.
    action: str

    parent: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    # The timestamp when the event occurred.
    created_at: datetime

    change: EventResponseChange

class EventResponse(RequiredEventResponse, OptionalEventResponse):
    pass
