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


class RequiredAuditLogEventResource(TypedDict):
    pass

class OptionalAuditLogEventResource(TypedDict, total=False):
    # The type of resource.
    resource_type: str

    # The subtype of resource. Most resources will not have a subtype.
    resource_subtype: str

    # Globally unique identifier of the resource.
    gid: str

    # The name of the resource.
    name: typing.Optional[str]

    # The email of the resource, if applicable.
    email: str

class AuditLogEventResource(RequiredAuditLogEventResource, OptionalAuditLogEventResource):
    pass
