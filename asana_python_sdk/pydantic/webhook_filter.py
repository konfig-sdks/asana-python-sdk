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

from asana_python_sdk.pydantic.webhook_filter_fields import WebhookFilterFields

class WebhookFilter(BaseModel):
    # The type of the resource which created the event when modified; for example, to filter to changes on regular tasks this field should be set to `task`.
    resource_type: typing.Optional[str] = Field(None, alias='resource_type')

    # The resource subtype of the resource that the filter applies to. This should be set to the same value as is returned on the `resource_subtype` field on the resources themselves.
    resource_subtype: typing.Optional[str] = Field(None, alias='resource_subtype')

    # The type of change on the **resource** to pass through the filter. For more information refer to `Event.action` in the [event](https://raw.githubusercontent.com) schema. This can be one of `changed`, `added`, `removed`, `deleted`, and `undeleted` depending on the nature of what has occurred on the resource.
    action: typing.Optional[str] = Field(None, alias='action')

    fields: typing.Optional[WebhookFilterFields] = Field(None, alias='fields')
    class Config:
        arbitrary_types_allowed = True
