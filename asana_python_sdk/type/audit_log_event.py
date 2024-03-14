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

from asana_python_sdk.type.audit_log_event_actor import AuditLogEventActor
from asana_python_sdk.type.audit_log_event_context import AuditLogEventContext
from asana_python_sdk.type.audit_log_event_resource import AuditLogEventResource

class RequiredAuditLogEvent(TypedDict):
    pass

class OptionalAuditLogEvent(TypedDict, total=False):
    # Globally unique identifier of the `AuditLogEvent`, as a string.
    gid: str

    # The time the event was created.
    created_at: datetime

    # The type of the event.
    event_type: str

    # The category that this `event_type` belongs to.
    event_category: str

    actor: AuditLogEventActor

    resource: AuditLogEventResource

    # Event specific details. The schema will vary depending on the `event_type`.
    details: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    context: AuditLogEventContext

class AuditLogEvent(RequiredAuditLogEvent, OptionalAuditLogEvent):
    pass
