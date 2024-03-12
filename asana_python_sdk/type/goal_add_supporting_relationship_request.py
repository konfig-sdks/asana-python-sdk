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


class RequiredGoalAddSupportingRelationshipRequest(TypedDict):
    # The gid of the supporting resource to add to the parent goal. Must be the gid of a goal, project, task, or portfolio.
    supporting_resource: str

class OptionalGoalAddSupportingRelationshipRequest(TypedDict, total=False):
    # An id of a subgoal of this parent goal. The new subgoal will be added before the one specified here. `insert_before` and `insert_after` parameters cannot both be specified. Currently only supported when adding a subgoal.
    insert_before: str

    # An id of a subgoal of this parent goal. The new subgoal will be added after the one specified here. `insert_before` and `insert_after` parameters cannot both be specified. Currently only supported when adding a subgoal.
    insert_after: str

    # The weight that the supporting resource's progress will contribute to the supported goal's progress. This can only be 0 or 1.
    contribution_weight: typing.Union[int, float]

class GoalAddSupportingRelationshipRequest(RequiredGoalAddSupportingRelationshipRequest, OptionalGoalAddSupportingRelationshipRequest):
    pass
