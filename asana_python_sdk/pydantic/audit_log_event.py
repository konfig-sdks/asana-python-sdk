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

from asana_python_sdk.pydantic.audit_log_event_actor import AuditLogEventActor
from asana_python_sdk.pydantic.audit_log_event_context import AuditLogEventContext
from asana_python_sdk.pydantic.audit_log_event_resource import AuditLogEventResource

class AuditLogEvent(BaseModel):
    # Globally unique identifier of the `AuditLogEvent`, as a string.
    gid: typing.Optional[str] = Field(None, alias='gid')

    # The time the event was created.
    created_at: typing.Optional[datetime] = Field(None, alias='created_at')

    # The type of the event.
    event_type: typing.Optional[str] = Field(None, alias='event_type')

    # The category that this `event_type` belongs to.
    event_category: typing.Optional[str] = Field(None, alias='event_category')

    actor: typing.Optional[AuditLogEventActor] = Field(None, alias='actor')

    resource: typing.Optional[AuditLogEventResource] = Field(None, alias='resource')

    # Event specific details. The schema will vary depending on the `event_type`.
    details: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='details')

    context: typing.Optional[AuditLogEventContext] = Field(None, alias='context')
    class Config:
        arbitrary_types_allowed = True
