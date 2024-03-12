import typing_extensions

from asana_python_sdk.apis.tags import TagValues
from asana_python_sdk.apis.tags.tasks_api import TasksApi
from asana_python_sdk.apis.tags.projects_api import ProjectsApi
from asana_python_sdk.apis.tags.portfolios_api import PortfoliosApi
from asana_python_sdk.apis.tags.goals_api import GoalsApi
from asana_python_sdk.apis.tags.custom_fields_api import CustomFieldsApi
from asana_python_sdk.apis.tags.tags_api import TagsApi
from asana_python_sdk.apis.tags.sections_api import SectionsApi
from asana_python_sdk.apis.tags.teams_api import TeamsApi
from asana_python_sdk.apis.tags.goal_relationships_api import GoalRelationshipsApi
from asana_python_sdk.apis.tags.project_templates_api import ProjectTemplatesApi
from asana_python_sdk.apis.tags.stories_api import StoriesApi
from asana_python_sdk.apis.tags.users_api import UsersApi
from asana_python_sdk.apis.tags.webhooks_api import WebhooksApi
from asana_python_sdk.apis.tags.workspaces_api import WorkspacesApi
from asana_python_sdk.apis.tags.time_tracking_entries_api import TimeTrackingEntriesApi
from asana_python_sdk.apis.tags.attachments_api import AttachmentsApi
from asana_python_sdk.apis.tags.project_briefs_api import ProjectBriefsApi
from asana_python_sdk.apis.tags.project_statuses_api import ProjectStatusesApi
from asana_python_sdk.apis.tags.status_updates_api import StatusUpdatesApi
from asana_python_sdk.apis.tags.task_templates_api import TaskTemplatesApi
from asana_python_sdk.apis.tags.team_memberships_api import TeamMembershipsApi
from asana_python_sdk.apis.tags.memberships_api import MembershipsApi
from asana_python_sdk.apis.tags.portfolio_memberships_api import PortfolioMembershipsApi
from asana_python_sdk.apis.tags.workspace_memberships_api import WorkspaceMembershipsApi
from asana_python_sdk.apis.tags.custom_field_settings_api import CustomFieldSettingsApi
from asana_python_sdk.apis.tags.organization_exports_api import OrganizationExportsApi
from asana_python_sdk.apis.tags.project_memberships_api import ProjectMembershipsApi
from asana_python_sdk.apis.tags.time_periods_api import TimePeriodsApi
from asana_python_sdk.apis.tags.user_task_lists_api import UserTaskListsApi
from asana_python_sdk.apis.tags.audit_log_api_api import AuditLogAPIApi
from asana_python_sdk.apis.tags.batch_api_api import BatchAPIApi
from asana_python_sdk.apis.tags.events_api import EventsApi
from asana_python_sdk.apis.tags.jobs_api import JobsApi
from asana_python_sdk.apis.tags.typeahead_api import TypeaheadApi
from asana_python_sdk.apis.tags.rules_api import RulesApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.TASKS: TasksApi,
        TagValues.PROJECTS: ProjectsApi,
        TagValues.PORTFOLIOS: PortfoliosApi,
        TagValues.GOALS: GoalsApi,
        TagValues.CUSTOM_FIELDS: CustomFieldsApi,
        TagValues.TAGS: TagsApi,
        TagValues.SECTIONS: SectionsApi,
        TagValues.TEAMS: TeamsApi,
        TagValues.GOAL_RELATIONSHIPS: GoalRelationshipsApi,
        TagValues.PROJECT_TEMPLATES: ProjectTemplatesApi,
        TagValues.STORIES: StoriesApi,
        TagValues.USERS: UsersApi,
        TagValues.WEBHOOKS: WebhooksApi,
        TagValues.WORKSPACES: WorkspacesApi,
        TagValues.TIME_TRACKING_ENTRIES: TimeTrackingEntriesApi,
        TagValues.ATTACHMENTS: AttachmentsApi,
        TagValues.PROJECT_BRIEFS: ProjectBriefsApi,
        TagValues.PROJECT_STATUSES: ProjectStatusesApi,
        TagValues.STATUS_UPDATES: StatusUpdatesApi,
        TagValues.TASK_TEMPLATES: TaskTemplatesApi,
        TagValues.TEAM_MEMBERSHIPS: TeamMembershipsApi,
        TagValues.MEMBERSHIPS: MembershipsApi,
        TagValues.PORTFOLIO_MEMBERSHIPS: PortfolioMembershipsApi,
        TagValues.WORKSPACE_MEMBERSHIPS: WorkspaceMembershipsApi,
        TagValues.CUSTOM_FIELD_SETTINGS: CustomFieldSettingsApi,
        TagValues.ORGANIZATION_EXPORTS: OrganizationExportsApi,
        TagValues.PROJECT_MEMBERSHIPS: ProjectMembershipsApi,
        TagValues.TIME_PERIODS: TimePeriodsApi,
        TagValues.USER_TASK_LISTS: UserTaskListsApi,
        TagValues.AUDIT_LOG_API: AuditLogAPIApi,
        TagValues.BATCH_API: BatchAPIApi,
        TagValues.EVENTS: EventsApi,
        TagValues.JOBS: JobsApi,
        TagValues.TYPEAHEAD: TypeaheadApi,
        TagValues.RULES: RulesApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.TASKS: TasksApi,
        TagValues.PROJECTS: ProjectsApi,
        TagValues.PORTFOLIOS: PortfoliosApi,
        TagValues.GOALS: GoalsApi,
        TagValues.CUSTOM_FIELDS: CustomFieldsApi,
        TagValues.TAGS: TagsApi,
        TagValues.SECTIONS: SectionsApi,
        TagValues.TEAMS: TeamsApi,
        TagValues.GOAL_RELATIONSHIPS: GoalRelationshipsApi,
        TagValues.PROJECT_TEMPLATES: ProjectTemplatesApi,
        TagValues.STORIES: StoriesApi,
        TagValues.USERS: UsersApi,
        TagValues.WEBHOOKS: WebhooksApi,
        TagValues.WORKSPACES: WorkspacesApi,
        TagValues.TIME_TRACKING_ENTRIES: TimeTrackingEntriesApi,
        TagValues.ATTACHMENTS: AttachmentsApi,
        TagValues.PROJECT_BRIEFS: ProjectBriefsApi,
        TagValues.PROJECT_STATUSES: ProjectStatusesApi,
        TagValues.STATUS_UPDATES: StatusUpdatesApi,
        TagValues.TASK_TEMPLATES: TaskTemplatesApi,
        TagValues.TEAM_MEMBERSHIPS: TeamMembershipsApi,
        TagValues.MEMBERSHIPS: MembershipsApi,
        TagValues.PORTFOLIO_MEMBERSHIPS: PortfolioMembershipsApi,
        TagValues.WORKSPACE_MEMBERSHIPS: WorkspaceMembershipsApi,
        TagValues.CUSTOM_FIELD_SETTINGS: CustomFieldSettingsApi,
        TagValues.ORGANIZATION_EXPORTS: OrganizationExportsApi,
        TagValues.PROJECT_MEMBERSHIPS: ProjectMembershipsApi,
        TagValues.TIME_PERIODS: TimePeriodsApi,
        TagValues.USER_TASK_LISTS: UserTaskListsApi,
        TagValues.AUDIT_LOG_API: AuditLogAPIApi,
        TagValues.BATCH_API: BatchAPIApi,
        TagValues.EVENTS: EventsApi,
        TagValues.JOBS: JobsApi,
        TagValues.TYPEAHEAD: TypeaheadApi,
        TagValues.RULES: RulesApi,
    }
)
