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


class AddCustomFieldSettingRequest(BaseModel):
    # The custom field to associate with this container.
    custom_field: str = Field(alias='custom_field')

    # Whether this field should be considered important to this container (for instance, to display in the list view of items in the container).
    is_important: typing.Optional[bool] = Field(None, alias='is_important')

    # A gid of a Custom Field Setting on this container, before which the new Custom Field Setting will be added.  `insert_before` and `insert_after` parameters cannot both be specified.
    insert_before: typing.Optional[str] = Field(None, alias='insert_before')

    # A gid of a Custom Field Setting on this container, after which the new Custom Field Setting will be added.  `insert_before` and `insert_after` parameters cannot both be specified.
    insert_after: typing.Optional[str] = Field(None, alias='insert_after')
    class Config:
        arbitrary_types_allowed = True
