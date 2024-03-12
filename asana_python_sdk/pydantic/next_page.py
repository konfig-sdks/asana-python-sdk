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


class NextPage(BaseModel):
    # Pagination offset for the request.
    offset: typing.Optional[str] = Field(None, alias='offset')

    # A relative path containing the query parameters to fetch for next_page
    path: typing.Optional[str] = Field(None, alias='path')

    # A full uri containing the query parameters to fetch for next_page
    uri: typing.Optional[str] = Field(None, alias='uri')
    class Config:
        arbitrary_types_allowed = True
