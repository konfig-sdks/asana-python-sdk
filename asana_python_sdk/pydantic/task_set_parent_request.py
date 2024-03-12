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


class TaskSetParentRequest(BaseModel):
    # The new parent of the task, or `null` for no parent.
    parent: str = Field(alias='parent')

    # A subtask of the parent to insert the task after, or `null` to insert at the beginning of the list.
    insert_after: typing.Optional[str] = Field(None, alias='insert_after')

    # A subtask of the parent to insert the task before, or `null` to insert at the end of the list.
    insert_before: typing.Optional[str] = Field(None, alias='insert_before')
    class Config:
        arbitrary_types_allowed = True
