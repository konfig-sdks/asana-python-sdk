# coding: utf-8

"""
    Asana

    This is the interface for interacting with the [Asana Platform](https://developers.asana.com). Our API reference is generated from our [OpenAPI spec] (https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml).

    The version of the OpenAPI document: 1.0
    Created by: https://asana.com/support
"""

from asana_python_sdk.paths.memberships.post import CreateNewRecord
from asana_python_sdk.paths.memberships_membership_gid.delete import DeleteRecord
from asana_python_sdk.paths.memberships_membership_gid.get import GetMembershipRecord
from asana_python_sdk.paths.memberships.get import GetMultiple
from asana_python_sdk.apis.tags.memberships_api_raw import MembershipsApiRaw


class MembershipsApi(
    CreateNewRecord,
    DeleteRecord,
    GetMembershipRecord,
    GetMultiple,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: MembershipsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = MembershipsApiRaw(api_client)
