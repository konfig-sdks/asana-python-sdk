# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from asana_python_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    TASKS = "Tasks"
    PROJECTS = "Projects"
    PORTFOLIOS = "Portfolios"
    GOALS = "Goals"
    CUSTOM_FIELDS = "Custom fields"
    TAGS = "Tags"
    SECTIONS = "Sections"
    TEAMS = "Teams"
    GOAL_RELATIONSHIPS = "Goal relationships"
    PROJECT_TEMPLATES = "Project templates"
    STORIES = "Stories"
    USERS = "Users"
    WEBHOOKS = "Webhooks"
    WORKSPACES = "Workspaces"
    TIME_TRACKING_ENTRIES = "Time tracking entries"
    ATTACHMENTS = "Attachments"
    PROJECT_BRIEFS = "Project briefs"
    PROJECT_STATUSES = "Project statuses"
    STATUS_UPDATES = "Status updates"
    TASK_TEMPLATES = "Task templates"
    TEAM_MEMBERSHIPS = "Team memberships"
    MEMBERSHIPS = "Memberships"
    PORTFOLIO_MEMBERSHIPS = "Portfolio memberships"
    WORKSPACE_MEMBERSHIPS = "Workspace memberships"
    CUSTOM_FIELD_SETTINGS = "Custom field settings"
    ORGANIZATION_EXPORTS = "Organization exports"
    PROJECT_MEMBERSHIPS = "Project memberships"
    TIME_PERIODS = "Time periods"
    USER_TASK_LISTS = "User task lists"
    AUDIT_LOG_API = "Audit log API"
    BATCH_API = "Batch API"
    EVENTS = "Events"
    JOBS = "Jobs"
    TYPEAHEAD = "Typeahead"
    RULES = "Rules"
