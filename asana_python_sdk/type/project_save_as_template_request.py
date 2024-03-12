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


class RequiredProjectSaveAsTemplateRequest(TypedDict):
    # The name of the new project template.
    name: str

    # Sets the project template to public to its team.
    public: bool

class OptionalProjectSaveAsTemplateRequest(TypedDict, total=False):
    # Sets the team of the new project template. If the project exists in an organization, specify team and not workspace.
    team: str

    # Sets the workspace of the new project template. Only specify workspace if the project exists in a workspace.
    workspace: str

class ProjectSaveAsTemplateRequest(RequiredProjectSaveAsTemplateRequest, OptionalProjectSaveAsTemplateRequest):
    pass
