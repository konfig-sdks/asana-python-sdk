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


class ProjectSaveAsTemplateRequest(BaseModel):
    # The name of the new project template.
    name: str = Field(alias='name')

    # Sets the project template to public to its team.
    public: bool = Field(alias='public')

    # Sets the team of the new project template. If the project exists in an organization, specify team and not workspace.
    team: typing.Optional[str] = Field(None, alias='team')

    # Sets the workspace of the new project template. Only specify workspace if the project exists in a workspace.
    workspace: typing.Optional[str] = Field(None, alias='workspace')
    class Config:
        arbitrary_types_allowed = True
