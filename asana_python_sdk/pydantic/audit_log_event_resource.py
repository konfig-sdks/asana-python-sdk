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


class AuditLogEventResource(BaseModel):
    # The type of resource.
    resource_type: typing.Optional[str] = Field(None, alias='resource_type')

    # The subtype of resource. Most resources will not have a subtype.
    resource_subtype: typing.Optional[str] = Field(None, alias='resource_subtype')

    # Globally unique identifier of the resource.
    gid: typing.Optional[str] = Field(None, alias='gid')

    # The name of the resource.
    name: typing.Optional[typing.Optional[str]] = Field(None, alias='name')

    # The email of the resource, if applicable.
    email: typing.Optional[str] = Field(None, alias='email')
    class Config:
        arbitrary_types_allowed = True
