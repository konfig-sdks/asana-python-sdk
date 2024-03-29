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


class RequiredNextPage(TypedDict):
    pass

class OptionalNextPage(TypedDict, total=False):
    # Pagination offset for the request.
    offset: str

    # A relative path containing the query parameters to fetch for next_page
    path: str

    # A full uri containing the query parameters to fetch for next_page
    uri: str

class NextPage(RequiredNextPage, OptionalNextPage):
    pass
