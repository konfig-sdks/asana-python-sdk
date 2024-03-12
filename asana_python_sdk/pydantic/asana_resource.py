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


class AsanaResource(BaseModel):
    # Globally unique identifier of the resource, as a string.
    gid: typing.Optional[str] = Field(None, alias='gid')

    # The base type of this resource.
    resource_type: typing.Optional[str] = Field(None, alias='resource_type')
    class Config:
        arbitrary_types_allowed = True
