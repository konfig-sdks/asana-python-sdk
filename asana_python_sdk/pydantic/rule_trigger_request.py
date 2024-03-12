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

from asana_python_sdk.pydantic.rule_trigger_request_action_data import RuleTriggerRequestActionData

class RuleTriggerRequest(BaseModel):
    # The ID of the resource. For the duration of the beta, this resource is always a task, and this task must exist in the project in which the rule is created.
    resource: str = Field(alias='resource')

    action_data: RuleTriggerRequestActionData = Field(alias='action_data')
    class Config:
        arbitrary_types_allowed = True
