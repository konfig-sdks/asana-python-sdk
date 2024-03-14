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


class RequiredAuditLogEventContext(TypedDict):
    pass

class OptionalAuditLogEventContext(TypedDict, total=False):
    # The type of context. Can be one of `web`, `desktop`, `mobile`, `asana_support`, `asana`, `email`, or `api`.
    context_type: str

    # The authentication method used in the context of an API request. Only present if the `context_type` is `api`. Can be one of `cookie`, `oauth`, `personal_access_token`, or `service_account`.
    api_authentication_method: str

    # The IP address of the client that initiated the event, if applicable.
    client_ip_address: str

    # The user agent of the client that initiated the event, if applicable.
    user_agent: str

    # The name of the OAuth App that initiated the event. Only present if the `api_authentication_method` is `oauth`.
    oauth_app_name: str

class AuditLogEventContext(RequiredAuditLogEventContext, OptionalAuditLogEventContext):
    pass
