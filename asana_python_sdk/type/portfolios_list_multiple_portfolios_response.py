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

from asana_python_sdk.type.next_page import NextPage
from asana_python_sdk.type.portfolio_compact import PortfolioCompact

class RequiredPortfoliosListMultiplePortfoliosResponse(TypedDict):
    pass

class OptionalPortfoliosListMultiplePortfoliosResponse(TypedDict, total=False):
    data: typing.List[PortfolioCompact]

    next_page: NextPage

class PortfoliosListMultiplePortfoliosResponse(RequiredPortfoliosListMultiplePortfoliosResponse, OptionalPortfoliosListMultiplePortfoliosResponse):
    pass
