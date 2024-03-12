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
from pydantic import BaseModel, Field, RootModel

from asana_python_sdk.pydantic.batch_request_action_options_fields import BatchRequestActionOptionsFields

class BatchRequestActionOptions(BaseModel):
    # Pagination limit for the request.
    limit: typing.Optional[int] = Field(None, alias='limit')

    # Pagination offset for the request.
    offset: typing.Optional[int] = Field(None, alias='offset')

    fields: typing.Optional[BatchRequestActionOptionsFields] = Field(None, alias='fields')
    class Config:
        arbitrary_types_allowed = True
