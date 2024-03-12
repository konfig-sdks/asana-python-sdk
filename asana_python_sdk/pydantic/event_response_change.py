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


class EventResponseChange(BaseModel):
    # The name of the field that has changed in the resource.
    field: typing.Optional[str] = Field(None, alias='field')

    # The type of action taken on the **field** which has been changed.  This can be one of `changed`, `added`, or `removed` depending on the nature of the change.
    action: typing.Optional[str] = Field(None, alias='action')

    # *Conditional.* This property is only present when the value of the event's `change.action` is `changed` _and_ the `new_value` is an Asana resource. This will be only the `gid` and `resource_type` of the resource when the events come from webhooks; this will be the compact representation (and can have fields expanded with [opt_fields](https://raw.githubusercontent.com)) when using the [get events](https://raw.githubusercontent.com) endpoint.
    new_value: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='new_value')

    # *Conditional.* This property is only present when the value of the event's `change.action` is `added` _and_ the `added_value` is an Asana resource. This will be only the `gid` and `resource_type` of the resource when the events come from webhooks; this will be the compact representation (and can have fields expanded with [opt_fields](https://raw.githubusercontent.com)) when using the [get events](https://raw.githubusercontent.com) endpoint.
    added_value: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='added_value')

    # *Conditional.* This property is only present when the value of the event's `change.action` is `removed` _and_ the `removed_value` is an Asana resource. This will be only the `gid` and `resource_type` of the resource when the events come from webhooks; this will be the compact representation (and can have fields expanded with [opt_fields](https://raw.githubusercontent.com)) when using the [get events](https://raw.githubusercontent.com) endpoint.
    removed_value: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='removed_value')
    class Config:
        arbitrary_types_allowed = True
