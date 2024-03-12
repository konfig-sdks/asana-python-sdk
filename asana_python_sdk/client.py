# coding: utf-8
"""
    Asana

    This is the interface for interacting with the [Asana Platform](https://developers.asana.com). Our API reference is generated from our [OpenAPI spec] (https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml).

    The version of the OpenAPI document: 1.0
    Created by: https://asana.com/support
"""

import typing
import inspect
from datetime import date, datetime
from asana_python_sdk.client_custom import ClientCustom
from asana_python_sdk.configuration import Configuration
from asana_python_sdk.api_client import ApiClient
from asana_python_sdk.type_util import copy_signature
from asana_python_sdk.apis.tags.attachments_api import AttachmentsApi
from asana_python_sdk.apis.tags.audit_log_api_api import AuditLogAPIApi
from asana_python_sdk.apis.tags.batch_api_api import BatchAPIApi
from asana_python_sdk.apis.tags.custom_field_settings_api import CustomFieldSettingsApi
from asana_python_sdk.apis.tags.custom_fields_api import CustomFieldsApi
from asana_python_sdk.apis.tags.events_api import EventsApi
from asana_python_sdk.apis.tags.goal_relationships_api import GoalRelationshipsApi
from asana_python_sdk.apis.tags.goals_api import GoalsApi
from asana_python_sdk.apis.tags.jobs_api import JobsApi
from asana_python_sdk.apis.tags.memberships_api import MembershipsApi
from asana_python_sdk.apis.tags.organization_exports_api import OrganizationExportsApi
from asana_python_sdk.apis.tags.portfolio_memberships_api import PortfolioMembershipsApi
from asana_python_sdk.apis.tags.portfolios_api import PortfoliosApi
from asana_python_sdk.apis.tags.project_briefs_api import ProjectBriefsApi
from asana_python_sdk.apis.tags.project_memberships_api import ProjectMembershipsApi
from asana_python_sdk.apis.tags.project_statuses_api import ProjectStatusesApi
from asana_python_sdk.apis.tags.project_templates_api import ProjectTemplatesApi
from asana_python_sdk.apis.tags.projects_api import ProjectsApi
from asana_python_sdk.apis.tags.rules_api import RulesApi
from asana_python_sdk.apis.tags.sections_api import SectionsApi
from asana_python_sdk.apis.tags.status_updates_api import StatusUpdatesApi
from asana_python_sdk.apis.tags.stories_api import StoriesApi
from asana_python_sdk.apis.tags.tags_api import TagsApi
from asana_python_sdk.apis.tags.task_templates_api import TaskTemplatesApi
from asana_python_sdk.apis.tags.tasks_api import TasksApi
from asana_python_sdk.apis.tags.team_memberships_api import TeamMembershipsApi
from asana_python_sdk.apis.tags.teams_api import TeamsApi
from asana_python_sdk.apis.tags.time_periods_api import TimePeriodsApi
from asana_python_sdk.apis.tags.time_tracking_entries_api import TimeTrackingEntriesApi
from asana_python_sdk.apis.tags.typeahead_api import TypeaheadApi
from asana_python_sdk.apis.tags.user_task_lists_api import UserTaskListsApi
from asana_python_sdk.apis.tags.users_api import UsersApi
from asana_python_sdk.apis.tags.webhooks_api import WebhooksApi
from asana_python_sdk.apis.tags.workspace_memberships_api import WorkspaceMembershipsApi
from asana_python_sdk.apis.tags.workspaces_api import WorkspacesApi



class Asana(ClientCustom):

    def __init__(self, configuration: typing.Union[Configuration, None] = None, **kwargs):
        super().__init__(configuration, **kwargs)
        if (len(kwargs) > 0):
            configuration = Configuration(**kwargs)
        if (configuration is None):
            raise Exception("configuration is required")
        api_client = ApiClient(configuration)
        self.attachments: AttachmentsApi = AttachmentsApi(api_client)
        self.audit_log_api: AuditLogAPIApi = AuditLogAPIApi(api_client)
        self.batch_api: BatchAPIApi = BatchAPIApi(api_client)
        self.custom_field_settings: CustomFieldSettingsApi = CustomFieldSettingsApi(api_client)
        self.custom_fields: CustomFieldsApi = CustomFieldsApi(api_client)
        self.events: EventsApi = EventsApi(api_client)
        self.goal_relationships: GoalRelationshipsApi = GoalRelationshipsApi(api_client)
        self.goals: GoalsApi = GoalsApi(api_client)
        self.jobs: JobsApi = JobsApi(api_client)
        self.memberships: MembershipsApi = MembershipsApi(api_client)
        self.organization_exports: OrganizationExportsApi = OrganizationExportsApi(api_client)
        self.portfolio_memberships: PortfolioMembershipsApi = PortfolioMembershipsApi(api_client)
        self.portfolios: PortfoliosApi = PortfoliosApi(api_client)
        self.project_briefs: ProjectBriefsApi = ProjectBriefsApi(api_client)
        self.project_memberships: ProjectMembershipsApi = ProjectMembershipsApi(api_client)
        self.project_statuses: ProjectStatusesApi = ProjectStatusesApi(api_client)
        self.project_templates: ProjectTemplatesApi = ProjectTemplatesApi(api_client)
        self.projects: ProjectsApi = ProjectsApi(api_client)
        self.rules: RulesApi = RulesApi(api_client)
        self.sections: SectionsApi = SectionsApi(api_client)
        self.status_updates: StatusUpdatesApi = StatusUpdatesApi(api_client)
        self.stories: StoriesApi = StoriesApi(api_client)
        self.tags: TagsApi = TagsApi(api_client)
        self.task_templates: TaskTemplatesApi = TaskTemplatesApi(api_client)
        self.tasks: TasksApi = TasksApi(api_client)
        self.team_memberships: TeamMembershipsApi = TeamMembershipsApi(api_client)
        self.teams: TeamsApi = TeamsApi(api_client)
        self.time_periods: TimePeriodsApi = TimePeriodsApi(api_client)
        self.time_tracking_entries: TimeTrackingEntriesApi = TimeTrackingEntriesApi(api_client)
        self.typeahead: TypeaheadApi = TypeaheadApi(api_client)
        self.user_task_lists: UserTaskListsApi = UserTaskListsApi(api_client)
        self.users: UsersApi = UsersApi(api_client)
        self.webhooks: WebhooksApi = WebhooksApi(api_client)
        self.workspace_memberships: WorkspaceMembershipsApi = WorkspaceMembershipsApi(api_client)
        self.workspaces: WorkspacesApi = WorkspacesApi(api_client)
