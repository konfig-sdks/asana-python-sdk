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


class RequiredMembershipRequest(TypedDict):
    pass

class OptionalMembershipRequest(TypedDict, total=False):
    # *Optional*. Denotes if a member is active. Applies to all memberships
    is_active: bool

class MembershipRequest(RequiredMembershipRequest, OptionalMembershipRequest):
    pass
