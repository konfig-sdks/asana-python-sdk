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


class GoalRemoveSupportingRelationshipRequest(BaseModel):
    # The gid of the supporting resource to remove from the parent goal. Must be the gid of a goal, project, task, or portfolio.
    supporting_resource: str = Field(alias='supporting_resource')
    class Config:
        arbitrary_types_allowed = True
