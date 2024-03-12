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


class RequiredEventResponseChange(TypedDict):
    pass

class OptionalEventResponseChange(TypedDict, total=False):
    # The name of the field that has changed in the resource.
    field: str

    # The type of action taken on the **field** which has been changed.  This can be one of `changed`, `added`, or `removed` depending on the nature of the change.
    action: str

    # *Conditional.* This property is only present when the value of the event's `change.action` is `changed` _and_ the `new_value` is an Asana resource. This will be only the `gid` and `resource_type` of the resource when the events come from webhooks; this will be the compact representation (and can have fields expanded with [opt_fields](https://raw.githubusercontent.com)) when using the [get events](https://raw.githubusercontent.com) endpoint.
    new_value: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    # *Conditional.* This property is only present when the value of the event's `change.action` is `added` _and_ the `added_value` is an Asana resource. This will be only the `gid` and `resource_type` of the resource when the events come from webhooks; this will be the compact representation (and can have fields expanded with [opt_fields](https://raw.githubusercontent.com)) when using the [get events](https://raw.githubusercontent.com) endpoint.
    added_value: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    # *Conditional.* This property is only present when the value of the event's `change.action` is `removed` _and_ the `removed_value` is an Asana resource. This will be only the `gid` and `resource_type` of the resource when the events come from webhooks; this will be the compact representation (and can have fields expanded with [opt_fields](https://raw.githubusercontent.com)) when using the [get events](https://raw.githubusercontent.com) endpoint.
    removed_value: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

class EventResponseChange(RequiredEventResponseChange, OptionalEventResponseChange):
    pass
