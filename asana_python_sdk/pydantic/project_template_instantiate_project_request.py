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

from asana_python_sdk.pydantic.date_variable_request import DateVariableRequest
from asana_python_sdk.pydantic.requested_role_request import RequestedRoleRequest

class ProjectTemplateInstantiateProjectRequest(BaseModel):
    # The name of the new project.
    name: str = Field(alias='name')

    # *Optional*. Sets the team of the new project. If the project template exists in an _organization_, you may specify a value for `team`. If no value is provided then it defaults to the same team as the project template.
    team: typing.Optional[str] = Field(None, alias='team')

    # Sets the project to public to its team.
    public: typing.Optional[bool] = Field(None, alias='public')

    # *Optional*. If set to `true`, the endpoint returns an \"Unprocessable Entity\" error if you fail to provide a calendar date value for any date variable. If set to `false`, a default date is used for each unfulfilled date variable (e.g., the current date is used as the Start Date of a project).
    is_strict: typing.Optional[bool] = Field(None, alias='is_strict')

    # Array of mappings of date variables to calendar dates.
    requested_dates: typing.Optional[typing.List[DateVariableRequest]] = Field(None, alias='requested_dates')

    # Array of mappings of template roles to user ids
    requested_roles: typing.Optional[typing.List[RequestedRoleRequest]] = Field(None, alias='requested_roles')
    class Config:
        arbitrary_types_allowed = True
