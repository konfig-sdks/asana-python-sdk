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

from asana_python_sdk.pydantic.webhook_request_filters import WebhookRequestFilters

class WebhookRequest(BaseModel):
    # A resource ID to subscribe to. Many Asana resources are valid to create webhooks on, but higher-level resources require filters.
    resource: str = Field(alias='resource')

    # The URL to receive the HTTP POST. The full URL will be used to deliver events from this webhook (including parameters) which allows encoding of application-specific state when the webhook is created.
    target: str = Field(alias='target')

    filters: typing.Optional[WebhookRequestFilters] = Field(None, alias='filters')
    class Config:
        arbitrary_types_allowed = True
