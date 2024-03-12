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

from asana_python_sdk.type.batch_request_action_options_fields import BatchRequestActionOptionsFields

class RequiredBatchRequestActionOptions(TypedDict):
    pass

class OptionalBatchRequestActionOptions(TypedDict, total=False):
    # Pagination limit for the request.
    limit: int

    # Pagination offset for the request.
    offset: int

    fields: BatchRequestActionOptionsFields

class BatchRequestActionOptions(RequiredBatchRequestActionOptions, OptionalBatchRequestActionOptions):
    pass
