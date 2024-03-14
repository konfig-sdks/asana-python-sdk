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


class RequiredEnumOptionInsertRequest(TypedDict):
    # The gid of the enum option to relocate.
    enum_option: str

class OptionalEnumOptionInsertRequest(TypedDict, total=False):
    # An existing enum option within this custom field before which the new enum option should be inserted. Cannot be provided together with after_enum_option.
    before_enum_option: str

    # An existing enum option within this custom field after which the new enum option should be inserted. Cannot be provided together with before_enum_option.
    after_enum_option: str

class EnumOptionInsertRequest(RequiredEnumOptionInsertRequest, OptionalEnumOptionInsertRequest):
    pass
