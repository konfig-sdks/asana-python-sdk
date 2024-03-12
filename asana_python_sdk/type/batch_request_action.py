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

from asana_python_sdk.type.batch_request_action_options import BatchRequestActionOptions

class RequiredBatchRequestAction(TypedDict):
    # The path of the desired endpoint relative to the API’s base URL. Query parameters are not accepted here; put them in `data` instead.
    relative_path: str

    # The HTTP method you wish to emulate for the action.
    method: str

class OptionalBatchRequestAction(TypedDict, total=False):
    # For `GET` requests, this should be a map of query parameters you would have normally passed in the URL. Options and pagination are not accepted here; put them in `options` instead. For `POST`, `PATCH`, and `PUT` methods, this should be the content you would have normally put in the data field of the body.
    data: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    options: BatchRequestActionOptions

class BatchRequestAction(RequiredBatchRequestAction, OptionalBatchRequestAction):
    pass
