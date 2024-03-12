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


class ProjectDuplicateRequestScheduleDates(BaseModel):
    # Determines if the auto-shifted dates should skip weekends.
    should_skip_weekends: bool = Field(alias='should_skip_weekends')

    # Sets the last due date in the duplicated project to the given date. The rest of the due dates will be offset by the same amount as the due dates in the original project.
    due_on: typing.Optional[str] = Field(None, alias='due_on')

    # Sets the first start date in the duplicated project to the given date. The rest of the start dates will be offset by the same amount as the start dates in the original project.
    start_on: typing.Optional[str] = Field(None, alias='start_on')
    class Config:
        arbitrary_types_allowed = True
