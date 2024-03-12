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

from asana_python_sdk.type.date_variable_request import DateVariableRequest
from asana_python_sdk.type.requested_role_request import RequestedRoleRequest

class RequiredProjectTemplateInstantiateProjectRequest(TypedDict):
    # The name of the new project.
    name: str

class OptionalProjectTemplateInstantiateProjectRequest(TypedDict, total=False):
    # *Optional*. Sets the team of the new project. If the project template exists in an _organization_, you may specify a value for `team`. If no value is provided then it defaults to the same team as the project template.
    team: str

    # Sets the project to public to its team.
    public: bool

    # *Optional*. If set to `true`, the endpoint returns an \"Unprocessable Entity\" error if you fail to provide a calendar date value for any date variable. If set to `false`, a default date is used for each unfulfilled date variable (e.g., the current date is used as the Start Date of a project).
    is_strict: bool

    # Array of mappings of date variables to calendar dates.
    requested_dates: typing.List[DateVariableRequest]

    # Array of mappings of template roles to user ids
    requested_roles: typing.List[RequestedRoleRequest]

class ProjectTemplateInstantiateProjectRequest(RequiredProjectTemplateInstantiateProjectRequest, OptionalProjectTemplateInstantiateProjectRequest):
    pass
