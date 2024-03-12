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


class RequiredBatchResponse(TypedDict):
    pass

class OptionalBatchResponse(TypedDict, total=False):
    # The HTTP status code that the invoked endpoint returned.
    status_code: int

    # A map of HTTP headers specific to this result. This is primarily used for returning a `Location` header to accompany a `201 Created` result.  The parent HTTP response will contain all common headers.
    headers: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # The JSON body that the invoked endpoint returned.
    body: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

class BatchResponse(RequiredBatchResponse, OptionalBatchResponse):
    pass
