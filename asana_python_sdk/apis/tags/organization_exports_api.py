# coding: utf-8

"""
    Asana

    This is the interface for interacting with the [Asana Platform](https://developers.asana.com). Our API reference is generated from our [OpenAPI spec](https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml).

    The version of the OpenAPI document: 1.0
    Created by: https://asana.com/support
"""

from asana_python_sdk.paths.organization_exports.post import CreateExportRequest
from asana_python_sdk.paths.organization_exports_organization_export_gid.get import GetExportDetails
from asana_python_sdk.apis.tags.organization_exports_api_raw import OrganizationExportsApiRaw


class OrganizationExportsApi(
    CreateExportRequest,
    GetExportDetails,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: OrganizationExportsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = OrganizationExportsApiRaw(api_client)
