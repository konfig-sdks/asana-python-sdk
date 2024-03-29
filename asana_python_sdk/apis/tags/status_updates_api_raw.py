# coding: utf-8

"""
    Asana

    This is the interface for interacting with the [Asana Platform](https://developers.asana.com). Our API reference is generated from our [OpenAPI spec](https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml).

    The version of the OpenAPI document: 1.0
    Created by: https://asana.com/support
"""

from asana_python_sdk.paths.status_updates.post import CreateNewStatusUpdateRecordRaw
from asana_python_sdk.paths.status_updates_status_update_gid.delete import DeleteSpecificStatusUpdateRaw
from asana_python_sdk.paths.status_updates.get import GetCompactRecordsRaw
from asana_python_sdk.paths.status_updates_status_update_gid.get import GetRecordByIdRaw


class StatusUpdatesApiRaw(
    CreateNewStatusUpdateRecordRaw,
    DeleteSpecificStatusUpdateRaw,
    GetCompactRecordsRaw,
    GetRecordByIdRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
