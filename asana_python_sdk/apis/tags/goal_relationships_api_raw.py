# coding: utf-8

"""
    Asana

    This is the interface for interacting with the [Asana Platform](https://developers.asana.com). Our API reference is generated from our [OpenAPI spec] (https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml).

    The version of the OpenAPI document: 1.0
    Created by: https://asana.com/support
"""

from asana_python_sdk.paths.goals_goal_gid_add_supporting_relationship.post import CreateSupportingRelationshipRaw
from asana_python_sdk.paths.goal_relationships.get import GetCompactRecordsRaw
from asana_python_sdk.paths.goal_relationships_goal_relationship_gid.get import GetRecordByIdRaw
from asana_python_sdk.paths.goals_goal_gid_remove_supporting_relationship.post import RemoveSupportingRelationshipRaw
from asana_python_sdk.paths.goal_relationships_goal_relationship_gid.put import UpdateGoalRelationshipRecordRaw


class GoalRelationshipsApiRaw(
    CreateSupportingRelationshipRaw,
    GetCompactRecordsRaw,
    GetRecordByIdRaw,
    RemoveSupportingRelationshipRaw,
    UpdateGoalRelationshipRecordRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
