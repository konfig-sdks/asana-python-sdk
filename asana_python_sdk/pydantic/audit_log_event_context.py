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


class AuditLogEventContext(BaseModel):
    # The type of context. Can be one of `web`, `desktop`, `mobile`, `asana_support`, `asana`, `email`, or `api`.
    context_type: typing.Optional[Literal["web", "desktop", "mobile", "asana_support", "asana", "email", "api"]] = Field(None, alias='context_type')

    # The authentication method used in the context of an API request. Only present if the `context_type` is `api`. Can be one of `cookie`, `oauth`, `personal_access_token`, or `service_account`.
    api_authentication_method: typing.Optional[Literal["cookie", "oauth", "personal_access_token", "service_account"]] = Field(None, alias='api_authentication_method')

    # The IP address of the client that initiated the event, if applicable.
    client_ip_address: typing.Optional[str] = Field(None, alias='client_ip_address')

    # The user agent of the client that initiated the event, if applicable.
    user_agent: typing.Optional[str] = Field(None, alias='user_agent')

    # The name of the OAuth App that initiated the event. Only present if the `api_authentication_method` is `oauth`.
    oauth_app_name: typing.Optional[str] = Field(None, alias='oauth_app_name')
    class Config:
        arbitrary_types_allowed = True
