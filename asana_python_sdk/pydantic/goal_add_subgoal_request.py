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


class GoalAddSubgoalRequest(BaseModel):
    # The goal gid to add as subgoal to a parent goal
    subgoal: str = Field(alias='subgoal')

    # An id of a subgoal of this parent goal. The new subgoal will be added before the one specified here. `insert_before` and `insert_after` parameters cannot both be specified.
    insert_before: typing.Optional[str] = Field(None, alias='insert_before')

    # An id of a subgoal of this parent goal. The new subgoal will be added after the one specified here. `insert_before` and `insert_after` parameters cannot both be specified.
    insert_after: typing.Optional[str] = Field(None, alias='insert_after')
    class Config:
        arbitrary_types_allowed = True
