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


class RequiredPortfolioAddItemRequest(TypedDict):
    # The item to add to the portfolio.
    item: str

class OptionalPortfolioAddItemRequest(TypedDict, total=False):
    # An id of an item in this portfolio. The new item will be added before the one specified here. `insert_before` and `insert_after` parameters cannot both be specified.
    insert_before: str

    # An id of an item in this portfolio. The new item will be added after the one specified here. `insert_before` and `insert_after` parameters cannot both be specified.
    insert_after: str

class PortfolioAddItemRequest(RequiredPortfolioAddItemRequest, OptionalPortfolioAddItemRequest):
    pass
