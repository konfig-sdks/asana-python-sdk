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


class TaskAddProjectRequest(BaseModel):
    # The project to add the task to.
    project: str = Field(alias='project')

    # A task in the project to insert the task after, or `null` to insert at the beginning of the list.
    insert_after: typing.Optional[typing.Optional[str]] = Field(None, alias='insert_after')

    # A task in the project to insert the task before, or `null` to insert at the end of the list.
    insert_before: typing.Optional[typing.Optional[str]] = Field(None, alias='insert_before')

    # A section in the project to insert the task into. The task will be inserted at the bottom of the section.
    section: typing.Optional[typing.Optional[str]] = Field(None, alias='section')
    class Config:
        arbitrary_types_allowed = True
