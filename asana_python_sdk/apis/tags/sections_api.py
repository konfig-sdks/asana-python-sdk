# coding: utf-8

"""
    Asana

    This is the interface for interacting with the [Asana Platform](https://developers.asana.com). Our API reference is generated from our [OpenAPI spec](https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml).

    The version of the OpenAPI document: 1.0
    Created by: https://asana.com/support
"""

from asana_python_sdk.paths.sections_section_gid_add_task.post import AddTaskToSection
from asana_python_sdk.paths.projects_project_gid_sections.post import CreateNewSection
from asana_python_sdk.paths.sections_section_gid.delete import DeleteSection
from asana_python_sdk.paths.sections_section_gid.get import GetRecord
from asana_python_sdk.paths.projects_project_gid_sections.get import ListProjectSections
from asana_python_sdk.paths.projects_project_gid_sections_insert.post import MoveOrInsert
from asana_python_sdk.paths.sections_section_gid.put import UpdateSectionRecord
from asana_python_sdk.apis.tags.sections_api_raw import SectionsApiRaw


class SectionsApi(
    AddTaskToSection,
    CreateNewSection,
    DeleteSection,
    GetRecord,
    ListProjectSections,
    MoveOrInsert,
    UpdateSectionRecord,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: SectionsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = SectionsApiRaw(api_client)
