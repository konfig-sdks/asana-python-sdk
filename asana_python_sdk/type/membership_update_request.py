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


class RequiredMembershipUpdateRequest(TypedDict):
    pass

class OptionalMembershipUpdateRequest(TypedDict, total=False):
    # The role given to the member. Can be `editor` or `commenter`.
    role: str

class MembershipUpdateRequest(RequiredMembershipUpdateRequest, OptionalMembershipUpdateRequest):
    pass
