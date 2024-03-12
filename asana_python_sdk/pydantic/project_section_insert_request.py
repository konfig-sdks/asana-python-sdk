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


class ProjectSectionInsertRequest(BaseModel):
    # The section to reorder.
    section: str = Field(alias='section')

    # Insert the given section immediately before the section specified by this parameter.
    before_section: typing.Optional[str] = Field(None, alias='before_section')

    # Insert the given section immediately after the section specified by this parameter.
    after_section: typing.Optional[str] = Field(None, alias='after_section')
    class Config:
        arbitrary_types_allowed = True
