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


class RequiredAuditLogEventActor(TypedDict):
    pass

class OptionalAuditLogEventActor(TypedDict, total=False):
    # The type of actor. Can be one of `user`, `asana`, `asana_support`, `anonymous`, or `external_administrator`.
    actor_type: str

    # Globally unique identifier of the actor, if it is a user.
    gid: str

    # The name of the actor, if it is a user.
    name: str

    # The email of the actor, if it is a user.
    email: str

class AuditLogEventActor(RequiredAuditLogEventActor, OptionalAuditLogEventActor):
    pass
