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


class AuditLogEventActor(BaseModel):
    # The type of actor. Can be one of `user`, `asana`, `asana_support`, `anonymous`, or `external_administrator`.
    actor_type: typing.Optional[Literal["user", "asana", "asana_support", "anonymous", "external_administrator"]] = Field(None, alias='actor_type')

    # Globally unique identifier of the actor, if it is a user.
    gid: typing.Optional[str] = Field(None, alias='gid')

    # The name of the actor, if it is a user.
    name: typing.Optional[str] = Field(None, alias='name')

    # The email of the actor, if it is a user.
    email: typing.Optional[str] = Field(None, alias='email')
    class Config:
        arbitrary_types_allowed = True
