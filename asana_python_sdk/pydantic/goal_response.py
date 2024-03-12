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

from asana_python_sdk.pydantic.goal_base import GoalBase
from asana_python_sdk.pydantic.goal_metric_base import GoalMetricBase
from asana_python_sdk.pydantic.like import Like
from asana_python_sdk.pydantic.status_update_compact import StatusUpdateCompact
from asana_python_sdk.pydantic.team_compact import TeamCompact
from asana_python_sdk.pydantic.time_period_compact import TimePeriodCompact
from asana_python_sdk.pydantic.user_compact import UserCompact
from asana_python_sdk.pydantic.workspace_compact import WorkspaceCompact

GoalResponse = typing.Union[GoalBase,typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]
