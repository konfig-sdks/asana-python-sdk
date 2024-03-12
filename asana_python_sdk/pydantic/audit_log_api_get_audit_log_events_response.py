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

from asana_python_sdk.pydantic.audit_log_event import AuditLogEvent
from asana_python_sdk.pydantic.next_page import NextPage

class AuditLogApiGetAuditLogEventsResponse(BaseModel):
    data: typing.Optional[typing.List[AuditLogEvent]] = Field(None, alias='data')

    next_page: typing.Optional[NextPage] = Field(None, alias='next_page')
    class Config:
        arbitrary_types_allowed = True
