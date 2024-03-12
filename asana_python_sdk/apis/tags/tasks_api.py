# coding: utf-8

"""
    Asana

    This is the interface for interacting with the [Asana Platform](https://developers.asana.com). Our API reference is generated from our [OpenAPI spec] (https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml).

    The version of the OpenAPI document: 1.0
    Created by: https://asana.com/support
"""

from asana_python_sdk.paths.tasks_task_gid_add_followers.post import AddFollowersToTask
from asana_python_sdk.paths.tasks_task_gid_add_project.post import AddProjectToTask
from asana_python_sdk.paths.tasks_task_gid_add_tag.post import AddTagToTask
from asana_python_sdk.paths.tasks.post import CreateNewTask
from asana_python_sdk.paths.tasks_task_gid_subtasks.post import CreateSubtaskRecord
from asana_python_sdk.paths.tasks_task_gid.delete import DeleteTask
from asana_python_sdk.paths.tasks_task_gid_duplicate.post import DuplicateTaskJob
from asana_python_sdk.paths.tasks_task_gid_dependencies.get import GetAllDependencies
from asana_python_sdk.paths.workspaces_workspace_gid_tasks_custom_id_custom_id.get import GetByCustomId
from asana_python_sdk.paths.tasks_task_gid_dependents.get import GetDependents
from asana_python_sdk.paths.tasks.get import GetMultiple
from asana_python_sdk.paths.tags_tag_gid_tasks.get import GetMultipleWithTag
from asana_python_sdk.paths.sections_section_gid_tasks.get import GetSectionTasks
from asana_python_sdk.paths.tasks_task_gid_subtasks.get import GetSubtaskList
from asana_python_sdk.paths.tasks_task_gid.get import GetTaskRecord
from asana_python_sdk.paths.projects_project_gid_tasks.get import GetTasksByProject
from asana_python_sdk.paths.user_task_lists_user_task_list_gid_tasks.get import GetUserTaskListTasks
from asana_python_sdk.paths.tasks_task_gid_remove_followers.post import RemoveFollowersFromTask
from asana_python_sdk.paths.tasks_task_gid_remove_project.post import RemoveProjectFromTask
from asana_python_sdk.paths.tasks_task_gid_remove_tag.post import RemoveTagFromTask
from asana_python_sdk.paths.workspaces_workspace_gid_tasks_search.get import SearchInWorkspace
from asana_python_sdk.paths.tasks_task_gid_add_dependencies.post import SetDependenciesForTask
from asana_python_sdk.paths.tasks_task_gid_set_parent.post import SetParentTask
from asana_python_sdk.paths.tasks_task_gid_add_dependents.post import SetTaskDependents
from asana_python_sdk.paths.tasks_task_gid_remove_dependencies.post import UnlinkDependenciesFromTask
from asana_python_sdk.paths.tasks_task_gid_remove_dependents.post import UnlinkDependents
from asana_python_sdk.paths.tasks_task_gid.put import UpdateTaskRecord
from asana_python_sdk.apis.tags.tasks_api_raw import TasksApiRaw


class TasksApi(
    AddFollowersToTask,
    AddProjectToTask,
    AddTagToTask,
    CreateNewTask,
    CreateSubtaskRecord,
    DeleteTask,
    DuplicateTaskJob,
    GetAllDependencies,
    GetByCustomId,
    GetDependents,
    GetMultiple,
    GetMultipleWithTag,
    GetSectionTasks,
    GetSubtaskList,
    GetTaskRecord,
    GetTasksByProject,
    GetUserTaskListTasks,
    RemoveFollowersFromTask,
    RemoveProjectFromTask,
    RemoveTagFromTask,
    SearchInWorkspace,
    SetDependenciesForTask,
    SetParentTask,
    SetTaskDependents,
    UnlinkDependenciesFromTask,
    UnlinkDependents,
    UpdateTaskRecord,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: TasksApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = TasksApiRaw(api_client)
