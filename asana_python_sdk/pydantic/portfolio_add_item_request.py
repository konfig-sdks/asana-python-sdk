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
from pydantic import BaseModel, Field, RootModel


class PortfolioAddItemRequest(BaseModel):
    # The item to add to the portfolio.
    item: str = Field(alias='item')

    # An id of an item in this portfolio. The new item will be added before the one specified here. `insert_before` and `insert_after` parameters cannot both be specified.
    insert_before: typing.Optional[str] = Field(None, alias='insert_before')

    # An id of an item in this portfolio. The new item will be added after the one specified here. `insert_before` and `insert_after` parameters cannot both be specified.
    insert_after: typing.Optional[str] = Field(None, alias='insert_after')
    class Config:
        arbitrary_types_allowed = True
