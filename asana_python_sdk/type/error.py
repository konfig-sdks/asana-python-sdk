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


class RequiredError(TypedDict):
    pass

class OptionalError(TypedDict, total=False):
    # Message providing more detail about the error that occurred, if available.
    message: str

    # Additional information directing developers to resources on how to address and fix the problem, if available.
    help: str

    # *500 errors only*. A unique error phrase which can be used when contacting developer support to help identify the exact occurrence of the problem in Asana’s logs.
    phrase: str

class Error(RequiredError, OptionalError):
    pass
