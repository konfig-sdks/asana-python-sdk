<div align="left">

[![Visit Asana](./header.png)](https://asana.com)

# Asana<a id="asana"></a>

This is the interface for interacting with the [Asana Platform](https://developers.asana.com). Our API reference is generated from our [OpenAPI spec](https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml).


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`asana.attachments.delete_specific`](#asanaattachmentsdelete_specific)
  * [`asana.attachments.get_all_for_object`](#asanaattachmentsget_all_for_object)
  * [`asana.attachments.get_attachment_record`](#asanaattachmentsget_attachment_record)
  * [`asana.attachments.upload_attachment`](#asanaattachmentsupload_attachment)
  * [`asana.audit_log_api.get_audit_log_events`](#asanaaudit_log_apiget_audit_log_events)
  * [`asana.batch_api.submit_parallel_requests`](#asanabatch_apisubmit_parallel_requests)
  * [`asana.custom_field_settings.get_portfolio_custom_field_settings`](#asanacustom_field_settingsget_portfolio_custom_field_settings)
  * [`asana.custom_field_settings.get_project_custom_field_settings`](#asanacustom_field_settingsget_project_custom_field_settings)
  * [`asana.custom_fields.add_enum_option`](#asanacustom_fieldsadd_enum_option)
  * [`asana.custom_fields.create_new_field_record`](#asanacustom_fieldscreate_new_field_record)
  * [`asana.custom_fields.delete_field_record`](#asanacustom_fieldsdelete_field_record)
  * [`asana.custom_fields.get_metadata`](#asanacustom_fieldsget_metadata)
  * [`asana.custom_fields.list_workspace_custom_fields`](#asanacustom_fieldslist_workspace_custom_fields)
  * [`asana.custom_fields.reorder_enum_option`](#asanacustom_fieldsreorder_enum_option)
  * [`asana.custom_fields.update_enum_option`](#asanacustom_fieldsupdate_enum_option)
  * [`asana.custom_fields.update_field_record`](#asanacustom_fieldsupdate_field_record)
  * [`asana.events.get_resource_events`](#asanaeventsget_resource_events)
  * [`asana.goal_relationships.create_supporting_relationship`](#asanagoal_relationshipscreate_supporting_relationship)
  * [`asana.goal_relationships.get_compact_records`](#asanagoal_relationshipsget_compact_records)
  * [`asana.goal_relationships.get_record_by_id`](#asanagoal_relationshipsget_record_by_id)
  * [`asana.goal_relationships.remove_supporting_relationship`](#asanagoal_relationshipsremove_supporting_relationship)
  * [`asana.goal_relationships.update_goal_relationship_record`](#asanagoal_relationshipsupdate_goal_relationship_record)
  * [`asana.goals.add_collaborators_to_goal`](#asanagoalsadd_collaborators_to_goal)
  * [`asana.goals.create_metric`](#asanagoalscreate_metric)
  * [`asana.goals.create_new_goal_record`](#asanagoalscreate_new_goal_record)
  * [`asana.goals.delete_record`](#asanagoalsdelete_record)
  * [`asana.goals.get_compact_records`](#asanagoalsget_compact_records)
  * [`asana.goals.get_goal_record`](#asanagoalsget_goal_record)
  * [`asana.goals.get_parent_goals`](#asanagoalsget_parent_goals)
  * [`asana.goals.remove_followers_from_goal`](#asanagoalsremove_followers_from_goal)
  * [`asana.goals.update_goal_record`](#asanagoalsupdate_goal_record)
  * [`asana.goals.update_metric_current_value`](#asanagoalsupdate_metric_current_value)
  * [`asana.jobs.get_by_id`](#asanajobsget_by_id)
  * [`asana.memberships.create_new_record`](#asanamembershipscreate_new_record)
  * [`asana.memberships.delete_record`](#asanamembershipsdelete_record)
  * [`asana.memberships.get_membership_record`](#asanamembershipsget_membership_record)
  * [`asana.memberships.get_multiple`](#asanamembershipsget_multiple)
  * [`asana.organization_exports.create_export_request`](#asanaorganization_exportscreate_export_request)
  * [`asana.organization_exports.get_export_details`](#asanaorganization_exportsget_export_details)
  * [`asana.portfolio_memberships.get_compact`](#asanaportfolio_membershipsget_compact)
  * [`asana.portfolio_memberships.get_complete_record`](#asanaportfolio_membershipsget_complete_record)
  * [`asana.portfolio_memberships.list_multiple_memberships`](#asanaportfolio_membershipslist_multiple_memberships)
  * [`asana.portfolios.add_custom_field_setting`](#asanaportfoliosadd_custom_field_setting)
  * [`asana.portfolios.add_members_to_portfolio`](#asanaportfoliosadd_members_to_portfolio)
  * [`asana.portfolios.add_portfolio_item`](#asanaportfoliosadd_portfolio_item)
  * [`asana.portfolios.create_new_portfolio_record`](#asanaportfolioscreate_new_portfolio_record)
  * [`asana.portfolios.delete_record`](#asanaportfoliosdelete_record)
  * [`asana.portfolios.get_items`](#asanaportfoliosget_items)
  * [`asana.portfolios.get_record`](#asanaportfoliosget_record)
  * [`asana.portfolios.list_multiple_portfolios`](#asanaportfolioslist_multiple_portfolios)
  * [`asana.portfolios.remove_custom_field_setting`](#asanaportfoliosremove_custom_field_setting)
  * [`asana.portfolios.remove_item_from_portfolio`](#asanaportfoliosremove_item_from_portfolio)
  * [`asana.portfolios.remove_members_from_portfolio`](#asanaportfoliosremove_members_from_portfolio)
  * [`asana.portfolios.update_portfolio_record`](#asanaportfoliosupdate_portfolio_record)
  * [`asana.project_briefs.create_new_record`](#asanaproject_briefscreate_new_record)
  * [`asana.project_briefs.get_full_record`](#asanaproject_briefsget_full_record)
  * [`asana.project_briefs.remove_brief`](#asanaproject_briefsremove_brief)
  * [`asana.project_briefs.update_brief_record`](#asanaproject_briefsupdate_brief_record)
  * [`asana.project_memberships.get_compact_records`](#asanaproject_membershipsget_compact_records)
  * [`asana.project_memberships.get_record`](#asanaproject_membershipsget_record)
  * [`asana.project_statuses.create_new_status_update_record`](#asanaproject_statusescreate_new_status_update_record)
  * [`asana.project_statuses.delete_specific_status_update`](#asanaproject_statusesdelete_specific_status_update)
  * [`asana.project_statuses.get_project_updates`](#asanaproject_statusesget_project_updates)
  * [`asana.project_statuses.get_status_update_record`](#asanaproject_statusesget_status_update_record)
  * [`asana.project_templates.delete_template_record`](#asanaproject_templatesdelete_template_record)
  * [`asana.project_templates.get_all_template_records`](#asanaproject_templatesget_all_template_records)
  * [`asana.project_templates.get_record`](#asanaproject_templatesget_record)
  * [`asana.project_templates.instantiate_project_job`](#asanaproject_templatesinstantiate_project_job)
  * [`asana.project_templates.list_multiple`](#asanaproject_templateslist_multiple)
  * [`asana.projects.add_custom_field_setting`](#asanaprojectsadd_custom_field_setting)
  * [`asana.projects.add_followers_to_project`](#asanaprojectsadd_followers_to_project)
  * [`asana.projects.add_members_to_project`](#asanaprojectsadd_members_to_project)
  * [`asana.projects.create_in_workspace`](#asanaprojectscreate_in_workspace)
  * [`asana.projects.create_new_project_record`](#asanaprojectscreate_new_project_record)
  * [`asana.projects.create_project_for_team`](#asanaprojectscreate_project_for_team)
  * [`asana.projects.create_project_template_job`](#asanaprojectscreate_project_template_job)
  * [`asana.projects.delete_project_by_id`](#asanaprojectsdelete_project_by_id)
  * [`asana.projects.duplicate_project_job`](#asanaprojectsduplicate_project_job)
  * [`asana.projects.get_all_in_workspace`](#asanaprojectsget_all_in_workspace)
  * [`asana.projects.get_project_record`](#asanaprojectsget_project_record)
  * [`asana.projects.get_task_counts`](#asanaprojectsget_task_counts)
  * [`asana.projects.get_team_projects`](#asanaprojectsget_team_projects)
  * [`asana.projects.list_multiple`](#asanaprojectslist_multiple)
  * [`asana.projects.remove_custom_field`](#asanaprojectsremove_custom_field)
  * [`asana.projects.remove_members_from_project`](#asanaprojectsremove_members_from_project)
  * [`asana.projects.remove_project_followers`](#asanaprojectsremove_project_followers)
  * [`asana.projects.task_projects_list`](#asanaprojectstask_projects_list)
  * [`asana.projects.update_project_record`](#asanaprojectsupdate_project_record)
  * [`asana.rules.trigger_rule_request`](#asanarulestrigger_rule_request)
  * [`asana.sections.add_task_to_section`](#asanasectionsadd_task_to_section)
  * [`asana.sections.create_new_section`](#asanasectionscreate_new_section)
  * [`asana.sections.delete_section`](#asanasectionsdelete_section)
  * [`asana.sections.get_record`](#asanasectionsget_record)
  * [`asana.sections.list_project_sections`](#asanasectionslist_project_sections)
  * [`asana.sections.move_or_insert`](#asanasectionsmove_or_insert)
  * [`asana.sections.update_section_record`](#asanasectionsupdate_section_record)
  * [`asana.status_updates.create_new_status_update_record`](#asanastatus_updatescreate_new_status_update_record)
  * [`asana.status_updates.delete_specific_status_update`](#asanastatus_updatesdelete_specific_status_update)
  * [`asana.status_updates.get_compact_records`](#asanastatus_updatesget_compact_records)
  * [`asana.status_updates.get_record_by_id`](#asanastatus_updatesget_record_by_id)
  * [`asana.stories.create_comment`](#asanastoriescreate_comment)
  * [`asana.stories.delete_story_record`](#asanastoriesdelete_story_record)
  * [`asana.stories.get_full_record`](#asanastoriesget_full_record)
  * [`asana.stories.get_task_stories`](#asanastoriesget_task_stories)
  * [`asana.stories.update_full_record`](#asanastoriesupdate_full_record)
  * [`asana.tags.create_new_tag_record`](#asanatagscreate_new_tag_record)
  * [`asana.tags.create_tag_in_workspace`](#asanatagscreate_tag_in_workspace)
  * [`asana.tags.get_filtered_tags`](#asanatagsget_filtered_tags)
  * [`asana.tags.get_record`](#asanatagsget_record)
  * [`asana.tags.get_task_tags`](#asanatagsget_task_tags)
  * [`asana.tags.list_filtered_tags`](#asanatagslist_filtered_tags)
  * [`asana.tags.remove_tag`](#asanatagsremove_tag)
  * [`asana.tags.update_tag_record`](#asanatagsupdate_tag_record)
  * [`asana.task_templates.delete_task_template`](#asanatask_templatesdelete_task_template)
  * [`asana.task_templates.get_single_template`](#asanatask_templatesget_single_template)
  * [`asana.task_templates.instantiate_task_job`](#asanatask_templatesinstantiate_task_job)
  * [`asana.task_templates.list_multiple`](#asanatask_templateslist_multiple)
  * [`asana.tasks.add_followers_to_task`](#asanatasksadd_followers_to_task)
  * [`asana.tasks.add_project_to_task`](#asanatasksadd_project_to_task)
  * [`asana.tasks.add_tag_to_task`](#asanatasksadd_tag_to_task)
  * [`asana.tasks.create_new_task`](#asanataskscreate_new_task)
  * [`asana.tasks.create_subtask_record`](#asanataskscreate_subtask_record)
  * [`asana.tasks.delete_task`](#asanatasksdelete_task)
  * [`asana.tasks.duplicate_task_job`](#asanatasksduplicate_task_job)
  * [`asana.tasks.get_all_dependencies`](#asanatasksget_all_dependencies)
  * [`asana.tasks.get_by_custom_id`](#asanatasksget_by_custom_id)
  * [`asana.tasks.get_dependents`](#asanatasksget_dependents)
  * [`asana.tasks.get_multiple`](#asanatasksget_multiple)
  * [`asana.tasks.get_multiple_with_tag`](#asanatasksget_multiple_with_tag)
  * [`asana.tasks.get_section_tasks`](#asanatasksget_section_tasks)
  * [`asana.tasks.get_subtask_list`](#asanatasksget_subtask_list)
  * [`asana.tasks.get_task_record`](#asanatasksget_task_record)
  * [`asana.tasks.get_tasks_by_project`](#asanatasksget_tasks_by_project)
  * [`asana.tasks.get_user_task_list_tasks`](#asanatasksget_user_task_list_tasks)
  * [`asana.tasks.remove_followers_from_task`](#asanatasksremove_followers_from_task)
  * [`asana.tasks.remove_project_from_task`](#asanatasksremove_project_from_task)
  * [`asana.tasks.remove_tag_from_task`](#asanatasksremove_tag_from_task)
  * [`asana.tasks.search_in_workspace`](#asanataskssearch_in_workspace)
  * [`asana.tasks.set_dependencies_for_task`](#asanatasksset_dependencies_for_task)
  * [`asana.tasks.set_parent_task`](#asanatasksset_parent_task)
  * [`asana.tasks.set_task_dependents`](#asanatasksset_task_dependents)
  * [`asana.tasks.unlink_dependencies_from_task`](#asanatasksunlink_dependencies_from_task)
  * [`asana.tasks.unlink_dependents`](#asanatasksunlink_dependents)
  * [`asana.tasks.update_task_record`](#asanatasksupdate_task_record)
  * [`asana.team_memberships.get_compact`](#asanateam_membershipsget_compact)
  * [`asana.team_memberships.get_compact_records`](#asanateam_membershipsget_compact_records)
  * [`asana.team_memberships.get_record_by_id`](#asanateam_membershipsget_record_by_id)
  * [`asana.team_memberships.get_user_compact`](#asanateam_membershipsget_user_compact)
  * [`asana.teams.add_user_to_team`](#asanateamsadd_user_to_team)
  * [`asana.teams.create_team_record`](#asanateamscreate_team_record)
  * [`asana.teams.get_team_record`](#asanateamsget_team_record)
  * [`asana.teams.get_user_teams`](#asanateamsget_user_teams)
  * [`asana.teams.list_workspace_teams`](#asanateamslist_workspace_teams)
  * [`asana.teams.remove_user_from_team`](#asanateamsremove_user_from_team)
  * [`asana.teams.update_team_record`](#asanateamsupdate_team_record)
  * [`asana.time_periods.get_compact_time_periods`](#asanatime_periodsget_compact_time_periods)
  * [`asana.time_periods.get_full_record`](#asanatime_periodsget_full_record)
  * [`asana.time_tracking_entries.create_new_time_entry_record`](#asanatime_tracking_entriescreate_new_time_entry_record)
  * [`asana.time_tracking_entries.delete_time_entry`](#asanatime_tracking_entriesdelete_time_entry)
  * [`asana.time_tracking_entries.get_for_task`](#asanatime_tracking_entriesget_for_task)
  * [`asana.time_tracking_entries.get_record`](#asanatime_tracking_entriesget_record)
  * [`asana.time_tracking_entries.update_time_tracking_entry`](#asanatime_tracking_entriesupdate_time_tracking_entry)
  * [`asana.typeahead.get_results`](#asanatypeaheadget_results)
  * [`asana.user_task_lists.get_record`](#asanauser_task_listsget_record)
  * [`asana.user_task_lists.get_user_task_list`](#asanauser_task_listsget_user_task_list)
  * [`asana.users.get_favorites_for_user`](#asanausersget_favorites_for_user)
  * [`asana.users.get_user_record`](#asanausersget_user_record)
  * [`asana.users.list_multiple_users`](#asanauserslist_multiple_users)
  * [`asana.users.list_team_users`](#asanauserslist_team_users)
  * [`asana.users.list_workspace_users`](#asanauserslist_workspace_users)
  * [`asana.webhooks.establish_webhook`](#asanawebhooksestablish_webhook)
  * [`asana.webhooks.get_webhook_record`](#asanawebhooksget_webhook_record)
  * [`asana.webhooks.list_multiple_webhooks`](#asanawebhookslist_multiple_webhooks)
  * [`asana.webhooks.remove_webhook`](#asanawebhooksremove_webhook)
  * [`asana.webhooks.update_webhook_filters`](#asanawebhooksupdate_webhook_filters)
  * [`asana.workspace_memberships.get_record_by_id`](#asanaworkspace_membershipsget_record_by_id)
  * [`asana.workspace_memberships.get_user_memberships`](#asanaworkspace_membershipsget_user_memberships)
  * [`asana.workspace_memberships.list_for_workspace`](#asanaworkspace_membershipslist_for_workspace)
  * [`asana.workspaces.add_user_to_workspace`](#asanaworkspacesadd_user_to_workspace)
  * [`asana.workspaces.get_workspace_record`](#asanaworkspacesget_workspace_record)
  * [`asana.workspaces.list_multiple`](#asanaworkspaceslist_multiple)
  * [`asana.workspaces.remove_user_from_workspace`](#asanaworkspacesremove_user_from_workspace)
  * [`asana.workspaces.update_workspace_record`](#asanaworkspacesupdate_workspace_record)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Asana&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from asana_python_sdk import Asana, ApiException

asana = Asana(

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',,

    access_token = 'YOUR_BEARER_TOKEN'
)

try:
    # Delete an attachment
    delete_specific_response = asana.attachments.delete_specific(
        attachment_gid="12345",
        opt_pretty=True,
    )
    print(delete_specific_response)
except ApiException as e:
    print("Exception when calling AttachmentsApi.delete_specific: %s\n" % e)
    pprint(e.body)
    if e.status == 400:
        pprint(e.body["errors"])
    if e.status == 401:
        pprint(e.body["errors"])
    if e.status == 500:
        pprint(e.body["errors"])
    if e.status == 403:
        pprint(e.body["errors"])
    if e.status == 404:
        pprint(e.body["errors"])
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python

import asyncio
from pprint import pprint
from asana_python_sdk import Asana, ApiException

asana = Asana(

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',,

    access_token = 'YOUR_BEARER_TOKEN'
)

async def main():
    try:
        # Delete an attachment
        delete_specific_response = await asana.attachments.adelete_specific(
            attachment_gid="12345",
            opt_pretty=True,
        )
        print(delete_specific_response)
    except ApiException as e:
        print("Exception when calling AttachmentsApi.delete_specific: %s\n" % e)
        pprint(e.body)
        if e.status == 400:
            pprint(e.body["errors"])
        if e.status == 401:
            pprint(e.body["errors"])
        if e.status == 500:
            pprint(e.body["errors"])
        if e.status == 403:
            pprint(e.body["errors"])
        if e.status == 404:
            pprint(e.body["errors"])
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)

asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from asana_python_sdk import Asana, ApiException

asana = Asana(

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',,

    access_token = 'YOUR_BEARER_TOKEN'
)

try:
    # Delete an attachment
    delete_specific_response = asana.attachments.raw.delete_specific(
        attachment_gid="12345",
        opt_pretty=True,
    )
    pprint(delete_specific_response.body)
    pprint(delete_specific_response.body["data"])
    pprint(delete_specific_response.headers)
    pprint(delete_specific_response.status)
    pprint(delete_specific_response.round_trip_time)
except ApiException as e:
    print("Exception when calling AttachmentsApi.delete_specific: %s\n" % e)
    pprint(e.body)
    if e.status == 400:
        pprint(e.body["errors"])
    if e.status == 401:
        pprint(e.body["errors"])
    if e.status == 500:
        pprint(e.body["errors"])
    if e.status == 403:
        pprint(e.body["errors"])
    if e.status == 404:
        pprint(e.body["errors"])
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `asana.attachments.delete_specific`<a id="asanaattachmentsdelete_specific"></a>

Deletes a specific, existing attachment.

Returns an empty data record.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_specific_response = asana.attachments.delete_specific(
    attachment_gid="12345",
    opt_pretty=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### attachment_gid: `str`<a id="attachment_gid-str"></a>

Globally unique identifier for the attachment.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

#### 🔄 Return<a id="🔄-return"></a>

[`AttachmentsDeleteSpecificResponse`](./asana_python_sdk/pydantic/attachments_delete_specific_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/attachments/{attachment_gid}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.attachments.get_all_for_object`<a id="asanaattachmentsget_all_for_object"></a>

Returns the compact records for all attachments on the object.

There are three possible `parent` values for this request: `project`, `project_brief`, and `task`. For a project, an attachment refers to a file uploaded to the "Key resources" section in the project Overview. For a project brief, an attachment refers to inline files in the project brief itself. For a task, an attachment refers to a file directly associated to that task.

Note that within the Asana app, inline images in the task description do not appear in the index of image thumbnails nor as stories in the task. However, requests made to `GET /attachments` for a task will return all of the images in the task, including inline images.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_for_object_response = asana.attachments.get_all_for_object(
    parent="159874",
    opt_pretty=True,
    limit=50,
    offset="eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9",
    opt_fields=["connected_to_app", "created_at", "download_url", "host", "name", "offset", "parent", "parent.created_by", "parent.name", "parent.resource_subtype", "path", "permanent_url", "resource_subtype", "size", "uri", "view_url"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### parent: `str`<a id="parent-str"></a>

Globally unique identifier for object to fetch statuses from. Must be a GID for a `project`, `project_brief`, or `task`.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### limit: `int`<a id="limit-int"></a>

Results per page. The number of objects to return per page. The value must be between 1 and 100.

##### offset: `str`<a id="offset-str"></a>

Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`AttachmentsGetAllForObjectResponse`](./asana_python_sdk/pydantic/attachments_get_all_for_object_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/attachments` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.attachments.get_attachment_record`<a id="asanaattachmentsget_attachment_record"></a>

Get the full record for a single attachment.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_attachment_record_response = asana.attachments.get_attachment_record(
    attachment_gid="12345",
    opt_pretty=True,
    opt_fields=["connected_to_app", "created_at", "download_url", "host", "name", "parent", "parent.created_by", "parent.name", "parent.resource_subtype", "permanent_url", "resource_subtype", "size", "view_url"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### attachment_gid: `str`<a id="attachment_gid-str"></a>

Globally unique identifier for the attachment.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`AttachmentsGetAttachmentRecordResponse`](./asana_python_sdk/pydantic/attachments_get_attachment_record_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/attachments/{attachment_gid}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.attachments.upload_attachment`<a id="asanaattachmentsupload_attachment"></a>

Upload an attachment.

This method uploads an attachment on an object and returns the compact
record for the created attachment object. This is possible by either:

- Providing the URL of the external resource being attached, or
- Downloading the file content first and then uploading it as any other attachment. Note that it is not possible to attach
files from third party services such as Dropbox, Box, Vimeo & Google Drive via the API

The 100MB size limit on attachments in Asana is enforced on this endpoint.

This endpoint expects a multipart/form-data encoded request containing the full contents of the file to be uploaded.

Requests made should follow the HTTP/1.1 specification that line
terminators are of the form `CRLF` or `\r\n` outlined
[here](http://www.w3.org/Protocols/HTTP/1.1/draft-ietf-http-v11-spec-01#Basic-Rules) in order for the server to reliably and properly handle the request.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
upload_attachment_response = asana.attachments.upload_attachment(
    parent="string_example",
    opt_pretty=True,
    opt_fields=["connected_to_app", "created_at", "download_url", "host", "name", "parent", "parent.created_by", "parent.name", "parent.resource_subtype", "permanent_url", "resource_subtype", "size", "view_url"],
    resource_subtype="external",
    file=open('/path/to/file', 'rb'),
    url="string_example",
    name="string_example",
    connect_to_app=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### parent: `str`<a id="parent-str"></a>

Required identifier of the parent task, project, or project_brief, as a string. 

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

##### resource_subtype: `str`<a id="resource_subtype-str"></a>

The type of the attachment. Must be one of the given values. If not specified, a file attachment of type `asana` will be assumed. Note that if the value of `resource_subtype` is `external`, a `parent`, `name`, and `url` must also be provided. 

##### file: `IO`<a id="file-io"></a>

Required for `asana` attachments. 

##### url: `str`<a id="url-str"></a>

The URL of the external resource being attached. Required for attachments of type `external`. 

##### name: `str`<a id="name-str"></a>

The name of the external resource being attached. Required for attachments of type `external`. 

##### connect_to_app: `bool`<a id="connect_to_app-bool"></a>

*Optional*. Only relevant for external attachments with a parent task. A boolean indicating whether the current app should be connected with the attachment for the purposes of showing an app components widget. Requires the app to have been added to a project the parent task is in. 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AttachmentRequest`](./asana_python_sdk/type/attachment_request.py)
The file you want to upload.  *Note when using curl:*  Be sure to add an `‘@’` before the file path, and use the `--form` option instead of the `-d` option.  When uploading PDFs with curl, force the content-type to be pdf by appending the content type to the file path: `--form \"file=@file.pdf;type=application/pdf\"`.

#### 🔄 Return<a id="🔄-return"></a>

[`AttachmentsUploadAttachmentResponse`](./asana_python_sdk/pydantic/attachments_upload_attachment_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/attachments` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.audit_log_api.get_audit_log_events`<a id="asanaaudit_log_apiget_audit_log_events"></a>

Retrieve the audit log events that have been captured in your domain.

This endpoint will return a list of [AuditLogEvent](https://developers.asana.com/reference/rest-api-reference) objects, sorted by creation time in ascending order. Note that the Audit Log API captures events from October 8th, 2021 and later. Queries for events before this date will not return results.

There are a number of query parameters (below) that can be used to filter the set of [AuditLogEvent](https://developers.asana.com/reference/rest-api-reference) objects that are returned in the response. Any combination of query parameters is valid. When no filters are provided, all of the events that have been captured in your domain will match.

The list of events will always be [paginated](https://developers.asana.com/reference/rest-api-reference). The default limit is 1000 events. The next set of events can be retrieved using the `offset` from the previous response. If there are no events that match the provided filters in your domain, the endpoint will return `null` for the `next_page` field. Querying again with the same filters may return new events if they were captured after the last request. Once a response includes a `next_page` with an `offset`, subsequent requests can be made with the latest `offset` to poll for new events that match the provided filters.

*Note: If the filters you provided match events in your domain and `next_page` is present in the response, we will continue to send `next_page` on subsequent requests even when there are no more events that match the filters. This was put in place so that you can implement an audit log stream that will return future events that match these filters. If you are not interested in future events that match the filters you have defined, you can rely on checking empty `data` response for the end of current events that match your filters.*

When no `offset` is provided, the response will begin with the oldest events that match the provided filters. It is important to note that [AuditLogEvent](https://developers.asana.com/reference/rest-api-reference) objects will be permanently deleted from our systems after 90 days. If you wish to keep a permanent record of these events, we recommend using a SIEM tool to ingest and store these logs.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_audit_log_events_response = asana.audit_log_api.get_audit_log_events(
    workspace_gid="12345",
    start_at="1970-01-01T00:00:00.00Z",
    end_at="1970-01-01T00:00:00.00Z",
    event_type="string_example",
    actor_type="user",
    actor_gid="string_example",
    resource_gid="string_example",
    limit=50,
    offset="eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### workspace_gid: `str`<a id="workspace_gid-str"></a>

Globally unique identifier for the workspace or organization.

##### start_at: `datetime`<a id="start_at-datetime"></a>

Filter to events created after this time (inclusive).

##### end_at: `datetime`<a id="end_at-datetime"></a>

Filter to events created before this time (exclusive).

##### event_type: `str`<a id="event_type-str"></a>

Filter to events of this type. Refer to the [supported audit log events](/docs/audit-log-events#supported-audit-log-events) for a full list of values.

##### actor_type: `str`<a id="actor_type-str"></a>

Filter to events with an actor of this type. This only needs to be included if querying for actor types without an ID. If `actor_gid` is included, this should be excluded.

##### actor_gid: `str`<a id="actor_gid-str"></a>

Filter to events triggered by the actor with this ID.

##### resource_gid: `str`<a id="resource_gid-str"></a>

Filter to events with this resource ID.

##### limit: `int`<a id="limit-int"></a>

Results per page. The number of objects to return per page. The value must be between 1 and 100.

##### offset: `str`<a id="offset-str"></a>

Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'

#### 🔄 Return<a id="🔄-return"></a>

[`AuditLogApiGetAuditLogEventsResponse`](./asana_python_sdk/pydantic/audit_log_api_get_audit_log_events_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workspaces/{workspace_gid}/audit_log_events` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.batch_api.submit_parallel_requests`<a id="asanabatch_apisubmit_parallel_requests"></a>

Make multiple requests in parallel to Asana's API.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
submit_parallel_requests_response = asana.batch_api.submit_parallel_requests(
    data={
    },
    opt_pretty=True,
    opt_fields=["body", "headers", "status_code"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### data: [`BatchRequest`](./asana_python_sdk/type/batch_request.py)<a id="data-batchrequestasana_python_sdktypebatch_requestpy"></a>


##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BatchApiSubmitParallelRequestsRequest`](./asana_python_sdk/type/batch_api_submit_parallel_requests_request.py)
The requests to batch together via the Batch API.

#### 🔄 Return<a id="🔄-return"></a>

[`BatchApiSubmitParallelRequestsResponse`](./asana_python_sdk/pydantic/batch_api_submit_parallel_requests_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/batch` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.custom_field_settings.get_portfolio_custom_field_settings`<a id="asanacustom_field_settingsget_portfolio_custom_field_settings"></a>

Returns a list of all of the custom fields settings on a portfolio, in compact form.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_portfolio_custom_field_settings_response = asana.custom_field_settings.get_portfolio_custom_field_settings(
    portfolio_gid="12345",
    opt_pretty=True,
    limit=50,
    offset="eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9",
    opt_fields=["custom_field", "custom_field.asana_created_field", "custom_field.created_by", "custom_field.created_by.name", "custom_field.currency_code", "custom_field.custom_label", "custom_field.custom_label_position", "custom_field.date_value", "custom_field.date_value.date", "custom_field.date_value.date_time", "custom_field.description", "custom_field.display_value", "custom_field.enabled", "custom_field.enum_options", "custom_field.enum_options.color", "custom_field.enum_options.enabled", "custom_field.enum_options.name", "custom_field.enum_value", "custom_field.enum_value.color", "custom_field.enum_value.enabled", "custom_field.enum_value.name", "custom_field.format", "custom_field.has_notifications_enabled", "custom_field.id_prefix", "custom_field.is_formula_field", "custom_field.is_global_to_workspace", "custom_field.is_value_read_only", "custom_field.multi_enum_values", "custom_field.multi_enum_values.color", "custom_field.multi_enum_values.enabled", "custom_field.multi_enum_values.name", "custom_field.name", "custom_field.number_value", "custom_field.people_value", "custom_field.people_value.name", "custom_field.precision", "custom_field.representation_type", "custom_field.resource_subtype", "custom_field.text_value", "custom_field.type", "is_important", "offset", "parent", "parent.name", "path", "project", "project.name", "uri"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### portfolio_gid: `str`<a id="portfolio_gid-str"></a>

Globally unique identifier for the portfolio.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### limit: `int`<a id="limit-int"></a>

Results per page. The number of objects to return per page. The value must be between 1 and 100.

##### offset: `str`<a id="offset-str"></a>

Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`CustomFieldSettingsGetPortfolioCustomFieldSettingsResponse`](./asana_python_sdk/pydantic/custom_field_settings_get_portfolio_custom_field_settings_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/portfolios/{portfolio_gid}/custom_field_settings` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.custom_field_settings.get_project_custom_field_settings`<a id="asanacustom_field_settingsget_project_custom_field_settings"></a>

Returns a list of all of the custom fields settings on a project, in compact form. Note that, as in all queries to collections which return compact representation, `opt_fields` can be used to include more data than is returned in the compact representation. See the [documentation for input/output options](https://developers.asana.com/docs/inputoutput-options) for more information.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_project_custom_field_settings_response = asana.custom_field_settings.get_project_custom_field_settings(
    project_gid="1331",
    opt_pretty=True,
    limit=50,
    offset="eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9",
    opt_fields=["custom_field", "custom_field.asana_created_field", "custom_field.created_by", "custom_field.created_by.name", "custom_field.currency_code", "custom_field.custom_label", "custom_field.custom_label_position", "custom_field.date_value", "custom_field.date_value.date", "custom_field.date_value.date_time", "custom_field.description", "custom_field.display_value", "custom_field.enabled", "custom_field.enum_options", "custom_field.enum_options.color", "custom_field.enum_options.enabled", "custom_field.enum_options.name", "custom_field.enum_value", "custom_field.enum_value.color", "custom_field.enum_value.enabled", "custom_field.enum_value.name", "custom_field.format", "custom_field.has_notifications_enabled", "custom_field.id_prefix", "custom_field.is_formula_field", "custom_field.is_global_to_workspace", "custom_field.is_value_read_only", "custom_field.multi_enum_values", "custom_field.multi_enum_values.color", "custom_field.multi_enum_values.enabled", "custom_field.multi_enum_values.name", "custom_field.name", "custom_field.number_value", "custom_field.people_value", "custom_field.people_value.name", "custom_field.precision", "custom_field.representation_type", "custom_field.resource_subtype", "custom_field.text_value", "custom_field.type", "is_important", "offset", "parent", "parent.name", "path", "project", "project.name", "uri"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_gid: `str`<a id="project_gid-str"></a>

Globally unique identifier for the project.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### limit: `int`<a id="limit-int"></a>

Results per page. The number of objects to return per page. The value must be between 1 and 100.

##### offset: `str`<a id="offset-str"></a>

Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`CustomFieldSettingsGetProjectCustomFieldSettingsResponse`](./asana_python_sdk/pydantic/custom_field_settings_get_project_custom_field_settings_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/projects/{project_gid}/custom_field_settings` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.custom_fields.add_enum_option`<a id="asanacustom_fieldsadd_enum_option"></a>

Creates an enum option and adds it to this custom field’s list of enum options. A custom field can have at most 500 enum options (including disabled options). By default new enum options are inserted at the end of a custom field’s list.
Locked custom fields can only have enum options added by the user who locked the field.
Returns the full record of the newly created enum option.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_enum_option_response = asana.custom_fields.add_enum_option(
    custom_field_gid="12345",
    data=None,
    opt_pretty=True,
    opt_fields=["color", "enabled", "name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### custom_field_gid: `str`<a id="custom_field_gid-str"></a>

Globally unique identifier for the custom field.

##### data: `EnumOptionRequest`<a id="data-enumoptionrequest"></a>

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CustomFieldsAddEnumOptionRequest`](./asana_python_sdk/type/custom_fields_add_enum_option_request.py)
The enum option object to create.

#### 🔄 Return<a id="🔄-return"></a>

[`CustomFieldsAddEnumOptionResponse`](./asana_python_sdk/pydantic/custom_fields_add_enum_option_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/custom_fields/{custom_field_gid}/enum_options` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.custom_fields.create_new_field_record`<a id="asanacustom_fieldscreate_new_field_record"></a>

Creates a new custom field in a workspace. Every custom field is required
to be created in a specific workspace, and this workspace cannot be
changed once set.

A custom field’s name must be unique within a workspace and not conflict
with names of existing task properties such as `Due Date` or `Assignee`.
A custom field’s type must be one of `text`, `enum`, `multi_enum`, `number`,
`date`, or `people`.

Returns the full record of the newly created custom field.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_field_record_response = asana.custom_fields.create_new_field_record(
    data=None,
    opt_pretty=True,
    opt_fields=["asana_created_field", "created_by", "created_by.name", "currency_code", "custom_label", "custom_label_position", "date_value", "date_value.date", "date_value.date_time", "description", "display_value", "enabled", "enum_options", "enum_options.color", "enum_options.enabled", "enum_options.name", "enum_value", "enum_value.color", "enum_value.enabled", "enum_value.name", "format", "has_notifications_enabled", "id_prefix", "is_formula_field", "is_global_to_workspace", "is_value_read_only", "multi_enum_values", "multi_enum_values.color", "multi_enum_values.enabled", "multi_enum_values.name", "name", "number_value", "people_value", "people_value.name", "precision", "representation_type", "resource_subtype", "text_value", "type"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### data: `CustomFieldRequest`<a id="data-customfieldrequest"></a>

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CustomFieldsCreateNewFieldRecordRequest`](./asana_python_sdk/type/custom_fields_create_new_field_record_request.py)
The custom field object to create.

#### 🔄 Return<a id="🔄-return"></a>

[`CustomFieldsCreateNewFieldRecordResponse`](./asana_python_sdk/pydantic/custom_fields_create_new_field_record_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/custom_fields` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.custom_fields.delete_field_record`<a id="asanacustom_fieldsdelete_field_record"></a>

A specific, existing custom field can be deleted by making a DELETE request on the URL for that custom field.
Locked custom fields can only be deleted by the user who locked the field.
Returns an empty data record.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_field_record_response = asana.custom_fields.delete_field_record(
    custom_field_gid="12345",
    opt_pretty=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### custom_field_gid: `str`<a id="custom_field_gid-str"></a>

Globally unique identifier for the custom field.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

#### 🔄 Return<a id="🔄-return"></a>

[`CustomFieldsDeleteFieldRecordResponse`](./asana_python_sdk/pydantic/custom_fields_delete_field_record_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/custom_fields/{custom_field_gid}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.custom_fields.get_metadata`<a id="asanacustom_fieldsget_metadata"></a>

Get the complete definition of a custom field’s metadata.

Since custom fields can be defined for one of a number of types, and
these types have different data and behaviors, there are fields that are
relevant to a particular type. For instance, as noted above, enum_options
is only relevant for the enum type and defines the set of choices that
the enum could represent. The examples below show some of these
type-specific custom field definitions.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_metadata_response = asana.custom_fields.get_metadata(
    custom_field_gid="12345",
    opt_pretty=True,
    opt_fields=["asana_created_field", "created_by", "created_by.name", "currency_code", "custom_label", "custom_label_position", "date_value", "date_value.date", "date_value.date_time", "description", "display_value", "enabled", "enum_options", "enum_options.color", "enum_options.enabled", "enum_options.name", "enum_value", "enum_value.color", "enum_value.enabled", "enum_value.name", "format", "has_notifications_enabled", "id_prefix", "is_formula_field", "is_global_to_workspace", "is_value_read_only", "multi_enum_values", "multi_enum_values.color", "multi_enum_values.enabled", "multi_enum_values.name", "name", "number_value", "people_value", "people_value.name", "precision", "representation_type", "resource_subtype", "text_value", "type"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### custom_field_gid: `str`<a id="custom_field_gid-str"></a>

Globally unique identifier for the custom field.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`CustomFieldsGetMetadataResponse`](./asana_python_sdk/pydantic/custom_fields_get_metadata_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/custom_fields/{custom_field_gid}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.custom_fields.list_workspace_custom_fields`<a id="asanacustom_fieldslist_workspace_custom_fields"></a>

Returns a list of the compact representation of all of the custom fields in a workspace.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_workspace_custom_fields_response = asana.custom_fields.list_workspace_custom_fields(
    workspace_gid="12345",
    opt_pretty=True,
    limit=50,
    offset="eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9",
    opt_fields=["asana_created_field", "created_by", "created_by.name", "currency_code", "custom_label", "custom_label_position", "date_value", "date_value.date", "date_value.date_time", "description", "display_value", "enabled", "enum_options", "enum_options.color", "enum_options.enabled", "enum_options.name", "enum_value", "enum_value.color", "enum_value.enabled", "enum_value.name", "format", "has_notifications_enabled", "id_prefix", "is_formula_field", "is_global_to_workspace", "is_value_read_only", "multi_enum_values", "multi_enum_values.color", "multi_enum_values.enabled", "multi_enum_values.name", "name", "number_value", "offset", "path", "people_value", "people_value.name", "precision", "representation_type", "resource_subtype", "text_value", "type", "uri"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### workspace_gid: `str`<a id="workspace_gid-str"></a>

Globally unique identifier for the workspace or organization.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### limit: `int`<a id="limit-int"></a>

Results per page. The number of objects to return per page. The value must be between 1 and 100.

##### offset: `str`<a id="offset-str"></a>

Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`CustomFieldsListWorkspaceCustomFieldsResponse`](./asana_python_sdk/pydantic/custom_fields_list_workspace_custom_fields_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workspaces/{workspace_gid}/custom_fields` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.custom_fields.reorder_enum_option`<a id="asanacustom_fieldsreorder_enum_option"></a>

Moves a particular enum option to be either before or after another specified enum option in the custom field.
Locked custom fields can only be reordered by the user who locked the field.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
reorder_enum_option_response = asana.custom_fields.reorder_enum_option(
    custom_field_gid="12345",
    data={
        "enum_option": "97285",
        "before_enum_option": "12345",
        "after_enum_option": "12345",
    },
    opt_pretty=True,
    opt_fields=["color", "enabled", "name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### custom_field_gid: `str`<a id="custom_field_gid-str"></a>

Globally unique identifier for the custom field.

##### data: [`EnumOptionInsertRequest`](./asana_python_sdk/type/enum_option_insert_request.py)<a id="data-enumoptioninsertrequestasana_python_sdktypeenum_option_insert_requestpy"></a>


##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CustomFieldsReorderEnumOptionRequest`](./asana_python_sdk/type/custom_fields_reorder_enum_option_request.py)
The enum option object to create.

#### 🔄 Return<a id="🔄-return"></a>

[`CustomFieldsReorderEnumOptionResponse`](./asana_python_sdk/pydantic/custom_fields_reorder_enum_option_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/custom_fields/{custom_field_gid}/enum_options/insert` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.custom_fields.update_enum_option`<a id="asanacustom_fieldsupdate_enum_option"></a>

Updates an existing enum option. Enum custom fields require at least one enabled enum option.
Locked custom fields can only be updated by the user who locked the field.
Returns the full record of the updated enum option.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_enum_option_response = asana.custom_fields.update_enum_option(
    enum_option_gid="124578",
    data=None,
    opt_pretty=True,
    opt_fields=["color", "enabled", "name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### enum_option_gid: `str`<a id="enum_option_gid-str"></a>

Globally unique identifier for the enum option.

##### data: [`EnumOption`](./asana_python_sdk/type/enum_option.py)<a id="data-enumoptionasana_python_sdktypeenum_optionpy"></a>


##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CustomFieldsUpdateEnumOptionRequest`](./asana_python_sdk/type/custom_fields_update_enum_option_request.py)
The enum option object to update

#### 🔄 Return<a id="🔄-return"></a>

[`CustomFieldsUpdateEnumOptionResponse`](./asana_python_sdk/pydantic/custom_fields_update_enum_option_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/enum_options/{enum_option_gid}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.custom_fields.update_field_record`<a id="asanacustom_fieldsupdate_field_record"></a>

A specific, existing custom field can be updated by making a PUT request on the URL for that custom field. Only the fields provided in the `data` block will be updated; any unspecified fields will remain unchanged
When using this method, it is best to specify only those fields you wish to change, or else you may overwrite changes made by another user since you last retrieved the custom field.
A custom field’s `type` cannot be updated.
An enum custom field’s `enum_options` cannot be updated with this endpoint. Instead see “Work With Enum Options” for information on how to update `enum_options`.
Locked custom fields can only be updated by the user who locked the field.
Returns the complete updated custom field record.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_field_record_response = asana.custom_fields.update_field_record(
    custom_field_gid="12345",
    data=None,
    opt_pretty=True,
    opt_fields=["asana_created_field", "created_by", "created_by.name", "currency_code", "custom_label", "custom_label_position", "date_value", "date_value.date", "date_value.date_time", "description", "display_value", "enabled", "enum_options", "enum_options.color", "enum_options.enabled", "enum_options.name", "enum_value", "enum_value.color", "enum_value.enabled", "enum_value.name", "format", "has_notifications_enabled", "id_prefix", "is_formula_field", "is_global_to_workspace", "is_value_read_only", "multi_enum_values", "multi_enum_values.color", "multi_enum_values.enabled", "multi_enum_values.name", "name", "number_value", "people_value", "people_value.name", "precision", "representation_type", "resource_subtype", "text_value", "type"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### custom_field_gid: `str`<a id="custom_field_gid-str"></a>

Globally unique identifier for the custom field.

##### data: `CustomFieldRequest`<a id="data-customfieldrequest"></a>

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CustomFieldsUpdateFieldRecordRequest`](./asana_python_sdk/type/custom_fields_update_field_record_request.py)
The custom field object with all updated properties.

#### 🔄 Return<a id="🔄-return"></a>

[`CustomFieldsUpdateFieldRecordResponse`](./asana_python_sdk/pydantic/custom_fields_update_field_record_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/custom_fields/{custom_field_gid}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.events.get_resource_events`<a id="asanaeventsget_resource_events"></a>

Returns the full record for all events that have occurred since the sync
token was created.

A `GET` request to the endpoint `/[path_to_resource]/events` can be made in
lieu of including the resource ID in the data for the request.

Asana limits a single sync token to 100 events. If more than 100 events exist
for a given resource, `has_more: true` will be returned in the response, indicating
that there are more events to pull.

*Note: The resource returned will be the resource that triggered the
event. This may be different from the one that the events were requested
for. For example, a subscription to a project will contain events for
tasks contained within the project.*

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_resource_events_response = asana.events.get_resource_events(
    resource="12345",
    sync="de4774f6915eae04714ca93bb2f5ee81",
    opt_pretty=True,
    opt_fields=["action", "change", "change.action", "change.added_value", "change.field", "change.new_value", "change.removed_value", "created_at", "parent", "parent.name", "resource", "resource.name", "type", "user", "user.name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### resource: `str`<a id="resource-str"></a>

A resource ID to subscribe to. The resource can be a task, project, or goal.

##### sync: `str`<a id="sync-str"></a>

A sync token received from the last request, or none on first sync. Events will be returned from the point in time that the sync token was generated. *Note: On your first request, omit the sync token. The response will be the same as for an expired sync token, and will include a new valid sync token.If the sync token is too old (which may happen from time to time) the API will return a `412 Precondition Failed` error, and include a fresh sync token in the response.*

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`EventsGetResourceEventsResponse`](./asana_python_sdk/pydantic/events_get_resource_events_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/events` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.goal_relationships.create_supporting_relationship`<a id="asanagoal_relationshipscreate_supporting_relationship"></a>

Creates a goal relationship by adding a supporting resource to a given goal.

Returns the newly created goal relationship record.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_supporting_relationship_response = asana.goal_relationships.create_supporting_relationship(
    goal_gid="12345",
    data={
        "supporting_resource": "12345",
        "insert_before": "1331",
        "insert_after": "1331",
        "contribution_weight": 1,
    },
    opt_pretty=True,
    opt_fields=["contribution_weight", "resource_subtype", "supported_goal", "supported_goal.name", "supported_goal.owner", "supported_goal.owner.name", "supporting_resource", "supporting_resource.name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### goal_gid: `str`<a id="goal_gid-str"></a>

Globally unique identifier for the goal.

##### data: [`GoalAddSupportingRelationshipRequest`](./asana_python_sdk/type/goal_add_supporting_relationship_request.py)<a id="data-goaladdsupportingrelationshiprequestasana_python_sdktypegoal_add_supporting_relationship_requestpy"></a>


##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GoalRelationshipsCreateSupportingRelationshipRequest`](./asana_python_sdk/type/goal_relationships_create_supporting_relationship_request.py)
The supporting resource to be added to the goal

#### 🔄 Return<a id="🔄-return"></a>

[`GoalRelationshipsCreateSupportingRelationshipResponse`](./asana_python_sdk/pydantic/goal_relationships_create_supporting_relationship_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/goals/{goal_gid}/addSupportingRelationship` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.goal_relationships.get_compact_records`<a id="asanagoal_relationshipsget_compact_records"></a>

Returns compact goal relationship records.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_compact_records_response = asana.goal_relationships.get_compact_records(
    supported_goal="12345",
    opt_pretty=True,
    limit=50,
    offset="eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9",
    resource_subtype="subgoal",
    opt_fields=["contribution_weight", "offset", "path", "resource_subtype", "supported_goal", "supported_goal.name", "supported_goal.owner", "supported_goal.owner.name", "supporting_resource", "supporting_resource.name", "uri"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### supported_goal: `str`<a id="supported_goal-str"></a>

Globally unique identifier for the supported goal in the goal relationship.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### limit: `int`<a id="limit-int"></a>

Results per page. The number of objects to return per page. The value must be between 1 and 100.

##### offset: `str`<a id="offset-str"></a>

Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'

##### resource_subtype: `str`<a id="resource_subtype-str"></a>

If provided, filter to goal relationships with a given resource_subtype.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`GoalRelationshipsGetCompactRecordsResponse`](./asana_python_sdk/pydantic/goal_relationships_get_compact_records_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/goal_relationships` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.goal_relationships.get_record_by_id`<a id="asanagoal_relationshipsget_record_by_id"></a>

Returns the complete updated goal relationship record for a single goal relationship.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_record_by_id_response = asana.goal_relationships.get_record_by_id(
    goal_relationship_gid="12345",
    opt_pretty=True,
    opt_fields=["contribution_weight", "resource_subtype", "supported_goal", "supported_goal.name", "supported_goal.owner", "supported_goal.owner.name", "supporting_resource", "supporting_resource.name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### goal_relationship_gid: `str`<a id="goal_relationship_gid-str"></a>

Globally unique identifier for the goal relationship.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`GoalRelationshipsGetRecordByIdResponse`](./asana_python_sdk/pydantic/goal_relationships_get_record_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/goal_relationships/{goal_relationship_gid}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.goal_relationships.remove_supporting_relationship`<a id="asanagoal_relationshipsremove_supporting_relationship"></a>

Removes a goal relationship for a given parent goal.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_supporting_relationship_response = asana.goal_relationships.remove_supporting_relationship(
    goal_gid="12345",
    data={
        "supporting_resource": "12345",
    },
    opt_pretty=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### goal_gid: `str`<a id="goal_gid-str"></a>

Globally unique identifier for the goal.

##### data: [`GoalRemoveSupportingRelationshipRequest`](./asana_python_sdk/type/goal_remove_supporting_relationship_request.py)<a id="data-goalremovesupportingrelationshiprequestasana_python_sdktypegoal_remove_supporting_relationship_requestpy"></a>


##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GoalRelationshipsRemoveSupportingRelationshipRequest`](./asana_python_sdk/type/goal_relationships_remove_supporting_relationship_request.py)
The supporting resource to be removed from the goal

#### 🔄 Return<a id="🔄-return"></a>

[`GoalRelationshipsRemoveSupportingRelationshipResponse`](./asana_python_sdk/pydantic/goal_relationships_remove_supporting_relationship_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/goals/{goal_gid}/removeSupportingRelationship` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.goal_relationships.update_goal_relationship_record`<a id="asanagoal_relationshipsupdate_goal_relationship_record"></a>

An existing goal relationship can be updated by making a PUT request on the URL for
that goal relationship. Only the fields provided in the `data` block will be updated;
any unspecified fields will remain unchanged.

Returns the complete updated goal relationship record.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_goal_relationship_record_response = asana.goal_relationships.update_goal_relationship_record(
    goal_relationship_gid="12345",
    data=None,
    opt_pretty=True,
    opt_fields=["contribution_weight", "resource_subtype", "supported_goal", "supported_goal.name", "supported_goal.owner", "supported_goal.owner.name", "supporting_resource", "supporting_resource.name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### goal_relationship_gid: `str`<a id="goal_relationship_gid-str"></a>

Globally unique identifier for the goal relationship.

##### data: `GoalRelationshipRequest`<a id="data-goalrelationshiprequest"></a>

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GoalRelationshipsUpdateGoalRelationshipRecordRequest`](./asana_python_sdk/type/goal_relationships_update_goal_relationship_record_request.py)
The updated fields for the goal relationship.

#### 🔄 Return<a id="🔄-return"></a>

[`GoalRelationshipsUpdateGoalRelationshipRecordResponse`](./asana_python_sdk/pydantic/goal_relationships_update_goal_relationship_record_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/goal_relationships/{goal_relationship_gid}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.goals.add_collaborators_to_goal`<a id="asanagoalsadd_collaborators_to_goal"></a>

Adds followers to a goal. Returns the goal the followers were added to.
Each goal can be associated with zero or more followers in the system.
Requests to add/remove followers, if successful, will return the complete updated goal record, described above.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_collaborators_to_goal_response = asana.goals.add_collaborators_to_goal(
    goal_gid="12345",
    data={
        "followers": ["13579", "321654"],
    },
    opt_pretty=True,
    opt_fields=["current_status_update", "current_status_update.resource_subtype", "current_status_update.title", "due_on", "followers", "followers.name", "html_notes", "is_workspace_level", "liked", "likes", "likes.user", "likes.user.name", "metric", "metric.can_manage", "metric.currency_code", "metric.current_display_value", "metric.current_number_value", "metric.initial_number_value", "metric.precision", "metric.progress_source", "metric.resource_subtype", "metric.target_number_value", "metric.unit", "name", "notes", "num_likes", "owner", "owner.name", "start_on", "status", "team", "team.name", "time_period", "time_period.display_name", "time_period.end_on", "time_period.period", "time_period.start_on", "workspace", "workspace.name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### goal_gid: `str`<a id="goal_gid-str"></a>

Globally unique identifier for the goal.

##### data: [`TaskAddFollowersRequest`](./asana_python_sdk/type/task_add_followers_request.py)<a id="data-taskaddfollowersrequestasana_python_sdktypetask_add_followers_requestpy"></a>


##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GoalsAddCollaboratorsToGoalRequest`](./asana_python_sdk/type/goals_add_collaborators_to_goal_request.py)
The followers to be added as collaborators

#### 🔄 Return<a id="🔄-return"></a>

[`GoalsAddCollaboratorsToGoalResponse`](./asana_python_sdk/pydantic/goals_add_collaborators_to_goal_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/goals/{goal_gid}/addFollowers` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.goals.create_metric`<a id="asanagoalscreate_metric"></a>

Creates and adds a goal metric to a specified goal. Note that this replaces an existing goal metric if one already exists.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_metric_response = asana.goals.create_metric(
    goal_gid="12345",
    data=None,
    opt_pretty=True,
    opt_fields=["current_status_update", "current_status_update.resource_subtype", "current_status_update.title", "due_on", "followers", "followers.name", "html_notes", "is_workspace_level", "liked", "likes", "likes.user", "likes.user.name", "metric", "metric.can_manage", "metric.currency_code", "metric.current_display_value", "metric.current_number_value", "metric.initial_number_value", "metric.precision", "metric.progress_source", "metric.resource_subtype", "metric.target_number_value", "metric.unit", "name", "notes", "num_likes", "owner", "owner.name", "start_on", "status", "team", "team.name", "time_period", "time_period.display_name", "time_period.end_on", "time_period.period", "time_period.start_on", "workspace", "workspace.name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### goal_gid: `str`<a id="goal_gid-str"></a>

Globally unique identifier for the goal.

##### data: [`GoalMetricBase`](./asana_python_sdk/type/goal_metric_base.py)<a id="data-goalmetricbaseasana_python_sdktypegoal_metric_basepy"></a>


##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GoalsCreateMetricRequest`](./asana_python_sdk/type/goals_create_metric_request.py)
The goal metric to create.

#### 🔄 Return<a id="🔄-return"></a>

[`GoalsCreateMetricResponse`](./asana_python_sdk/pydantic/goals_create_metric_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/goals/{goal_gid}/setMetric` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.goals.create_new_goal_record`<a id="asanagoalscreate_new_goal_record"></a>

Creates a new goal in a workspace or team.

Returns the full record of the newly created goal.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_goal_record_response = asana.goals.create_new_goal_record(
    data=None,
    opt_pretty=True,
    opt_fields=["current_status_update", "current_status_update.resource_subtype", "current_status_update.title", "due_on", "followers", "followers.name", "html_notes", "is_workspace_level", "liked", "likes", "likes.user", "likes.user.name", "metric", "metric.can_manage", "metric.currency_code", "metric.current_display_value", "metric.current_number_value", "metric.initial_number_value", "metric.precision", "metric.progress_source", "metric.resource_subtype", "metric.target_number_value", "metric.unit", "name", "notes", "num_likes", "owner", "owner.name", "start_on", "status", "team", "team.name", "time_period", "time_period.display_name", "time_period.end_on", "time_period.period", "time_period.start_on", "workspace", "workspace.name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### data: `GoalRequest`<a id="data-goalrequest"></a>

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GoalsCreateNewGoalRecordRequest`](./asana_python_sdk/type/goals_create_new_goal_record_request.py)
The goal to create.

#### 🔄 Return<a id="🔄-return"></a>

[`GoalsCreateNewGoalRecordResponse`](./asana_python_sdk/pydantic/goals_create_new_goal_record_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/goals` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.goals.delete_record`<a id="asanagoalsdelete_record"></a>

A specific, existing goal can be deleted by making a DELETE request on the URL for that goal.

Returns an empty data record.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_record_response = asana.goals.delete_record(
    goal_gid="12345",
    opt_pretty=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### goal_gid: `str`<a id="goal_gid-str"></a>

Globally unique identifier for the goal.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

#### 🔄 Return<a id="🔄-return"></a>

[`GoalsDeleteRecordResponse`](./asana_python_sdk/pydantic/goals_delete_record_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/goals/{goal_gid}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.goals.get_compact_records`<a id="asanagoalsget_compact_records"></a>

Returns compact goal records.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_compact_records_response = asana.goals.get_compact_records(
    opt_pretty=True,
    portfolio="159874",
    project="512241",
    task="78424",
    is_workspace_level=False,
    team="31326",
    workspace="31326",
    time_periods=[
        "221693,506165"
    ],
    limit=50,
    offset="eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9",
    opt_fields=["current_status_update", "current_status_update.resource_subtype", "current_status_update.title", "due_on", "followers", "followers.name", "html_notes", "is_workspace_level", "liked", "likes", "likes.user", "likes.user.name", "metric", "metric.can_manage", "metric.currency_code", "metric.current_display_value", "metric.current_number_value", "metric.initial_number_value", "metric.precision", "metric.progress_source", "metric.resource_subtype", "metric.target_number_value", "metric.unit", "name", "notes", "num_likes", "offset", "owner", "owner.name", "path", "start_on", "status", "team", "team.name", "time_period", "time_period.display_name", "time_period.end_on", "time_period.period", "time_period.start_on", "uri", "workspace", "workspace.name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### portfolio: `str`<a id="portfolio-str"></a>

Globally unique identifier for supporting portfolio.

##### project: `str`<a id="project-str"></a>

Globally unique identifier for supporting project.

##### task: `str`<a id="task-str"></a>

Globally unique identifier for supporting task.

##### is_workspace_level: `bool`<a id="is_workspace_level-bool"></a>

Filter to goals with is_workspace_level set to query value. Must be used with the workspace parameter.

##### team: `str`<a id="team-str"></a>

Globally unique identifier for the team.

##### workspace: `str`<a id="workspace-str"></a>

Globally unique identifier for the workspace.

##### time_periods: List[`str`]<a id="time_periods-liststr"></a>

Globally unique identifiers for the time periods.

##### limit: `int`<a id="limit-int"></a>

Results per page. The number of objects to return per page. The value must be between 1 and 100.

##### offset: `str`<a id="offset-str"></a>

Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`GoalsGetCompactRecordsResponse`](./asana_python_sdk/pydantic/goals_get_compact_records_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/goals` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.goals.get_goal_record`<a id="asanagoalsget_goal_record"></a>

Returns the complete goal record for a single goal.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_goal_record_response = asana.goals.get_goal_record(
    goal_gid="12345",
    opt_pretty=True,
    opt_fields=["current_status_update", "current_status_update.resource_subtype", "current_status_update.title", "due_on", "followers", "followers.name", "html_notes", "is_workspace_level", "liked", "likes", "likes.user", "likes.user.name", "metric", "metric.can_manage", "metric.currency_code", "metric.current_display_value", "metric.current_number_value", "metric.initial_number_value", "metric.precision", "metric.progress_source", "metric.resource_subtype", "metric.target_number_value", "metric.unit", "name", "notes", "num_likes", "owner", "owner.name", "start_on", "status", "team", "team.name", "time_period", "time_period.display_name", "time_period.end_on", "time_period.period", "time_period.start_on", "workspace", "workspace.name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### goal_gid: `str`<a id="goal_gid-str"></a>

Globally unique identifier for the goal.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`GoalsGetGoalRecordResponse`](./asana_python_sdk/pydantic/goals_get_goal_record_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/goals/{goal_gid}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.goals.get_parent_goals`<a id="asanagoalsget_parent_goals"></a>

Returns a compact representation of all of the parent goals of a goal.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_parent_goals_response = asana.goals.get_parent_goals(
    goal_gid="12345",
    opt_pretty=True,
    opt_fields=["current_status_update", "current_status_update.resource_subtype", "current_status_update.title", "due_on", "followers", "followers.name", "html_notes", "is_workspace_level", "liked", "likes", "likes.user", "likes.user.name", "metric", "metric.can_manage", "metric.currency_code", "metric.current_display_value", "metric.current_number_value", "metric.initial_number_value", "metric.precision", "metric.progress_source", "metric.resource_subtype", "metric.target_number_value", "metric.unit", "name", "notes", "num_likes", "owner", "owner.name", "start_on", "status", "team", "team.name", "time_period", "time_period.display_name", "time_period.end_on", "time_period.period", "time_period.start_on", "workspace", "workspace.name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### goal_gid: `str`<a id="goal_gid-str"></a>

Globally unique identifier for the goal.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`GoalsGetParentGoalsResponse`](./asana_python_sdk/pydantic/goals_get_parent_goals_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/goals/{goal_gid}/parentGoals` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.goals.remove_followers_from_goal`<a id="asanagoalsremove_followers_from_goal"></a>

Removes followers from a goal. Returns the goal the followers were removed from.
Each goal can be associated with zero or more followers in the system.
Requests to add/remove followers, if successful, will return the complete updated goal record, described above.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_followers_from_goal_response = asana.goals.remove_followers_from_goal(
    goal_gid="12345",
    data={
        "followers": ["13579", "321654"],
    },
    opt_pretty=True,
    opt_fields=["current_status_update", "current_status_update.resource_subtype", "current_status_update.title", "due_on", "followers", "followers.name", "html_notes", "is_workspace_level", "liked", "likes", "likes.user", "likes.user.name", "metric", "metric.can_manage", "metric.currency_code", "metric.current_display_value", "metric.current_number_value", "metric.initial_number_value", "metric.precision", "metric.progress_source", "metric.resource_subtype", "metric.target_number_value", "metric.unit", "name", "notes", "num_likes", "owner", "owner.name", "start_on", "status", "team", "team.name", "time_period", "time_period.display_name", "time_period.end_on", "time_period.period", "time_period.start_on", "workspace", "workspace.name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### goal_gid: `str`<a id="goal_gid-str"></a>

Globally unique identifier for the goal.

##### data: [`TaskAddFollowersRequest`](./asana_python_sdk/type/task_add_followers_request.py)<a id="data-taskaddfollowersrequestasana_python_sdktypetask_add_followers_requestpy"></a>


##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GoalsRemoveFollowersFromGoalRequest`](./asana_python_sdk/type/goals_remove_followers_from_goal_request.py)
The followers to be removed as collaborators

#### 🔄 Return<a id="🔄-return"></a>

[`GoalsRemoveFollowersFromGoalResponse`](./asana_python_sdk/pydantic/goals_remove_followers_from_goal_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/goals/{goal_gid}/removeFollowers` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.goals.update_goal_record`<a id="asanagoalsupdate_goal_record"></a>

An existing goal can be updated by making a PUT request on the URL for
that goal. Only the fields provided in the `data` block will be updated;
any unspecified fields will remain unchanged.

Returns the complete updated goal record.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_goal_record_response = asana.goals.update_goal_record(
    goal_gid="12345",
    data=None,
    opt_pretty=True,
    opt_fields=["current_status_update", "current_status_update.resource_subtype", "current_status_update.title", "due_on", "followers", "followers.name", "html_notes", "is_workspace_level", "liked", "likes", "likes.user", "likes.user.name", "metric", "metric.can_manage", "metric.currency_code", "metric.current_display_value", "metric.current_number_value", "metric.initial_number_value", "metric.precision", "metric.progress_source", "metric.resource_subtype", "metric.target_number_value", "metric.unit", "name", "notes", "num_likes", "owner", "owner.name", "start_on", "status", "team", "team.name", "time_period", "time_period.display_name", "time_period.end_on", "time_period.period", "time_period.start_on", "workspace", "workspace.name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### goal_gid: `str`<a id="goal_gid-str"></a>

Globally unique identifier for the goal.

##### data: `GoalUpdateRequest`<a id="data-goalupdaterequest"></a>

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GoalsUpdateGoalRecordRequest`](./asana_python_sdk/type/goals_update_goal_record_request.py)
The updated fields for the goal.

#### 🔄 Return<a id="🔄-return"></a>

[`GoalsUpdateGoalRecordResponse`](./asana_python_sdk/pydantic/goals_update_goal_record_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/goals/{goal_gid}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.goals.update_metric_current_value`<a id="asanagoalsupdate_metric_current_value"></a>

Updates a goal's existing metric's `current_number_value` if one exists,
otherwise responds with a 400 status code.

Returns the complete updated goal metric record.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_metric_current_value_response = asana.goals.update_metric_current_value(
    goal_gid="12345",
    data=None,
    opt_pretty=True,
    opt_fields=["current_status_update", "current_status_update.resource_subtype", "current_status_update.title", "due_on", "followers", "followers.name", "html_notes", "is_workspace_level", "liked", "likes", "likes.user", "likes.user.name", "metric", "metric.can_manage", "metric.currency_code", "metric.current_display_value", "metric.current_number_value", "metric.initial_number_value", "metric.precision", "metric.progress_source", "metric.resource_subtype", "metric.target_number_value", "metric.unit", "name", "notes", "num_likes", "owner", "owner.name", "start_on", "status", "team", "team.name", "time_period", "time_period.display_name", "time_period.end_on", "time_period.period", "time_period.start_on", "workspace", "workspace.name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### goal_gid: `str`<a id="goal_gid-str"></a>

Globally unique identifier for the goal.

##### data: [`GoalMetricCurrentValueRequest`](./asana_python_sdk/type/goal_metric_current_value_request.py)<a id="data-goalmetriccurrentvaluerequestasana_python_sdktypegoal_metric_current_value_requestpy"></a>


##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GoalsUpdateMetricCurrentValueRequest`](./asana_python_sdk/type/goals_update_metric_current_value_request.py)
The updated fields for the goal metric.

#### 🔄 Return<a id="🔄-return"></a>

[`GoalsUpdateMetricCurrentValueResponse`](./asana_python_sdk/pydantic/goals_update_metric_current_value_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/goals/{goal_gid}/setMetricCurrentValue` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.jobs.get_by_id`<a id="asanajobsget_by_id"></a>

Returns the full record for a job.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = asana.jobs.get_by_id(
    job_gid="12345",
    opt_pretty=True,
    opt_fields=["new_project", "new_project.name", "new_project_template", "new_project_template.name", "new_task", "new_task.created_by", "new_task.name", "new_task.resource_subtype", "new_task_template", "new_task_template.name", "resource_subtype", "status"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### job_gid: `str`<a id="job_gid-str"></a>

Globally unique identifier for the job.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`JobsGetByIdResponse`](./asana_python_sdk/pydantic/jobs_get_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/jobs/{job_gid}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.memberships.create_new_record`<a id="asanamembershipscreate_new_record"></a>

Creates a new membership in a `goal` or `project`. `Teams` or `users` can be a member
of `goals` or `projects`.

Returns the full record of the newly created membership.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_record_response = asana.memberships.create_new_record(
    data=None,
    opt_pretty=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### data: [`CreateMembershipRequest`](./asana_python_sdk/type/create_membership_request.py)<a id="data-createmembershiprequestasana_python_sdktypecreate_membership_requestpy"></a>


##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MembershipsCreateNewRecordRequest`](./asana_python_sdk/type/memberships_create_new_record_request.py)
The updated fields for the membership.

#### 🔄 Return<a id="🔄-return"></a>

[`MembershipsCreateNewRecordResponse`](./asana_python_sdk/pydantic/memberships_create_new_record_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/memberships` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.memberships.delete_record`<a id="asanamembershipsdelete_record"></a>

A specific, existing membership for a `goal` or `project` can be deleted by making a `DELETE` request
on the URL for that membership.

Returns an empty data record.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_record_response = asana.memberships.delete_record(
    membership_gid="12345",
    opt_pretty=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### membership_gid: `str`<a id="membership_gid-str"></a>

Globally unique identifier for the membership.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

#### 🔄 Return<a id="🔄-return"></a>

[`MembershipsDeleteRecordResponse`](./asana_python_sdk/pydantic/memberships_delete_record_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/memberships/{membership_gid}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.memberships.get_membership_record`<a id="asanamembershipsget_membership_record"></a>

Returns compact `project_membership` record for a single membership. `GET` only supports project memberships currently

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_membership_record_response = asana.memberships.get_membership_record(
    membership_gid="12345",
    opt_pretty=True,
    opt_fields=["access_level", "member", "member.name", "parent", "parent.name", "resource_subtype"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### membership_gid: `str`<a id="membership_gid-str"></a>

Globally unique identifier for the membership.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`MembershipsGetMembershipRecordResponse`](./asana_python_sdk/pydantic/memberships_get_membership_record_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/memberships/{membership_gid}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.memberships.get_multiple`<a id="asanamembershipsget_multiple"></a>

Returns compact `goal_membership` or `project_membership` records. The possible types for `parent` in this request are `goal` or `project`. An additional member (user GID or team GID) can be passed in to filter to a specific membership.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_multiple_response = asana.memberships.get_multiple(
    opt_pretty=True,
    parent="159874",
    member="1061493",
    limit=50,
    offset="eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9",
    opt_fields=["offset", "path", "uri"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### parent: `str`<a id="parent-str"></a>

Globally unique identifier for `goal` or `project`.

##### member: `str`<a id="member-str"></a>

Globally unique identifier for `team` or `user`.

##### limit: `int`<a id="limit-int"></a>

Results per page. The number of objects to return per page. The value must be between 1 and 100.

##### offset: `str`<a id="offset-str"></a>

Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`MembershipsGetMultipleResponse`](./asana_python_sdk/pydantic/memberships_get_multiple_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/memberships` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.organization_exports.create_export_request`<a id="asanaorganization_exportscreate_export_request"></a>

This method creates a request to export an Organization. Asana will complete the export at some point after you create the request.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_export_request_response = asana.organization_exports.create_export_request(
    data={
        "organization": "1331",
    },
    opt_pretty=True,
    opt_fields=["created_at", "download_url", "organization", "organization.name", "state"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### data: [`OrganizationExportRequest`](./asana_python_sdk/type/organization_export_request.py)<a id="data-organizationexportrequestasana_python_sdktypeorganization_export_requestpy"></a>


##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`OrganizationExportsCreateExportRequestRequest`](./asana_python_sdk/type/organization_exports_create_export_request_request.py)
The organization to export.

#### 🔄 Return<a id="🔄-return"></a>

[`OrganizationExportsCreateExportRequestResponse`](./asana_python_sdk/pydantic/organization_exports_create_export_request_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/organization_exports` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.organization_exports.get_export_details`<a id="asanaorganization_exportsget_export_details"></a>

Returns details of a previously-requested Organization export.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_export_details_response = asana.organization_exports.get_export_details(
    organization_export_gid="12345",
    opt_pretty=True,
    opt_fields=["created_at", "download_url", "organization", "organization.name", "state"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### organization_export_gid: `str`<a id="organization_export_gid-str"></a>

Globally unique identifier for the organization export.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`OrganizationExportsGetExportDetailsResponse`](./asana_python_sdk/pydantic/organization_exports_get_export_details_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/organization_exports/{organization_export_gid}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.portfolio_memberships.get_compact`<a id="asanaportfolio_membershipsget_compact"></a>

Returns the compact portfolio membership records for the portfolio.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_compact_response = asana.portfolio_memberships.get_compact(
    portfolio_gid="12345",
    user="me",
    opt_pretty=True,
    limit=50,
    offset="eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9",
    opt_fields=["offset", "path", "portfolio", "portfolio.name", "uri", "user", "user.name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### portfolio_gid: `str`<a id="portfolio_gid-str"></a>

Globally unique identifier for the portfolio.

##### user: `str`<a id="user-str"></a>

A string identifying a user. This can either be the string \"me\", an email, or the gid of a user.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### limit: `int`<a id="limit-int"></a>

Results per page. The number of objects to return per page. The value must be between 1 and 100.

##### offset: `str`<a id="offset-str"></a>

Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`PortfolioMembershipsGetCompactResponse`](./asana_python_sdk/pydantic/portfolio_memberships_get_compact_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/portfolios/{portfolio_gid}/portfolio_memberships` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.portfolio_memberships.get_complete_record`<a id="asanaportfolio_membershipsget_complete_record"></a>

Returns the complete portfolio record for a single portfolio membership.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_complete_record_response = asana.portfolio_memberships.get_complete_record(
    portfolio_membership_gid="1331",
    opt_pretty=True,
    opt_fields=["portfolio", "portfolio.name", "user", "user.name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### portfolio_membership_gid: `str`<a id="portfolio_membership_gid-str"></a>

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`PortfolioMembershipsGetCompleteRecordResponse`](./asana_python_sdk/pydantic/portfolio_memberships_get_complete_record_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/portfolio_memberships/{portfolio_membership_gid}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.portfolio_memberships.list_multiple_memberships`<a id="asanaportfolio_membershipslist_multiple_memberships"></a>

Returns a list of portfolio memberships in compact representation. You must specify `portfolio`, `portfolio` and `user`, or `workspace` and `user`.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_multiple_memberships_response = asana.portfolio_memberships.list_multiple_memberships(
    portfolio="12345",
    workspace="12345",
    user="me",
    opt_pretty=True,
    limit=50,
    offset="eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9",
    opt_fields=["offset", "path", "portfolio", "portfolio.name", "uri", "user", "user.name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### portfolio: `str`<a id="portfolio-str"></a>

The portfolio to filter results on.

##### workspace: `str`<a id="workspace-str"></a>

The workspace to filter results on.

##### user: `str`<a id="user-str"></a>

A string identifying a user. This can either be the string \"me\", an email, or the gid of a user.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### limit: `int`<a id="limit-int"></a>

Results per page. The number of objects to return per page. The value must be between 1 and 100.

##### offset: `str`<a id="offset-str"></a>

Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`PortfolioMembershipsListMultipleMembershipsResponse`](./asana_python_sdk/pydantic/portfolio_memberships_list_multiple_memberships_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/portfolio_memberships` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.portfolios.add_custom_field_setting`<a id="asanaportfoliosadd_custom_field_setting"></a>

Custom fields are associated with portfolios by way of custom field settings.  This method creates a setting for the portfolio.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_custom_field_setting_response = asana.portfolios.add_custom_field_setting(
    portfolio_gid="12345",
    data={
        "custom_field": "14916",
        "is_important": True,
        "insert_before": "1331",
        "insert_after": "1331",
    },
    opt_pretty=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### portfolio_gid: `str`<a id="portfolio_gid-str"></a>

Globally unique identifier for the portfolio.

##### data: [`AddCustomFieldSettingRequest`](./asana_python_sdk/type/add_custom_field_setting_request.py)<a id="data-addcustomfieldsettingrequestasana_python_sdktypeadd_custom_field_setting_requestpy"></a>


##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PortfoliosAddCustomFieldSettingRequest`](./asana_python_sdk/type/portfolios_add_custom_field_setting_request.py)
Information about the custom field setting.

#### 🔄 Return<a id="🔄-return"></a>

[`PortfoliosAddCustomFieldSettingResponse`](./asana_python_sdk/pydantic/portfolios_add_custom_field_setting_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/portfolios/{portfolio_gid}/addCustomFieldSetting` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.portfolios.add_members_to_portfolio`<a id="asanaportfoliosadd_members_to_portfolio"></a>

Adds the specified list of users as members of the portfolio.
Returns the updated portfolio record.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_members_to_portfolio_response = asana.portfolios.add_members_to_portfolio(
    portfolio_gid="12345",
    data={
        "members": "521621,621373",
    },
    opt_pretty=True,
    opt_fields=["color", "created_at", "created_by", "created_by.name", "current_status_update", "current_status_update.resource_subtype", "current_status_update.title", "custom_field_settings", "custom_field_settings.custom_field", "custom_field_settings.custom_field.asana_created_field", "custom_field_settings.custom_field.created_by", "custom_field_settings.custom_field.created_by.name", "custom_field_settings.custom_field.currency_code", "custom_field_settings.custom_field.custom_label", "custom_field_settings.custom_field.custom_label_position", "custom_field_settings.custom_field.date_value", "custom_field_settings.custom_field.date_value.date", "custom_field_settings.custom_field.date_value.date_time", "custom_field_settings.custom_field.description", "custom_field_settings.custom_field.display_value", "custom_field_settings.custom_field.enabled", "custom_field_settings.custom_field.enum_options", "custom_field_settings.custom_field.enum_options.color", "custom_field_settings.custom_field.enum_options.enabled", "custom_field_settings.custom_field.enum_options.name", "custom_field_settings.custom_field.enum_value", "custom_field_settings.custom_field.enum_value.color", "custom_field_settings.custom_field.enum_value.enabled", "custom_field_settings.custom_field.enum_value.name", "custom_field_settings.custom_field.format", "custom_field_settings.custom_field.has_notifications_enabled", "custom_field_settings.custom_field.id_prefix", "custom_field_settings.custom_field.is_formula_field", "custom_field_settings.custom_field.is_global_to_workspace", "custom_field_settings.custom_field.is_value_read_only", "custom_field_settings.custom_field.multi_enum_values", "custom_field_settings.custom_field.multi_enum_values.color", "custom_field_settings.custom_field.multi_enum_values.enabled", "custom_field_settings.custom_field.multi_enum_values.name", "custom_field_settings.custom_field.name", "custom_field_settings.custom_field.number_value", "custom_field_settings.custom_field.people_value", "custom_field_settings.custom_field.people_value.name", "custom_field_settings.custom_field.precision", "custom_field_settings.custom_field.representation_type", "custom_field_settings.custom_field.resource_subtype", "custom_field_settings.custom_field.text_value", "custom_field_settings.custom_field.type", "custom_field_settings.is_important", "custom_field_settings.parent", "custom_field_settings.parent.name", "custom_field_settings.project", "custom_field_settings.project.name", "custom_fields", "custom_fields.date_value", "custom_fields.date_value.date", "custom_fields.date_value.date_time", "custom_fields.display_value", "custom_fields.enabled", "custom_fields.enum_options", "custom_fields.enum_options.color", "custom_fields.enum_options.enabled", "custom_fields.enum_options.name", "custom_fields.enum_value", "custom_fields.enum_value.color", "custom_fields.enum_value.enabled", "custom_fields.enum_value.name", "custom_fields.id_prefix", "custom_fields.is_formula_field", "custom_fields.multi_enum_values", "custom_fields.multi_enum_values.color", "custom_fields.multi_enum_values.enabled", "custom_fields.multi_enum_values.name", "custom_fields.name", "custom_fields.number_value", "custom_fields.representation_type", "custom_fields.resource_subtype", "custom_fields.text_value", "custom_fields.type", "due_on", "members", "members.name", "name", "owner", "owner.name", "permalink_url", "project_templates", "project_templates.name", "public", "start_on", "workspace", "workspace.name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### portfolio_gid: `str`<a id="portfolio_gid-str"></a>

Globally unique identifier for the portfolio.

##### data: [`AddMembersRequest`](./asana_python_sdk/type/add_members_request.py)<a id="data-addmembersrequestasana_python_sdktypeadd_members_requestpy"></a>


##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PortfoliosAddMembersToPortfolioRequest`](./asana_python_sdk/type/portfolios_add_members_to_portfolio_request.py)
Information about the members being added.

#### 🔄 Return<a id="🔄-return"></a>

[`PortfoliosAddMembersToPortfolioResponse`](./asana_python_sdk/pydantic/portfolios_add_members_to_portfolio_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/portfolios/{portfolio_gid}/addMembers` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.portfolios.add_portfolio_item`<a id="asanaportfoliosadd_portfolio_item"></a>

Add an item to a portfolio.
Returns an empty data block.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_portfolio_item_response = asana.portfolios.add_portfolio_item(
    portfolio_gid="12345",
    data={
        "item": "1331",
        "insert_before": "1331",
        "insert_after": "1331",
    },
    opt_pretty=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### portfolio_gid: `str`<a id="portfolio_gid-str"></a>

Globally unique identifier for the portfolio.

##### data: [`PortfolioAddItemRequest`](./asana_python_sdk/type/portfolio_add_item_request.py)<a id="data-portfolioadditemrequestasana_python_sdktypeportfolio_add_item_requestpy"></a>


##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PortfoliosAddPortfolioItemRequest`](./asana_python_sdk/type/portfolios_add_portfolio_item_request.py)
Information about the item being inserted.

#### 🔄 Return<a id="🔄-return"></a>

[`PortfoliosAddPortfolioItemResponse`](./asana_python_sdk/pydantic/portfolios_add_portfolio_item_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/portfolios/{portfolio_gid}/addItem` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.portfolios.create_new_portfolio_record`<a id="asanaportfolioscreate_new_portfolio_record"></a>

Creates a new portfolio in the given workspace with the supplied name.

Note that portfolios created in the Asana UI may have some state
(like the “Priority” custom field) which is automatically added
to the portfolio when it is created. Portfolios created via our
API will *not* be created with the same initial state to allow
integrations to create their own starting state on a portfolio.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_portfolio_record_response = asana.portfolios.create_new_portfolio_record(
    data=None,
    opt_pretty=True,
    opt_fields=["color", "created_at", "created_by", "created_by.name", "current_status_update", "current_status_update.resource_subtype", "current_status_update.title", "custom_field_settings", "custom_field_settings.custom_field", "custom_field_settings.custom_field.asana_created_field", "custom_field_settings.custom_field.created_by", "custom_field_settings.custom_field.created_by.name", "custom_field_settings.custom_field.currency_code", "custom_field_settings.custom_field.custom_label", "custom_field_settings.custom_field.custom_label_position", "custom_field_settings.custom_field.date_value", "custom_field_settings.custom_field.date_value.date", "custom_field_settings.custom_field.date_value.date_time", "custom_field_settings.custom_field.description", "custom_field_settings.custom_field.display_value", "custom_field_settings.custom_field.enabled", "custom_field_settings.custom_field.enum_options", "custom_field_settings.custom_field.enum_options.color", "custom_field_settings.custom_field.enum_options.enabled", "custom_field_settings.custom_field.enum_options.name", "custom_field_settings.custom_field.enum_value", "custom_field_settings.custom_field.enum_value.color", "custom_field_settings.custom_field.enum_value.enabled", "custom_field_settings.custom_field.enum_value.name", "custom_field_settings.custom_field.format", "custom_field_settings.custom_field.has_notifications_enabled", "custom_field_settings.custom_field.id_prefix", "custom_field_settings.custom_field.is_formula_field", "custom_field_settings.custom_field.is_global_to_workspace", "custom_field_settings.custom_field.is_value_read_only", "custom_field_settings.custom_field.multi_enum_values", "custom_field_settings.custom_field.multi_enum_values.color", "custom_field_settings.custom_field.multi_enum_values.enabled", "custom_field_settings.custom_field.multi_enum_values.name", "custom_field_settings.custom_field.name", "custom_field_settings.custom_field.number_value", "custom_field_settings.custom_field.people_value", "custom_field_settings.custom_field.people_value.name", "custom_field_settings.custom_field.precision", "custom_field_settings.custom_field.representation_type", "custom_field_settings.custom_field.resource_subtype", "custom_field_settings.custom_field.text_value", "custom_field_settings.custom_field.type", "custom_field_settings.is_important", "custom_field_settings.parent", "custom_field_settings.parent.name", "custom_field_settings.project", "custom_field_settings.project.name", "custom_fields", "custom_fields.date_value", "custom_fields.date_value.date", "custom_fields.date_value.date_time", "custom_fields.display_value", "custom_fields.enabled", "custom_fields.enum_options", "custom_fields.enum_options.color", "custom_fields.enum_options.enabled", "custom_fields.enum_options.name", "custom_fields.enum_value", "custom_fields.enum_value.color", "custom_fields.enum_value.enabled", "custom_fields.enum_value.name", "custom_fields.id_prefix", "custom_fields.is_formula_field", "custom_fields.multi_enum_values", "custom_fields.multi_enum_values.color", "custom_fields.multi_enum_values.enabled", "custom_fields.multi_enum_values.name", "custom_fields.name", "custom_fields.number_value", "custom_fields.representation_type", "custom_fields.resource_subtype", "custom_fields.text_value", "custom_fields.type", "due_on", "members", "members.name", "name", "owner", "owner.name", "permalink_url", "project_templates", "project_templates.name", "public", "start_on", "workspace", "workspace.name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### data: `PortfolioRequest`<a id="data-portfoliorequest"></a>

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PortfoliosCreateNewPortfolioRecordRequest`](./asana_python_sdk/type/portfolios_create_new_portfolio_record_request.py)
The portfolio to create.

#### 🔄 Return<a id="🔄-return"></a>

[`PortfoliosCreateNewPortfolioRecordResponse`](./asana_python_sdk/pydantic/portfolios_create_new_portfolio_record_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/portfolios` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.portfolios.delete_record`<a id="asanaportfoliosdelete_record"></a>

An existing portfolio can be deleted by making a DELETE request on
the URL for that portfolio.

Returns an empty data record.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_record_response = asana.portfolios.delete_record(
    portfolio_gid="12345",
    opt_pretty=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### portfolio_gid: `str`<a id="portfolio_gid-str"></a>

Globally unique identifier for the portfolio.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

#### 🔄 Return<a id="🔄-return"></a>

[`PortfoliosDeleteRecordResponse`](./asana_python_sdk/pydantic/portfolios_delete_record_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/portfolios/{portfolio_gid}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.portfolios.get_items`<a id="asanaportfoliosget_items"></a>

Get a list of the items in compact form in a portfolio.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_items_response = asana.portfolios.get_items(
    portfolio_gid="12345",
    opt_pretty=True,
    limit=50,
    offset="eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9",
    opt_fields=["archived", "color", "completed", "completed_at", "completed_by", "completed_by.name", "created_at", "created_from_template", "created_from_template.name", "current_status", "current_status.author", "current_status.author.name", "current_status.color", "current_status.created_at", "current_status.created_by", "current_status.created_by.name", "current_status.html_text", "current_status.modified_at", "current_status.text", "current_status.title", "current_status_update", "current_status_update.resource_subtype", "current_status_update.title", "custom_field_settings", "custom_field_settings.custom_field", "custom_field_settings.custom_field.asana_created_field", "custom_field_settings.custom_field.created_by", "custom_field_settings.custom_field.created_by.name", "custom_field_settings.custom_field.currency_code", "custom_field_settings.custom_field.custom_label", "custom_field_settings.custom_field.custom_label_position", "custom_field_settings.custom_field.date_value", "custom_field_settings.custom_field.date_value.date", "custom_field_settings.custom_field.date_value.date_time", "custom_field_settings.custom_field.description", "custom_field_settings.custom_field.display_value", "custom_field_settings.custom_field.enabled", "custom_field_settings.custom_field.enum_options", "custom_field_settings.custom_field.enum_options.color", "custom_field_settings.custom_field.enum_options.enabled", "custom_field_settings.custom_field.enum_options.name", "custom_field_settings.custom_field.enum_value", "custom_field_settings.custom_field.enum_value.color", "custom_field_settings.custom_field.enum_value.enabled", "custom_field_settings.custom_field.enum_value.name", "custom_field_settings.custom_field.format", "custom_field_settings.custom_field.has_notifications_enabled", "custom_field_settings.custom_field.id_prefix", "custom_field_settings.custom_field.is_formula_field", "custom_field_settings.custom_field.is_global_to_workspace", "custom_field_settings.custom_field.is_value_read_only", "custom_field_settings.custom_field.multi_enum_values", "custom_field_settings.custom_field.multi_enum_values.color", "custom_field_settings.custom_field.multi_enum_values.enabled", "custom_field_settings.custom_field.multi_enum_values.name", "custom_field_settings.custom_field.name", "custom_field_settings.custom_field.number_value", "custom_field_settings.custom_field.people_value", "custom_field_settings.custom_field.people_value.name", "custom_field_settings.custom_field.precision", "custom_field_settings.custom_field.representation_type", "custom_field_settings.custom_field.resource_subtype", "custom_field_settings.custom_field.text_value", "custom_field_settings.custom_field.type", "custom_field_settings.is_important", "custom_field_settings.parent", "custom_field_settings.parent.name", "custom_field_settings.project", "custom_field_settings.project.name", "custom_fields", "custom_fields.date_value", "custom_fields.date_value.date", "custom_fields.date_value.date_time", "custom_fields.display_value", "custom_fields.enabled", "custom_fields.enum_options", "custom_fields.enum_options.color", "custom_fields.enum_options.enabled", "custom_fields.enum_options.name", "custom_fields.enum_value", "custom_fields.enum_value.color", "custom_fields.enum_value.enabled", "custom_fields.enum_value.name", "custom_fields.id_prefix", "custom_fields.is_formula_field", "custom_fields.multi_enum_values", "custom_fields.multi_enum_values.color", "custom_fields.multi_enum_values.enabled", "custom_fields.multi_enum_values.name", "custom_fields.name", "custom_fields.number_value", "custom_fields.representation_type", "custom_fields.resource_subtype", "custom_fields.text_value", "custom_fields.type", "default_access_level", "default_view", "due_date", "due_on", "followers", "followers.name", "html_notes", "icon", "members", "members.name", "minimum_access_level_for_customization", "minimum_access_level_for_sharing", "modified_at", "name", "notes", "offset", "owner", "path", "permalink_url", "privacy_setting", "project_brief", "public", "start_on", "team", "team.name", "uri", "workspace", "workspace.name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### portfolio_gid: `str`<a id="portfolio_gid-str"></a>

Globally unique identifier for the portfolio.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### limit: `int`<a id="limit-int"></a>

Results per page. The number of objects to return per page. The value must be between 1 and 100.

##### offset: `str`<a id="offset-str"></a>

Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`PortfoliosGetItemsResponse`](./asana_python_sdk/pydantic/portfolios_get_items_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/portfolios/{portfolio_gid}/items` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.portfolios.get_record`<a id="asanaportfoliosget_record"></a>

Returns the complete portfolio record for a single portfolio.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_record_response = asana.portfolios.get_record(
    portfolio_gid="12345",
    opt_pretty=True,
    opt_fields=["color", "created_at", "created_by", "created_by.name", "current_status_update", "current_status_update.resource_subtype", "current_status_update.title", "custom_field_settings", "custom_field_settings.custom_field", "custom_field_settings.custom_field.asana_created_field", "custom_field_settings.custom_field.created_by", "custom_field_settings.custom_field.created_by.name", "custom_field_settings.custom_field.currency_code", "custom_field_settings.custom_field.custom_label", "custom_field_settings.custom_field.custom_label_position", "custom_field_settings.custom_field.date_value", "custom_field_settings.custom_field.date_value.date", "custom_field_settings.custom_field.date_value.date_time", "custom_field_settings.custom_field.description", "custom_field_settings.custom_field.display_value", "custom_field_settings.custom_field.enabled", "custom_field_settings.custom_field.enum_options", "custom_field_settings.custom_field.enum_options.color", "custom_field_settings.custom_field.enum_options.enabled", "custom_field_settings.custom_field.enum_options.name", "custom_field_settings.custom_field.enum_value", "custom_field_settings.custom_field.enum_value.color", "custom_field_settings.custom_field.enum_value.enabled", "custom_field_settings.custom_field.enum_value.name", "custom_field_settings.custom_field.format", "custom_field_settings.custom_field.has_notifications_enabled", "custom_field_settings.custom_field.id_prefix", "custom_field_settings.custom_field.is_formula_field", "custom_field_settings.custom_field.is_global_to_workspace", "custom_field_settings.custom_field.is_value_read_only", "custom_field_settings.custom_field.multi_enum_values", "custom_field_settings.custom_field.multi_enum_values.color", "custom_field_settings.custom_field.multi_enum_values.enabled", "custom_field_settings.custom_field.multi_enum_values.name", "custom_field_settings.custom_field.name", "custom_field_settings.custom_field.number_value", "custom_field_settings.custom_field.people_value", "custom_field_settings.custom_field.people_value.name", "custom_field_settings.custom_field.precision", "custom_field_settings.custom_field.representation_type", "custom_field_settings.custom_field.resource_subtype", "custom_field_settings.custom_field.text_value", "custom_field_settings.custom_field.type", "custom_field_settings.is_important", "custom_field_settings.parent", "custom_field_settings.parent.name", "custom_field_settings.project", "custom_field_settings.project.name", "custom_fields", "custom_fields.date_value", "custom_fields.date_value.date", "custom_fields.date_value.date_time", "custom_fields.display_value", "custom_fields.enabled", "custom_fields.enum_options", "custom_fields.enum_options.color", "custom_fields.enum_options.enabled", "custom_fields.enum_options.name", "custom_fields.enum_value", "custom_fields.enum_value.color", "custom_fields.enum_value.enabled", "custom_fields.enum_value.name", "custom_fields.id_prefix", "custom_fields.is_formula_field", "custom_fields.multi_enum_values", "custom_fields.multi_enum_values.color", "custom_fields.multi_enum_values.enabled", "custom_fields.multi_enum_values.name", "custom_fields.name", "custom_fields.number_value", "custom_fields.representation_type", "custom_fields.resource_subtype", "custom_fields.text_value", "custom_fields.type", "due_on", "members", "members.name", "name", "owner", "owner.name", "permalink_url", "project_templates", "project_templates.name", "public", "start_on", "workspace", "workspace.name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### portfolio_gid: `str`<a id="portfolio_gid-str"></a>

Globally unique identifier for the portfolio.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`PortfoliosGetRecordResponse`](./asana_python_sdk/pydantic/portfolios_get_record_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/portfolios/{portfolio_gid}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.portfolios.list_multiple_portfolios`<a id="asanaportfolioslist_multiple_portfolios"></a>

Returns a list of the portfolios in compact representation that are owned by the current API user.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_multiple_portfolios_response = asana.portfolios.list_multiple_portfolios(
    workspace="1331",
    opt_pretty=True,
    limit=50,
    offset="eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9",
    owner="14916",
    opt_fields=["color", "created_at", "created_by", "created_by.name", "current_status_update", "current_status_update.resource_subtype", "current_status_update.title", "custom_field_settings", "custom_field_settings.custom_field", "custom_field_settings.custom_field.asana_created_field", "custom_field_settings.custom_field.created_by", "custom_field_settings.custom_field.created_by.name", "custom_field_settings.custom_field.currency_code", "custom_field_settings.custom_field.custom_label", "custom_field_settings.custom_field.custom_label_position", "custom_field_settings.custom_field.date_value", "custom_field_settings.custom_field.date_value.date", "custom_field_settings.custom_field.date_value.date_time", "custom_field_settings.custom_field.description", "custom_field_settings.custom_field.display_value", "custom_field_settings.custom_field.enabled", "custom_field_settings.custom_field.enum_options", "custom_field_settings.custom_field.enum_options.color", "custom_field_settings.custom_field.enum_options.enabled", "custom_field_settings.custom_field.enum_options.name", "custom_field_settings.custom_field.enum_value", "custom_field_settings.custom_field.enum_value.color", "custom_field_settings.custom_field.enum_value.enabled", "custom_field_settings.custom_field.enum_value.name", "custom_field_settings.custom_field.format", "custom_field_settings.custom_field.has_notifications_enabled", "custom_field_settings.custom_field.id_prefix", "custom_field_settings.custom_field.is_formula_field", "custom_field_settings.custom_field.is_global_to_workspace", "custom_field_settings.custom_field.is_value_read_only", "custom_field_settings.custom_field.multi_enum_values", "custom_field_settings.custom_field.multi_enum_values.color", "custom_field_settings.custom_field.multi_enum_values.enabled", "custom_field_settings.custom_field.multi_enum_values.name", "custom_field_settings.custom_field.name", "custom_field_settings.custom_field.number_value", "custom_field_settings.custom_field.people_value", "custom_field_settings.custom_field.people_value.name", "custom_field_settings.custom_field.precision", "custom_field_settings.custom_field.representation_type", "custom_field_settings.custom_field.resource_subtype", "custom_field_settings.custom_field.text_value", "custom_field_settings.custom_field.type", "custom_field_settings.is_important", "custom_field_settings.parent", "custom_field_settings.parent.name", "custom_field_settings.project", "custom_field_settings.project.name", "custom_fields", "custom_fields.date_value", "custom_fields.date_value.date", "custom_fields.date_value.date_time", "custom_fields.display_value", "custom_fields.enabled", "custom_fields.enum_options", "custom_fields.enum_options.color", "custom_fields.enum_options.enabled", "custom_fields.enum_options.name", "custom_fields.enum_value", "custom_fields.enum_value.color", "custom_fields.enum_value.enabled", "custom_fields.enum_value.name", "custom_fields.id_prefix", "custom_fields.is_formula_field", "custom_fields.multi_enum_values", "custom_fields.multi_enum_values.color", "custom_fields.multi_enum_values.enabled", "custom_fields.multi_enum_values.name", "custom_fields.name", "custom_fields.number_value", "custom_fields.representation_type", "custom_fields.resource_subtype", "custom_fields.text_value", "custom_fields.type", "due_on", "members", "members.name", "name", "offset", "owner", "owner.name", "path", "permalink_url", "project_templates", "project_templates.name", "public", "start_on", "uri", "workspace", "workspace.name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### workspace: `str`<a id="workspace-str"></a>

The workspace or organization to filter portfolios on.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### limit: `int`<a id="limit-int"></a>

Results per page. The number of objects to return per page. The value must be between 1 and 100.

##### offset: `str`<a id="offset-str"></a>

Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'

##### owner: `str`<a id="owner-str"></a>

The user who owns the portfolio. Currently, API users can only get a list of portfolios that they themselves own, unless the request is made from a Service Account. In the case of a Service Account, if this parameter is specified, then all portfolios owned by this parameter are returned. Otherwise, all portfolios across the workspace are returned.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`PortfoliosListMultiplePortfoliosResponse`](./asana_python_sdk/pydantic/portfolios_list_multiple_portfolios_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/portfolios` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.portfolios.remove_custom_field_setting`<a id="asanaportfoliosremove_custom_field_setting"></a>

Removes a custom field setting from a portfolio.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_custom_field_setting_response = asana.portfolios.remove_custom_field_setting(
    portfolio_gid="12345",
    data={
        "custom_field": "14916",
    },
    opt_pretty=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### portfolio_gid: `str`<a id="portfolio_gid-str"></a>

Globally unique identifier for the portfolio.

##### data: [`RemoveCustomFieldSettingRequest`](./asana_python_sdk/type/remove_custom_field_setting_request.py)<a id="data-removecustomfieldsettingrequestasana_python_sdktyperemove_custom_field_setting_requestpy"></a>


##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PortfoliosRemoveCustomFieldSettingRequest`](./asana_python_sdk/type/portfolios_remove_custom_field_setting_request.py)
Information about the custom field setting being removed.

#### 🔄 Return<a id="🔄-return"></a>

[`PortfoliosRemoveCustomFieldSettingResponse`](./asana_python_sdk/pydantic/portfolios_remove_custom_field_setting_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/portfolios/{portfolio_gid}/removeCustomFieldSetting` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.portfolios.remove_item_from_portfolio`<a id="asanaportfoliosremove_item_from_portfolio"></a>

Remove an item from a portfolio.
Returns an empty data block.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_item_from_portfolio_response = asana.portfolios.remove_item_from_portfolio(
    portfolio_gid="12345",
    data={
        "item": "1331",
    },
    opt_pretty=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### portfolio_gid: `str`<a id="portfolio_gid-str"></a>

Globally unique identifier for the portfolio.

##### data: [`PortfolioRemoveItemRequest`](./asana_python_sdk/type/portfolio_remove_item_request.py)<a id="data-portfolioremoveitemrequestasana_python_sdktypeportfolio_remove_item_requestpy"></a>


##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PortfoliosRemoveItemFromPortfolioRequest`](./asana_python_sdk/type/portfolios_remove_item_from_portfolio_request.py)
Information about the item being removed.

#### 🔄 Return<a id="🔄-return"></a>

[`PortfoliosRemoveItemFromPortfolioResponse`](./asana_python_sdk/pydantic/portfolios_remove_item_from_portfolio_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/portfolios/{portfolio_gid}/removeItem` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.portfolios.remove_members_from_portfolio`<a id="asanaportfoliosremove_members_from_portfolio"></a>

Removes the specified list of users from members of the portfolio.
Returns the updated portfolio record.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_members_from_portfolio_response = asana.portfolios.remove_members_from_portfolio(
    portfolio_gid="12345",
    data={
        "members": "521621,621373",
    },
    opt_pretty=True,
    opt_fields=["color", "created_at", "created_by", "created_by.name", "current_status_update", "current_status_update.resource_subtype", "current_status_update.title", "custom_field_settings", "custom_field_settings.custom_field", "custom_field_settings.custom_field.asana_created_field", "custom_field_settings.custom_field.created_by", "custom_field_settings.custom_field.created_by.name", "custom_field_settings.custom_field.currency_code", "custom_field_settings.custom_field.custom_label", "custom_field_settings.custom_field.custom_label_position", "custom_field_settings.custom_field.date_value", "custom_field_settings.custom_field.date_value.date", "custom_field_settings.custom_field.date_value.date_time", "custom_field_settings.custom_field.description", "custom_field_settings.custom_field.display_value", "custom_field_settings.custom_field.enabled", "custom_field_settings.custom_field.enum_options", "custom_field_settings.custom_field.enum_options.color", "custom_field_settings.custom_field.enum_options.enabled", "custom_field_settings.custom_field.enum_options.name", "custom_field_settings.custom_field.enum_value", "custom_field_settings.custom_field.enum_value.color", "custom_field_settings.custom_field.enum_value.enabled", "custom_field_settings.custom_field.enum_value.name", "custom_field_settings.custom_field.format", "custom_field_settings.custom_field.has_notifications_enabled", "custom_field_settings.custom_field.id_prefix", "custom_field_settings.custom_field.is_formula_field", "custom_field_settings.custom_field.is_global_to_workspace", "custom_field_settings.custom_field.is_value_read_only", "custom_field_settings.custom_field.multi_enum_values", "custom_field_settings.custom_field.multi_enum_values.color", "custom_field_settings.custom_field.multi_enum_values.enabled", "custom_field_settings.custom_field.multi_enum_values.name", "custom_field_settings.custom_field.name", "custom_field_settings.custom_field.number_value", "custom_field_settings.custom_field.people_value", "custom_field_settings.custom_field.people_value.name", "custom_field_settings.custom_field.precision", "custom_field_settings.custom_field.representation_type", "custom_field_settings.custom_field.resource_subtype", "custom_field_settings.custom_field.text_value", "custom_field_settings.custom_field.type", "custom_field_settings.is_important", "custom_field_settings.parent", "custom_field_settings.parent.name", "custom_field_settings.project", "custom_field_settings.project.name", "custom_fields", "custom_fields.date_value", "custom_fields.date_value.date", "custom_fields.date_value.date_time", "custom_fields.display_value", "custom_fields.enabled", "custom_fields.enum_options", "custom_fields.enum_options.color", "custom_fields.enum_options.enabled", "custom_fields.enum_options.name", "custom_fields.enum_value", "custom_fields.enum_value.color", "custom_fields.enum_value.enabled", "custom_fields.enum_value.name", "custom_fields.id_prefix", "custom_fields.is_formula_field", "custom_fields.multi_enum_values", "custom_fields.multi_enum_values.color", "custom_fields.multi_enum_values.enabled", "custom_fields.multi_enum_values.name", "custom_fields.name", "custom_fields.number_value", "custom_fields.representation_type", "custom_fields.resource_subtype", "custom_fields.text_value", "custom_fields.type", "due_on", "members", "members.name", "name", "owner", "owner.name", "permalink_url", "project_templates", "project_templates.name", "public", "start_on", "workspace", "workspace.name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### portfolio_gid: `str`<a id="portfolio_gid-str"></a>

Globally unique identifier for the portfolio.

##### data: [`RemoveMembersRequest`](./asana_python_sdk/type/remove_members_request.py)<a id="data-removemembersrequestasana_python_sdktyperemove_members_requestpy"></a>


##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PortfoliosRemoveMembersFromPortfolioRequest`](./asana_python_sdk/type/portfolios_remove_members_from_portfolio_request.py)
Information about the members being removed.

#### 🔄 Return<a id="🔄-return"></a>

[`PortfoliosRemoveMembersFromPortfolioResponse`](./asana_python_sdk/pydantic/portfolios_remove_members_from_portfolio_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/portfolios/{portfolio_gid}/removeMembers` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.portfolios.update_portfolio_record`<a id="asanaportfoliosupdate_portfolio_record"></a>

An existing portfolio can be updated by making a PUT request on the URL for
that portfolio. Only the fields provided in the `data` block will be updated;
any unspecified fields will remain unchanged.

Returns the complete updated portfolio record.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_portfolio_record_response = asana.portfolios.update_portfolio_record(
    portfolio_gid="12345",
    data=None,
    opt_pretty=True,
    opt_fields=["color", "created_at", "created_by", "created_by.name", "current_status_update", "current_status_update.resource_subtype", "current_status_update.title", "custom_field_settings", "custom_field_settings.custom_field", "custom_field_settings.custom_field.asana_created_field", "custom_field_settings.custom_field.created_by", "custom_field_settings.custom_field.created_by.name", "custom_field_settings.custom_field.currency_code", "custom_field_settings.custom_field.custom_label", "custom_field_settings.custom_field.custom_label_position", "custom_field_settings.custom_field.date_value", "custom_field_settings.custom_field.date_value.date", "custom_field_settings.custom_field.date_value.date_time", "custom_field_settings.custom_field.description", "custom_field_settings.custom_field.display_value", "custom_field_settings.custom_field.enabled", "custom_field_settings.custom_field.enum_options", "custom_field_settings.custom_field.enum_options.color", "custom_field_settings.custom_field.enum_options.enabled", "custom_field_settings.custom_field.enum_options.name", "custom_field_settings.custom_field.enum_value", "custom_field_settings.custom_field.enum_value.color", "custom_field_settings.custom_field.enum_value.enabled", "custom_field_settings.custom_field.enum_value.name", "custom_field_settings.custom_field.format", "custom_field_settings.custom_field.has_notifications_enabled", "custom_field_settings.custom_field.id_prefix", "custom_field_settings.custom_field.is_formula_field", "custom_field_settings.custom_field.is_global_to_workspace", "custom_field_settings.custom_field.is_value_read_only", "custom_field_settings.custom_field.multi_enum_values", "custom_field_settings.custom_field.multi_enum_values.color", "custom_field_settings.custom_field.multi_enum_values.enabled", "custom_field_settings.custom_field.multi_enum_values.name", "custom_field_settings.custom_field.name", "custom_field_settings.custom_field.number_value", "custom_field_settings.custom_field.people_value", "custom_field_settings.custom_field.people_value.name", "custom_field_settings.custom_field.precision", "custom_field_settings.custom_field.representation_type", "custom_field_settings.custom_field.resource_subtype", "custom_field_settings.custom_field.text_value", "custom_field_settings.custom_field.type", "custom_field_settings.is_important", "custom_field_settings.parent", "custom_field_settings.parent.name", "custom_field_settings.project", "custom_field_settings.project.name", "custom_fields", "custom_fields.date_value", "custom_fields.date_value.date", "custom_fields.date_value.date_time", "custom_fields.display_value", "custom_fields.enabled", "custom_fields.enum_options", "custom_fields.enum_options.color", "custom_fields.enum_options.enabled", "custom_fields.enum_options.name", "custom_fields.enum_value", "custom_fields.enum_value.color", "custom_fields.enum_value.enabled", "custom_fields.enum_value.name", "custom_fields.id_prefix", "custom_fields.is_formula_field", "custom_fields.multi_enum_values", "custom_fields.multi_enum_values.color", "custom_fields.multi_enum_values.enabled", "custom_fields.multi_enum_values.name", "custom_fields.name", "custom_fields.number_value", "custom_fields.representation_type", "custom_fields.resource_subtype", "custom_fields.text_value", "custom_fields.type", "due_on", "members", "members.name", "name", "owner", "owner.name", "permalink_url", "project_templates", "project_templates.name", "public", "start_on", "workspace", "workspace.name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### portfolio_gid: `str`<a id="portfolio_gid-str"></a>

Globally unique identifier for the portfolio.

##### data: `PortfolioRequest`<a id="data-portfoliorequest"></a>

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PortfoliosUpdatePortfolioRecordRequest`](./asana_python_sdk/type/portfolios_update_portfolio_record_request.py)
The updated fields for the portfolio.

#### 🔄 Return<a id="🔄-return"></a>

[`PortfoliosUpdatePortfolioRecordResponse`](./asana_python_sdk/pydantic/portfolios_update_portfolio_record_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/portfolios/{portfolio_gid}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.project_briefs.create_new_record`<a id="asanaproject_briefscreate_new_record"></a>

Creates a new project brief.

Returns the full record of the newly created project brief.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_record_response = asana.project_briefs.create_new_record(
    project_gid="1331",
    data=None,
    opt_pretty=True,
    opt_fields=["html_text", "permalink_url", "project", "project.name", "text", "title"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_gid: `str`<a id="project_gid-str"></a>

Globally unique identifier for the project.

##### data: `ProjectBriefRequest`<a id="data-projectbriefrequest"></a>

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ProjectBriefsCreateNewRecordRequest`](./asana_python_sdk/type/project_briefs_create_new_record_request.py)
The project brief to create.

#### 🔄 Return<a id="🔄-return"></a>

[`ProjectBriefsCreateNewRecordResponse`](./asana_python_sdk/pydantic/project_briefs_create_new_record_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/projects/{project_gid}/project_briefs` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.project_briefs.get_full_record`<a id="asanaproject_briefsget_full_record"></a>

Get the full record for a project brief.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_full_record_response = asana.project_briefs.get_full_record(
    project_brief_gid="12345",
    opt_pretty=True,
    opt_fields=["html_text", "permalink_url", "project", "project.name", "text", "title"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_brief_gid: `str`<a id="project_brief_gid-str"></a>

Globally unique identifier for the project brief.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`ProjectBriefsGetFullRecordResponse`](./asana_python_sdk/pydantic/project_briefs_get_full_record_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/project_briefs/{project_brief_gid}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.project_briefs.remove_brief`<a id="asanaproject_briefsremove_brief"></a>

Deletes a specific, existing project brief.

Returns an empty data record.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_brief_response = asana.project_briefs.remove_brief(
    project_brief_gid="12345",
    opt_pretty=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_brief_gid: `str`<a id="project_brief_gid-str"></a>

Globally unique identifier for the project brief.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

#### 🔄 Return<a id="🔄-return"></a>

[`ProjectBriefsRemoveBriefResponse`](./asana_python_sdk/pydantic/project_briefs_remove_brief_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/project_briefs/{project_brief_gid}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.project_briefs.update_brief_record`<a id="asanaproject_briefsupdate_brief_record"></a>

An existing project brief can be updated by making a PUT request on the URL for
that project brief. Only the fields provided in the `data` block will be updated;
any unspecified fields will remain unchanged.

Returns the complete updated project brief record.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_brief_record_response = asana.project_briefs.update_brief_record(
    project_brief_gid="12345",
    data=None,
    opt_pretty=True,
    opt_fields=["html_text", "permalink_url", "project", "project.name", "text", "title"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_brief_gid: `str`<a id="project_brief_gid-str"></a>

Globally unique identifier for the project brief.

##### data: `ProjectBriefRequest`<a id="data-projectbriefrequest"></a>

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ProjectBriefsUpdateBriefRecordRequest`](./asana_python_sdk/type/project_briefs_update_brief_record_request.py)
The updated fields for the project brief.

#### 🔄 Return<a id="🔄-return"></a>

[`ProjectBriefsUpdateBriefRecordResponse`](./asana_python_sdk/pydantic/project_briefs_update_brief_record_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/project_briefs/{project_brief_gid}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.project_memberships.get_compact_records`<a id="asanaproject_membershipsget_compact_records"></a>

Returns the compact project membership records for the project.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_compact_records_response = asana.project_memberships.get_compact_records(
    project_gid="1331",
    user="me",
    opt_pretty=True,
    limit=50,
    offset="eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9",
    opt_fields=["access_level", "member", "member.name", "offset", "parent", "parent.name", "path", "uri"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_gid: `str`<a id="project_gid-str"></a>

Globally unique identifier for the project.

##### user: `str`<a id="user-str"></a>

A string identifying a user. This can either be the string \"me\", an email, or the gid of a user.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### limit: `int`<a id="limit-int"></a>

Results per page. The number of objects to return per page. The value must be between 1 and 100.

##### offset: `str`<a id="offset-str"></a>

Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`ProjectMembershipsGetCompactRecordsResponse`](./asana_python_sdk/pydantic/project_memberships_get_compact_records_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/projects/{project_gid}/project_memberships` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.project_memberships.get_record`<a id="asanaproject_membershipsget_record"></a>

Returns the complete project record for a single project membership.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_record_response = asana.project_memberships.get_record(
    project_membership_gid="1331",
    opt_pretty=True,
    opt_fields=["access_level", "member", "member.name", "parent", "parent.name", "project", "project.name", "user", "user.name", "write_access"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_membership_gid: `str`<a id="project_membership_gid-str"></a>

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`ProjectMembershipsGetRecordResponse`](./asana_python_sdk/pydantic/project_memberships_get_record_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/project_memberships/{project_membership_gid}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.project_statuses.create_new_status_update_record`<a id="asanaproject_statusescreate_new_status_update_record"></a>

*Deprecated: new integrations should prefer the `/status_updates` route.*

Creates a new status update on the project.

Returns the full record of the newly created project status update.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_status_update_record_response = asana.project_statuses.create_new_status_update_record(
    project_gid="1331",
    data=None,
    opt_pretty=True,
    opt_fields=["author", "author.name", "color", "created_at", "created_by", "created_by.name", "html_text", "modified_at", "text", "title"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_gid: `str`<a id="project_gid-str"></a>

Globally unique identifier for the project.

##### data: `ProjectStatusBase`<a id="data-projectstatusbase"></a>

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ProjectStatusesCreateNewStatusUpdateRecordRequest`](./asana_python_sdk/type/project_statuses_create_new_status_update_record_request.py)
The project status to create.

#### 🔄 Return<a id="🔄-return"></a>

[`ProjectStatusesCreateNewStatusUpdateRecordResponse`](./asana_python_sdk/pydantic/project_statuses_create_new_status_update_record_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/projects/{project_gid}/project_statuses` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.project_statuses.delete_specific_status_update`<a id="asanaproject_statusesdelete_specific_status_update"></a>

*Deprecated: new integrations should prefer the `/status_updates/{status_gid}` route.*

Deletes a specific, existing project status update.

Returns an empty data record.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_specific_status_update_response = asana.project_statuses.delete_specific_status_update(
    project_status_gid="321654",
    opt_pretty=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_status_gid: `str`<a id="project_status_gid-str"></a>

The project status update to get.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

#### 🔄 Return<a id="🔄-return"></a>

[`ProjectStatusesDeleteSpecificStatusUpdateResponse`](./asana_python_sdk/pydantic/project_statuses_delete_specific_status_update_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/project_statuses/{project_status_gid}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.project_statuses.get_project_updates`<a id="asanaproject_statusesget_project_updates"></a>

*Deprecated: new integrations should prefer the `/status_updates` route.*

Returns the compact project status update records for all updates on the project.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_project_updates_response = asana.project_statuses.get_project_updates(
    project_gid="1331",
    opt_pretty=True,
    limit=50,
    offset="eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9",
    opt_fields=["author", "author.name", "color", "created_at", "created_by", "created_by.name", "html_text", "modified_at", "offset", "path", "text", "title", "uri"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_gid: `str`<a id="project_gid-str"></a>

Globally unique identifier for the project.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### limit: `int`<a id="limit-int"></a>

Results per page. The number of objects to return per page. The value must be between 1 and 100.

##### offset: `str`<a id="offset-str"></a>

Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`ProjectStatusesGetProjectUpdatesResponse`](./asana_python_sdk/pydantic/project_statuses_get_project_updates_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/projects/{project_gid}/project_statuses` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.project_statuses.get_status_update_record`<a id="asanaproject_statusesget_status_update_record"></a>

*Deprecated: new integrations should prefer the `/status_updates/{status_gid}` route.*

Returns the complete record for a single status update.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_status_update_record_response = asana.project_statuses.get_status_update_record(
    project_status_gid="321654",
    opt_pretty=True,
    opt_fields=["author", "author.name", "color", "created_at", "created_by", "created_by.name", "html_text", "modified_at", "text", "title"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_status_gid: `str`<a id="project_status_gid-str"></a>

The project status update to get.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`ProjectStatusesGetStatusUpdateRecordResponse`](./asana_python_sdk/pydantic/project_statuses_get_status_update_record_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/project_statuses/{project_status_gid}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.project_templates.delete_template_record`<a id="asanaproject_templatesdelete_template_record"></a>

A specific, existing project template can be deleted by making a DELETE request on the URL for that project template.

Returns an empty data record.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_template_record_response = asana.project_templates.delete_template_record(
    project_template_gid="1331",
    opt_pretty=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_template_gid: `str`<a id="project_template_gid-str"></a>

Globally unique identifier for the project template.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

#### 🔄 Return<a id="🔄-return"></a>

[`ProjectTemplatesDeleteTemplateRecordResponse`](./asana_python_sdk/pydantic/project_templates_delete_template_record_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/project_templates/{project_template_gid}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.project_templates.get_all_template_records`<a id="asanaproject_templatesget_all_template_records"></a>

Returns the compact project template records for all project templates in the team.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_template_records_response = asana.project_templates.get_all_template_records(
    team_gid="159874",
    opt_pretty=True,
    limit=50,
    offset="eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9",
    opt_fields=["color", "description", "html_description", "name", "offset", "owner", "path", "public", "requested_dates", "requested_dates.description", "requested_dates.name", "requested_roles", "requested_roles.name", "team", "team.name", "uri"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### team_gid: `str`<a id="team_gid-str"></a>

Globally unique identifier for the team.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### limit: `int`<a id="limit-int"></a>

Results per page. The number of objects to return per page. The value must be between 1 and 100.

##### offset: `str`<a id="offset-str"></a>

Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`ProjectTemplatesGetAllTemplateRecordsResponse`](./asana_python_sdk/pydantic/project_templates_get_all_template_records_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teams/{team_gid}/project_templates` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.project_templates.get_record`<a id="asanaproject_templatesget_record"></a>

Returns the complete project template record for a single project template.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_record_response = asana.project_templates.get_record(
    project_template_gid="1331",
    opt_pretty=True,
    opt_fields=["color", "description", "html_description", "name", "owner", "public", "requested_dates", "requested_dates.description", "requested_dates.name", "requested_roles", "requested_roles.name", "team", "team.name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_template_gid: `str`<a id="project_template_gid-str"></a>

Globally unique identifier for the project template.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`ProjectTemplatesGetRecordResponse`](./asana_python_sdk/pydantic/project_templates_get_record_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/project_templates/{project_template_gid}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.project_templates.instantiate_project_job`<a id="asanaproject_templatesinstantiate_project_job"></a>

Creates and returns a job that will asynchronously handle the project instantiation.

To form this request, it is recommended to first make a request to [get a project template](https://developers.asana.com/reference/rest-api-reference). Then, from the response, copy the `gid` from the object in the `requested_dates` array. This `gid` should be used in `requested_dates` to instantiate a project.

_Note: The body of this request will differ if your workspace is an organization. To determine if your workspace is an organization, use the [is_organization](https://developers.asana.com/reference/rest-api-reference) parameter._

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
instantiate_project_job_response = asana.project_templates.instantiate_project_job(
    project_template_gid="1331",
    data={
        "name": "New Project Name",
        "team": "12345",
        "public": True,
        "is_strict": True,
    },
    opt_pretty=True,
    opt_fields=["new_project", "new_project.name", "new_project_template", "new_project_template.name", "new_task", "new_task.created_by", "new_task.name", "new_task.resource_subtype", "new_task_template", "new_task_template.name", "resource_subtype", "status"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_template_gid: `str`<a id="project_template_gid-str"></a>

Globally unique identifier for the project template.

##### data: [`ProjectTemplateInstantiateProjectRequest`](./asana_python_sdk/type/project_template_instantiate_project_request.py)<a id="data-projecttemplateinstantiateprojectrequestasana_python_sdktypeproject_template_instantiate_project_requestpy"></a>


##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ProjectTemplatesInstantiateProjectJobRequest`](./asana_python_sdk/type/project_templates_instantiate_project_job_request.py)
Describes the inputs used for instantiating a project, such as the resulting project's name, which team it should be created in, and values for date variables.

#### 🔄 Return<a id="🔄-return"></a>

[`ProjectTemplatesInstantiateProjectJobResponse`](./asana_python_sdk/pydantic/project_templates_instantiate_project_job_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/project_templates/{project_template_gid}/instantiateProject` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.project_templates.list_multiple`<a id="asanaproject_templateslist_multiple"></a>

Returns the compact project template records for all project templates in the given team or workspace.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_multiple_response = asana.project_templates.list_multiple(
    opt_pretty=True,
    workspace="12345",
    team="14916",
    limit=50,
    offset="eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9",
    opt_fields=["color", "description", "html_description", "name", "offset", "owner", "path", "public", "requested_dates", "requested_dates.description", "requested_dates.name", "requested_roles", "requested_roles.name", "team", "team.name", "uri"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### workspace: `str`<a id="workspace-str"></a>

The workspace to filter results on.

##### team: `str`<a id="team-str"></a>

The team to filter projects on.

##### limit: `int`<a id="limit-int"></a>

Results per page. The number of objects to return per page. The value must be between 1 and 100.

##### offset: `str`<a id="offset-str"></a>

Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`ProjectTemplatesListMultipleResponse`](./asana_python_sdk/pydantic/project_templates_list_multiple_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/project_templates` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.projects.add_custom_field_setting`<a id="asanaprojectsadd_custom_field_setting"></a>

Custom fields are associated with projects by way of custom field settings.  This method creates a setting for the project.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_custom_field_setting_response = asana.projects.add_custom_field_setting(
    project_gid="1331",
    data={
        "custom_field": "14916",
        "is_important": True,
        "insert_before": "1331",
        "insert_after": "1331",
    },
    opt_pretty=True,
    opt_fields=["custom_field", "custom_field.asana_created_field", "custom_field.created_by", "custom_field.created_by.name", "custom_field.currency_code", "custom_field.custom_label", "custom_field.custom_label_position", "custom_field.date_value", "custom_field.date_value.date", "custom_field.date_value.date_time", "custom_field.description", "custom_field.display_value", "custom_field.enabled", "custom_field.enum_options", "custom_field.enum_options.color", "custom_field.enum_options.enabled", "custom_field.enum_options.name", "custom_field.enum_value", "custom_field.enum_value.color", "custom_field.enum_value.enabled", "custom_field.enum_value.name", "custom_field.format", "custom_field.has_notifications_enabled", "custom_field.id_prefix", "custom_field.is_formula_field", "custom_field.is_global_to_workspace", "custom_field.is_value_read_only", "custom_field.multi_enum_values", "custom_field.multi_enum_values.color", "custom_field.multi_enum_values.enabled", "custom_field.multi_enum_values.name", "custom_field.name", "custom_field.number_value", "custom_field.people_value", "custom_field.people_value.name", "custom_field.precision", "custom_field.representation_type", "custom_field.resource_subtype", "custom_field.text_value", "custom_field.type", "is_important", "parent", "parent.name", "project", "project.name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_gid: `str`<a id="project_gid-str"></a>

Globally unique identifier for the project.

##### data: [`AddCustomFieldSettingRequest`](./asana_python_sdk/type/add_custom_field_setting_request.py)<a id="data-addcustomfieldsettingrequestasana_python_sdktypeadd_custom_field_setting_requestpy"></a>


##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ProjectsAddCustomFieldSettingRequest`](./asana_python_sdk/type/projects_add_custom_field_setting_request.py)
Information about the custom field setting.

#### 🔄 Return<a id="🔄-return"></a>

[`ProjectsAddCustomFieldSettingResponse`](./asana_python_sdk/pydantic/projects_add_custom_field_setting_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/projects/{project_gid}/addCustomFieldSetting` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.projects.add_followers_to_project`<a id="asanaprojectsadd_followers_to_project"></a>

Adds the specified list of users as followers to the project. Followers are a subset of members who have opted in to receive "tasks added" notifications for a project. Therefore, if the users are not already members of the project, they will also become members as a result of this operation.
Returns the updated project record.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_followers_to_project_response = asana.projects.add_followers_to_project(
    project_gid="1331",
    data={
        "followers": "521621,621373",
    },
    opt_pretty=True,
    opt_fields=["archived", "color", "completed", "completed_at", "completed_by", "completed_by.name", "created_at", "created_from_template", "created_from_template.name", "current_status", "current_status.author", "current_status.author.name", "current_status.color", "current_status.created_at", "current_status.created_by", "current_status.created_by.name", "current_status.html_text", "current_status.modified_at", "current_status.text", "current_status.title", "current_status_update", "current_status_update.resource_subtype", "current_status_update.title", "custom_field_settings", "custom_field_settings.custom_field", "custom_field_settings.custom_field.asana_created_field", "custom_field_settings.custom_field.created_by", "custom_field_settings.custom_field.created_by.name", "custom_field_settings.custom_field.currency_code", "custom_field_settings.custom_field.custom_label", "custom_field_settings.custom_field.custom_label_position", "custom_field_settings.custom_field.date_value", "custom_field_settings.custom_field.date_value.date", "custom_field_settings.custom_field.date_value.date_time", "custom_field_settings.custom_field.description", "custom_field_settings.custom_field.display_value", "custom_field_settings.custom_field.enabled", "custom_field_settings.custom_field.enum_options", "custom_field_settings.custom_field.enum_options.color", "custom_field_settings.custom_field.enum_options.enabled", "custom_field_settings.custom_field.enum_options.name", "custom_field_settings.custom_field.enum_value", "custom_field_settings.custom_field.enum_value.color", "custom_field_settings.custom_field.enum_value.enabled", "custom_field_settings.custom_field.enum_value.name", "custom_field_settings.custom_field.format", "custom_field_settings.custom_field.has_notifications_enabled", "custom_field_settings.custom_field.id_prefix", "custom_field_settings.custom_field.is_formula_field", "custom_field_settings.custom_field.is_global_to_workspace", "custom_field_settings.custom_field.is_value_read_only", "custom_field_settings.custom_field.multi_enum_values", "custom_field_settings.custom_field.multi_enum_values.color", "custom_field_settings.custom_field.multi_enum_values.enabled", "custom_field_settings.custom_field.multi_enum_values.name", "custom_field_settings.custom_field.name", "custom_field_settings.custom_field.number_value", "custom_field_settings.custom_field.people_value", "custom_field_settings.custom_field.people_value.name", "custom_field_settings.custom_field.precision", "custom_field_settings.custom_field.representation_type", "custom_field_settings.custom_field.resource_subtype", "custom_field_settings.custom_field.text_value", "custom_field_settings.custom_field.type", "custom_field_settings.is_important", "custom_field_settings.parent", "custom_field_settings.parent.name", "custom_field_settings.project", "custom_field_settings.project.name", "custom_fields", "custom_fields.date_value", "custom_fields.date_value.date", "custom_fields.date_value.date_time", "custom_fields.display_value", "custom_fields.enabled", "custom_fields.enum_options", "custom_fields.enum_options.color", "custom_fields.enum_options.enabled", "custom_fields.enum_options.name", "custom_fields.enum_value", "custom_fields.enum_value.color", "custom_fields.enum_value.enabled", "custom_fields.enum_value.name", "custom_fields.id_prefix", "custom_fields.is_formula_field", "custom_fields.multi_enum_values", "custom_fields.multi_enum_values.color", "custom_fields.multi_enum_values.enabled", "custom_fields.multi_enum_values.name", "custom_fields.name", "custom_fields.number_value", "custom_fields.representation_type", "custom_fields.resource_subtype", "custom_fields.text_value", "custom_fields.type", "default_access_level", "default_view", "due_date", "due_on", "followers", "followers.name", "html_notes", "icon", "members", "members.name", "minimum_access_level_for_customization", "minimum_access_level_for_sharing", "modified_at", "name", "notes", "owner", "permalink_url", "privacy_setting", "project_brief", "public", "start_on", "team", "team.name", "workspace", "workspace.name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_gid: `str`<a id="project_gid-str"></a>

Globally unique identifier for the project.

##### data: [`AddFollowersRequest`](./asana_python_sdk/type/add_followers_request.py)<a id="data-addfollowersrequestasana_python_sdktypeadd_followers_requestpy"></a>


##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ProjectsAddFollowersToProjectRequest`](./asana_python_sdk/type/projects_add_followers_to_project_request.py)
Information about the followers being added.

#### 🔄 Return<a id="🔄-return"></a>

[`ProjectsAddFollowersToProjectResponse`](./asana_python_sdk/pydantic/projects_add_followers_to_project_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/projects/{project_gid}/addFollowers` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.projects.add_members_to_project`<a id="asanaprojectsadd_members_to_project"></a>

Adds the specified list of users as members of the project. Note that a user being added as a member may also be added as a *follower* as a result of this operation. This is because the user's default notification settings (i.e., in the "Notifcations" tab of "My Profile Settings") will override this endpoint's default behavior of setting "Tasks added" notifications to `false`.
Returns the updated project record.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_members_to_project_response = asana.projects.add_members_to_project(
    project_gid="1331",
    data={
        "members": "521621,621373",
    },
    opt_pretty=True,
    opt_fields=["archived", "color", "completed", "completed_at", "completed_by", "completed_by.name", "created_at", "created_from_template", "created_from_template.name", "current_status", "current_status.author", "current_status.author.name", "current_status.color", "current_status.created_at", "current_status.created_by", "current_status.created_by.name", "current_status.html_text", "current_status.modified_at", "current_status.text", "current_status.title", "current_status_update", "current_status_update.resource_subtype", "current_status_update.title", "custom_field_settings", "custom_field_settings.custom_field", "custom_field_settings.custom_field.asana_created_field", "custom_field_settings.custom_field.created_by", "custom_field_settings.custom_field.created_by.name", "custom_field_settings.custom_field.currency_code", "custom_field_settings.custom_field.custom_label", "custom_field_settings.custom_field.custom_label_position", "custom_field_settings.custom_field.date_value", "custom_field_settings.custom_field.date_value.date", "custom_field_settings.custom_field.date_value.date_time", "custom_field_settings.custom_field.description", "custom_field_settings.custom_field.display_value", "custom_field_settings.custom_field.enabled", "custom_field_settings.custom_field.enum_options", "custom_field_settings.custom_field.enum_options.color", "custom_field_settings.custom_field.enum_options.enabled", "custom_field_settings.custom_field.enum_options.name", "custom_field_settings.custom_field.enum_value", "custom_field_settings.custom_field.enum_value.color", "custom_field_settings.custom_field.enum_value.enabled", "custom_field_settings.custom_field.enum_value.name", "custom_field_settings.custom_field.format", "custom_field_settings.custom_field.has_notifications_enabled", "custom_field_settings.custom_field.id_prefix", "custom_field_settings.custom_field.is_formula_field", "custom_field_settings.custom_field.is_global_to_workspace", "custom_field_settings.custom_field.is_value_read_only", "custom_field_settings.custom_field.multi_enum_values", "custom_field_settings.custom_field.multi_enum_values.color", "custom_field_settings.custom_field.multi_enum_values.enabled", "custom_field_settings.custom_field.multi_enum_values.name", "custom_field_settings.custom_field.name", "custom_field_settings.custom_field.number_value", "custom_field_settings.custom_field.people_value", "custom_field_settings.custom_field.people_value.name", "custom_field_settings.custom_field.precision", "custom_field_settings.custom_field.representation_type", "custom_field_settings.custom_field.resource_subtype", "custom_field_settings.custom_field.text_value", "custom_field_settings.custom_field.type", "custom_field_settings.is_important", "custom_field_settings.parent", "custom_field_settings.parent.name", "custom_field_settings.project", "custom_field_settings.project.name", "custom_fields", "custom_fields.date_value", "custom_fields.date_value.date", "custom_fields.date_value.date_time", "custom_fields.display_value", "custom_fields.enabled", "custom_fields.enum_options", "custom_fields.enum_options.color", "custom_fields.enum_options.enabled", "custom_fields.enum_options.name", "custom_fields.enum_value", "custom_fields.enum_value.color", "custom_fields.enum_value.enabled", "custom_fields.enum_value.name", "custom_fields.id_prefix", "custom_fields.is_formula_field", "custom_fields.multi_enum_values", "custom_fields.multi_enum_values.color", "custom_fields.multi_enum_values.enabled", "custom_fields.multi_enum_values.name", "custom_fields.name", "custom_fields.number_value", "custom_fields.representation_type", "custom_fields.resource_subtype", "custom_fields.text_value", "custom_fields.type", "default_access_level", "default_view", "due_date", "due_on", "followers", "followers.name", "html_notes", "icon", "members", "members.name", "minimum_access_level_for_customization", "minimum_access_level_for_sharing", "modified_at", "name", "notes", "owner", "permalink_url", "privacy_setting", "project_brief", "public", "start_on", "team", "team.name", "workspace", "workspace.name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_gid: `str`<a id="project_gid-str"></a>

Globally unique identifier for the project.

##### data: [`AddMembersRequest`](./asana_python_sdk/type/add_members_request.py)<a id="data-addmembersrequestasana_python_sdktypeadd_members_requestpy"></a>


##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ProjectsAddMembersToProjectRequest`](./asana_python_sdk/type/projects_add_members_to_project_request.py)
Information about the members being added.

#### 🔄 Return<a id="🔄-return"></a>

[`ProjectsAddMembersToProjectResponse`](./asana_python_sdk/pydantic/projects_add_members_to_project_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/projects/{project_gid}/addMembers` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.projects.create_in_workspace`<a id="asanaprojectscreate_in_workspace"></a>

Creates a project in the workspace.

If the workspace for your project is an organization, you must also
supply a team to share the project with.

Returns the full record of the newly created project.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_in_workspace_response = asana.projects.create_in_workspace(
    workspace_gid="12345",
    data=None,
    opt_pretty=True,
    opt_fields=["archived", "color", "completed", "completed_at", "completed_by", "completed_by.name", "created_at", "created_from_template", "created_from_template.name", "current_status", "current_status.author", "current_status.author.name", "current_status.color", "current_status.created_at", "current_status.created_by", "current_status.created_by.name", "current_status.html_text", "current_status.modified_at", "current_status.text", "current_status.title", "current_status_update", "current_status_update.resource_subtype", "current_status_update.title", "custom_field_settings", "custom_field_settings.custom_field", "custom_field_settings.custom_field.asana_created_field", "custom_field_settings.custom_field.created_by", "custom_field_settings.custom_field.created_by.name", "custom_field_settings.custom_field.currency_code", "custom_field_settings.custom_field.custom_label", "custom_field_settings.custom_field.custom_label_position", "custom_field_settings.custom_field.date_value", "custom_field_settings.custom_field.date_value.date", "custom_field_settings.custom_field.date_value.date_time", "custom_field_settings.custom_field.description", "custom_field_settings.custom_field.display_value", "custom_field_settings.custom_field.enabled", "custom_field_settings.custom_field.enum_options", "custom_field_settings.custom_field.enum_options.color", "custom_field_settings.custom_field.enum_options.enabled", "custom_field_settings.custom_field.enum_options.name", "custom_field_settings.custom_field.enum_value", "custom_field_settings.custom_field.enum_value.color", "custom_field_settings.custom_field.enum_value.enabled", "custom_field_settings.custom_field.enum_value.name", "custom_field_settings.custom_field.format", "custom_field_settings.custom_field.has_notifications_enabled", "custom_field_settings.custom_field.id_prefix", "custom_field_settings.custom_field.is_formula_field", "custom_field_settings.custom_field.is_global_to_workspace", "custom_field_settings.custom_field.is_value_read_only", "custom_field_settings.custom_field.multi_enum_values", "custom_field_settings.custom_field.multi_enum_values.color", "custom_field_settings.custom_field.multi_enum_values.enabled", "custom_field_settings.custom_field.multi_enum_values.name", "custom_field_settings.custom_field.name", "custom_field_settings.custom_field.number_value", "custom_field_settings.custom_field.people_value", "custom_field_settings.custom_field.people_value.name", "custom_field_settings.custom_field.precision", "custom_field_settings.custom_field.representation_type", "custom_field_settings.custom_field.resource_subtype", "custom_field_settings.custom_field.text_value", "custom_field_settings.custom_field.type", "custom_field_settings.is_important", "custom_field_settings.parent", "custom_field_settings.parent.name", "custom_field_settings.project", "custom_field_settings.project.name", "custom_fields", "custom_fields.date_value", "custom_fields.date_value.date", "custom_fields.date_value.date_time", "custom_fields.display_value", "custom_fields.enabled", "custom_fields.enum_options", "custom_fields.enum_options.color", "custom_fields.enum_options.enabled", "custom_fields.enum_options.name", "custom_fields.enum_value", "custom_fields.enum_value.color", "custom_fields.enum_value.enabled", "custom_fields.enum_value.name", "custom_fields.id_prefix", "custom_fields.is_formula_field", "custom_fields.multi_enum_values", "custom_fields.multi_enum_values.color", "custom_fields.multi_enum_values.enabled", "custom_fields.multi_enum_values.name", "custom_fields.name", "custom_fields.number_value", "custom_fields.representation_type", "custom_fields.resource_subtype", "custom_fields.text_value", "custom_fields.type", "default_access_level", "default_view", "due_date", "due_on", "followers", "followers.name", "html_notes", "icon", "members", "members.name", "minimum_access_level_for_customization", "minimum_access_level_for_sharing", "modified_at", "name", "notes", "owner", "permalink_url", "privacy_setting", "project_brief", "public", "start_on", "team", "team.name", "workspace", "workspace.name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### workspace_gid: `str`<a id="workspace_gid-str"></a>

Globally unique identifier for the workspace or organization.

##### data: `ProjectRequest`<a id="data-projectrequest"></a>

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ProjectsCreateInWorkspaceRequest`](./asana_python_sdk/type/projects_create_in_workspace_request.py)
The new project to create.

#### 🔄 Return<a id="🔄-return"></a>

[`ProjectsCreateInWorkspaceResponse`](./asana_python_sdk/pydantic/projects_create_in_workspace_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workspaces/{workspace_gid}/projects` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.projects.create_new_project_record`<a id="asanaprojectscreate_new_project_record"></a>

Create a new project in a workspace or team.

Every project is required to be created in a specific workspace or
organization, and this cannot be changed once set. Note that you can use
the `workspace` parameter regardless of whether or not it is an
organization.

If the workspace for your project is an organization, you must also
supply a `team` to share the project with.

Returns the full record of the newly created project.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_project_record_response = asana.projects.create_new_project_record(
    data=None,
    opt_pretty=True,
    opt_fields=["archived", "color", "completed", "completed_at", "completed_by", "completed_by.name", "created_at", "created_from_template", "created_from_template.name", "current_status", "current_status.author", "current_status.author.name", "current_status.color", "current_status.created_at", "current_status.created_by", "current_status.created_by.name", "current_status.html_text", "current_status.modified_at", "current_status.text", "current_status.title", "current_status_update", "current_status_update.resource_subtype", "current_status_update.title", "custom_field_settings", "custom_field_settings.custom_field", "custom_field_settings.custom_field.asana_created_field", "custom_field_settings.custom_field.created_by", "custom_field_settings.custom_field.created_by.name", "custom_field_settings.custom_field.currency_code", "custom_field_settings.custom_field.custom_label", "custom_field_settings.custom_field.custom_label_position", "custom_field_settings.custom_field.date_value", "custom_field_settings.custom_field.date_value.date", "custom_field_settings.custom_field.date_value.date_time", "custom_field_settings.custom_field.description", "custom_field_settings.custom_field.display_value", "custom_field_settings.custom_field.enabled", "custom_field_settings.custom_field.enum_options", "custom_field_settings.custom_field.enum_options.color", "custom_field_settings.custom_field.enum_options.enabled", "custom_field_settings.custom_field.enum_options.name", "custom_field_settings.custom_field.enum_value", "custom_field_settings.custom_field.enum_value.color", "custom_field_settings.custom_field.enum_value.enabled", "custom_field_settings.custom_field.enum_value.name", "custom_field_settings.custom_field.format", "custom_field_settings.custom_field.has_notifications_enabled", "custom_field_settings.custom_field.id_prefix", "custom_field_settings.custom_field.is_formula_field", "custom_field_settings.custom_field.is_global_to_workspace", "custom_field_settings.custom_field.is_value_read_only", "custom_field_settings.custom_field.multi_enum_values", "custom_field_settings.custom_field.multi_enum_values.color", "custom_field_settings.custom_field.multi_enum_values.enabled", "custom_field_settings.custom_field.multi_enum_values.name", "custom_field_settings.custom_field.name", "custom_field_settings.custom_field.number_value", "custom_field_settings.custom_field.people_value", "custom_field_settings.custom_field.people_value.name", "custom_field_settings.custom_field.precision", "custom_field_settings.custom_field.representation_type", "custom_field_settings.custom_field.resource_subtype", "custom_field_settings.custom_field.text_value", "custom_field_settings.custom_field.type", "custom_field_settings.is_important", "custom_field_settings.parent", "custom_field_settings.parent.name", "custom_field_settings.project", "custom_field_settings.project.name", "custom_fields", "custom_fields.date_value", "custom_fields.date_value.date", "custom_fields.date_value.date_time", "custom_fields.display_value", "custom_fields.enabled", "custom_fields.enum_options", "custom_fields.enum_options.color", "custom_fields.enum_options.enabled", "custom_fields.enum_options.name", "custom_fields.enum_value", "custom_fields.enum_value.color", "custom_fields.enum_value.enabled", "custom_fields.enum_value.name", "custom_fields.id_prefix", "custom_fields.is_formula_field", "custom_fields.multi_enum_values", "custom_fields.multi_enum_values.color", "custom_fields.multi_enum_values.enabled", "custom_fields.multi_enum_values.name", "custom_fields.name", "custom_fields.number_value", "custom_fields.representation_type", "custom_fields.resource_subtype", "custom_fields.text_value", "custom_fields.type", "default_access_level", "default_view", "due_date", "due_on", "followers", "followers.name", "html_notes", "icon", "members", "members.name", "minimum_access_level_for_customization", "minimum_access_level_for_sharing", "modified_at", "name", "notes", "owner", "permalink_url", "privacy_setting", "project_brief", "public", "start_on", "team", "team.name", "workspace", "workspace.name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### data: `ProjectRequest`<a id="data-projectrequest"></a>

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ProjectsCreateNewProjectRecordRequest`](./asana_python_sdk/type/projects_create_new_project_record_request.py)
The project to create.

#### 🔄 Return<a id="🔄-return"></a>

[`ProjectsCreateNewProjectRecordResponse`](./asana_python_sdk/pydantic/projects_create_new_project_record_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/projects` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.projects.create_project_for_team`<a id="asanaprojectscreate_project_for_team"></a>

Creates a project shared with the given team.

Returns the full record of the newly created project.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_project_for_team_response = asana.projects.create_project_for_team(
    team_gid="159874",
    data=None,
    opt_pretty=True,
    opt_fields=["archived", "color", "completed", "completed_at", "completed_by", "completed_by.name", "created_at", "created_from_template", "created_from_template.name", "current_status", "current_status.author", "current_status.author.name", "current_status.color", "current_status.created_at", "current_status.created_by", "current_status.created_by.name", "current_status.html_text", "current_status.modified_at", "current_status.text", "current_status.title", "current_status_update", "current_status_update.resource_subtype", "current_status_update.title", "custom_field_settings", "custom_field_settings.custom_field", "custom_field_settings.custom_field.asana_created_field", "custom_field_settings.custom_field.created_by", "custom_field_settings.custom_field.created_by.name", "custom_field_settings.custom_field.currency_code", "custom_field_settings.custom_field.custom_label", "custom_field_settings.custom_field.custom_label_position", "custom_field_settings.custom_field.date_value", "custom_field_settings.custom_field.date_value.date", "custom_field_settings.custom_field.date_value.date_time", "custom_field_settings.custom_field.description", "custom_field_settings.custom_field.display_value", "custom_field_settings.custom_field.enabled", "custom_field_settings.custom_field.enum_options", "custom_field_settings.custom_field.enum_options.color", "custom_field_settings.custom_field.enum_options.enabled", "custom_field_settings.custom_field.enum_options.name", "custom_field_settings.custom_field.enum_value", "custom_field_settings.custom_field.enum_value.color", "custom_field_settings.custom_field.enum_value.enabled", "custom_field_settings.custom_field.enum_value.name", "custom_field_settings.custom_field.format", "custom_field_settings.custom_field.has_notifications_enabled", "custom_field_settings.custom_field.id_prefix", "custom_field_settings.custom_field.is_formula_field", "custom_field_settings.custom_field.is_global_to_workspace", "custom_field_settings.custom_field.is_value_read_only", "custom_field_settings.custom_field.multi_enum_values", "custom_field_settings.custom_field.multi_enum_values.color", "custom_field_settings.custom_field.multi_enum_values.enabled", "custom_field_settings.custom_field.multi_enum_values.name", "custom_field_settings.custom_field.name", "custom_field_settings.custom_field.number_value", "custom_field_settings.custom_field.people_value", "custom_field_settings.custom_field.people_value.name", "custom_field_settings.custom_field.precision", "custom_field_settings.custom_field.representation_type", "custom_field_settings.custom_field.resource_subtype", "custom_field_settings.custom_field.text_value", "custom_field_settings.custom_field.type", "custom_field_settings.is_important", "custom_field_settings.parent", "custom_field_settings.parent.name", "custom_field_settings.project", "custom_field_settings.project.name", "custom_fields", "custom_fields.date_value", "custom_fields.date_value.date", "custom_fields.date_value.date_time", "custom_fields.display_value", "custom_fields.enabled", "custom_fields.enum_options", "custom_fields.enum_options.color", "custom_fields.enum_options.enabled", "custom_fields.enum_options.name", "custom_fields.enum_value", "custom_fields.enum_value.color", "custom_fields.enum_value.enabled", "custom_fields.enum_value.name", "custom_fields.id_prefix", "custom_fields.is_formula_field", "custom_fields.multi_enum_values", "custom_fields.multi_enum_values.color", "custom_fields.multi_enum_values.enabled", "custom_fields.multi_enum_values.name", "custom_fields.name", "custom_fields.number_value", "custom_fields.representation_type", "custom_fields.resource_subtype", "custom_fields.text_value", "custom_fields.type", "default_access_level", "default_view", "due_date", "due_on", "followers", "followers.name", "html_notes", "icon", "members", "members.name", "minimum_access_level_for_customization", "minimum_access_level_for_sharing", "modified_at", "name", "notes", "owner", "permalink_url", "privacy_setting", "project_brief", "public", "start_on", "team", "team.name", "workspace", "workspace.name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### team_gid: `str`<a id="team_gid-str"></a>

Globally unique identifier for the team.

##### data: `ProjectRequest`<a id="data-projectrequest"></a>

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ProjectsCreateProjectForTeamRequest`](./asana_python_sdk/type/projects_create_project_for_team_request.py)
The new project to create.

#### 🔄 Return<a id="🔄-return"></a>

[`ProjectsCreateProjectForTeamResponse`](./asana_python_sdk/pydantic/projects_create_project_for_team_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teams/{team_gid}/projects` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.projects.create_project_template_job`<a id="asanaprojectscreate_project_template_job"></a>

Creates and returns a job that will asynchronously handle the project template creation. Note that
while the resulting project template can be accessed with the API, it won't be visible in the Asana
UI until Project Templates 2.0 is launched in the app. See more in [this forum post](https://forum.asana.com/t/a-new-api-for-project-templates/156432).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_project_template_job_response = asana.projects.create_project_template_job(
    project_gid="1331",
    data={
        "name": "New Project Template",
        "team": "12345",
        "workspace": "12345",
        "public": True,
    },
    opt_pretty=True,
    opt_fields=["new_project", "new_project.name", "new_project_template", "new_project_template.name", "new_task", "new_task.created_by", "new_task.name", "new_task.resource_subtype", "new_task_template", "new_task_template.name", "resource_subtype", "status"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_gid: `str`<a id="project_gid-str"></a>

Globally unique identifier for the project.

##### data: [`ProjectSaveAsTemplateRequest`](./asana_python_sdk/type/project_save_as_template_request.py)<a id="data-projectsaveastemplaterequestasana_python_sdktypeproject_save_as_template_requestpy"></a>


##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ProjectsCreateProjectTemplateJobRequest`](./asana_python_sdk/type/projects_create_project_template_job_request.py)
Describes the inputs used for creating a project template, such as the resulting project template's name, which team it should be created in.

#### 🔄 Return<a id="🔄-return"></a>

[`ProjectsCreateProjectTemplateJobResponse`](./asana_python_sdk/pydantic/projects_create_project_template_job_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/projects/{project_gid}/saveAsTemplate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.projects.delete_project_by_id`<a id="asanaprojectsdelete_project_by_id"></a>

A specific, existing project can be deleted by making a DELETE request on
the URL for that project.

Returns an empty data record.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_project_by_id_response = asana.projects.delete_project_by_id(
    project_gid="1331",
    opt_pretty=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_gid: `str`<a id="project_gid-str"></a>

Globally unique identifier for the project.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

#### 🔄 Return<a id="🔄-return"></a>

[`ProjectsDeleteProjectByIdResponse`](./asana_python_sdk/pydantic/projects_delete_project_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/projects/{project_gid}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.projects.duplicate_project_job`<a id="asanaprojectsduplicate_project_job"></a>

Creates and returns a job that will asynchronously handle the duplication.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
duplicate_project_job_response = asana.projects.duplicate_project_job(
    project_gid="1331",
    data={
        "name": "New Project Name",
        "team": "12345",
        "include": "[allocations,members,notes,forms,task_notes,task_assignee,task_subtasks,task_attachments,task_dates,task_dependencies,task_followers,task_tags,task_projects]",
    },
    opt_pretty=True,
    opt_fields=["new_project", "new_project.name", "new_project_template", "new_project_template.name", "new_task", "new_task.created_by", "new_task.name", "new_task.resource_subtype", "new_task_template", "new_task_template.name", "resource_subtype", "status"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_gid: `str`<a id="project_gid-str"></a>

Globally unique identifier for the project.

##### data: [`ProjectDuplicateRequest`](./asana_python_sdk/type/project_duplicate_request.py)<a id="data-projectduplicaterequestasana_python_sdktypeproject_duplicate_requestpy"></a>


##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ProjectsDuplicateProjectJobRequest`](./asana_python_sdk/type/projects_duplicate_project_job_request.py)
Describes the duplicate's name and the elements that will be duplicated.

#### 🔄 Return<a id="🔄-return"></a>

[`ProjectsDuplicateProjectJobResponse`](./asana_python_sdk/pydantic/projects_duplicate_project_job_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/projects/{project_gid}/duplicate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.projects.get_all_in_workspace`<a id="asanaprojectsget_all_in_workspace"></a>

Returns the compact project records for all projects in the workspace.
*Note: This endpoint may timeout for large domains. Prefer the `/teams/{team_gid}/projects` endpoint.*

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_in_workspace_response = asana.projects.get_all_in_workspace(
    workspace_gid="12345",
    opt_pretty=True,
    limit=50,
    offset="eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9",
    archived=False,
    opt_fields=["archived", "color", "completed", "completed_at", "completed_by", "completed_by.name", "created_at", "created_from_template", "created_from_template.name", "current_status", "current_status.author", "current_status.author.name", "current_status.color", "current_status.created_at", "current_status.created_by", "current_status.created_by.name", "current_status.html_text", "current_status.modified_at", "current_status.text", "current_status.title", "current_status_update", "current_status_update.resource_subtype", "current_status_update.title", "custom_field_settings", "custom_field_settings.custom_field", "custom_field_settings.custom_field.asana_created_field", "custom_field_settings.custom_field.created_by", "custom_field_settings.custom_field.created_by.name", "custom_field_settings.custom_field.currency_code", "custom_field_settings.custom_field.custom_label", "custom_field_settings.custom_field.custom_label_position", "custom_field_settings.custom_field.date_value", "custom_field_settings.custom_field.date_value.date", "custom_field_settings.custom_field.date_value.date_time", "custom_field_settings.custom_field.description", "custom_field_settings.custom_field.display_value", "custom_field_settings.custom_field.enabled", "custom_field_settings.custom_field.enum_options", "custom_field_settings.custom_field.enum_options.color", "custom_field_settings.custom_field.enum_options.enabled", "custom_field_settings.custom_field.enum_options.name", "custom_field_settings.custom_field.enum_value", "custom_field_settings.custom_field.enum_value.color", "custom_field_settings.custom_field.enum_value.enabled", "custom_field_settings.custom_field.enum_value.name", "custom_field_settings.custom_field.format", "custom_field_settings.custom_field.has_notifications_enabled", "custom_field_settings.custom_field.id_prefix", "custom_field_settings.custom_field.is_formula_field", "custom_field_settings.custom_field.is_global_to_workspace", "custom_field_settings.custom_field.is_value_read_only", "custom_field_settings.custom_field.multi_enum_values", "custom_field_settings.custom_field.multi_enum_values.color", "custom_field_settings.custom_field.multi_enum_values.enabled", "custom_field_settings.custom_field.multi_enum_values.name", "custom_field_settings.custom_field.name", "custom_field_settings.custom_field.number_value", "custom_field_settings.custom_field.people_value", "custom_field_settings.custom_field.people_value.name", "custom_field_settings.custom_field.precision", "custom_field_settings.custom_field.representation_type", "custom_field_settings.custom_field.resource_subtype", "custom_field_settings.custom_field.text_value", "custom_field_settings.custom_field.type", "custom_field_settings.is_important", "custom_field_settings.parent", "custom_field_settings.parent.name", "custom_field_settings.project", "custom_field_settings.project.name", "custom_fields", "custom_fields.date_value", "custom_fields.date_value.date", "custom_fields.date_value.date_time", "custom_fields.display_value", "custom_fields.enabled", "custom_fields.enum_options", "custom_fields.enum_options.color", "custom_fields.enum_options.enabled", "custom_fields.enum_options.name", "custom_fields.enum_value", "custom_fields.enum_value.color", "custom_fields.enum_value.enabled", "custom_fields.enum_value.name", "custom_fields.id_prefix", "custom_fields.is_formula_field", "custom_fields.multi_enum_values", "custom_fields.multi_enum_values.color", "custom_fields.multi_enum_values.enabled", "custom_fields.multi_enum_values.name", "custom_fields.name", "custom_fields.number_value", "custom_fields.representation_type", "custom_fields.resource_subtype", "custom_fields.text_value", "custom_fields.type", "default_access_level", "default_view", "due_date", "due_on", "followers", "followers.name", "html_notes", "icon", "members", "members.name", "minimum_access_level_for_customization", "minimum_access_level_for_sharing", "modified_at", "name", "notes", "offset", "owner", "path", "permalink_url", "privacy_setting", "project_brief", "public", "start_on", "team", "team.name", "uri", "workspace", "workspace.name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### workspace_gid: `str`<a id="workspace_gid-str"></a>

Globally unique identifier for the workspace or organization.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### limit: `int`<a id="limit-int"></a>

Results per page. The number of objects to return per page. The value must be between 1 and 100.

##### offset: `str`<a id="offset-str"></a>

Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'

##### archived: `bool`<a id="archived-bool"></a>

Only return projects whose `archived` field takes on the value of this parameter.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`ProjectsGetAllInWorkspaceResponse`](./asana_python_sdk/pydantic/projects_get_all_in_workspace_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workspaces/{workspace_gid}/projects` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.projects.get_project_record`<a id="asanaprojectsget_project_record"></a>

Returns the complete project record for a single project.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_project_record_response = asana.projects.get_project_record(
    project_gid="1331",
    opt_pretty=True,
    opt_fields=["archived", "color", "completed", "completed_at", "completed_by", "completed_by.name", "created_at", "created_from_template", "created_from_template.name", "current_status", "current_status.author", "current_status.author.name", "current_status.color", "current_status.created_at", "current_status.created_by", "current_status.created_by.name", "current_status.html_text", "current_status.modified_at", "current_status.text", "current_status.title", "current_status_update", "current_status_update.resource_subtype", "current_status_update.title", "custom_field_settings", "custom_field_settings.custom_field", "custom_field_settings.custom_field.asana_created_field", "custom_field_settings.custom_field.created_by", "custom_field_settings.custom_field.created_by.name", "custom_field_settings.custom_field.currency_code", "custom_field_settings.custom_field.custom_label", "custom_field_settings.custom_field.custom_label_position", "custom_field_settings.custom_field.date_value", "custom_field_settings.custom_field.date_value.date", "custom_field_settings.custom_field.date_value.date_time", "custom_field_settings.custom_field.description", "custom_field_settings.custom_field.display_value", "custom_field_settings.custom_field.enabled", "custom_field_settings.custom_field.enum_options", "custom_field_settings.custom_field.enum_options.color", "custom_field_settings.custom_field.enum_options.enabled", "custom_field_settings.custom_field.enum_options.name", "custom_field_settings.custom_field.enum_value", "custom_field_settings.custom_field.enum_value.color", "custom_field_settings.custom_field.enum_value.enabled", "custom_field_settings.custom_field.enum_value.name", "custom_field_settings.custom_field.format", "custom_field_settings.custom_field.has_notifications_enabled", "custom_field_settings.custom_field.id_prefix", "custom_field_settings.custom_field.is_formula_field", "custom_field_settings.custom_field.is_global_to_workspace", "custom_field_settings.custom_field.is_value_read_only", "custom_field_settings.custom_field.multi_enum_values", "custom_field_settings.custom_field.multi_enum_values.color", "custom_field_settings.custom_field.multi_enum_values.enabled", "custom_field_settings.custom_field.multi_enum_values.name", "custom_field_settings.custom_field.name", "custom_field_settings.custom_field.number_value", "custom_field_settings.custom_field.people_value", "custom_field_settings.custom_field.people_value.name", "custom_field_settings.custom_field.precision", "custom_field_settings.custom_field.representation_type", "custom_field_settings.custom_field.resource_subtype", "custom_field_settings.custom_field.text_value", "custom_field_settings.custom_field.type", "custom_field_settings.is_important", "custom_field_settings.parent", "custom_field_settings.parent.name", "custom_field_settings.project", "custom_field_settings.project.name", "custom_fields", "custom_fields.date_value", "custom_fields.date_value.date", "custom_fields.date_value.date_time", "custom_fields.display_value", "custom_fields.enabled", "custom_fields.enum_options", "custom_fields.enum_options.color", "custom_fields.enum_options.enabled", "custom_fields.enum_options.name", "custom_fields.enum_value", "custom_fields.enum_value.color", "custom_fields.enum_value.enabled", "custom_fields.enum_value.name", "custom_fields.id_prefix", "custom_fields.is_formula_field", "custom_fields.multi_enum_values", "custom_fields.multi_enum_values.color", "custom_fields.multi_enum_values.enabled", "custom_fields.multi_enum_values.name", "custom_fields.name", "custom_fields.number_value", "custom_fields.representation_type", "custom_fields.resource_subtype", "custom_fields.text_value", "custom_fields.type", "default_access_level", "default_view", "due_date", "due_on", "followers", "followers.name", "html_notes", "icon", "members", "members.name", "minimum_access_level_for_customization", "minimum_access_level_for_sharing", "modified_at", "name", "notes", "owner", "permalink_url", "privacy_setting", "project_brief", "public", "start_on", "team", "team.name", "workspace", "workspace.name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_gid: `str`<a id="project_gid-str"></a>

Globally unique identifier for the project.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`ProjectsGetProjectRecordResponse`](./asana_python_sdk/pydantic/projects_get_project_record_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/projects/{project_gid}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.projects.get_task_counts`<a id="asanaprojectsget_task_counts"></a>

Get an object that holds task count fields. **All fields are excluded by default**. You must [opt in](https://developers.asana.com/reference/rest-api-reference) using `opt_fields` to get any information from this endpoint.

This endpoint has an additional [rate limit](https://developers.asana.com/reference/rest-api-reference) and each field counts especially high against our [cost limits](/docs/rate-limits#cost-limits).

Milestones are just tasks, so they are included in the `num_tasks`, `num_incomplete_tasks`, and `num_completed_tasks` counts.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_task_counts_response = asana.projects.get_task_counts(
    project_gid="1331",
    opt_pretty=True,
    opt_fields=["num_completed_milestones", "num_completed_tasks", "num_incomplete_milestones", "num_incomplete_tasks", "num_milestones", "num_tasks"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_gid: `str`<a id="project_gid-str"></a>

Globally unique identifier for the project.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`ProjectsGetTaskCountsResponse`](./asana_python_sdk/pydantic/projects_get_task_counts_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/projects/{project_gid}/task_counts` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.projects.get_team_projects`<a id="asanaprojectsget_team_projects"></a>

Returns the compact project records for all projects in the team.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_team_projects_response = asana.projects.get_team_projects(
    team_gid="159874",
    opt_pretty=True,
    limit=50,
    offset="eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9",
    archived=False,
    opt_fields=["archived", "color", "completed", "completed_at", "completed_by", "completed_by.name", "created_at", "created_from_template", "created_from_template.name", "current_status", "current_status.author", "current_status.author.name", "current_status.color", "current_status.created_at", "current_status.created_by", "current_status.created_by.name", "current_status.html_text", "current_status.modified_at", "current_status.text", "current_status.title", "current_status_update", "current_status_update.resource_subtype", "current_status_update.title", "custom_field_settings", "custom_field_settings.custom_field", "custom_field_settings.custom_field.asana_created_field", "custom_field_settings.custom_field.created_by", "custom_field_settings.custom_field.created_by.name", "custom_field_settings.custom_field.currency_code", "custom_field_settings.custom_field.custom_label", "custom_field_settings.custom_field.custom_label_position", "custom_field_settings.custom_field.date_value", "custom_field_settings.custom_field.date_value.date", "custom_field_settings.custom_field.date_value.date_time", "custom_field_settings.custom_field.description", "custom_field_settings.custom_field.display_value", "custom_field_settings.custom_field.enabled", "custom_field_settings.custom_field.enum_options", "custom_field_settings.custom_field.enum_options.color", "custom_field_settings.custom_field.enum_options.enabled", "custom_field_settings.custom_field.enum_options.name", "custom_field_settings.custom_field.enum_value", "custom_field_settings.custom_field.enum_value.color", "custom_field_settings.custom_field.enum_value.enabled", "custom_field_settings.custom_field.enum_value.name", "custom_field_settings.custom_field.format", "custom_field_settings.custom_field.has_notifications_enabled", "custom_field_settings.custom_field.id_prefix", "custom_field_settings.custom_field.is_formula_field", "custom_field_settings.custom_field.is_global_to_workspace", "custom_field_settings.custom_field.is_value_read_only", "custom_field_settings.custom_field.multi_enum_values", "custom_field_settings.custom_field.multi_enum_values.color", "custom_field_settings.custom_field.multi_enum_values.enabled", "custom_field_settings.custom_field.multi_enum_values.name", "custom_field_settings.custom_field.name", "custom_field_settings.custom_field.number_value", "custom_field_settings.custom_field.people_value", "custom_field_settings.custom_field.people_value.name", "custom_field_settings.custom_field.precision", "custom_field_settings.custom_field.representation_type", "custom_field_settings.custom_field.resource_subtype", "custom_field_settings.custom_field.text_value", "custom_field_settings.custom_field.type", "custom_field_settings.is_important", "custom_field_settings.parent", "custom_field_settings.parent.name", "custom_field_settings.project", "custom_field_settings.project.name", "custom_fields", "custom_fields.date_value", "custom_fields.date_value.date", "custom_fields.date_value.date_time", "custom_fields.display_value", "custom_fields.enabled", "custom_fields.enum_options", "custom_fields.enum_options.color", "custom_fields.enum_options.enabled", "custom_fields.enum_options.name", "custom_fields.enum_value", "custom_fields.enum_value.color", "custom_fields.enum_value.enabled", "custom_fields.enum_value.name", "custom_fields.id_prefix", "custom_fields.is_formula_field", "custom_fields.multi_enum_values", "custom_fields.multi_enum_values.color", "custom_fields.multi_enum_values.enabled", "custom_fields.multi_enum_values.name", "custom_fields.name", "custom_fields.number_value", "custom_fields.representation_type", "custom_fields.resource_subtype", "custom_fields.text_value", "custom_fields.type", "default_access_level", "default_view", "due_date", "due_on", "followers", "followers.name", "html_notes", "icon", "members", "members.name", "minimum_access_level_for_customization", "minimum_access_level_for_sharing", "modified_at", "name", "notes", "offset", "owner", "path", "permalink_url", "privacy_setting", "project_brief", "public", "start_on", "team", "team.name", "uri", "workspace", "workspace.name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### team_gid: `str`<a id="team_gid-str"></a>

Globally unique identifier for the team.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### limit: `int`<a id="limit-int"></a>

Results per page. The number of objects to return per page. The value must be between 1 and 100.

##### offset: `str`<a id="offset-str"></a>

Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'

##### archived: `bool`<a id="archived-bool"></a>

Only return projects whose `archived` field takes on the value of this parameter.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`ProjectsGetTeamProjectsResponse`](./asana_python_sdk/pydantic/projects_get_team_projects_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teams/{team_gid}/projects` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.projects.list_multiple`<a id="asanaprojectslist_multiple"></a>

Returns the compact project records for some filtered set of projects. Use one or more of the parameters provided to filter the projects returned.
*Note: This endpoint may timeout for large domains. Try filtering by team!*

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_multiple_response = asana.projects.list_multiple(
    opt_pretty=True,
    limit=50,
    offset="eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9",
    workspace="1331",
    team="14916",
    archived=False,
    opt_fields=["archived", "color", "completed", "completed_at", "completed_by", "completed_by.name", "created_at", "created_from_template", "created_from_template.name", "current_status", "current_status.author", "current_status.author.name", "current_status.color", "current_status.created_at", "current_status.created_by", "current_status.created_by.name", "current_status.html_text", "current_status.modified_at", "current_status.text", "current_status.title", "current_status_update", "current_status_update.resource_subtype", "current_status_update.title", "custom_field_settings", "custom_field_settings.custom_field", "custom_field_settings.custom_field.asana_created_field", "custom_field_settings.custom_field.created_by", "custom_field_settings.custom_field.created_by.name", "custom_field_settings.custom_field.currency_code", "custom_field_settings.custom_field.custom_label", "custom_field_settings.custom_field.custom_label_position", "custom_field_settings.custom_field.date_value", "custom_field_settings.custom_field.date_value.date", "custom_field_settings.custom_field.date_value.date_time", "custom_field_settings.custom_field.description", "custom_field_settings.custom_field.display_value", "custom_field_settings.custom_field.enabled", "custom_field_settings.custom_field.enum_options", "custom_field_settings.custom_field.enum_options.color", "custom_field_settings.custom_field.enum_options.enabled", "custom_field_settings.custom_field.enum_options.name", "custom_field_settings.custom_field.enum_value", "custom_field_settings.custom_field.enum_value.color", "custom_field_settings.custom_field.enum_value.enabled", "custom_field_settings.custom_field.enum_value.name", "custom_field_settings.custom_field.format", "custom_field_settings.custom_field.has_notifications_enabled", "custom_field_settings.custom_field.id_prefix", "custom_field_settings.custom_field.is_formula_field", "custom_field_settings.custom_field.is_global_to_workspace", "custom_field_settings.custom_field.is_value_read_only", "custom_field_settings.custom_field.multi_enum_values", "custom_field_settings.custom_field.multi_enum_values.color", "custom_field_settings.custom_field.multi_enum_values.enabled", "custom_field_settings.custom_field.multi_enum_values.name", "custom_field_settings.custom_field.name", "custom_field_settings.custom_field.number_value", "custom_field_settings.custom_field.people_value", "custom_field_settings.custom_field.people_value.name", "custom_field_settings.custom_field.precision", "custom_field_settings.custom_field.representation_type", "custom_field_settings.custom_field.resource_subtype", "custom_field_settings.custom_field.text_value", "custom_field_settings.custom_field.type", "custom_field_settings.is_important", "custom_field_settings.parent", "custom_field_settings.parent.name", "custom_field_settings.project", "custom_field_settings.project.name", "custom_fields", "custom_fields.date_value", "custom_fields.date_value.date", "custom_fields.date_value.date_time", "custom_fields.display_value", "custom_fields.enabled", "custom_fields.enum_options", "custom_fields.enum_options.color", "custom_fields.enum_options.enabled", "custom_fields.enum_options.name", "custom_fields.enum_value", "custom_fields.enum_value.color", "custom_fields.enum_value.enabled", "custom_fields.enum_value.name", "custom_fields.id_prefix", "custom_fields.is_formula_field", "custom_fields.multi_enum_values", "custom_fields.multi_enum_values.color", "custom_fields.multi_enum_values.enabled", "custom_fields.multi_enum_values.name", "custom_fields.name", "custom_fields.number_value", "custom_fields.representation_type", "custom_fields.resource_subtype", "custom_fields.text_value", "custom_fields.type", "default_access_level", "default_view", "due_date", "due_on", "followers", "followers.name", "html_notes", "icon", "members", "members.name", "minimum_access_level_for_customization", "minimum_access_level_for_sharing", "modified_at", "name", "notes", "offset", "owner", "path", "permalink_url", "privacy_setting", "project_brief", "public", "start_on", "team", "team.name", "uri", "workspace", "workspace.name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### limit: `int`<a id="limit-int"></a>

Results per page. The number of objects to return per page. The value must be between 1 and 100.

##### offset: `str`<a id="offset-str"></a>

Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'

##### workspace: `str`<a id="workspace-str"></a>

The workspace or organization to filter projects on.

##### team: `str`<a id="team-str"></a>

The team to filter projects on.

##### archived: `bool`<a id="archived-bool"></a>

Only return projects whose `archived` field takes on the value of this parameter.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`ProjectsListMultipleResponse`](./asana_python_sdk/pydantic/projects_list_multiple_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/projects` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.projects.remove_custom_field`<a id="asanaprojectsremove_custom_field"></a>

Removes a custom field setting from a project.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_custom_field_response = asana.projects.remove_custom_field(
    project_gid="1331",
    data={
        "custom_field": "14916",
    },
    opt_pretty=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_gid: `str`<a id="project_gid-str"></a>

Globally unique identifier for the project.

##### data: [`RemoveCustomFieldSettingRequest`](./asana_python_sdk/type/remove_custom_field_setting_request.py)<a id="data-removecustomfieldsettingrequestasana_python_sdktyperemove_custom_field_setting_requestpy"></a>


##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ProjectsRemoveCustomFieldRequest`](./asana_python_sdk/type/projects_remove_custom_field_request.py)
Information about the custom field setting being removed.

#### 🔄 Return<a id="🔄-return"></a>

[`ProjectsRemoveCustomFieldResponse`](./asana_python_sdk/pydantic/projects_remove_custom_field_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/projects/{project_gid}/removeCustomFieldSetting` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.projects.remove_members_from_project`<a id="asanaprojectsremove_members_from_project"></a>

Removes the specified list of users from members of the project.
Returns the updated project record.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_members_from_project_response = asana.projects.remove_members_from_project(
    project_gid="1331",
    data={
        "members": "521621,621373",
    },
    opt_pretty=True,
    opt_fields=["archived", "color", "completed", "completed_at", "completed_by", "completed_by.name", "created_at", "created_from_template", "created_from_template.name", "current_status", "current_status.author", "current_status.author.name", "current_status.color", "current_status.created_at", "current_status.created_by", "current_status.created_by.name", "current_status.html_text", "current_status.modified_at", "current_status.text", "current_status.title", "current_status_update", "current_status_update.resource_subtype", "current_status_update.title", "custom_field_settings", "custom_field_settings.custom_field", "custom_field_settings.custom_field.asana_created_field", "custom_field_settings.custom_field.created_by", "custom_field_settings.custom_field.created_by.name", "custom_field_settings.custom_field.currency_code", "custom_field_settings.custom_field.custom_label", "custom_field_settings.custom_field.custom_label_position", "custom_field_settings.custom_field.date_value", "custom_field_settings.custom_field.date_value.date", "custom_field_settings.custom_field.date_value.date_time", "custom_field_settings.custom_field.description", "custom_field_settings.custom_field.display_value", "custom_field_settings.custom_field.enabled", "custom_field_settings.custom_field.enum_options", "custom_field_settings.custom_field.enum_options.color", "custom_field_settings.custom_field.enum_options.enabled", "custom_field_settings.custom_field.enum_options.name", "custom_field_settings.custom_field.enum_value", "custom_field_settings.custom_field.enum_value.color", "custom_field_settings.custom_field.enum_value.enabled", "custom_field_settings.custom_field.enum_value.name", "custom_field_settings.custom_field.format", "custom_field_settings.custom_field.has_notifications_enabled", "custom_field_settings.custom_field.id_prefix", "custom_field_settings.custom_field.is_formula_field", "custom_field_settings.custom_field.is_global_to_workspace", "custom_field_settings.custom_field.is_value_read_only", "custom_field_settings.custom_field.multi_enum_values", "custom_field_settings.custom_field.multi_enum_values.color", "custom_field_settings.custom_field.multi_enum_values.enabled", "custom_field_settings.custom_field.multi_enum_values.name", "custom_field_settings.custom_field.name", "custom_field_settings.custom_field.number_value", "custom_field_settings.custom_field.people_value", "custom_field_settings.custom_field.people_value.name", "custom_field_settings.custom_field.precision", "custom_field_settings.custom_field.representation_type", "custom_field_settings.custom_field.resource_subtype", "custom_field_settings.custom_field.text_value", "custom_field_settings.custom_field.type", "custom_field_settings.is_important", "custom_field_settings.parent", "custom_field_settings.parent.name", "custom_field_settings.project", "custom_field_settings.project.name", "custom_fields", "custom_fields.date_value", "custom_fields.date_value.date", "custom_fields.date_value.date_time", "custom_fields.display_value", "custom_fields.enabled", "custom_fields.enum_options", "custom_fields.enum_options.color", "custom_fields.enum_options.enabled", "custom_fields.enum_options.name", "custom_fields.enum_value", "custom_fields.enum_value.color", "custom_fields.enum_value.enabled", "custom_fields.enum_value.name", "custom_fields.id_prefix", "custom_fields.is_formula_field", "custom_fields.multi_enum_values", "custom_fields.multi_enum_values.color", "custom_fields.multi_enum_values.enabled", "custom_fields.multi_enum_values.name", "custom_fields.name", "custom_fields.number_value", "custom_fields.representation_type", "custom_fields.resource_subtype", "custom_fields.text_value", "custom_fields.type", "default_access_level", "default_view", "due_date", "due_on", "followers", "followers.name", "html_notes", "icon", "members", "members.name", "minimum_access_level_for_customization", "minimum_access_level_for_sharing", "modified_at", "name", "notes", "owner", "permalink_url", "privacy_setting", "project_brief", "public", "start_on", "team", "team.name", "workspace", "workspace.name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_gid: `str`<a id="project_gid-str"></a>

Globally unique identifier for the project.

##### data: [`RemoveMembersRequest`](./asana_python_sdk/type/remove_members_request.py)<a id="data-removemembersrequestasana_python_sdktyperemove_members_requestpy"></a>


##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ProjectsRemoveMembersFromProjectRequest`](./asana_python_sdk/type/projects_remove_members_from_project_request.py)
Information about the members being removed.

#### 🔄 Return<a id="🔄-return"></a>

[`ProjectsRemoveMembersFromProjectResponse`](./asana_python_sdk/pydantic/projects_remove_members_from_project_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/projects/{project_gid}/removeMembers` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.projects.remove_project_followers`<a id="asanaprojectsremove_project_followers"></a>

Removes the specified list of users from following the project, this will not affect project membership status.
Returns the updated project record.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_project_followers_response = asana.projects.remove_project_followers(
    project_gid="1331",
    data={
        "followers": "521621,621373",
    },
    opt_pretty=True,
    opt_fields=["archived", "color", "completed", "completed_at", "completed_by", "completed_by.name", "created_at", "created_from_template", "created_from_template.name", "current_status", "current_status.author", "current_status.author.name", "current_status.color", "current_status.created_at", "current_status.created_by", "current_status.created_by.name", "current_status.html_text", "current_status.modified_at", "current_status.text", "current_status.title", "current_status_update", "current_status_update.resource_subtype", "current_status_update.title", "custom_field_settings", "custom_field_settings.custom_field", "custom_field_settings.custom_field.asana_created_field", "custom_field_settings.custom_field.created_by", "custom_field_settings.custom_field.created_by.name", "custom_field_settings.custom_field.currency_code", "custom_field_settings.custom_field.custom_label", "custom_field_settings.custom_field.custom_label_position", "custom_field_settings.custom_field.date_value", "custom_field_settings.custom_field.date_value.date", "custom_field_settings.custom_field.date_value.date_time", "custom_field_settings.custom_field.description", "custom_field_settings.custom_field.display_value", "custom_field_settings.custom_field.enabled", "custom_field_settings.custom_field.enum_options", "custom_field_settings.custom_field.enum_options.color", "custom_field_settings.custom_field.enum_options.enabled", "custom_field_settings.custom_field.enum_options.name", "custom_field_settings.custom_field.enum_value", "custom_field_settings.custom_field.enum_value.color", "custom_field_settings.custom_field.enum_value.enabled", "custom_field_settings.custom_field.enum_value.name", "custom_field_settings.custom_field.format", "custom_field_settings.custom_field.has_notifications_enabled", "custom_field_settings.custom_field.id_prefix", "custom_field_settings.custom_field.is_formula_field", "custom_field_settings.custom_field.is_global_to_workspace", "custom_field_settings.custom_field.is_value_read_only", "custom_field_settings.custom_field.multi_enum_values", "custom_field_settings.custom_field.multi_enum_values.color", "custom_field_settings.custom_field.multi_enum_values.enabled", "custom_field_settings.custom_field.multi_enum_values.name", "custom_field_settings.custom_field.name", "custom_field_settings.custom_field.number_value", "custom_field_settings.custom_field.people_value", "custom_field_settings.custom_field.people_value.name", "custom_field_settings.custom_field.precision", "custom_field_settings.custom_field.representation_type", "custom_field_settings.custom_field.resource_subtype", "custom_field_settings.custom_field.text_value", "custom_field_settings.custom_field.type", "custom_field_settings.is_important", "custom_field_settings.parent", "custom_field_settings.parent.name", "custom_field_settings.project", "custom_field_settings.project.name", "custom_fields", "custom_fields.date_value", "custom_fields.date_value.date", "custom_fields.date_value.date_time", "custom_fields.display_value", "custom_fields.enabled", "custom_fields.enum_options", "custom_fields.enum_options.color", "custom_fields.enum_options.enabled", "custom_fields.enum_options.name", "custom_fields.enum_value", "custom_fields.enum_value.color", "custom_fields.enum_value.enabled", "custom_fields.enum_value.name", "custom_fields.id_prefix", "custom_fields.is_formula_field", "custom_fields.multi_enum_values", "custom_fields.multi_enum_values.color", "custom_fields.multi_enum_values.enabled", "custom_fields.multi_enum_values.name", "custom_fields.name", "custom_fields.number_value", "custom_fields.representation_type", "custom_fields.resource_subtype", "custom_fields.text_value", "custom_fields.type", "default_access_level", "default_view", "due_date", "due_on", "followers", "followers.name", "html_notes", "icon", "members", "members.name", "minimum_access_level_for_customization", "minimum_access_level_for_sharing", "modified_at", "name", "notes", "owner", "permalink_url", "privacy_setting", "project_brief", "public", "start_on", "team", "team.name", "workspace", "workspace.name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_gid: `str`<a id="project_gid-str"></a>

Globally unique identifier for the project.

##### data: [`RemoveFollowersRequest`](./asana_python_sdk/type/remove_followers_request.py)<a id="data-removefollowersrequestasana_python_sdktyperemove_followers_requestpy"></a>


##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ProjectsRemoveProjectFollowersRequest`](./asana_python_sdk/type/projects_remove_project_followers_request.py)
Information about the followers being removed.

#### 🔄 Return<a id="🔄-return"></a>

[`ProjectsRemoveProjectFollowersResponse`](./asana_python_sdk/pydantic/projects_remove_project_followers_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/projects/{project_gid}/removeFollowers` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.projects.task_projects_list`<a id="asanaprojectstask_projects_list"></a>

Returns a compact representation of all of the projects the task is in.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
task_projects_list_response = asana.projects.task_projects_list(
    task_gid="321654",
    opt_pretty=True,
    limit=50,
    offset="eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9",
    opt_fields=["archived", "color", "completed", "completed_at", "completed_by", "completed_by.name", "created_at", "created_from_template", "created_from_template.name", "current_status", "current_status.author", "current_status.author.name", "current_status.color", "current_status.created_at", "current_status.created_by", "current_status.created_by.name", "current_status.html_text", "current_status.modified_at", "current_status.text", "current_status.title", "current_status_update", "current_status_update.resource_subtype", "current_status_update.title", "custom_field_settings", "custom_field_settings.custom_field", "custom_field_settings.custom_field.asana_created_field", "custom_field_settings.custom_field.created_by", "custom_field_settings.custom_field.created_by.name", "custom_field_settings.custom_field.currency_code", "custom_field_settings.custom_field.custom_label", "custom_field_settings.custom_field.custom_label_position", "custom_field_settings.custom_field.date_value", "custom_field_settings.custom_field.date_value.date", "custom_field_settings.custom_field.date_value.date_time", "custom_field_settings.custom_field.description", "custom_field_settings.custom_field.display_value", "custom_field_settings.custom_field.enabled", "custom_field_settings.custom_field.enum_options", "custom_field_settings.custom_field.enum_options.color", "custom_field_settings.custom_field.enum_options.enabled", "custom_field_settings.custom_field.enum_options.name", "custom_field_settings.custom_field.enum_value", "custom_field_settings.custom_field.enum_value.color", "custom_field_settings.custom_field.enum_value.enabled", "custom_field_settings.custom_field.enum_value.name", "custom_field_settings.custom_field.format", "custom_field_settings.custom_field.has_notifications_enabled", "custom_field_settings.custom_field.id_prefix", "custom_field_settings.custom_field.is_formula_field", "custom_field_settings.custom_field.is_global_to_workspace", "custom_field_settings.custom_field.is_value_read_only", "custom_field_settings.custom_field.multi_enum_values", "custom_field_settings.custom_field.multi_enum_values.color", "custom_field_settings.custom_field.multi_enum_values.enabled", "custom_field_settings.custom_field.multi_enum_values.name", "custom_field_settings.custom_field.name", "custom_field_settings.custom_field.number_value", "custom_field_settings.custom_field.people_value", "custom_field_settings.custom_field.people_value.name", "custom_field_settings.custom_field.precision", "custom_field_settings.custom_field.representation_type", "custom_field_settings.custom_field.resource_subtype", "custom_field_settings.custom_field.text_value", "custom_field_settings.custom_field.type", "custom_field_settings.is_important", "custom_field_settings.parent", "custom_field_settings.parent.name", "custom_field_settings.project", "custom_field_settings.project.name", "custom_fields", "custom_fields.date_value", "custom_fields.date_value.date", "custom_fields.date_value.date_time", "custom_fields.display_value", "custom_fields.enabled", "custom_fields.enum_options", "custom_fields.enum_options.color", "custom_fields.enum_options.enabled", "custom_fields.enum_options.name", "custom_fields.enum_value", "custom_fields.enum_value.color", "custom_fields.enum_value.enabled", "custom_fields.enum_value.name", "custom_fields.id_prefix", "custom_fields.is_formula_field", "custom_fields.multi_enum_values", "custom_fields.multi_enum_values.color", "custom_fields.multi_enum_values.enabled", "custom_fields.multi_enum_values.name", "custom_fields.name", "custom_fields.number_value", "custom_fields.representation_type", "custom_fields.resource_subtype", "custom_fields.text_value", "custom_fields.type", "default_access_level", "default_view", "due_date", "due_on", "followers", "followers.name", "html_notes", "icon", "members", "members.name", "minimum_access_level_for_customization", "minimum_access_level_for_sharing", "modified_at", "name", "notes", "offset", "owner", "path", "permalink_url", "privacy_setting", "project_brief", "public", "start_on", "team", "team.name", "uri", "workspace", "workspace.name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### task_gid: `str`<a id="task_gid-str"></a>

The task to operate on.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### limit: `int`<a id="limit-int"></a>

Results per page. The number of objects to return per page. The value must be between 1 and 100.

##### offset: `str`<a id="offset-str"></a>

Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`ProjectsTaskProjectsListResponse`](./asana_python_sdk/pydantic/projects_task_projects_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tasks/{task_gid}/projects` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.projects.update_project_record`<a id="asanaprojectsupdate_project_record"></a>

A specific, existing project can be updated by making a PUT request on
the URL for that project. Only the fields provided in the `data` block
will be updated; any unspecified fields will remain unchanged.

When using this method, it is best to specify only those fields you wish
to change, or else you may overwrite changes made by another user since
you last retrieved the task.

Returns the complete updated project record.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_project_record_response = asana.projects.update_project_record(
    project_gid="1331",
    data=None,
    opt_pretty=True,
    opt_fields=["archived", "color", "completed", "completed_at", "completed_by", "completed_by.name", "created_at", "created_from_template", "created_from_template.name", "current_status", "current_status.author", "current_status.author.name", "current_status.color", "current_status.created_at", "current_status.created_by", "current_status.created_by.name", "current_status.html_text", "current_status.modified_at", "current_status.text", "current_status.title", "current_status_update", "current_status_update.resource_subtype", "current_status_update.title", "custom_field_settings", "custom_field_settings.custom_field", "custom_field_settings.custom_field.asana_created_field", "custom_field_settings.custom_field.created_by", "custom_field_settings.custom_field.created_by.name", "custom_field_settings.custom_field.currency_code", "custom_field_settings.custom_field.custom_label", "custom_field_settings.custom_field.custom_label_position", "custom_field_settings.custom_field.date_value", "custom_field_settings.custom_field.date_value.date", "custom_field_settings.custom_field.date_value.date_time", "custom_field_settings.custom_field.description", "custom_field_settings.custom_field.display_value", "custom_field_settings.custom_field.enabled", "custom_field_settings.custom_field.enum_options", "custom_field_settings.custom_field.enum_options.color", "custom_field_settings.custom_field.enum_options.enabled", "custom_field_settings.custom_field.enum_options.name", "custom_field_settings.custom_field.enum_value", "custom_field_settings.custom_field.enum_value.color", "custom_field_settings.custom_field.enum_value.enabled", "custom_field_settings.custom_field.enum_value.name", "custom_field_settings.custom_field.format", "custom_field_settings.custom_field.has_notifications_enabled", "custom_field_settings.custom_field.id_prefix", "custom_field_settings.custom_field.is_formula_field", "custom_field_settings.custom_field.is_global_to_workspace", "custom_field_settings.custom_field.is_value_read_only", "custom_field_settings.custom_field.multi_enum_values", "custom_field_settings.custom_field.multi_enum_values.color", "custom_field_settings.custom_field.multi_enum_values.enabled", "custom_field_settings.custom_field.multi_enum_values.name", "custom_field_settings.custom_field.name", "custom_field_settings.custom_field.number_value", "custom_field_settings.custom_field.people_value", "custom_field_settings.custom_field.people_value.name", "custom_field_settings.custom_field.precision", "custom_field_settings.custom_field.representation_type", "custom_field_settings.custom_field.resource_subtype", "custom_field_settings.custom_field.text_value", "custom_field_settings.custom_field.type", "custom_field_settings.is_important", "custom_field_settings.parent", "custom_field_settings.parent.name", "custom_field_settings.project", "custom_field_settings.project.name", "custom_fields", "custom_fields.date_value", "custom_fields.date_value.date", "custom_fields.date_value.date_time", "custom_fields.display_value", "custom_fields.enabled", "custom_fields.enum_options", "custom_fields.enum_options.color", "custom_fields.enum_options.enabled", "custom_fields.enum_options.name", "custom_fields.enum_value", "custom_fields.enum_value.color", "custom_fields.enum_value.enabled", "custom_fields.enum_value.name", "custom_fields.id_prefix", "custom_fields.is_formula_field", "custom_fields.multi_enum_values", "custom_fields.multi_enum_values.color", "custom_fields.multi_enum_values.enabled", "custom_fields.multi_enum_values.name", "custom_fields.name", "custom_fields.number_value", "custom_fields.representation_type", "custom_fields.resource_subtype", "custom_fields.text_value", "custom_fields.type", "default_access_level", "default_view", "due_date", "due_on", "followers", "followers.name", "html_notes", "icon", "members", "members.name", "minimum_access_level_for_customization", "minimum_access_level_for_sharing", "modified_at", "name", "notes", "owner", "permalink_url", "privacy_setting", "project_brief", "public", "start_on", "team", "team.name", "workspace", "workspace.name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_gid: `str`<a id="project_gid-str"></a>

Globally unique identifier for the project.

##### data: `ProjectUpdateRequest`<a id="data-projectupdaterequest"></a>

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ProjectsUpdateProjectRecordRequest`](./asana_python_sdk/type/projects_update_project_record_request.py)
The updated fields for the project.

#### 🔄 Return<a id="🔄-return"></a>

[`ProjectsUpdateProjectRecordResponse`](./asana_python_sdk/pydantic/projects_update_project_record_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/projects/{project_gid}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.rules.trigger_rule_request`<a id="asanarulestrigger_rule_request"></a>

Trigger a rule which uses an ["incoming web request"](https://developers.asana.com/reference/rest-api-reference) trigger.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trigger_rule_request_response = asana.rules.trigger_rule_request(
    rule_trigger_gid="12345",
    data={
        "resource": "12345",
        "action_data": {
            "jira_ticket_name": "Test",
            "jira_ticket_id": "123",
        },
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### rule_trigger_gid: `str`<a id="rule_trigger_gid-str"></a>

The ID of the incoming web request trigger. This value is a path parameter that is automatically generated for the API endpoint.

##### data: [`RuleTriggerRequest`](./asana_python_sdk/type/rule_trigger_request.py)<a id="data-ruletriggerrequestasana_python_sdktyperule_trigger_requestpy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`RulesTriggerRuleRequestRequest`](./asana_python_sdk/type/rules_trigger_rule_request_request.py)
A dictionary of variables accessible from within the rule.

#### 🔄 Return<a id="🔄-return"></a>

[`RulesTriggerRuleRequestResponse`](./asana_python_sdk/pydantic/rules_trigger_rule_request_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/rule_triggers/{rule_trigger_gid}/run` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.sections.add_task_to_section`<a id="asanasectionsadd_task_to_section"></a>

Add a task to a specific, existing section. This will remove the task from other sections of the project.

The task will be inserted at the top of a section unless an insert_before or insert_after parameter is declared.

This does not work for separators (tasks with the resource_subtype of section).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_task_to_section_response = asana.sections.add_task_to_section(
    section_gid="321654",
    data={
        "task": "123456",
        "insert_before": "86420",
        "insert_after": "987654",
    },
    opt_pretty=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### section_gid: `str`<a id="section_gid-str"></a>

The globally unique identifier for the section.

##### data: [`SectionTaskInsertRequest`](./asana_python_sdk/type/section_task_insert_request.py)<a id="data-sectiontaskinsertrequestasana_python_sdktypesection_task_insert_requestpy"></a>


##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SectionsAddTaskToSectionRequest`](./asana_python_sdk/type/sections_add_task_to_section_request.py)
The task and optionally the insert location.

#### 🔄 Return<a id="🔄-return"></a>

[`SectionsAddTaskToSectionResponse`](./asana_python_sdk/pydantic/sections_add_task_to_section_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/sections/{section_gid}/addTask` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.sections.create_new_section`<a id="asanasectionscreate_new_section"></a>

Creates a new section in a project.
Returns the full record of the newly created section.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_section_response = asana.sections.create_new_section(
    project_gid="1331",
    data={
        "name": "Next Actions",
        "insert_before": "86420",
        "insert_after": "987654",
    },
    opt_pretty=True,
    opt_fields=["created_at", "name", "project", "project.name", "projects", "projects.name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_gid: `str`<a id="project_gid-str"></a>

Globally unique identifier for the project.

##### data: [`SectionRequest`](./asana_python_sdk/type/section_request.py)<a id="data-sectionrequestasana_python_sdktypesection_requestpy"></a>


##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SectionsCreateNewSectionRequest`](./asana_python_sdk/type/sections_create_new_section_request.py)
The section to create.

#### 🔄 Return<a id="🔄-return"></a>

[`SectionsCreateNewSectionResponse`](./asana_python_sdk/pydantic/sections_create_new_section_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/projects/{project_gid}/sections` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.sections.delete_section`<a id="asanasectionsdelete_section"></a>

A specific, existing section can be deleted by making a DELETE request on
the URL for that section.

Note that sections must be empty to be deleted.

The last remaining section cannot be deleted.

Returns an empty data block.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_section_response = asana.sections.delete_section(
    section_gid="321654",
    opt_pretty=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### section_gid: `str`<a id="section_gid-str"></a>

The globally unique identifier for the section.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

#### 🔄 Return<a id="🔄-return"></a>

[`SectionsDeleteSectionResponse`](./asana_python_sdk/pydantic/sections_delete_section_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/sections/{section_gid}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.sections.get_record`<a id="asanasectionsget_record"></a>

Returns the complete record for a single section.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_record_response = asana.sections.get_record(
    section_gid="321654",
    opt_pretty=True,
    opt_fields=["created_at", "name", "project", "project.name", "projects", "projects.name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### section_gid: `str`<a id="section_gid-str"></a>

The globally unique identifier for the section.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`SectionsGetRecordResponse`](./asana_python_sdk/pydantic/sections_get_record_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/sections/{section_gid}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.sections.list_project_sections`<a id="asanasectionslist_project_sections"></a>

Returns the compact records for all sections in the specified project.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_project_sections_response = asana.sections.list_project_sections(
    project_gid="1331",
    opt_pretty=True,
    limit=50,
    offset="eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9",
    opt_fields=["created_at", "name", "offset", "path", "project", "project.name", "projects", "projects.name", "uri"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_gid: `str`<a id="project_gid-str"></a>

Globally unique identifier for the project.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### limit: `int`<a id="limit-int"></a>

Results per page. The number of objects to return per page. The value must be between 1 and 100.

##### offset: `str`<a id="offset-str"></a>

Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`SectionsListProjectSectionsResponse`](./asana_python_sdk/pydantic/sections_list_project_sections_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/projects/{project_gid}/sections` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.sections.move_or_insert`<a id="asanasectionsmove_or_insert"></a>

Move sections relative to each other. One of
`before_section` or `after_section` is required.

Sections cannot be moved between projects.

Returns an empty data block.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
move_or_insert_response = asana.sections.move_or_insert(
    project_gid="1331",
    data={
        "section": "321654",
        "before_section": "86420",
        "after_section": "987654",
    },
    opt_pretty=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_gid: `str`<a id="project_gid-str"></a>

Globally unique identifier for the project.

##### data: [`ProjectSectionInsertRequest`](./asana_python_sdk/type/project_section_insert_request.py)<a id="data-projectsectioninsertrequestasana_python_sdktypeproject_section_insert_requestpy"></a>


##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SectionsMoveOrInsertRequest`](./asana_python_sdk/type/sections_move_or_insert_request.py)
The section's move action.

#### 🔄 Return<a id="🔄-return"></a>

[`SectionsMoveOrInsertResponse`](./asana_python_sdk/pydantic/sections_move_or_insert_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/projects/{project_gid}/sections/insert` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.sections.update_section_record`<a id="asanasectionsupdate_section_record"></a>

A specific, existing section can be updated by making a PUT request on
the URL for that project. Only the fields provided in the `data` block
will be updated; any unspecified fields will remain unchanged. (note that
at this time, the only field that can be updated is the `name` field.)

When using this method, it is best to specify only those fields you wish
to change, or else you may overwrite changes made by another user since
you last retrieved the task.

Returns the complete updated section record.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_section_record_response = asana.sections.update_section_record(
    section_gid="321654",
    data={
        "name": "Next Actions",
        "insert_before": "86420",
        "insert_after": "987654",
    },
    opt_pretty=True,
    opt_fields=["created_at", "name", "project", "project.name", "projects", "projects.name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### section_gid: `str`<a id="section_gid-str"></a>

The globally unique identifier for the section.

##### data: [`SectionRequest`](./asana_python_sdk/type/section_request.py)<a id="data-sectionrequestasana_python_sdktypesection_requestpy"></a>


##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SectionsUpdateSectionRecordRequest`](./asana_python_sdk/type/sections_update_section_record_request.py)
The section to create.

#### 🔄 Return<a id="🔄-return"></a>

[`SectionsUpdateSectionRecordResponse`](./asana_python_sdk/pydantic/sections_update_section_record_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/sections/{section_gid}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.status_updates.create_new_status_update_record`<a id="asanastatus_updatescreate_new_status_update_record"></a>

Creates a new status update on an object.
Returns the full record of the newly created status update.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_status_update_record_response = asana.status_updates.create_new_status_update_record(
    data=None,
    opt_pretty=True,
    limit=50,
    offset="eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9",
    opt_fields=["author", "author.name", "created_at", "created_by", "created_by.name", "hearted", "hearts", "hearts.user", "hearts.user.name", "html_text", "liked", "likes", "likes.user", "likes.user.name", "modified_at", "num_hearts", "num_likes", "parent", "parent.name", "resource_subtype", "status_type", "text", "title"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### data: `StatusUpdateRequest`<a id="data-statusupdaterequest"></a>

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### limit: `int`<a id="limit-int"></a>

Results per page. The number of objects to return per page. The value must be between 1 and 100.

##### offset: `str`<a id="offset-str"></a>

Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`StatusUpdatesCreateNewStatusUpdateRecordRequest`](./asana_python_sdk/type/status_updates_create_new_status_update_record_request.py)
The status update to create.

#### 🔄 Return<a id="🔄-return"></a>

[`StatusUpdatesCreateNewStatusUpdateRecordResponse`](./asana_python_sdk/pydantic/status_updates_create_new_status_update_record_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/status_updates` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.status_updates.delete_specific_status_update`<a id="asanastatus_updatesdelete_specific_status_update"></a>

Deletes a specific, existing status update.

Returns an empty data record.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_specific_status_update_response = asana.status_updates.delete_specific_status_update(
    status_update_gid="321654",
    opt_pretty=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### status_update_gid: `str`<a id="status_update_gid-str"></a>

The status update to get.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

#### 🔄 Return<a id="🔄-return"></a>

[`StatusUpdatesDeleteSpecificStatusUpdateResponse`](./asana_python_sdk/pydantic/status_updates_delete_specific_status_update_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/status_updates/{status_update_gid}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.status_updates.get_compact_records`<a id="asanastatus_updatesget_compact_records"></a>

Returns the compact status update records for all updates on the object.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_compact_records_response = asana.status_updates.get_compact_records(
    parent="159874",
    opt_pretty=True,
    limit=50,
    offset="eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9",
    created_since="2012-02-22T02:06:58.158Z",
    opt_fields=["author", "author.name", "created_at", "created_by", "created_by.name", "hearted", "hearts", "hearts.user", "hearts.user.name", "html_text", "liked", "likes", "likes.user", "likes.user.name", "modified_at", "num_hearts", "num_likes", "offset", "parent", "parent.name", "path", "resource_subtype", "status_type", "text", "title", "uri"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### parent: `str`<a id="parent-str"></a>

Globally unique identifier for object to fetch statuses from. Must be a GID for a project, portfolio, or goal.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### limit: `int`<a id="limit-int"></a>

Results per page. The number of objects to return per page. The value must be between 1 and 100.

##### offset: `str`<a id="offset-str"></a>

Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'

##### created_since: `datetime`<a id="created_since-datetime"></a>

Only return statuses that have been created since the given time.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`StatusUpdatesGetCompactRecordsResponse`](./asana_python_sdk/pydantic/status_updates_get_compact_records_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/status_updates` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.status_updates.get_record_by_id`<a id="asanastatus_updatesget_record_by_id"></a>

Returns the complete record for a single status update.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_record_by_id_response = asana.status_updates.get_record_by_id(
    status_update_gid="321654",
    opt_pretty=True,
    opt_fields=["author", "author.name", "created_at", "created_by", "created_by.name", "hearted", "hearts", "hearts.user", "hearts.user.name", "html_text", "liked", "likes", "likes.user", "likes.user.name", "modified_at", "num_hearts", "num_likes", "parent", "parent.name", "resource_subtype", "status_type", "text", "title"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### status_update_gid: `str`<a id="status_update_gid-str"></a>

The status update to get.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`StatusUpdatesGetRecordByIdResponse`](./asana_python_sdk/pydantic/status_updates_get_record_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/status_updates/{status_update_gid}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.stories.create_comment`<a id="asanastoriescreate_comment"></a>

Adds a story to a task. This endpoint currently only allows for comment
stories to be created. The comment will be authored by the currently
authenticated user, and timestamped when the server receives the request.

Returns the full record for the new story added to the task.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_comment_response = asana.stories.create_comment(
    task_gid="321654",
    data=None,
    opt_pretty=True,
    opt_fields=["assignee", "assignee.name", "created_at", "created_by", "created_by.name", "custom_field", "custom_field.date_value", "custom_field.date_value.date", "custom_field.date_value.date_time", "custom_field.display_value", "custom_field.enabled", "custom_field.enum_options", "custom_field.enum_options.color", "custom_field.enum_options.enabled", "custom_field.enum_options.name", "custom_field.enum_value", "custom_field.enum_value.color", "custom_field.enum_value.enabled", "custom_field.enum_value.name", "custom_field.id_prefix", "custom_field.is_formula_field", "custom_field.multi_enum_values", "custom_field.multi_enum_values.color", "custom_field.multi_enum_values.enabled", "custom_field.multi_enum_values.name", "custom_field.name", "custom_field.number_value", "custom_field.representation_type", "custom_field.resource_subtype", "custom_field.text_value", "custom_field.type", "dependency", "dependency.created_by", "dependency.name", "dependency.resource_subtype", "duplicate_of", "duplicate_of.created_by", "duplicate_of.name", "duplicate_of.resource_subtype", "duplicated_from", "duplicated_from.created_by", "duplicated_from.name", "duplicated_from.resource_subtype", "follower", "follower.name", "hearted", "hearts", "hearts.user", "hearts.user.name", "html_text", "is_editable", "is_edited", "is_pinned", "liked", "likes", "likes.user", "likes.user.name", "new_approval_status", "new_date_value", "new_dates", "new_dates.due_at", "new_dates.due_on", "new_dates.start_on", "new_enum_value", "new_enum_value.color", "new_enum_value.enabled", "new_enum_value.name", "new_multi_enum_values", "new_multi_enum_values.color", "new_multi_enum_values.enabled", "new_multi_enum_values.name", "new_name", "new_number_value", "new_people_value", "new_people_value.name", "new_resource_subtype", "new_section", "new_section.name", "new_text_value", "num_hearts", "num_likes", "old_approval_status", "old_date_value", "old_dates", "old_dates.due_at", "old_dates.due_on", "old_dates.start_on", "old_enum_value", "old_enum_value.color", "old_enum_value.enabled", "old_enum_value.name", "old_multi_enum_values", "old_multi_enum_values.color", "old_multi_enum_values.enabled", "old_multi_enum_values.name", "old_name", "old_number_value", "old_people_value", "old_people_value.name", "old_resource_subtype", "old_section", "old_section.name", "old_text_value", "previews", "previews.fallback", "previews.footer", "previews.header", "previews.header_link", "previews.html_text", "previews.text", "previews.title", "previews.title_link", "project", "project.name", "resource_subtype", "source", "sticker_name", "story", "story.created_at", "story.created_by", "story.created_by.name", "story.resource_subtype", "story.text", "tag", "tag.name", "target", "target.created_by", "target.name", "target.resource_subtype", "task", "task.created_by", "task.name", "task.resource_subtype", "text", "type"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### task_gid: `str`<a id="task_gid-str"></a>

The task to operate on.

##### data: [`StoryBase`](./asana_python_sdk/type/story_base.py)<a id="data-storybaseasana_python_sdktypestory_basepy"></a>


##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`StoriesCreateCommentRequest`](./asana_python_sdk/type/stories_create_comment_request.py)
The story to create.

#### 🔄 Return<a id="🔄-return"></a>

[`StoriesCreateCommentResponse`](./asana_python_sdk/pydantic/stories_create_comment_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tasks/{task_gid}/stories` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.stories.delete_story_record`<a id="asanastoriesdelete_story_record"></a>

Deletes a story. A user can only delete stories they have created.

Returns an empty data record.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_story_record_response = asana.stories.delete_story_record(
    story_gid="35678",
    opt_pretty=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### story_gid: `str`<a id="story_gid-str"></a>

Globally unique identifier for the story.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

#### 🔄 Return<a id="🔄-return"></a>

[`StoriesDeleteStoryRecordResponse`](./asana_python_sdk/pydantic/stories_delete_story_record_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/stories/{story_gid}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.stories.get_full_record`<a id="asanastoriesget_full_record"></a>

Returns the full record for a single story.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_full_record_response = asana.stories.get_full_record(
    story_gid="35678",
    opt_pretty=True,
    opt_fields=["assignee", "assignee.name", "created_at", "created_by", "created_by.name", "custom_field", "custom_field.date_value", "custom_field.date_value.date", "custom_field.date_value.date_time", "custom_field.display_value", "custom_field.enabled", "custom_field.enum_options", "custom_field.enum_options.color", "custom_field.enum_options.enabled", "custom_field.enum_options.name", "custom_field.enum_value", "custom_field.enum_value.color", "custom_field.enum_value.enabled", "custom_field.enum_value.name", "custom_field.id_prefix", "custom_field.is_formula_field", "custom_field.multi_enum_values", "custom_field.multi_enum_values.color", "custom_field.multi_enum_values.enabled", "custom_field.multi_enum_values.name", "custom_field.name", "custom_field.number_value", "custom_field.representation_type", "custom_field.resource_subtype", "custom_field.text_value", "custom_field.type", "dependency", "dependency.created_by", "dependency.name", "dependency.resource_subtype", "duplicate_of", "duplicate_of.created_by", "duplicate_of.name", "duplicate_of.resource_subtype", "duplicated_from", "duplicated_from.created_by", "duplicated_from.name", "duplicated_from.resource_subtype", "follower", "follower.name", "hearted", "hearts", "hearts.user", "hearts.user.name", "html_text", "is_editable", "is_edited", "is_pinned", "liked", "likes", "likes.user", "likes.user.name", "new_approval_status", "new_date_value", "new_dates", "new_dates.due_at", "new_dates.due_on", "new_dates.start_on", "new_enum_value", "new_enum_value.color", "new_enum_value.enabled", "new_enum_value.name", "new_multi_enum_values", "new_multi_enum_values.color", "new_multi_enum_values.enabled", "new_multi_enum_values.name", "new_name", "new_number_value", "new_people_value", "new_people_value.name", "new_resource_subtype", "new_section", "new_section.name", "new_text_value", "num_hearts", "num_likes", "old_approval_status", "old_date_value", "old_dates", "old_dates.due_at", "old_dates.due_on", "old_dates.start_on", "old_enum_value", "old_enum_value.color", "old_enum_value.enabled", "old_enum_value.name", "old_multi_enum_values", "old_multi_enum_values.color", "old_multi_enum_values.enabled", "old_multi_enum_values.name", "old_name", "old_number_value", "old_people_value", "old_people_value.name", "old_resource_subtype", "old_section", "old_section.name", "old_text_value", "previews", "previews.fallback", "previews.footer", "previews.header", "previews.header_link", "previews.html_text", "previews.text", "previews.title", "previews.title_link", "project", "project.name", "resource_subtype", "source", "sticker_name", "story", "story.created_at", "story.created_by", "story.created_by.name", "story.resource_subtype", "story.text", "tag", "tag.name", "target", "target.created_by", "target.name", "target.resource_subtype", "task", "task.created_by", "task.name", "task.resource_subtype", "text", "type"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### story_gid: `str`<a id="story_gid-str"></a>

Globally unique identifier for the story.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`StoriesGetFullRecordResponse`](./asana_python_sdk/pydantic/stories_get_full_record_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/stories/{story_gid}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.stories.get_task_stories`<a id="asanastoriesget_task_stories"></a>

Returns the compact records for all stories on the task.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_task_stories_response = asana.stories.get_task_stories(
    task_gid="321654",
    opt_pretty=True,
    limit=50,
    offset="eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9",
    opt_fields=["assignee", "assignee.name", "created_at", "created_by", "created_by.name", "custom_field", "custom_field.date_value", "custom_field.date_value.date", "custom_field.date_value.date_time", "custom_field.display_value", "custom_field.enabled", "custom_field.enum_options", "custom_field.enum_options.color", "custom_field.enum_options.enabled", "custom_field.enum_options.name", "custom_field.enum_value", "custom_field.enum_value.color", "custom_field.enum_value.enabled", "custom_field.enum_value.name", "custom_field.id_prefix", "custom_field.is_formula_field", "custom_field.multi_enum_values", "custom_field.multi_enum_values.color", "custom_field.multi_enum_values.enabled", "custom_field.multi_enum_values.name", "custom_field.name", "custom_field.number_value", "custom_field.representation_type", "custom_field.resource_subtype", "custom_field.text_value", "custom_field.type", "dependency", "dependency.created_by", "dependency.name", "dependency.resource_subtype", "duplicate_of", "duplicate_of.created_by", "duplicate_of.name", "duplicate_of.resource_subtype", "duplicated_from", "duplicated_from.created_by", "duplicated_from.name", "duplicated_from.resource_subtype", "follower", "follower.name", "hearted", "hearts", "hearts.user", "hearts.user.name", "html_text", "is_editable", "is_edited", "is_pinned", "liked", "likes", "likes.user", "likes.user.name", "new_approval_status", "new_date_value", "new_dates", "new_dates.due_at", "new_dates.due_on", "new_dates.start_on", "new_enum_value", "new_enum_value.color", "new_enum_value.enabled", "new_enum_value.name", "new_multi_enum_values", "new_multi_enum_values.color", "new_multi_enum_values.enabled", "new_multi_enum_values.name", "new_name", "new_number_value", "new_people_value", "new_people_value.name", "new_resource_subtype", "new_section", "new_section.name", "new_text_value", "num_hearts", "num_likes", "offset", "old_approval_status", "old_date_value", "old_dates", "old_dates.due_at", "old_dates.due_on", "old_dates.start_on", "old_enum_value", "old_enum_value.color", "old_enum_value.enabled", "old_enum_value.name", "old_multi_enum_values", "old_multi_enum_values.color", "old_multi_enum_values.enabled", "old_multi_enum_values.name", "old_name", "old_number_value", "old_people_value", "old_people_value.name", "old_resource_subtype", "old_section", "old_section.name", "old_text_value", "path", "previews", "previews.fallback", "previews.footer", "previews.header", "previews.header_link", "previews.html_text", "previews.text", "previews.title", "previews.title_link", "project", "project.name", "resource_subtype", "source", "sticker_name", "story", "story.created_at", "story.created_by", "story.created_by.name", "story.resource_subtype", "story.text", "tag", "tag.name", "target", "target.created_by", "target.name", "target.resource_subtype", "task", "task.created_by", "task.name", "task.resource_subtype", "text", "type", "uri"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### task_gid: `str`<a id="task_gid-str"></a>

The task to operate on.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### limit: `int`<a id="limit-int"></a>

Results per page. The number of objects to return per page. The value must be between 1 and 100.

##### offset: `str`<a id="offset-str"></a>

Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`StoriesGetTaskStoriesResponse`](./asana_python_sdk/pydantic/stories_get_task_stories_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tasks/{task_gid}/stories` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.stories.update_full_record`<a id="asanastoriesupdate_full_record"></a>

Updates the story and returns the full record for the updated story. Only comment stories can have their text updated, and only comment stories and attachment stories can be pinned. Only one of `text` and `html_text` can be specified.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_full_record_response = asana.stories.update_full_record(
    story_gid="35678",
    data=None,
    opt_pretty=True,
    opt_fields=["assignee", "assignee.name", "created_at", "created_by", "created_by.name", "custom_field", "custom_field.date_value", "custom_field.date_value.date", "custom_field.date_value.date_time", "custom_field.display_value", "custom_field.enabled", "custom_field.enum_options", "custom_field.enum_options.color", "custom_field.enum_options.enabled", "custom_field.enum_options.name", "custom_field.enum_value", "custom_field.enum_value.color", "custom_field.enum_value.enabled", "custom_field.enum_value.name", "custom_field.id_prefix", "custom_field.is_formula_field", "custom_field.multi_enum_values", "custom_field.multi_enum_values.color", "custom_field.multi_enum_values.enabled", "custom_field.multi_enum_values.name", "custom_field.name", "custom_field.number_value", "custom_field.representation_type", "custom_field.resource_subtype", "custom_field.text_value", "custom_field.type", "dependency", "dependency.created_by", "dependency.name", "dependency.resource_subtype", "duplicate_of", "duplicate_of.created_by", "duplicate_of.name", "duplicate_of.resource_subtype", "duplicated_from", "duplicated_from.created_by", "duplicated_from.name", "duplicated_from.resource_subtype", "follower", "follower.name", "hearted", "hearts", "hearts.user", "hearts.user.name", "html_text", "is_editable", "is_edited", "is_pinned", "liked", "likes", "likes.user", "likes.user.name", "new_approval_status", "new_date_value", "new_dates", "new_dates.due_at", "new_dates.due_on", "new_dates.start_on", "new_enum_value", "new_enum_value.color", "new_enum_value.enabled", "new_enum_value.name", "new_multi_enum_values", "new_multi_enum_values.color", "new_multi_enum_values.enabled", "new_multi_enum_values.name", "new_name", "new_number_value", "new_people_value", "new_people_value.name", "new_resource_subtype", "new_section", "new_section.name", "new_text_value", "num_hearts", "num_likes", "old_approval_status", "old_date_value", "old_dates", "old_dates.due_at", "old_dates.due_on", "old_dates.start_on", "old_enum_value", "old_enum_value.color", "old_enum_value.enabled", "old_enum_value.name", "old_multi_enum_values", "old_multi_enum_values.color", "old_multi_enum_values.enabled", "old_multi_enum_values.name", "old_name", "old_number_value", "old_people_value", "old_people_value.name", "old_resource_subtype", "old_section", "old_section.name", "old_text_value", "previews", "previews.fallback", "previews.footer", "previews.header", "previews.header_link", "previews.html_text", "previews.text", "previews.title", "previews.title_link", "project", "project.name", "resource_subtype", "source", "sticker_name", "story", "story.created_at", "story.created_by", "story.created_by.name", "story.resource_subtype", "story.text", "tag", "tag.name", "target", "target.created_by", "target.name", "target.resource_subtype", "task", "task.created_by", "task.name", "task.resource_subtype", "text", "type"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### story_gid: `str`<a id="story_gid-str"></a>

Globally unique identifier for the story.

##### data: [`StoryBase`](./asana_python_sdk/type/story_base.py)<a id="data-storybaseasana_python_sdktypestory_basepy"></a>


##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`StoriesUpdateFullRecordRequest`](./asana_python_sdk/type/stories_update_full_record_request.py)
The comment story to update.

#### 🔄 Return<a id="🔄-return"></a>

[`StoriesUpdateFullRecordResponse`](./asana_python_sdk/pydantic/stories_update_full_record_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/stories/{story_gid}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.tags.create_new_tag_record`<a id="asanatagscreate_new_tag_record"></a>

Creates a new tag in a workspace or organization.

Every tag is required to be created in a specific workspace or
organization, and this cannot be changed once set. Note that you can use
the workspace parameter regardless of whether or not it is an
organization.

Returns the full record of the newly created tag.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_tag_record_response = asana.tags.create_new_tag_record(
    data=None,
    opt_pretty=True,
    opt_fields=["color", "created_at", "followers", "followers.name", "name", "notes", "permalink_url", "workspace", "workspace.name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### data: `TagRequest`<a id="data-tagrequest"></a>

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TagsCreateNewTagRecordRequest`](./asana_python_sdk/type/tags_create_new_tag_record_request.py)
The tag to create.

#### 🔄 Return<a id="🔄-return"></a>

[`TagsCreateNewTagRecordResponse`](./asana_python_sdk/pydantic/tags_create_new_tag_record_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tags` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.tags.create_tag_in_workspace`<a id="asanatagscreate_tag_in_workspace"></a>

Creates a new tag in a workspace or organization.

Every tag is required to be created in a specific workspace or
organization, and this cannot be changed once set. Note that you can use
the workspace parameter regardless of whether or not it is an
organization.

Returns the full record of the newly created tag.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_tag_in_workspace_response = asana.tags.create_tag_in_workspace(
    workspace_gid="12345",
    data=None,
    opt_pretty=True,
    opt_fields=["color", "created_at", "followers", "followers.name", "name", "notes", "permalink_url", "workspace", "workspace.name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### workspace_gid: `str`<a id="workspace_gid-str"></a>

Globally unique identifier for the workspace or organization.

##### data: `TagCreateTagForWorkspaceRequest`<a id="data-tagcreatetagforworkspacerequest"></a>

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TagsCreateTagInWorkspaceRequest`](./asana_python_sdk/type/tags_create_tag_in_workspace_request.py)
The tag to create.

#### 🔄 Return<a id="🔄-return"></a>

[`TagsCreateTagInWorkspaceResponse`](./asana_python_sdk/pydantic/tags_create_tag_in_workspace_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workspaces/{workspace_gid}/tags` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.tags.get_filtered_tags`<a id="asanatagsget_filtered_tags"></a>

Returns the compact tag records for some filtered set of tags. Use one or more of the parameters provided to filter the tags returned.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_filtered_tags_response = asana.tags.get_filtered_tags(
    workspace_gid="12345",
    opt_pretty=True,
    limit=50,
    offset="eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9",
    opt_fields=["color", "created_at", "followers", "followers.name", "name", "notes", "offset", "path", "permalink_url", "uri", "workspace", "workspace.name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### workspace_gid: `str`<a id="workspace_gid-str"></a>

Globally unique identifier for the workspace or organization.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### limit: `int`<a id="limit-int"></a>

Results per page. The number of objects to return per page. The value must be between 1 and 100.

##### offset: `str`<a id="offset-str"></a>

Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`TagsGetFilteredTagsResponse`](./asana_python_sdk/pydantic/tags_get_filtered_tags_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workspaces/{workspace_gid}/tags` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.tags.get_record`<a id="asanatagsget_record"></a>

Returns the complete tag record for a single tag.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_record_response = asana.tags.get_record(
    tag_gid="11235",
    opt_pretty=True,
    opt_fields=["color", "created_at", "followers", "followers.name", "name", "notes", "permalink_url", "workspace", "workspace.name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tag_gid: `str`<a id="tag_gid-str"></a>

Globally unique identifier for the tag.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`TagsGetRecordResponse`](./asana_python_sdk/pydantic/tags_get_record_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tags/{tag_gid}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.tags.get_task_tags`<a id="asanatagsget_task_tags"></a>

Get a compact representation of all of the tags the task has.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_task_tags_response = asana.tags.get_task_tags(
    task_gid="321654",
    opt_pretty=True,
    limit=50,
    offset="eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9",
    opt_fields=["color", "created_at", "followers", "followers.name", "name", "notes", "offset", "path", "permalink_url", "uri", "workspace", "workspace.name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### task_gid: `str`<a id="task_gid-str"></a>

The task to operate on.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### limit: `int`<a id="limit-int"></a>

Results per page. The number of objects to return per page. The value must be between 1 and 100.

##### offset: `str`<a id="offset-str"></a>

Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`TagsGetTaskTagsResponse`](./asana_python_sdk/pydantic/tags_get_task_tags_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tasks/{task_gid}/tags` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.tags.list_filtered_tags`<a id="asanatagslist_filtered_tags"></a>

Returns the compact tag records for some filtered set of tags. Use one or more of the parameters provided to filter the tags returned.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_filtered_tags_response = asana.tags.list_filtered_tags(
    opt_pretty=True,
    limit=50,
    offset="eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9",
    workspace="1331",
    opt_fields=["color", "created_at", "followers", "followers.name", "name", "notes", "offset", "path", "permalink_url", "uri", "workspace", "workspace.name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### limit: `int`<a id="limit-int"></a>

Results per page. The number of objects to return per page. The value must be between 1 and 100.

##### offset: `str`<a id="offset-str"></a>

Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'

##### workspace: `str`<a id="workspace-str"></a>

The workspace to filter tags on.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`TagsListFilteredTagsResponse`](./asana_python_sdk/pydantic/tags_list_filtered_tags_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tags` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.tags.remove_tag`<a id="asanatagsremove_tag"></a>

A specific, existing tag can be deleted by making a DELETE request on
the URL for that tag.

Returns an empty data record.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_tag_response = asana.tags.remove_tag(
    tag_gid="11235",
    opt_pretty=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tag_gid: `str`<a id="tag_gid-str"></a>

Globally unique identifier for the tag.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

#### 🔄 Return<a id="🔄-return"></a>

[`TagsRemoveTagResponse`](./asana_python_sdk/pydantic/tags_remove_tag_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tags/{tag_gid}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.tags.update_tag_record`<a id="asanatagsupdate_tag_record"></a>

Updates the properties of a tag. Only the fields provided in the `data`
block will be updated; any unspecified fields will remain unchanged.

When using this method, it is best to specify only those fields you wish
to change, or else you may overwrite changes made by another user since
you last retrieved the tag.

Returns the complete updated tag record.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_tag_record_response = asana.tags.update_tag_record(
    tag_gid="11235",
    opt_pretty=True,
    opt_fields=["color", "created_at", "followers", "followers.name", "name", "notes", "permalink_url", "workspace", "workspace.name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tag_gid: `str`<a id="tag_gid-str"></a>

Globally unique identifier for the tag.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`TagsUpdateTagRecordResponse`](./asana_python_sdk/pydantic/tags_update_tag_record_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tags/{tag_gid}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.task_templates.delete_task_template`<a id="asanatask_templatesdelete_task_template"></a>

A specific, existing task template can be deleted by making a DELETE request on the URL for that task template. Returns an empty data record.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_task_template_response = asana.task_templates.delete_task_template(
    task_template_gid="1331",
    opt_pretty=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### task_template_gid: `str`<a id="task_template_gid-str"></a>

Globally unique identifier for the task template.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

#### 🔄 Return<a id="🔄-return"></a>

[`TaskTemplatesDeleteTaskTemplateResponse`](./asana_python_sdk/pydantic/task_templates_delete_task_template_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/task_templates/{task_template_gid}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.task_templates.get_single_template`<a id="asanatask_templatesget_single_template"></a>

Returns the complete task template record for a single task template.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_single_template_response = asana.task_templates.get_single_template(
    task_template_gid="1331",
    opt_pretty=True,
    opt_fields=["created_at", "created_by", "name", "project", "template"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### task_template_gid: `str`<a id="task_template_gid-str"></a>

Globally unique identifier for the task template.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`TaskTemplatesGetSingleTemplateResponse`](./asana_python_sdk/pydantic/task_templates_get_single_template_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/task_templates/{task_template_gid}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.task_templates.instantiate_task_job`<a id="asanatask_templatesinstantiate_task_job"></a>

Creates and returns a job that will asynchronously handle the task instantiation.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
instantiate_task_job_response = asana.task_templates.instantiate_task_job(
    task_template_gid="1331",
    data={
        "name": "New Task",
    },
    opt_pretty=True,
    opt_fields=["new_project", "new_project.name", "new_project_template", "new_project_template.name", "new_task", "new_task.created_by", "new_task.name", "new_task.resource_subtype", "new_task_template", "new_task_template.name", "resource_subtype", "status"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### task_template_gid: `str`<a id="task_template_gid-str"></a>

Globally unique identifier for the task template.

##### data: [`TaskTemplateInstantiateTaskRequest`](./asana_python_sdk/type/task_template_instantiate_task_request.py)<a id="data-tasktemplateinstantiatetaskrequestasana_python_sdktypetask_template_instantiate_task_requestpy"></a>


##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TaskTemplatesInstantiateTaskJobRequest`](./asana_python_sdk/type/task_templates_instantiate_task_job_request.py)
Describes the inputs used for instantiating a task - the task's name.

#### 🔄 Return<a id="🔄-return"></a>

[`TaskTemplatesInstantiateTaskJobResponse`](./asana_python_sdk/pydantic/task_templates_instantiate_task_job_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/task_templates/{task_template_gid}/instantiateTask` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.task_templates.list_multiple`<a id="asanatask_templateslist_multiple"></a>

Returns the compact task template records for some filtered set of task templates. You must specify a `project`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_multiple_response = asana.task_templates.list_multiple(
    opt_pretty=True,
    limit=50,
    offset="eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9",
    project="321654",
    opt_fields=["created_at", "created_by", "name", "project", "template"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### limit: `int`<a id="limit-int"></a>

Results per page. The number of objects to return per page. The value must be between 1 and 100.

##### offset: `str`<a id="offset-str"></a>

Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'

##### project: `str`<a id="project-str"></a>

The project to filter task templates on.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`TaskTemplatesListMultipleResponse`](./asana_python_sdk/pydantic/task_templates_list_multiple_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/task_templates` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.tasks.add_followers_to_task`<a id="asanatasksadd_followers_to_task"></a>

Adds followers to a task. Returns an empty data block.
Each task can be associated with zero or more followers in the system.
Requests to add/remove followers, if successful, will return the complete updated task record, described above.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_followers_to_task_response = asana.tasks.add_followers_to_task(
    task_gid="321654",
    data={
        "followers": ["13579", "321654"],
    },
    opt_pretty=True,
    opt_fields=["actual_time_minutes", "approval_status", "assignee", "assignee.name", "assignee_section", "assignee_section.name", "assignee_status", "completed", "completed_at", "completed_by", "completed_by.name", "created_at", "created_by", "custom_fields", "custom_fields.asana_created_field", "custom_fields.created_by", "custom_fields.created_by.name", "custom_fields.currency_code", "custom_fields.custom_label", "custom_fields.custom_label_position", "custom_fields.date_value", "custom_fields.date_value.date", "custom_fields.date_value.date_time", "custom_fields.description", "custom_fields.display_value", "custom_fields.enabled", "custom_fields.enum_options", "custom_fields.enum_options.color", "custom_fields.enum_options.enabled", "custom_fields.enum_options.name", "custom_fields.enum_value", "custom_fields.enum_value.color", "custom_fields.enum_value.enabled", "custom_fields.enum_value.name", "custom_fields.format", "custom_fields.has_notifications_enabled", "custom_fields.id_prefix", "custom_fields.is_formula_field", "custom_fields.is_global_to_workspace", "custom_fields.is_value_read_only", "custom_fields.multi_enum_values", "custom_fields.multi_enum_values.color", "custom_fields.multi_enum_values.enabled", "custom_fields.multi_enum_values.name", "custom_fields.name", "custom_fields.number_value", "custom_fields.people_value", "custom_fields.people_value.name", "custom_fields.precision", "custom_fields.representation_type", "custom_fields.resource_subtype", "custom_fields.text_value", "custom_fields.type", "dependencies", "dependents", "due_at", "due_on", "external", "external.data", "followers", "followers.name", "hearted", "hearts", "hearts.user", "hearts.user.name", "html_notes", "is_rendered_as_separator", "liked", "likes", "likes.user", "likes.user.name", "memberships", "memberships.project", "memberships.project.name", "memberships.section", "memberships.section.name", "modified_at", "name", "notes", "num_hearts", "num_likes", "num_subtasks", "parent", "parent.created_by", "parent.name", "parent.resource_subtype", "permalink_url", "projects", "projects.name", "resource_subtype", "start_at", "start_on", "tags", "tags.name", "workspace", "workspace.name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### task_gid: `str`<a id="task_gid-str"></a>

The task to operate on.

##### data: [`TaskAddFollowersRequest`](./asana_python_sdk/type/task_add_followers_request.py)<a id="data-taskaddfollowersrequestasana_python_sdktypetask_add_followers_requestpy"></a>


##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TasksAddFollowersToTaskRequest`](./asana_python_sdk/type/tasks_add_followers_to_task_request.py)
The followers to add to the task.

#### 🔄 Return<a id="🔄-return"></a>

[`TasksAddFollowersToTaskResponse`](./asana_python_sdk/pydantic/tasks_add_followers_to_task_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tasks/{task_gid}/addFollowers` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.tasks.add_project_to_task`<a id="asanatasksadd_project_to_task"></a>

Adds the task to the specified project, in the optional location
specified. If no location arguments are given, the task will be added to
the end of the project.

`addProject` can also be used to reorder a task within a project or
section that already contains it.

At most one of `insert_before`, `insert_after`, or `section` should be
specified. Inserting into a section in an non-order-dependent way can be
done by specifying section, otherwise, to insert within a section in a
particular place, specify `insert_before` or `insert_after` and a task
within the section to anchor the position of this task.

Returns an empty data block.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_project_to_task_response = asana.tasks.add_project_to_task(
    task_gid="321654",
    data={
        "project": "13579",
        "insert_after": "124816",
        "insert_before": "432134",
        "section": "987654",
    },
    opt_pretty=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### task_gid: `str`<a id="task_gid-str"></a>

The task to operate on.

##### data: [`TaskAddProjectRequest`](./asana_python_sdk/type/task_add_project_request.py)<a id="data-taskaddprojectrequestasana_python_sdktypetask_add_project_requestpy"></a>


##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TasksAddProjectToTaskRequest`](./asana_python_sdk/type/tasks_add_project_to_task_request.py)
The project to add the task to.

#### 🔄 Return<a id="🔄-return"></a>

[`TasksAddProjectToTaskResponse`](./asana_python_sdk/pydantic/tasks_add_project_to_task_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tasks/{task_gid}/addProject` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.tasks.add_tag_to_task`<a id="asanatasksadd_tag_to_task"></a>

Adds a tag to a task. Returns an empty data block.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_tag_to_task_response = asana.tasks.add_tag_to_task(
    task_gid="321654",
    data={
        "tag": "13579",
    },
    opt_pretty=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### task_gid: `str`<a id="task_gid-str"></a>

The task to operate on.

##### data: [`TaskAddTagRequest`](./asana_python_sdk/type/task_add_tag_request.py)<a id="data-taskaddtagrequestasana_python_sdktypetask_add_tag_requestpy"></a>


##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TasksAddTagToTaskRequest`](./asana_python_sdk/type/tasks_add_tag_to_task_request.py)
The tag to add to the task.

#### 🔄 Return<a id="🔄-return"></a>

[`TasksAddTagToTaskResponse`](./asana_python_sdk/pydantic/tasks_add_tag_to_task_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tasks/{task_gid}/addTag` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.tasks.create_new_task`<a id="asanataskscreate_new_task"></a>

Creating a new task is as easy as POSTing to the `/tasks` endpoint with a
data block containing the fields you’d like to set on the task. Any
unspecified fields will take on default values.

Every task is required to be created in a specific workspace, and this
workspace cannot be changed once set. The workspace need not be set
explicitly if you specify `projects` or a `parent` task instead.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_task_response = asana.tasks.create_new_task(
    data=None,
    opt_pretty=True,
    opt_fields=["actual_time_minutes", "approval_status", "assignee", "assignee.name", "assignee_section", "assignee_section.name", "assignee_status", "completed", "completed_at", "completed_by", "completed_by.name", "created_at", "created_by", "custom_fields", "custom_fields.asana_created_field", "custom_fields.created_by", "custom_fields.created_by.name", "custom_fields.currency_code", "custom_fields.custom_label", "custom_fields.custom_label_position", "custom_fields.date_value", "custom_fields.date_value.date", "custom_fields.date_value.date_time", "custom_fields.description", "custom_fields.display_value", "custom_fields.enabled", "custom_fields.enum_options", "custom_fields.enum_options.color", "custom_fields.enum_options.enabled", "custom_fields.enum_options.name", "custom_fields.enum_value", "custom_fields.enum_value.color", "custom_fields.enum_value.enabled", "custom_fields.enum_value.name", "custom_fields.format", "custom_fields.has_notifications_enabled", "custom_fields.id_prefix", "custom_fields.is_formula_field", "custom_fields.is_global_to_workspace", "custom_fields.is_value_read_only", "custom_fields.multi_enum_values", "custom_fields.multi_enum_values.color", "custom_fields.multi_enum_values.enabled", "custom_fields.multi_enum_values.name", "custom_fields.name", "custom_fields.number_value", "custom_fields.people_value", "custom_fields.people_value.name", "custom_fields.precision", "custom_fields.representation_type", "custom_fields.resource_subtype", "custom_fields.text_value", "custom_fields.type", "dependencies", "dependents", "due_at", "due_on", "external", "external.data", "followers", "followers.name", "hearted", "hearts", "hearts.user", "hearts.user.name", "html_notes", "is_rendered_as_separator", "liked", "likes", "likes.user", "likes.user.name", "memberships", "memberships.project", "memberships.project.name", "memberships.section", "memberships.section.name", "modified_at", "name", "notes", "num_hearts", "num_likes", "num_subtasks", "parent", "parent.created_by", "parent.name", "parent.resource_subtype", "permalink_url", "projects", "projects.name", "resource_subtype", "start_at", "start_on", "tags", "tags.name", "workspace", "workspace.name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### data: `TaskRequest`<a id="data-taskrequest"></a>

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TasksCreateNewTaskRequest`](./asana_python_sdk/type/tasks_create_new_task_request.py)
The task to create.

#### 🔄 Return<a id="🔄-return"></a>

[`TasksCreateNewTaskResponse`](./asana_python_sdk/pydantic/tasks_create_new_task_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tasks` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.tasks.create_subtask_record`<a id="asanataskscreate_subtask_record"></a>

Creates a new subtask and adds it to the parent task. Returns the full record for the newly created subtask.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_subtask_record_response = asana.tasks.create_subtask_record(
    task_gid="321654",
    data=None,
    opt_pretty=True,
    opt_fields=["actual_time_minutes", "approval_status", "assignee", "assignee.name", "assignee_section", "assignee_section.name", "assignee_status", "completed", "completed_at", "completed_by", "completed_by.name", "created_at", "created_by", "custom_fields", "custom_fields.asana_created_field", "custom_fields.created_by", "custom_fields.created_by.name", "custom_fields.currency_code", "custom_fields.custom_label", "custom_fields.custom_label_position", "custom_fields.date_value", "custom_fields.date_value.date", "custom_fields.date_value.date_time", "custom_fields.description", "custom_fields.display_value", "custom_fields.enabled", "custom_fields.enum_options", "custom_fields.enum_options.color", "custom_fields.enum_options.enabled", "custom_fields.enum_options.name", "custom_fields.enum_value", "custom_fields.enum_value.color", "custom_fields.enum_value.enabled", "custom_fields.enum_value.name", "custom_fields.format", "custom_fields.has_notifications_enabled", "custom_fields.id_prefix", "custom_fields.is_formula_field", "custom_fields.is_global_to_workspace", "custom_fields.is_value_read_only", "custom_fields.multi_enum_values", "custom_fields.multi_enum_values.color", "custom_fields.multi_enum_values.enabled", "custom_fields.multi_enum_values.name", "custom_fields.name", "custom_fields.number_value", "custom_fields.people_value", "custom_fields.people_value.name", "custom_fields.precision", "custom_fields.representation_type", "custom_fields.resource_subtype", "custom_fields.text_value", "custom_fields.type", "dependencies", "dependents", "due_at", "due_on", "external", "external.data", "followers", "followers.name", "hearted", "hearts", "hearts.user", "hearts.user.name", "html_notes", "is_rendered_as_separator", "liked", "likes", "likes.user", "likes.user.name", "memberships", "memberships.project", "memberships.project.name", "memberships.section", "memberships.section.name", "modified_at", "name", "notes", "num_hearts", "num_likes", "num_subtasks", "parent", "parent.created_by", "parent.name", "parent.resource_subtype", "permalink_url", "projects", "projects.name", "resource_subtype", "start_at", "start_on", "tags", "tags.name", "workspace", "workspace.name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### task_gid: `str`<a id="task_gid-str"></a>

The task to operate on.

##### data: `TaskRequest`<a id="data-taskrequest"></a>

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TasksCreateSubtaskRecordRequest`](./asana_python_sdk/type/tasks_create_subtask_record_request.py)
The new subtask to create.

#### 🔄 Return<a id="🔄-return"></a>

[`TasksCreateSubtaskRecordResponse`](./asana_python_sdk/pydantic/tasks_create_subtask_record_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tasks/{task_gid}/subtasks` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.tasks.delete_task`<a id="asanatasksdelete_task"></a>

A specific, existing task can be deleted by making a DELETE request on
the URL for that task. Deleted tasks go into the “trash” of the user
making the delete request. Tasks can be recovered from the trash within a
period of 30 days; afterward they are completely removed from the system.

Returns an empty data record.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_task_response = asana.tasks.delete_task(
    task_gid="321654",
    opt_pretty=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### task_gid: `str`<a id="task_gid-str"></a>

The task to operate on.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

#### 🔄 Return<a id="🔄-return"></a>

[`TasksDeleteTaskResponse`](./asana_python_sdk/pydantic/tasks_delete_task_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tasks/{task_gid}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.tasks.duplicate_task_job`<a id="asanatasksduplicate_task_job"></a>

Creates and returns a job that will asynchronously handle the duplication.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
duplicate_task_job_response = asana.tasks.duplicate_task_job(
    task_gid="321654",
    data={
        "name": "New Task Name",
        "include": "[notes,assignee,subtasks,attachments,tags,followers,projects,dates,dependencies,parent]",
    },
    opt_pretty=True,
    opt_fields=["new_project", "new_project.name", "new_project_template", "new_project_template.name", "new_task", "new_task.created_by", "new_task.name", "new_task.resource_subtype", "new_task_template", "new_task_template.name", "resource_subtype", "status"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### task_gid: `str`<a id="task_gid-str"></a>

The task to operate on.

##### data: [`TaskDuplicateRequest`](./asana_python_sdk/type/task_duplicate_request.py)<a id="data-taskduplicaterequestasana_python_sdktypetask_duplicate_requestpy"></a>


##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TasksDuplicateTaskJobRequest`](./asana_python_sdk/type/tasks_duplicate_task_job_request.py)
Describes the duplicate's name and the fields that will be duplicated.

#### 🔄 Return<a id="🔄-return"></a>

[`TasksDuplicateTaskJobResponse`](./asana_python_sdk/pydantic/tasks_duplicate_task_job_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tasks/{task_gid}/duplicate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.tasks.get_all_dependencies`<a id="asanatasksget_all_dependencies"></a>

Returns the compact representations of all of the dependencies of a task.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_dependencies_response = asana.tasks.get_all_dependencies(
    task_gid="321654",
    opt_pretty=True,
    limit=50,
    offset="eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9",
    opt_fields=["actual_time_minutes", "approval_status", "assignee", "assignee.name", "assignee_section", "assignee_section.name", "assignee_status", "completed", "completed_at", "completed_by", "completed_by.name", "created_at", "created_by", "custom_fields", "custom_fields.asana_created_field", "custom_fields.created_by", "custom_fields.created_by.name", "custom_fields.currency_code", "custom_fields.custom_label", "custom_fields.custom_label_position", "custom_fields.date_value", "custom_fields.date_value.date", "custom_fields.date_value.date_time", "custom_fields.description", "custom_fields.display_value", "custom_fields.enabled", "custom_fields.enum_options", "custom_fields.enum_options.color", "custom_fields.enum_options.enabled", "custom_fields.enum_options.name", "custom_fields.enum_value", "custom_fields.enum_value.color", "custom_fields.enum_value.enabled", "custom_fields.enum_value.name", "custom_fields.format", "custom_fields.has_notifications_enabled", "custom_fields.id_prefix", "custom_fields.is_formula_field", "custom_fields.is_global_to_workspace", "custom_fields.is_value_read_only", "custom_fields.multi_enum_values", "custom_fields.multi_enum_values.color", "custom_fields.multi_enum_values.enabled", "custom_fields.multi_enum_values.name", "custom_fields.name", "custom_fields.number_value", "custom_fields.people_value", "custom_fields.people_value.name", "custom_fields.precision", "custom_fields.representation_type", "custom_fields.resource_subtype", "custom_fields.text_value", "custom_fields.type", "dependencies", "dependents", "due_at", "due_on", "external", "external.data", "followers", "followers.name", "hearted", "hearts", "hearts.user", "hearts.user.name", "html_notes", "is_rendered_as_separator", "liked", "likes", "likes.user", "likes.user.name", "memberships", "memberships.project", "memberships.project.name", "memberships.section", "memberships.section.name", "modified_at", "name", "notes", "num_hearts", "num_likes", "num_subtasks", "offset", "parent", "parent.created_by", "parent.name", "parent.resource_subtype", "path", "permalink_url", "projects", "projects.name", "resource_subtype", "start_at", "start_on", "tags", "tags.name", "uri", "workspace", "workspace.name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### task_gid: `str`<a id="task_gid-str"></a>

The task to operate on.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### limit: `int`<a id="limit-int"></a>

Results per page. The number of objects to return per page. The value must be between 1 and 100.

##### offset: `str`<a id="offset-str"></a>

Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`TasksGetAllDependenciesResponse`](./asana_python_sdk/pydantic/tasks_get_all_dependencies_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tasks/{task_gid}/dependencies` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.tasks.get_by_custom_id`<a id="asanatasksget_by_custom_id"></a>

Returns a task given a custom ID shortcode.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_custom_id_response = asana.tasks.get_by_custom_id(
    workspace_gid="12345",
    custom_id="EX-1",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### workspace_gid: `str`<a id="workspace_gid-str"></a>

Globally unique identifier for the workspace or organization.

##### custom_id: `str`<a id="custom_id-str"></a>

Generated custom ID for a task.

#### 🔄 Return<a id="🔄-return"></a>

[`TasksGetByCustomIdResponse`](./asana_python_sdk/pydantic/tasks_get_by_custom_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workspaces/{workspace_gid}/tasks/custom_id/{custom_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.tasks.get_dependents`<a id="asanatasksget_dependents"></a>

Returns the compact representations of all of the dependents of a task.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_dependents_response = asana.tasks.get_dependents(
    task_gid="321654",
    opt_pretty=True,
    limit=50,
    offset="eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9",
    opt_fields=["actual_time_minutes", "approval_status", "assignee", "assignee.name", "assignee_section", "assignee_section.name", "assignee_status", "completed", "completed_at", "completed_by", "completed_by.name", "created_at", "created_by", "custom_fields", "custom_fields.asana_created_field", "custom_fields.created_by", "custom_fields.created_by.name", "custom_fields.currency_code", "custom_fields.custom_label", "custom_fields.custom_label_position", "custom_fields.date_value", "custom_fields.date_value.date", "custom_fields.date_value.date_time", "custom_fields.description", "custom_fields.display_value", "custom_fields.enabled", "custom_fields.enum_options", "custom_fields.enum_options.color", "custom_fields.enum_options.enabled", "custom_fields.enum_options.name", "custom_fields.enum_value", "custom_fields.enum_value.color", "custom_fields.enum_value.enabled", "custom_fields.enum_value.name", "custom_fields.format", "custom_fields.has_notifications_enabled", "custom_fields.id_prefix", "custom_fields.is_formula_field", "custom_fields.is_global_to_workspace", "custom_fields.is_value_read_only", "custom_fields.multi_enum_values", "custom_fields.multi_enum_values.color", "custom_fields.multi_enum_values.enabled", "custom_fields.multi_enum_values.name", "custom_fields.name", "custom_fields.number_value", "custom_fields.people_value", "custom_fields.people_value.name", "custom_fields.precision", "custom_fields.representation_type", "custom_fields.resource_subtype", "custom_fields.text_value", "custom_fields.type", "dependencies", "dependents", "due_at", "due_on", "external", "external.data", "followers", "followers.name", "hearted", "hearts", "hearts.user", "hearts.user.name", "html_notes", "is_rendered_as_separator", "liked", "likes", "likes.user", "likes.user.name", "memberships", "memberships.project", "memberships.project.name", "memberships.section", "memberships.section.name", "modified_at", "name", "notes", "num_hearts", "num_likes", "num_subtasks", "offset", "parent", "parent.created_by", "parent.name", "parent.resource_subtype", "path", "permalink_url", "projects", "projects.name", "resource_subtype", "start_at", "start_on", "tags", "tags.name", "uri", "workspace", "workspace.name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### task_gid: `str`<a id="task_gid-str"></a>

The task to operate on.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### limit: `int`<a id="limit-int"></a>

Results per page. The number of objects to return per page. The value must be between 1 and 100.

##### offset: `str`<a id="offset-str"></a>

Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`TasksGetDependentsResponse`](./asana_python_sdk/pydantic/tasks_get_dependents_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tasks/{task_gid}/dependents` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.tasks.get_multiple`<a id="asanatasksget_multiple"></a>

Returns the compact task records for some filtered set of tasks. Use one or more of the parameters provided to filter the tasks returned. You must specify a `project` or `tag` if you do not specify `assignee` and `workspace`.

For more complex task retrieval, use [workspaces/{workspace_gid}/tasks/search](https://developers.asana.com/reference/rest-api-reference).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_multiple_response = asana.tasks.get_multiple(
    opt_pretty=True,
    limit=50,
    offset="eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9",
    assignee="14641",
    project="321654",
    section="321654",
    workspace="321654",
    completed_since="2012-02-22T02:06:58.158Z",
    modified_since="2012-02-22T02:06:58.158Z",
    opt_fields=["actual_time_minutes", "approval_status", "assignee", "assignee.name", "assignee_section", "assignee_section.name", "assignee_status", "completed", "completed_at", "completed_by", "completed_by.name", "created_at", "created_by", "custom_fields", "custom_fields.asana_created_field", "custom_fields.created_by", "custom_fields.created_by.name", "custom_fields.currency_code", "custom_fields.custom_label", "custom_fields.custom_label_position", "custom_fields.date_value", "custom_fields.date_value.date", "custom_fields.date_value.date_time", "custom_fields.description", "custom_fields.display_value", "custom_fields.enabled", "custom_fields.enum_options", "custom_fields.enum_options.color", "custom_fields.enum_options.enabled", "custom_fields.enum_options.name", "custom_fields.enum_value", "custom_fields.enum_value.color", "custom_fields.enum_value.enabled", "custom_fields.enum_value.name", "custom_fields.format", "custom_fields.has_notifications_enabled", "custom_fields.id_prefix", "custom_fields.is_formula_field", "custom_fields.is_global_to_workspace", "custom_fields.is_value_read_only", "custom_fields.multi_enum_values", "custom_fields.multi_enum_values.color", "custom_fields.multi_enum_values.enabled", "custom_fields.multi_enum_values.name", "custom_fields.name", "custom_fields.number_value", "custom_fields.people_value", "custom_fields.people_value.name", "custom_fields.precision", "custom_fields.representation_type", "custom_fields.resource_subtype", "custom_fields.text_value", "custom_fields.type", "dependencies", "dependents", "due_at", "due_on", "external", "external.data", "followers", "followers.name", "hearted", "hearts", "hearts.user", "hearts.user.name", "html_notes", "is_rendered_as_separator", "liked", "likes", "likes.user", "likes.user.name", "memberships", "memberships.project", "memberships.project.name", "memberships.section", "memberships.section.name", "modified_at", "name", "notes", "num_hearts", "num_likes", "num_subtasks", "offset", "parent", "parent.created_by", "parent.name", "parent.resource_subtype", "path", "permalink_url", "projects", "projects.name", "resource_subtype", "start_at", "start_on", "tags", "tags.name", "uri", "workspace", "workspace.name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### limit: `int`<a id="limit-int"></a>

Results per page. The number of objects to return per page. The value must be between 1 and 100.

##### offset: `str`<a id="offset-str"></a>

Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'

##### assignee: `str`<a id="assignee-str"></a>

The assignee to filter tasks on. If searching for unassigned tasks, assignee.any = null can be specified. *Note: If you specify `assignee`, you must also specify the `workspace` to filter on.*

##### project: `str`<a id="project-str"></a>

The project to filter tasks on.

##### section: `str`<a id="section-str"></a>

The section to filter tasks on.

##### workspace: `str`<a id="workspace-str"></a>

The workspace to filter tasks on. *Note: If you specify `workspace`, you must also specify the `assignee` to filter on.*

##### completed_since: `datetime`<a id="completed_since-datetime"></a>

Only return tasks that are either incomplete or that have been completed since this time.

##### modified_since: `datetime`<a id="modified_since-datetime"></a>

Only return tasks that have been modified since the given time.  *Note: A task is considered “modified” if any of its properties change, or associations between it and other objects are modified (e.g.  a task being added to a project). A task is not considered modified just because another object it is associated with (e.g. a subtask) is modified. Actions that count as modifying the task include assigning, renaming, completing, and adding stories.*

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`TasksGetMultipleResponse`](./asana_python_sdk/pydantic/tasks_get_multiple_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tasks` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.tasks.get_multiple_with_tag`<a id="asanatasksget_multiple_with_tag"></a>

Returns the compact task records for all tasks with the given tag. Tasks can have more than one tag at a time.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_multiple_with_tag_response = asana.tasks.get_multiple_with_tag(
    tag_gid="11235",
    opt_pretty=True,
    limit=50,
    offset="eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9",
    opt_fields=["actual_time_minutes", "approval_status", "assignee", "assignee.name", "assignee_section", "assignee_section.name", "assignee_status", "completed", "completed_at", "completed_by", "completed_by.name", "created_at", "created_by", "custom_fields", "custom_fields.asana_created_field", "custom_fields.created_by", "custom_fields.created_by.name", "custom_fields.currency_code", "custom_fields.custom_label", "custom_fields.custom_label_position", "custom_fields.date_value", "custom_fields.date_value.date", "custom_fields.date_value.date_time", "custom_fields.description", "custom_fields.display_value", "custom_fields.enabled", "custom_fields.enum_options", "custom_fields.enum_options.color", "custom_fields.enum_options.enabled", "custom_fields.enum_options.name", "custom_fields.enum_value", "custom_fields.enum_value.color", "custom_fields.enum_value.enabled", "custom_fields.enum_value.name", "custom_fields.format", "custom_fields.has_notifications_enabled", "custom_fields.id_prefix", "custom_fields.is_formula_field", "custom_fields.is_global_to_workspace", "custom_fields.is_value_read_only", "custom_fields.multi_enum_values", "custom_fields.multi_enum_values.color", "custom_fields.multi_enum_values.enabled", "custom_fields.multi_enum_values.name", "custom_fields.name", "custom_fields.number_value", "custom_fields.people_value", "custom_fields.people_value.name", "custom_fields.precision", "custom_fields.representation_type", "custom_fields.resource_subtype", "custom_fields.text_value", "custom_fields.type", "dependencies", "dependents", "due_at", "due_on", "external", "external.data", "followers", "followers.name", "hearted", "hearts", "hearts.user", "hearts.user.name", "html_notes", "is_rendered_as_separator", "liked", "likes", "likes.user", "likes.user.name", "memberships", "memberships.project", "memberships.project.name", "memberships.section", "memberships.section.name", "modified_at", "name", "notes", "num_hearts", "num_likes", "num_subtasks", "offset", "parent", "parent.created_by", "parent.name", "parent.resource_subtype", "path", "permalink_url", "projects", "projects.name", "resource_subtype", "start_at", "start_on", "tags", "tags.name", "uri", "workspace", "workspace.name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tag_gid: `str`<a id="tag_gid-str"></a>

Globally unique identifier for the tag.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### limit: `int`<a id="limit-int"></a>

Results per page. The number of objects to return per page. The value must be between 1 and 100.

##### offset: `str`<a id="offset-str"></a>

Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`TasksGetMultipleWithTagResponse`](./asana_python_sdk/pydantic/tasks_get_multiple_with_tag_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tags/{tag_gid}/tasks` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.tasks.get_section_tasks`<a id="asanatasksget_section_tasks"></a>

*Board view only*: Returns the compact section records for all tasks within the given section.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_section_tasks_response = asana.tasks.get_section_tasks(
    section_gid="321654",
    opt_pretty=True,
    limit=50,
    offset="eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9",
    completed_since="2012-02-22T02:06:58.158Z",
    opt_fields=["actual_time_minutes", "approval_status", "assignee", "assignee.name", "assignee_section", "assignee_section.name", "assignee_status", "completed", "completed_at", "completed_by", "completed_by.name", "created_at", "created_by", "custom_fields", "custom_fields.asana_created_field", "custom_fields.created_by", "custom_fields.created_by.name", "custom_fields.currency_code", "custom_fields.custom_label", "custom_fields.custom_label_position", "custom_fields.date_value", "custom_fields.date_value.date", "custom_fields.date_value.date_time", "custom_fields.description", "custom_fields.display_value", "custom_fields.enabled", "custom_fields.enum_options", "custom_fields.enum_options.color", "custom_fields.enum_options.enabled", "custom_fields.enum_options.name", "custom_fields.enum_value", "custom_fields.enum_value.color", "custom_fields.enum_value.enabled", "custom_fields.enum_value.name", "custom_fields.format", "custom_fields.has_notifications_enabled", "custom_fields.id_prefix", "custom_fields.is_formula_field", "custom_fields.is_global_to_workspace", "custom_fields.is_value_read_only", "custom_fields.multi_enum_values", "custom_fields.multi_enum_values.color", "custom_fields.multi_enum_values.enabled", "custom_fields.multi_enum_values.name", "custom_fields.name", "custom_fields.number_value", "custom_fields.people_value", "custom_fields.people_value.name", "custom_fields.precision", "custom_fields.representation_type", "custom_fields.resource_subtype", "custom_fields.text_value", "custom_fields.type", "dependencies", "dependents", "due_at", "due_on", "external", "external.data", "followers", "followers.name", "hearted", "hearts", "hearts.user", "hearts.user.name", "html_notes", "is_rendered_as_separator", "liked", "likes", "likes.user", "likes.user.name", "memberships", "memberships.project", "memberships.project.name", "memberships.section", "memberships.section.name", "modified_at", "name", "notes", "num_hearts", "num_likes", "num_subtasks", "offset", "parent", "parent.created_by", "parent.name", "parent.resource_subtype", "path", "permalink_url", "projects", "projects.name", "resource_subtype", "start_at", "start_on", "tags", "tags.name", "uri", "workspace", "workspace.name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### section_gid: `str`<a id="section_gid-str"></a>

The globally unique identifier for the section.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### limit: `int`<a id="limit-int"></a>

Results per page. The number of objects to return per page. The value must be between 1 and 100.

##### offset: `str`<a id="offset-str"></a>

Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'

##### completed_since: `str`<a id="completed_since-str"></a>

Only return tasks that are either incomplete or that have been completed since this time. Accepts a date-time string or the keyword *now*. 

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`TasksGetSectionTasksResponse`](./asana_python_sdk/pydantic/tasks_get_section_tasks_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/sections/{section_gid}/tasks` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.tasks.get_subtask_list`<a id="asanatasksget_subtask_list"></a>

Returns a compact representation of all of the subtasks of a task.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_subtask_list_response = asana.tasks.get_subtask_list(
    task_gid="321654",
    opt_pretty=True,
    limit=50,
    offset="eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9",
    opt_fields=["actual_time_minutes", "approval_status", "assignee", "assignee.name", "assignee_section", "assignee_section.name", "assignee_status", "completed", "completed_at", "completed_by", "completed_by.name", "created_at", "created_by", "custom_fields", "custom_fields.asana_created_field", "custom_fields.created_by", "custom_fields.created_by.name", "custom_fields.currency_code", "custom_fields.custom_label", "custom_fields.custom_label_position", "custom_fields.date_value", "custom_fields.date_value.date", "custom_fields.date_value.date_time", "custom_fields.description", "custom_fields.display_value", "custom_fields.enabled", "custom_fields.enum_options", "custom_fields.enum_options.color", "custom_fields.enum_options.enabled", "custom_fields.enum_options.name", "custom_fields.enum_value", "custom_fields.enum_value.color", "custom_fields.enum_value.enabled", "custom_fields.enum_value.name", "custom_fields.format", "custom_fields.has_notifications_enabled", "custom_fields.id_prefix", "custom_fields.is_formula_field", "custom_fields.is_global_to_workspace", "custom_fields.is_value_read_only", "custom_fields.multi_enum_values", "custom_fields.multi_enum_values.color", "custom_fields.multi_enum_values.enabled", "custom_fields.multi_enum_values.name", "custom_fields.name", "custom_fields.number_value", "custom_fields.people_value", "custom_fields.people_value.name", "custom_fields.precision", "custom_fields.representation_type", "custom_fields.resource_subtype", "custom_fields.text_value", "custom_fields.type", "dependencies", "dependents", "due_at", "due_on", "external", "external.data", "followers", "followers.name", "hearted", "hearts", "hearts.user", "hearts.user.name", "html_notes", "is_rendered_as_separator", "liked", "likes", "likes.user", "likes.user.name", "memberships", "memberships.project", "memberships.project.name", "memberships.section", "memberships.section.name", "modified_at", "name", "notes", "num_hearts", "num_likes", "num_subtasks", "offset", "parent", "parent.created_by", "parent.name", "parent.resource_subtype", "path", "permalink_url", "projects", "projects.name", "resource_subtype", "start_at", "start_on", "tags", "tags.name", "uri", "workspace", "workspace.name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### task_gid: `str`<a id="task_gid-str"></a>

The task to operate on.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### limit: `int`<a id="limit-int"></a>

Results per page. The number of objects to return per page. The value must be between 1 and 100.

##### offset: `str`<a id="offset-str"></a>

Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`TasksGetSubtaskListResponse`](./asana_python_sdk/pydantic/tasks_get_subtask_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tasks/{task_gid}/subtasks` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.tasks.get_task_record`<a id="asanatasksget_task_record"></a>

Returns the complete task record for a single task.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_task_record_response = asana.tasks.get_task_record(
    task_gid="321654",
    opt_pretty=True,
    opt_fields=["actual_time_minutes", "approval_status", "assignee", "assignee.name", "assignee_section", "assignee_section.name", "assignee_status", "completed", "completed_at", "completed_by", "completed_by.name", "created_at", "created_by", "custom_fields", "custom_fields.asana_created_field", "custom_fields.created_by", "custom_fields.created_by.name", "custom_fields.currency_code", "custom_fields.custom_label", "custom_fields.custom_label_position", "custom_fields.date_value", "custom_fields.date_value.date", "custom_fields.date_value.date_time", "custom_fields.description", "custom_fields.display_value", "custom_fields.enabled", "custom_fields.enum_options", "custom_fields.enum_options.color", "custom_fields.enum_options.enabled", "custom_fields.enum_options.name", "custom_fields.enum_value", "custom_fields.enum_value.color", "custom_fields.enum_value.enabled", "custom_fields.enum_value.name", "custom_fields.format", "custom_fields.has_notifications_enabled", "custom_fields.id_prefix", "custom_fields.is_formula_field", "custom_fields.is_global_to_workspace", "custom_fields.is_value_read_only", "custom_fields.multi_enum_values", "custom_fields.multi_enum_values.color", "custom_fields.multi_enum_values.enabled", "custom_fields.multi_enum_values.name", "custom_fields.name", "custom_fields.number_value", "custom_fields.people_value", "custom_fields.people_value.name", "custom_fields.precision", "custom_fields.representation_type", "custom_fields.resource_subtype", "custom_fields.text_value", "custom_fields.type", "dependencies", "dependents", "due_at", "due_on", "external", "external.data", "followers", "followers.name", "hearted", "hearts", "hearts.user", "hearts.user.name", "html_notes", "is_rendered_as_separator", "liked", "likes", "likes.user", "likes.user.name", "memberships", "memberships.project", "memberships.project.name", "memberships.section", "memberships.section.name", "modified_at", "name", "notes", "num_hearts", "num_likes", "num_subtasks", "parent", "parent.created_by", "parent.name", "parent.resource_subtype", "permalink_url", "projects", "projects.name", "resource_subtype", "start_at", "start_on", "tags", "tags.name", "workspace", "workspace.name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### task_gid: `str`<a id="task_gid-str"></a>

The task to operate on.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`TasksGetTaskRecordResponse`](./asana_python_sdk/pydantic/tasks_get_task_record_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tasks/{task_gid}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.tasks.get_tasks_by_project`<a id="asanatasksget_tasks_by_project"></a>

Returns the compact task records for all tasks within the given project, ordered by their priority within the project. Tasks can exist in more than one project at a time.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_tasks_by_project_response = asana.tasks.get_tasks_by_project(
    project_gid="1331",
    completed_since="2012-02-22T02:06:58.158Z",
    opt_pretty=True,
    limit=50,
    offset="eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9",
    opt_fields=["actual_time_minutes", "approval_status", "assignee", "assignee.name", "assignee_section", "assignee_section.name", "assignee_status", "completed", "completed_at", "completed_by", "completed_by.name", "created_at", "created_by", "custom_fields", "custom_fields.asana_created_field", "custom_fields.created_by", "custom_fields.created_by.name", "custom_fields.currency_code", "custom_fields.custom_label", "custom_fields.custom_label_position", "custom_fields.date_value", "custom_fields.date_value.date", "custom_fields.date_value.date_time", "custom_fields.description", "custom_fields.display_value", "custom_fields.enabled", "custom_fields.enum_options", "custom_fields.enum_options.color", "custom_fields.enum_options.enabled", "custom_fields.enum_options.name", "custom_fields.enum_value", "custom_fields.enum_value.color", "custom_fields.enum_value.enabled", "custom_fields.enum_value.name", "custom_fields.format", "custom_fields.has_notifications_enabled", "custom_fields.id_prefix", "custom_fields.is_formula_field", "custom_fields.is_global_to_workspace", "custom_fields.is_value_read_only", "custom_fields.multi_enum_values", "custom_fields.multi_enum_values.color", "custom_fields.multi_enum_values.enabled", "custom_fields.multi_enum_values.name", "custom_fields.name", "custom_fields.number_value", "custom_fields.people_value", "custom_fields.people_value.name", "custom_fields.precision", "custom_fields.representation_type", "custom_fields.resource_subtype", "custom_fields.text_value", "custom_fields.type", "dependencies", "dependents", "due_at", "due_on", "external", "external.data", "followers", "followers.name", "hearted", "hearts", "hearts.user", "hearts.user.name", "html_notes", "is_rendered_as_separator", "liked", "likes", "likes.user", "likes.user.name", "memberships", "memberships.project", "memberships.project.name", "memberships.section", "memberships.section.name", "modified_at", "name", "notes", "num_hearts", "num_likes", "num_subtasks", "offset", "parent", "parent.created_by", "parent.name", "parent.resource_subtype", "path", "permalink_url", "projects", "projects.name", "resource_subtype", "start_at", "start_on", "tags", "tags.name", "uri", "workspace", "workspace.name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_gid: `str`<a id="project_gid-str"></a>

Globally unique identifier for the project.

##### completed_since: `str`<a id="completed_since-str"></a>

Only return tasks that are either incomplete or that have been completed since this time. Accepts a date-time string or the keyword *now*. 

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### limit: `int`<a id="limit-int"></a>

Results per page. The number of objects to return per page. The value must be between 1 and 100.

##### offset: `str`<a id="offset-str"></a>

Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`TasksGetTasksByProjectResponse`](./asana_python_sdk/pydantic/tasks_get_tasks_by_project_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/projects/{project_gid}/tasks` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.tasks.get_user_task_list_tasks`<a id="asanatasksget_user_task_list_tasks"></a>

Returns the compact list of tasks in a user’s My Tasks list.
*Note: Access control is enforced for this endpoint as with all Asana API endpoints, meaning a user’s private tasks will be filtered out if the API-authenticated user does not have access to them.*
*Note: Both complete and incomplete tasks are returned by default unless they are filtered out (for example, setting `completed_since=now` will return only incomplete tasks, which is the default view for “My Tasks” in Asana.)*

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_task_list_tasks_response = asana.tasks.get_user_task_list_tasks(
    user_task_list_gid="12345",
    completed_since="2012-02-22T02:06:58.158Z",
    opt_pretty=True,
    limit=50,
    offset="eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9",
    opt_fields=["actual_time_minutes", "approval_status", "assignee", "assignee.name", "assignee_section", "assignee_section.name", "assignee_status", "completed", "completed_at", "completed_by", "completed_by.name", "created_at", "created_by", "custom_fields", "custom_fields.asana_created_field", "custom_fields.created_by", "custom_fields.created_by.name", "custom_fields.currency_code", "custom_fields.custom_label", "custom_fields.custom_label_position", "custom_fields.date_value", "custom_fields.date_value.date", "custom_fields.date_value.date_time", "custom_fields.description", "custom_fields.display_value", "custom_fields.enabled", "custom_fields.enum_options", "custom_fields.enum_options.color", "custom_fields.enum_options.enabled", "custom_fields.enum_options.name", "custom_fields.enum_value", "custom_fields.enum_value.color", "custom_fields.enum_value.enabled", "custom_fields.enum_value.name", "custom_fields.format", "custom_fields.has_notifications_enabled", "custom_fields.id_prefix", "custom_fields.is_formula_field", "custom_fields.is_global_to_workspace", "custom_fields.is_value_read_only", "custom_fields.multi_enum_values", "custom_fields.multi_enum_values.color", "custom_fields.multi_enum_values.enabled", "custom_fields.multi_enum_values.name", "custom_fields.name", "custom_fields.number_value", "custom_fields.people_value", "custom_fields.people_value.name", "custom_fields.precision", "custom_fields.representation_type", "custom_fields.resource_subtype", "custom_fields.text_value", "custom_fields.type", "dependencies", "dependents", "due_at", "due_on", "external", "external.data", "followers", "followers.name", "hearted", "hearts", "hearts.user", "hearts.user.name", "html_notes", "is_rendered_as_separator", "liked", "likes", "likes.user", "likes.user.name", "memberships", "memberships.project", "memberships.project.name", "memberships.section", "memberships.section.name", "modified_at", "name", "notes", "num_hearts", "num_likes", "num_subtasks", "offset", "parent", "parent.created_by", "parent.name", "parent.resource_subtype", "path", "permalink_url", "projects", "projects.name", "resource_subtype", "start_at", "start_on", "tags", "tags.name", "uri", "workspace", "workspace.name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_task_list_gid: `str`<a id="user_task_list_gid-str"></a>

Globally unique identifier for the user task list.

##### completed_since: `str`<a id="completed_since-str"></a>

Only return tasks that are either incomplete or that have been completed since this time. Accepts a date-time string or the keyword *now*. 

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### limit: `int`<a id="limit-int"></a>

Results per page. The number of objects to return per page. The value must be between 1 and 100.

##### offset: `str`<a id="offset-str"></a>

Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`TasksGetUserTaskListTasksResponse`](./asana_python_sdk/pydantic/tasks_get_user_task_list_tasks_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/user_task_lists/{user_task_list_gid}/tasks` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.tasks.remove_followers_from_task`<a id="asanatasksremove_followers_from_task"></a>

Removes each of the specified followers from the task if they are following. Returns the complete, updated record for the affected task.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_followers_from_task_response = asana.tasks.remove_followers_from_task(
    task_gid="321654",
    data={
        "followers": ["13579", "321654"],
    },
    opt_pretty=True,
    opt_fields=["actual_time_minutes", "approval_status", "assignee", "assignee.name", "assignee_section", "assignee_section.name", "assignee_status", "completed", "completed_at", "completed_by", "completed_by.name", "created_at", "created_by", "custom_fields", "custom_fields.asana_created_field", "custom_fields.created_by", "custom_fields.created_by.name", "custom_fields.currency_code", "custom_fields.custom_label", "custom_fields.custom_label_position", "custom_fields.date_value", "custom_fields.date_value.date", "custom_fields.date_value.date_time", "custom_fields.description", "custom_fields.display_value", "custom_fields.enabled", "custom_fields.enum_options", "custom_fields.enum_options.color", "custom_fields.enum_options.enabled", "custom_fields.enum_options.name", "custom_fields.enum_value", "custom_fields.enum_value.color", "custom_fields.enum_value.enabled", "custom_fields.enum_value.name", "custom_fields.format", "custom_fields.has_notifications_enabled", "custom_fields.id_prefix", "custom_fields.is_formula_field", "custom_fields.is_global_to_workspace", "custom_fields.is_value_read_only", "custom_fields.multi_enum_values", "custom_fields.multi_enum_values.color", "custom_fields.multi_enum_values.enabled", "custom_fields.multi_enum_values.name", "custom_fields.name", "custom_fields.number_value", "custom_fields.people_value", "custom_fields.people_value.name", "custom_fields.precision", "custom_fields.representation_type", "custom_fields.resource_subtype", "custom_fields.text_value", "custom_fields.type", "dependencies", "dependents", "due_at", "due_on", "external", "external.data", "followers", "followers.name", "hearted", "hearts", "hearts.user", "hearts.user.name", "html_notes", "is_rendered_as_separator", "liked", "likes", "likes.user", "likes.user.name", "memberships", "memberships.project", "memberships.project.name", "memberships.section", "memberships.section.name", "modified_at", "name", "notes", "num_hearts", "num_likes", "num_subtasks", "parent", "parent.created_by", "parent.name", "parent.resource_subtype", "permalink_url", "projects", "projects.name", "resource_subtype", "start_at", "start_on", "tags", "tags.name", "workspace", "workspace.name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### task_gid: `str`<a id="task_gid-str"></a>

The task to operate on.

##### data: [`TaskRemoveFollowersRequest`](./asana_python_sdk/type/task_remove_followers_request.py)<a id="data-taskremovefollowersrequestasana_python_sdktypetask_remove_followers_requestpy"></a>


##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TasksRemoveFollowersFromTaskRequest`](./asana_python_sdk/type/tasks_remove_followers_from_task_request.py)
The followers to remove from the task.

#### 🔄 Return<a id="🔄-return"></a>

[`TasksRemoveFollowersFromTaskResponse`](./asana_python_sdk/pydantic/tasks_remove_followers_from_task_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tasks/{task_gid}/removeFollowers` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.tasks.remove_project_from_task`<a id="asanatasksremove_project_from_task"></a>

Removes the task from the specified project. The task will still exist in
the system, but it will not be in the project anymore.

Returns an empty data block.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_project_from_task_response = asana.tasks.remove_project_from_task(
    task_gid="321654",
    data={
        "project": "13579",
    },
    opt_pretty=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### task_gid: `str`<a id="task_gid-str"></a>

The task to operate on.

##### data: [`TaskRemoveProjectRequest`](./asana_python_sdk/type/task_remove_project_request.py)<a id="data-taskremoveprojectrequestasana_python_sdktypetask_remove_project_requestpy"></a>


##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TasksRemoveProjectFromTaskRequest`](./asana_python_sdk/type/tasks_remove_project_from_task_request.py)
The project to remove the task from.

#### 🔄 Return<a id="🔄-return"></a>

[`TasksRemoveProjectFromTaskResponse`](./asana_python_sdk/pydantic/tasks_remove_project_from_task_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tasks/{task_gid}/removeProject` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.tasks.remove_tag_from_task`<a id="asanatasksremove_tag_from_task"></a>

Removes a tag from a task. Returns an empty data block.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_tag_from_task_response = asana.tasks.remove_tag_from_task(
    task_gid="321654",
    data={
        "tag": "13579",
    },
    opt_pretty=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### task_gid: `str`<a id="task_gid-str"></a>

The task to operate on.

##### data: [`TaskRemoveTagRequest`](./asana_python_sdk/type/task_remove_tag_request.py)<a id="data-taskremovetagrequestasana_python_sdktypetask_remove_tag_requestpy"></a>


##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TasksRemoveTagFromTaskRequest`](./asana_python_sdk/type/tasks_remove_tag_from_task_request.py)
The tag to remove from the task.

#### 🔄 Return<a id="🔄-return"></a>

[`TasksRemoveTagFromTaskResponse`](./asana_python_sdk/pydantic/tasks_remove_tag_from_task_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tasks/{task_gid}/removeTag` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.tasks.search_in_workspace`<a id="asanataskssearch_in_workspace"></a>

To mirror the functionality of the Asana web app's advanced search feature, the Asana API has a task search endpoint that allows you to build complex filters to find and retrieve the exact data you need.
#### Premium access<a id="premium-access"></a>
Like the Asana web product's advance search feature, this search endpoint will only be available to premium Asana users. A user is premium if any of the following is true:

- The workspace in which the search is being performed is a premium workspace - The user is a member of a premium team inside the workspace

Even if a user is only a member of a premium team inside a non-premium workspace, search will allow them to find data anywhere in the workspace, not just inside the premium team. Making a search request using credentials of a non-premium user will result in a `402 Payment Required` error.
#### Pagination<a id="pagination"></a>
Search results are not stable; repeating the same query multiple times may return the data in a different order, even if the data do not change. Because of this, the traditional [pagination](https://developers.asana.com/docs/#pagination) available elsewhere in the Asana API is not available here. However, you can paginate manually by sorting the search results by their creation time and then modifying each subsequent query to exclude data you have already seen. Page sizes are limited to a maximum of 100 items, and can be specified by the `limit` query parameter.
#### Eventual consistency<a id="eventual-consistency"></a>
Changes in Asana (regardless of whether they’re made though the web product or the API) are forwarded to our search infrastructure to be indexed. This process can take between 10 and 60 seconds to complete under normal operation, and longer during some production incidents. Making a change to a task that would alter its presence in a particular search query will not be reflected immediately. This is also true of the advanced search feature in the web product.
#### Rate limits<a id="rate-limits"></a>
You may receive a `429 Too Many Requests` response if you hit any of our [rate limits](https://developers.asana.com/docs/#rate-limits).
#### Custom field parameters<a id="custom-field-parameters"></a>
| Parameter name | Custom field type | Accepted type |
|---|---|---|
| custom_fields.{gid}.is_set | All | Boolean |
| custom_fields.{gid}.value | Text | String |
| custom_fields.{gid}.value | Number | Number |
| custom_fields.{gid}.value | Enum | Enum option ID |
| custom_fields.{gid}.starts_with | Text only | String |
| custom_fields.{gid}.ends_with | Text only | String |
| custom_fields.{gid}.contains | Text only | String |
| custom_fields.{gid}.less_than | Number only | Number |
| custom_fields.{gid}.greater_than | Number only | Number |


For example, if the gid of the custom field is 12345, these query parameter to find tasks where it is set would be `custom_fields.12345.is_set=true`. To match an exact value for an enum custom field, use the gid of the desired enum option and not the name of the enum option: `custom_fields.12345.value=67890`.

**Not Supported**: searching for multiple exact matches of a custom field, searching for multi-enum custom field

*Note: If you specify `projects.any` and `sections.any`, you will receive tasks for the project **and** tasks for the section. If you're looking for only tasks in a section, omit the `projects.any` from the request.*

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
search_in_workspace_response = asana.tasks.search_in_workspace(
    workspace_gid="12345",
    opt_pretty=True,
    text="Bug",
    resource_subtype="milestone",
    assignee_any="12345,23456,34567",
    assignee_not="12345,23456,34567",
    portfolios_any="12345,23456,34567",
    projects_any="12345,23456,34567",
    projects_not="12345,23456,34567",
    projects_all="12345,23456,34567",
    sections_any="12345,23456,34567",
    sections_not="12345,23456,34567",
    sections_all="12345,23456,34567",
    tags_any="12345,23456,34567",
    tags_not="12345,23456,34567",
    tags_all="12345,23456,34567",
    teams_any="12345,23456,34567",
    followers_not="12345,23456,34567",
    created_by_any="12345,23456,34567",
    created_by_not="12345,23456,34567",
    assigned_by_any="12345,23456,34567",
    assigned_by_not="12345,23456,34567",
    liked_by_not="12345,23456,34567",
    commented_on_by_not="12345,23456,34567",
    due_on_before="2019-09-15",
    due_on_after="2019-09-15",
    due_on="2019-09-15",
    due_at_before="2019-04-15T01:01:46.055Z",
    due_at_after="2019-04-15T01:01:46.055Z",
    start_on_before="2019-09-15",
    start_on_after="2019-09-15",
    start_on="2019-09-15",
    created_on_before="2019-09-15",
    created_on_after="2019-09-15",
    created_on="2019-09-15",
    created_at_before="2019-04-15T01:01:46.055Z",
    created_at_after="2019-04-15T01:01:46.055Z",
    completed_on_before="2019-09-15",
    completed_on_after="2019-09-15",
    completed_on="2019-09-15",
    completed_at_before="2019-04-15T01:01:46.055Z",
    completed_at_after="2019-04-15T01:01:46.055Z",
    modified_on_before="2019-09-15",
    modified_on_after="2019-09-15",
    modified_on="2019-09-15",
    modified_at_before="2019-04-15T01:01:46.055Z",
    modified_at_after="2019-04-15T01:01:46.055Z",
    is_blocking=False,
    is_blocked=False,
    has_attachment=False,
    completed=False,
    is_subtask=False,
    sort_by="likes",
    sort_ascending=True,
    opt_fields=["actual_time_minutes", "approval_status", "assignee", "assignee.name", "assignee_section", "assignee_section.name", "assignee_status", "completed", "completed_at", "completed_by", "completed_by.name", "created_at", "created_by", "custom_fields", "custom_fields.asana_created_field", "custom_fields.created_by", "custom_fields.created_by.name", "custom_fields.currency_code", "custom_fields.custom_label", "custom_fields.custom_label_position", "custom_fields.date_value", "custom_fields.date_value.date", "custom_fields.date_value.date_time", "custom_fields.description", "custom_fields.display_value", "custom_fields.enabled", "custom_fields.enum_options", "custom_fields.enum_options.color", "custom_fields.enum_options.enabled", "custom_fields.enum_options.name", "custom_fields.enum_value", "custom_fields.enum_value.color", "custom_fields.enum_value.enabled", "custom_fields.enum_value.name", "custom_fields.format", "custom_fields.has_notifications_enabled", "custom_fields.id_prefix", "custom_fields.is_formula_field", "custom_fields.is_global_to_workspace", "custom_fields.is_value_read_only", "custom_fields.multi_enum_values", "custom_fields.multi_enum_values.color", "custom_fields.multi_enum_values.enabled", "custom_fields.multi_enum_values.name", "custom_fields.name", "custom_fields.number_value", "custom_fields.people_value", "custom_fields.people_value.name", "custom_fields.precision", "custom_fields.representation_type", "custom_fields.resource_subtype", "custom_fields.text_value", "custom_fields.type", "dependencies", "dependents", "due_at", "due_on", "external", "external.data", "followers", "followers.name", "hearted", "hearts", "hearts.user", "hearts.user.name", "html_notes", "is_rendered_as_separator", "liked", "likes", "likes.user", "likes.user.name", "memberships", "memberships.project", "memberships.project.name", "memberships.section", "memberships.section.name", "modified_at", "name", "notes", "num_hearts", "num_likes", "num_subtasks", "parent", "parent.created_by", "parent.name", "parent.resource_subtype", "permalink_url", "projects", "projects.name", "resource_subtype", "start_at", "start_on", "tags", "tags.name", "workspace", "workspace.name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### workspace_gid: `str`<a id="workspace_gid-str"></a>

Globally unique identifier for the workspace or organization.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### text: `str`<a id="text-str"></a>

Performs full-text search on both task name and description

##### resource_subtype: `str`<a id="resource_subtype-str"></a>

Filters results by the task's resource_subtype

##### assignee_any: `str`<a id="assignee_any-str"></a>

Comma-separated list of user identifiers

##### assignee_not: `str`<a id="assignee_not-str"></a>

Comma-separated list of user identifiers

##### portfolios_any: `str`<a id="portfolios_any-str"></a>

Comma-separated list of portfolio IDs

##### projects_any: `str`<a id="projects_any-str"></a>

Comma-separated list of project IDs

##### projects_not: `str`<a id="projects_not-str"></a>

Comma-separated list of project IDs

##### projects_all: `str`<a id="projects_all-str"></a>

Comma-separated list of project IDs

##### sections_any: `str`<a id="sections_any-str"></a>

Comma-separated list of section or column IDs

##### sections_not: `str`<a id="sections_not-str"></a>

Comma-separated list of section or column IDs

##### sections_all: `str`<a id="sections_all-str"></a>

Comma-separated list of section or column IDs

##### tags_any: `str`<a id="tags_any-str"></a>

Comma-separated list of tag IDs

##### tags_not: `str`<a id="tags_not-str"></a>

Comma-separated list of tag IDs

##### tags_all: `str`<a id="tags_all-str"></a>

Comma-separated list of tag IDs

##### teams_any: `str`<a id="teams_any-str"></a>

Comma-separated list of team IDs

##### followers_not: `str`<a id="followers_not-str"></a>

Comma-separated list of user identifiers

##### created_by_any: `str`<a id="created_by_any-str"></a>

Comma-separated list of user identifiers

##### created_by_not: `str`<a id="created_by_not-str"></a>

Comma-separated list of user identifiers

##### assigned_by_any: `str`<a id="assigned_by_any-str"></a>

Comma-separated list of user identifiers

##### assigned_by_not: `str`<a id="assigned_by_not-str"></a>

Comma-separated list of user identifiers

##### liked_by_not: `str`<a id="liked_by_not-str"></a>

Comma-separated list of user identifiers

##### commented_on_by_not: `str`<a id="commented_on_by_not-str"></a>

Comma-separated list of user identifiers

##### due_on_before: `date`<a id="due_on_before-date"></a>

ISO 8601 date string

##### due_on_after: `date`<a id="due_on_after-date"></a>

ISO 8601 date string

##### due_on: `Optional[date]`<a id="due_on-optionaldate"></a>

ISO 8601 date string or `null`

##### due_at_before: `datetime`<a id="due_at_before-datetime"></a>

ISO 8601 datetime string

##### due_at_after: `datetime`<a id="due_at_after-datetime"></a>

ISO 8601 datetime string

##### start_on_before: `date`<a id="start_on_before-date"></a>

ISO 8601 date string

##### start_on_after: `date`<a id="start_on_after-date"></a>

ISO 8601 date string

##### start_on: `Optional[date]`<a id="start_on-optionaldate"></a>

ISO 8601 date string or `null`

##### created_on_before: `date`<a id="created_on_before-date"></a>

ISO 8601 date string

##### created_on_after: `date`<a id="created_on_after-date"></a>

ISO 8601 date string

##### created_on: `Optional[date]`<a id="created_on-optionaldate"></a>

ISO 8601 date string or `null`

##### created_at_before: `datetime`<a id="created_at_before-datetime"></a>

ISO 8601 datetime string

##### created_at_after: `datetime`<a id="created_at_after-datetime"></a>

ISO 8601 datetime string

##### completed_on_before: `date`<a id="completed_on_before-date"></a>

ISO 8601 date string

##### completed_on_after: `date`<a id="completed_on_after-date"></a>

ISO 8601 date string

##### completed_on: `Optional[date]`<a id="completed_on-optionaldate"></a>

ISO 8601 date string or `null`

##### completed_at_before: `datetime`<a id="completed_at_before-datetime"></a>

ISO 8601 datetime string

##### completed_at_after: `datetime`<a id="completed_at_after-datetime"></a>

ISO 8601 datetime string

##### modified_on_before: `date`<a id="modified_on_before-date"></a>

ISO 8601 date string

##### modified_on_after: `date`<a id="modified_on_after-date"></a>

ISO 8601 date string

##### modified_on: `Optional[date]`<a id="modified_on-optionaldate"></a>

ISO 8601 date string or `null`

##### modified_at_before: `datetime`<a id="modified_at_before-datetime"></a>

ISO 8601 datetime string

##### modified_at_after: `datetime`<a id="modified_at_after-datetime"></a>

ISO 8601 datetime string

##### is_blocking: `bool`<a id="is_blocking-bool"></a>

Filter to incomplete tasks with dependents

##### is_blocked: `bool`<a id="is_blocked-bool"></a>

Filter to tasks with incomplete dependencies

##### has_attachment: `bool`<a id="has_attachment-bool"></a>

Filter to tasks with attachments

##### completed: `bool`<a id="completed-bool"></a>

Filter to completed tasks

##### is_subtask: `bool`<a id="is_subtask-bool"></a>

Filter to subtasks

##### sort_by: `str`<a id="sort_by-str"></a>

One of `due_date`, `created_at`, `completed_at`, `likes`, or `modified_at`, defaults to `modified_at`

##### sort_ascending: `bool`<a id="sort_ascending-bool"></a>

Default `false`

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`TasksSearchInWorkspaceResponse`](./asana_python_sdk/pydantic/tasks_search_in_workspace_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workspaces/{workspace_gid}/tasks/search` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.tasks.set_dependencies_for_task`<a id="asanatasksset_dependencies_for_task"></a>

Marks a set of tasks as dependencies of this task, if they are not already dependencies. *A task can have at most 30 dependents and dependencies combined*.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
set_dependencies_for_task_response = asana.tasks.set_dependencies_for_task(
    task_gid="321654",
    data={
    },
    opt_pretty=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### task_gid: `str`<a id="task_gid-str"></a>

The task to operate on.

##### data: [`ModifyDependenciesRequest`](./asana_python_sdk/type/modify_dependencies_request.py)<a id="data-modifydependenciesrequestasana_python_sdktypemodify_dependencies_requestpy"></a>


##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TasksSetDependenciesForTaskRequest`](./asana_python_sdk/type/tasks_set_dependencies_for_task_request.py)
The list of tasks to set as dependencies.

#### 🔄 Return<a id="🔄-return"></a>

[`TasksSetDependenciesForTaskResponse`](./asana_python_sdk/pydantic/tasks_set_dependencies_for_task_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tasks/{task_gid}/addDependencies` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.tasks.set_parent_task`<a id="asanatasksset_parent_task"></a>

parent, or no parent task at all. Returns an empty data block. When using `insert_before` and `insert_after`, at most one of those two options can be specified, and they must already be subtasks of the parent.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
set_parent_task_response = asana.tasks.set_parent_task(
    task_gid="321654",
    data={
        "parent": "987654",
        "insert_after": "null",
        "insert_before": "124816",
    },
    opt_pretty=True,
    opt_fields=["actual_time_minutes", "approval_status", "assignee", "assignee.name", "assignee_section", "assignee_section.name", "assignee_status", "completed", "completed_at", "completed_by", "completed_by.name", "created_at", "created_by", "custom_fields", "custom_fields.asana_created_field", "custom_fields.created_by", "custom_fields.created_by.name", "custom_fields.currency_code", "custom_fields.custom_label", "custom_fields.custom_label_position", "custom_fields.date_value", "custom_fields.date_value.date", "custom_fields.date_value.date_time", "custom_fields.description", "custom_fields.display_value", "custom_fields.enabled", "custom_fields.enum_options", "custom_fields.enum_options.color", "custom_fields.enum_options.enabled", "custom_fields.enum_options.name", "custom_fields.enum_value", "custom_fields.enum_value.color", "custom_fields.enum_value.enabled", "custom_fields.enum_value.name", "custom_fields.format", "custom_fields.has_notifications_enabled", "custom_fields.id_prefix", "custom_fields.is_formula_field", "custom_fields.is_global_to_workspace", "custom_fields.is_value_read_only", "custom_fields.multi_enum_values", "custom_fields.multi_enum_values.color", "custom_fields.multi_enum_values.enabled", "custom_fields.multi_enum_values.name", "custom_fields.name", "custom_fields.number_value", "custom_fields.people_value", "custom_fields.people_value.name", "custom_fields.precision", "custom_fields.representation_type", "custom_fields.resource_subtype", "custom_fields.text_value", "custom_fields.type", "dependencies", "dependents", "due_at", "due_on", "external", "external.data", "followers", "followers.name", "hearted", "hearts", "hearts.user", "hearts.user.name", "html_notes", "is_rendered_as_separator", "liked", "likes", "likes.user", "likes.user.name", "memberships", "memberships.project", "memberships.project.name", "memberships.section", "memberships.section.name", "modified_at", "name", "notes", "num_hearts", "num_likes", "num_subtasks", "parent", "parent.created_by", "parent.name", "parent.resource_subtype", "permalink_url", "projects", "projects.name", "resource_subtype", "start_at", "start_on", "tags", "tags.name", "workspace", "workspace.name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### task_gid: `str`<a id="task_gid-str"></a>

The task to operate on.

##### data: [`TaskSetParentRequest`](./asana_python_sdk/type/task_set_parent_request.py)<a id="data-tasksetparentrequestasana_python_sdktypetask_set_parent_requestpy"></a>


##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TasksSetParentTaskRequest`](./asana_python_sdk/type/tasks_set_parent_task_request.py)
The new parent of the subtask.

#### 🔄 Return<a id="🔄-return"></a>

[`TasksSetParentTaskResponse`](./asana_python_sdk/pydantic/tasks_set_parent_task_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tasks/{task_gid}/setParent` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.tasks.set_task_dependents`<a id="asanatasksset_task_dependents"></a>

Marks a set of tasks as dependents of this task, if they are not already dependents. *A task can have at most 30 dependents and dependencies combined*.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
set_task_dependents_response = asana.tasks.set_task_dependents(
    task_gid="321654",
    data={
    },
    opt_pretty=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### task_gid: `str`<a id="task_gid-str"></a>

The task to operate on.

##### data: [`ModifyDependentsRequest`](./asana_python_sdk/type/modify_dependents_request.py)<a id="data-modifydependentsrequestasana_python_sdktypemodify_dependents_requestpy"></a>


##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TasksSetTaskDependentsRequest`](./asana_python_sdk/type/tasks_set_task_dependents_request.py)
The list of tasks to add as dependents.

#### 🔄 Return<a id="🔄-return"></a>

[`TasksSetTaskDependentsResponse`](./asana_python_sdk/pydantic/tasks_set_task_dependents_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tasks/{task_gid}/addDependents` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.tasks.unlink_dependencies_from_task`<a id="asanatasksunlink_dependencies_from_task"></a>

Unlinks a set of dependencies from this task.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
unlink_dependencies_from_task_response = asana.tasks.unlink_dependencies_from_task(
    task_gid="321654",
    data={
    },
    opt_pretty=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### task_gid: `str`<a id="task_gid-str"></a>

The task to operate on.

##### data: [`ModifyDependenciesRequest`](./asana_python_sdk/type/modify_dependencies_request.py)<a id="data-modifydependenciesrequestasana_python_sdktypemodify_dependencies_requestpy"></a>


##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TasksUnlinkDependenciesFromTaskRequest`](./asana_python_sdk/type/tasks_unlink_dependencies_from_task_request.py)
The list of tasks to unlink as dependencies.

#### 🔄 Return<a id="🔄-return"></a>

[`TasksUnlinkDependenciesFromTaskResponse`](./asana_python_sdk/pydantic/tasks_unlink_dependencies_from_task_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tasks/{task_gid}/removeDependencies` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.tasks.unlink_dependents`<a id="asanatasksunlink_dependents"></a>

Unlinks a set of dependents from this task.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
unlink_dependents_response = asana.tasks.unlink_dependents(
    task_gid="321654",
    data={
    },
    opt_pretty=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### task_gid: `str`<a id="task_gid-str"></a>

The task to operate on.

##### data: [`ModifyDependentsRequest`](./asana_python_sdk/type/modify_dependents_request.py)<a id="data-modifydependentsrequestasana_python_sdktypemodify_dependents_requestpy"></a>


##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TasksUnlinkDependentsRequest`](./asana_python_sdk/type/tasks_unlink_dependents_request.py)
The list of tasks to remove as dependents.

#### 🔄 Return<a id="🔄-return"></a>

[`TasksUnlinkDependentsResponse`](./asana_python_sdk/pydantic/tasks_unlink_dependents_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tasks/{task_gid}/removeDependents` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.tasks.update_task_record`<a id="asanatasksupdate_task_record"></a>

A specific, existing task can be updated by making a PUT request on the
URL for that task. Only the fields provided in the `data` block will be
updated; any unspecified fields will remain unchanged.

When using this method, it is best to specify only those fields you wish
to change, or else you may overwrite changes made by another user since
you last retrieved the task.

Returns the complete updated task record.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_task_record_response = asana.tasks.update_task_record(
    task_gid="321654",
    data=None,
    opt_pretty=True,
    opt_fields=["actual_time_minutes", "approval_status", "assignee", "assignee.name", "assignee_section", "assignee_section.name", "assignee_status", "completed", "completed_at", "completed_by", "completed_by.name", "created_at", "created_by", "custom_fields", "custom_fields.asana_created_field", "custom_fields.created_by", "custom_fields.created_by.name", "custom_fields.currency_code", "custom_fields.custom_label", "custom_fields.custom_label_position", "custom_fields.date_value", "custom_fields.date_value.date", "custom_fields.date_value.date_time", "custom_fields.description", "custom_fields.display_value", "custom_fields.enabled", "custom_fields.enum_options", "custom_fields.enum_options.color", "custom_fields.enum_options.enabled", "custom_fields.enum_options.name", "custom_fields.enum_value", "custom_fields.enum_value.color", "custom_fields.enum_value.enabled", "custom_fields.enum_value.name", "custom_fields.format", "custom_fields.has_notifications_enabled", "custom_fields.id_prefix", "custom_fields.is_formula_field", "custom_fields.is_global_to_workspace", "custom_fields.is_value_read_only", "custom_fields.multi_enum_values", "custom_fields.multi_enum_values.color", "custom_fields.multi_enum_values.enabled", "custom_fields.multi_enum_values.name", "custom_fields.name", "custom_fields.number_value", "custom_fields.people_value", "custom_fields.people_value.name", "custom_fields.precision", "custom_fields.representation_type", "custom_fields.resource_subtype", "custom_fields.text_value", "custom_fields.type", "dependencies", "dependents", "due_at", "due_on", "external", "external.data", "followers", "followers.name", "hearted", "hearts", "hearts.user", "hearts.user.name", "html_notes", "is_rendered_as_separator", "liked", "likes", "likes.user", "likes.user.name", "memberships", "memberships.project", "memberships.project.name", "memberships.section", "memberships.section.name", "modified_at", "name", "notes", "num_hearts", "num_likes", "num_subtasks", "parent", "parent.created_by", "parent.name", "parent.resource_subtype", "permalink_url", "projects", "projects.name", "resource_subtype", "start_at", "start_on", "tags", "tags.name", "workspace", "workspace.name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### task_gid: `str`<a id="task_gid-str"></a>

The task to operate on.

##### data: `TaskRequest`<a id="data-taskrequest"></a>

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TasksUpdateTaskRecordRequest`](./asana_python_sdk/type/tasks_update_task_record_request.py)
The task to update.

#### 🔄 Return<a id="🔄-return"></a>

[`TasksUpdateTaskRecordResponse`](./asana_python_sdk/pydantic/tasks_update_task_record_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tasks/{task_gid}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.team_memberships.get_compact`<a id="asanateam_membershipsget_compact"></a>

Returns the compact team memberships for the team.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_compact_response = asana.team_memberships.get_compact(
    team_gid="159874",
    opt_pretty=True,
    limit=50,
    offset="eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9",
    opt_fields=["is_admin", "is_guest", "is_limited_access", "offset", "path", "team", "team.name", "uri", "user", "user.name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### team_gid: `str`<a id="team_gid-str"></a>

Globally unique identifier for the team.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### limit: `int`<a id="limit-int"></a>

Results per page. The number of objects to return per page. The value must be between 1 and 100.

##### offset: `str`<a id="offset-str"></a>

Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`TeamMembershipsGetCompactResponse`](./asana_python_sdk/pydantic/team_memberships_get_compact_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teams/{team_gid}/team_memberships` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.team_memberships.get_compact_records`<a id="asanateam_membershipsget_compact_records"></a>

Returns compact team membership records.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_compact_records_response = asana.team_memberships.get_compact_records(
    opt_pretty=True,
    limit=50,
    offset="eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9",
    team="159874",
    user="512241",
    workspace="31326",
    opt_fields=["is_admin", "is_guest", "is_limited_access", "offset", "path", "team", "team.name", "uri", "user", "user.name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### limit: `int`<a id="limit-int"></a>

Results per page. The number of objects to return per page. The value must be between 1 and 100.

##### offset: `str`<a id="offset-str"></a>

Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'

##### team: `str`<a id="team-str"></a>

Globally unique identifier for the team.

##### user: `str`<a id="user-str"></a>

A string identifying a user. This can either be the string \"me\", an email, or the gid of a user. This parameter must be used with the workspace parameter.

##### workspace: `str`<a id="workspace-str"></a>

Globally unique identifier for the workspace. This parameter must be used with the user parameter.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`TeamMembershipsGetCompactRecordsResponse`](./asana_python_sdk/pydantic/team_memberships_get_compact_records_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/team_memberships` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.team_memberships.get_record_by_id`<a id="asanateam_membershipsget_record_by_id"></a>

Returns the complete team membership record for a single team membership.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_record_by_id_response = asana.team_memberships.get_record_by_id(
    team_membership_gid="724362",
    opt_pretty=True,
    opt_fields=["is_admin", "is_guest", "is_limited_access", "team", "team.name", "user", "user.name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### team_membership_gid: `str`<a id="team_membership_gid-str"></a>

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`TeamMembershipsGetRecordByIdResponse`](./asana_python_sdk/pydantic/team_memberships_get_record_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/team_memberships/{team_membership_gid}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.team_memberships.get_user_compact`<a id="asanateam_membershipsget_user_compact"></a>

Returns the compact team membership records for the user.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_compact_response = asana.team_memberships.get_user_compact(
    user_gid="me",
    workspace="31326",
    opt_pretty=True,
    limit=50,
    offset="eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9",
    opt_fields=["is_admin", "is_guest", "is_limited_access", "offset", "path", "team", "team.name", "uri", "user", "user.name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_gid: `str`<a id="user_gid-str"></a>

A string identifying a user. This can either be the string \"me\", an email, or the gid of a user.

##### workspace: `str`<a id="workspace-str"></a>

Globally unique identifier for the workspace.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### limit: `int`<a id="limit-int"></a>

Results per page. The number of objects to return per page. The value must be between 1 and 100.

##### offset: `str`<a id="offset-str"></a>

Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`TeamMembershipsGetUserCompactResponse`](./asana_python_sdk/pydantic/team_memberships_get_user_compact_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{user_gid}/team_memberships` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.teams.add_user_to_team`<a id="asanateamsadd_user_to_team"></a>

The user making this call must be a member of the team in order to add others. The user being added must exist in the same organization as the team.

Returns the complete team membership record for the newly added user.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_user_to_team_response = asana.teams.add_user_to_team(
    team_gid="159874",
    data={
        "user": "12345",
    },
    opt_pretty=True,
    opt_fields=["is_admin", "is_guest", "is_limited_access", "team", "team.name", "user", "user.name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### team_gid: `str`<a id="team_gid-str"></a>

Globally unique identifier for the team.

##### data: [`TeamAddUserRequest`](./asana_python_sdk/type/team_add_user_request.py)<a id="data-teamadduserrequestasana_python_sdktypeteam_add_user_requestpy"></a>


##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TeamsAddUserToTeamRequest`](./asana_python_sdk/type/teams_add_user_to_team_request.py)
The user to add to the team.

#### 🔄 Return<a id="🔄-return"></a>

[`TeamsAddUserToTeamResponse`](./asana_python_sdk/pydantic/teams_add_user_to_team_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teams/{team_gid}/addUser` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.teams.create_team_record`<a id="asanateamscreate_team_record"></a>

Creates a team within the current workspace.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_team_record_response = asana.teams.create_team_record(
    data=None,
    opt_pretty=True,
    opt_fields=["description", "edit_team_name_or_description_access_level", "edit_team_visibility_or_trash_team_access_level", "guest_invite_management_access_level", "html_description", "join_request_management_access_level", "member_invite_management_access_level", "name", "organization", "organization.name", "permalink_url", "team_member_removal_access_level", "visibility"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### data: `TeamRequest`<a id="data-teamrequest"></a>

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TeamsCreateTeamRecordRequest`](./asana_python_sdk/type/teams_create_team_record_request.py)
The team to create.

#### 🔄 Return<a id="🔄-return"></a>

[`TeamsCreateTeamRecordResponse`](./asana_python_sdk/pydantic/teams_create_team_record_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teams` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.teams.get_team_record`<a id="asanateamsget_team_record"></a>

Returns the full record for a single team.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_team_record_response = asana.teams.get_team_record(
    team_gid="159874",
    opt_pretty=True,
    opt_fields=["description", "edit_team_name_or_description_access_level", "edit_team_visibility_or_trash_team_access_level", "guest_invite_management_access_level", "html_description", "join_request_management_access_level", "member_invite_management_access_level", "name", "organization", "organization.name", "permalink_url", "team_member_removal_access_level", "visibility"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### team_gid: `str`<a id="team_gid-str"></a>

Globally unique identifier for the team.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`TeamsGetTeamRecordResponse`](./asana_python_sdk/pydantic/teams_get_team_record_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teams/{team_gid}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.teams.get_user_teams`<a id="asanateamsget_user_teams"></a>

Returns the compact records for all teams to which the given user is assigned.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_teams_response = asana.teams.get_user_teams(
    user_gid="me",
    organization="1331",
    opt_pretty=True,
    limit=50,
    offset="eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9",
    opt_fields=["description", "edit_team_name_or_description_access_level", "edit_team_visibility_or_trash_team_access_level", "guest_invite_management_access_level", "html_description", "join_request_management_access_level", "member_invite_management_access_level", "name", "offset", "organization", "organization.name", "path", "permalink_url", "team_member_removal_access_level", "uri", "visibility"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_gid: `str`<a id="user_gid-str"></a>

A string identifying a user. This can either be the string \"me\", an email, or the gid of a user.

##### organization: `str`<a id="organization-str"></a>

The workspace or organization to filter teams on.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### limit: `int`<a id="limit-int"></a>

Results per page. The number of objects to return per page. The value must be between 1 and 100.

##### offset: `str`<a id="offset-str"></a>

Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`TeamsGetUserTeamsResponse`](./asana_python_sdk/pydantic/teams_get_user_teams_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{user_gid}/teams` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.teams.list_workspace_teams`<a id="asanateamslist_workspace_teams"></a>

Returns the compact records for all teams in the workspace visible to the authorized user.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_workspace_teams_response = asana.teams.list_workspace_teams(
    workspace_gid="12345",
    opt_pretty=True,
    limit=50,
    offset="eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9",
    opt_fields=["description", "edit_team_name_or_description_access_level", "edit_team_visibility_or_trash_team_access_level", "guest_invite_management_access_level", "html_description", "join_request_management_access_level", "member_invite_management_access_level", "name", "offset", "organization", "organization.name", "path", "permalink_url", "team_member_removal_access_level", "uri", "visibility"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### workspace_gid: `str`<a id="workspace_gid-str"></a>

Globally unique identifier for the workspace or organization.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### limit: `int`<a id="limit-int"></a>

Results per page. The number of objects to return per page. The value must be between 1 and 100.

##### offset: `str`<a id="offset-str"></a>

Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`TeamsListWorkspaceTeamsResponse`](./asana_python_sdk/pydantic/teams_list_workspace_teams_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workspaces/{workspace_gid}/teams` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.teams.remove_user_from_team`<a id="asanateamsremove_user_from_team"></a>

The user making this call must be a member of the team in order to remove themselves or others.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_user_from_team_response = asana.teams.remove_user_from_team(
    team_gid="159874",
    data={
        "user": "12345",
    },
    opt_pretty=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### team_gid: `str`<a id="team_gid-str"></a>

Globally unique identifier for the team.

##### data: [`TeamRemoveUserRequest`](./asana_python_sdk/type/team_remove_user_request.py)<a id="data-teamremoveuserrequestasana_python_sdktypeteam_remove_user_requestpy"></a>


##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TeamsRemoveUserFromTeamRequest`](./asana_python_sdk/type/teams_remove_user_from_team_request.py)
The user to remove from the team.

#### 🔄 Return<a id="🔄-return"></a>

[`TeamsRemoveUserFromTeamResponse`](./asana_python_sdk/pydantic/teams_remove_user_from_team_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teams/{team_gid}/removeUser` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.teams.update_team_record`<a id="asanateamsupdate_team_record"></a>

Updates a team within the current workspace.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_team_record_response = asana.teams.update_team_record(
    team_gid="159874",
    data=None,
    opt_pretty=True,
    opt_fields=["description", "edit_team_name_or_description_access_level", "edit_team_visibility_or_trash_team_access_level", "guest_invite_management_access_level", "html_description", "join_request_management_access_level", "member_invite_management_access_level", "name", "organization", "organization.name", "permalink_url", "team_member_removal_access_level", "visibility"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### team_gid: `str`<a id="team_gid-str"></a>

Globally unique identifier for the team.

##### data: `TeamRequest`<a id="data-teamrequest"></a>

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TeamsUpdateTeamRecordRequest`](./asana_python_sdk/type/teams_update_team_record_request.py)
The team to update.

#### 🔄 Return<a id="🔄-return"></a>

[`TeamsUpdateTeamRecordResponse`](./asana_python_sdk/pydantic/teams_update_team_record_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teams/{team_gid}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.time_periods.get_compact_time_periods`<a id="asanatime_periodsget_compact_time_periods"></a>

Returns compact time period records.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_compact_time_periods_response = asana.time_periods.get_compact_time_periods(
    workspace="31326",
    opt_pretty=True,
    limit=50,
    offset="eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9",
    start_on="2019-09-15",
    end_on="2019-09-15",
    opt_fields=["display_name", "end_on", "offset", "parent", "parent.display_name", "parent.end_on", "parent.period", "parent.start_on", "path", "period", "start_on", "uri"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### workspace: `str`<a id="workspace-str"></a>

Globally unique identifier for the workspace.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### limit: `int`<a id="limit-int"></a>

Results per page. The number of objects to return per page. The value must be between 1 and 100.

##### offset: `str`<a id="offset-str"></a>

Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'

##### start_on: `date`<a id="start_on-date"></a>

ISO 8601 date string

##### end_on: `date`<a id="end_on-date"></a>

ISO 8601 date string

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`TimePeriodsGetCompactTimePeriodsResponse`](./asana_python_sdk/pydantic/time_periods_get_compact_time_periods_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/time_periods` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.time_periods.get_full_record`<a id="asanatime_periodsget_full_record"></a>

Returns the full record for a single time period.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_full_record_response = asana.time_periods.get_full_record(
    time_period_gid="917392",
    opt_pretty=True,
    opt_fields=["display_name", "end_on", "parent", "parent.display_name", "parent.end_on", "parent.period", "parent.start_on", "period", "start_on"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### time_period_gid: `str`<a id="time_period_gid-str"></a>

Globally unique identifier for the time period.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`TimePeriodsGetFullRecordResponse`](./asana_python_sdk/pydantic/time_periods_get_full_record_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/time_periods/{time_period_gid}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.time_tracking_entries.create_new_time_entry_record`<a id="asanatime_tracking_entriescreate_new_time_entry_record"></a>

Creates a time tracking entry on a given task.

Returns the record of the newly created time tracking entry.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_time_entry_record_response = asana.time_tracking_entries.create_new_time_entry_record(
    task_gid="321654",
    data={
        "duration_minutes": 12,
        "entered_on": "2023-03-19",
    },
    opt_pretty=True,
    opt_fields=["created_at", "created_by", "created_by.name", "duration_minutes", "entered_on", "task", "task.created_by", "task.name", "task.resource_subtype"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### task_gid: `str`<a id="task_gid-str"></a>

The task to operate on.

##### data: [`CreateTimeTrackingEntryRequest`](./asana_python_sdk/type/create_time_tracking_entry_request.py)<a id="data-createtimetrackingentryrequestasana_python_sdktypecreate_time_tracking_entry_requestpy"></a>


##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TimeTrackingEntriesCreateNewTimeEntryRecordRequest`](./asana_python_sdk/type/time_tracking_entries_create_new_time_entry_record_request.py)
Information about the time tracking entry.

#### 🔄 Return<a id="🔄-return"></a>

[`TimeTrackingEntriesCreateNewTimeEntryRecordResponse`](./asana_python_sdk/pydantic/time_tracking_entries_create_new_time_entry_record_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tasks/{task_gid}/time_tracking_entries` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.time_tracking_entries.delete_time_entry`<a id="asanatime_tracking_entriesdelete_time_entry"></a>

A specific, existing time tracking entry can be deleted by making a `DELETE` request on
the URL for that time tracking entry.

Returns an empty data record.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_time_entry_response = asana.time_tracking_entries.delete_time_entry(
    time_tracking_entry_gid="917392",
    opt_pretty=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### time_tracking_entry_gid: `str`<a id="time_tracking_entry_gid-str"></a>

Globally unique identifier for the time tracking entry.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

#### 🔄 Return<a id="🔄-return"></a>

[`TimeTrackingEntriesDeleteTimeEntryResponse`](./asana_python_sdk/pydantic/time_tracking_entries_delete_time_entry_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/time_tracking_entries/{time_tracking_entry_gid}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.time_tracking_entries.get_for_task`<a id="asanatime_tracking_entriesget_for_task"></a>

Returns time tracking entries for a given task.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_for_task_response = asana.time_tracking_entries.get_for_task(
    task_gid="321654",
    opt_pretty=True,
    limit=50,
    offset="eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9",
    opt_fields=["created_by", "created_by.name", "duration_minutes", "entered_on", "offset", "path", "uri"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### task_gid: `str`<a id="task_gid-str"></a>

The task to operate on.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### limit: `int`<a id="limit-int"></a>

Results per page. The number of objects to return per page. The value must be between 1 and 100.

##### offset: `str`<a id="offset-str"></a>

Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`TimeTrackingEntriesGetForTaskResponse`](./asana_python_sdk/pydantic/time_tracking_entries_get_for_task_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tasks/{task_gid}/time_tracking_entries` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.time_tracking_entries.get_record`<a id="asanatime_tracking_entriesget_record"></a>

Returns the complete time tracking entry record for a single time tracking entry.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_record_response = asana.time_tracking_entries.get_record(
    time_tracking_entry_gid="917392",
    opt_pretty=True,
    opt_fields=["created_at", "created_by", "created_by.name", "duration_minutes", "entered_on", "task", "task.created_by", "task.name", "task.resource_subtype"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### time_tracking_entry_gid: `str`<a id="time_tracking_entry_gid-str"></a>

Globally unique identifier for the time tracking entry.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`TimeTrackingEntriesGetRecordResponse`](./asana_python_sdk/pydantic/time_tracking_entries_get_record_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/time_tracking_entries/{time_tracking_entry_gid}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.time_tracking_entries.update_time_tracking_entry`<a id="asanatime_tracking_entriesupdate_time_tracking_entry"></a>

A specific, existing time tracking entry can be updated by making a `PUT` request on
the URL for that time tracking entry. Only the fields provided in the `data` block
will be updated; any unspecified fields will remain unchanged.

When using this method, it is best to specify only those fields you wish
to change, or else you may overwrite changes made by another user since
you last retrieved the task.

Returns the complete updated time tracking entry record.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_time_tracking_entry_response = asana.time_tracking_entries.update_time_tracking_entry(
    time_tracking_entry_gid="917392",
    data={
        "duration_minutes": 12,
        "entered_on": "2023-03-19",
    },
    opt_pretty=True,
    opt_fields=["created_at", "created_by", "created_by.name", "duration_minutes", "entered_on", "task", "task.created_by", "task.name", "task.resource_subtype"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### time_tracking_entry_gid: `str`<a id="time_tracking_entry_gid-str"></a>

Globally unique identifier for the time tracking entry.

##### data: [`UpdateTimeTrackingEntryRequest`](./asana_python_sdk/type/update_time_tracking_entry_request.py)<a id="data-updatetimetrackingentryrequestasana_python_sdktypeupdate_time_tracking_entry_requestpy"></a>


##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TimeTrackingEntriesUpdateTimeTrackingEntryRequest`](./asana_python_sdk/type/time_tracking_entries_update_time_tracking_entry_request.py)
The updated fields for the time tracking entry.

#### 🔄 Return<a id="🔄-return"></a>

[`TimeTrackingEntriesUpdateTimeTrackingEntryResponse`](./asana_python_sdk/pydantic/time_tracking_entries_update_time_tracking_entry_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/time_tracking_entries/{time_tracking_entry_gid}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.typeahead.get_results`<a id="asanatypeaheadget_results"></a>

Retrieves objects in the workspace based via an auto-completion/typeahead
search algorithm. This feature is meant to provide results quickly, so do
not rely on this API to provide extremely accurate search results. The
result set is limited to a single page of results with a maximum size, so
you won’t be able to fetch large numbers of results.

The typeahead search API provides search for objects from a single
workspace. This endpoint should be used to query for objects when
creating an auto-completion/typeahead search feature. This API is meant
to provide results quickly and should not be relied upon for accurate or
exhaustive search results. The results sets are limited in size and
cannot be paginated.

Queries return a compact representation of each object which is typically
the gid and name fields. Interested in a specific set of fields or all of
the fields?! Of course you are. Use field selectors to manipulate what
data is included in a response.

Resources with type `user` are returned in order of most contacted to
least contacted. This is determined by task assignments, adding the user
to projects, and adding the user as a follower to tasks, messages,
etc.

Resources with type `project` are returned in order of recency. This is
determined when the user visits the project, is added to the project, and
completes tasks in the project.

Resources with type `task` are returned with priority placed on tasks
the user is following, but no guarantee on the order of those tasks.

Resources with type `project_template` are returned with priority
placed on favorited project templates.

Leaving the `query` string empty or omitted will give you results, still
following the resource ordering above. This could be used to list users or
projects that are relevant for the requesting user's api token.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_results_response = asana.typeahead.get_results(
    workspace_gid="12345",
    resource_type="user",
    type="user",
    query="Greg",
    count=20,
    opt_pretty=True,
    opt_fields=["name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### workspace_gid: `str`<a id="workspace_gid-str"></a>

Globally unique identifier for the workspace or organization.

##### resource_type: `str`<a id="resource_type-str"></a>

The type of values the typeahead should return. You can choose from one of the following: `custom_field`, `goal`, `project`, `project_template`, `portfolio`, `tag`, `task`, `team`, and `user`. Note that unlike in the names of endpoints, the types listed here are in singular form (e.g. `task`). Using multiple types is not yet supported.

##### type: `str`<a id="type-str"></a>

*Deprecated: new integrations should prefer the resource_type field.*

##### query: `str`<a id="query-str"></a>

The string that will be used to search for relevant objects. If an empty string is passed in, the API will return results.

##### count: `int`<a id="count-int"></a>

The number of results to return. The default is 20 if this parameter is omitted, with a minimum of 1 and a maximum of 100. If there are fewer results found than requested, all will be returned.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`TypeaheadGetResultsResponse`](./asana_python_sdk/pydantic/typeahead_get_results_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workspaces/{workspace_gid}/typeahead` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.user_task_lists.get_record`<a id="asanauser_task_listsget_record"></a>

Returns the full record for a user task list.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_record_response = asana.user_task_lists.get_record(
    user_task_list_gid="12345",
    opt_pretty=True,
    opt_fields=["name", "owner", "workspace"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_task_list_gid: `str`<a id="user_task_list_gid-str"></a>

Globally unique identifier for the user task list.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`UserTaskListsGetRecordResponse`](./asana_python_sdk/pydantic/user_task_lists_get_record_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/user_task_lists/{user_task_list_gid}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.user_task_lists.get_user_task_list`<a id="asanauser_task_listsget_user_task_list"></a>

Returns the full record for a user's task list.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_task_list_response = asana.user_task_lists.get_user_task_list(
    user_gid="me",
    workspace="1234",
    opt_pretty=True,
    opt_fields=["name", "owner", "workspace"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_gid: `str`<a id="user_gid-str"></a>

A string identifying a user. This can either be the string \"me\", an email, or the gid of a user.

##### workspace: `str`<a id="workspace-str"></a>

The workspace in which to get the user task list.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`UserTaskListsGetUserTaskListResponse`](./asana_python_sdk/pydantic/user_task_lists_get_user_task_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{user_gid}/user_task_list` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.users.get_favorites_for_user`<a id="asanausersget_favorites_for_user"></a>

Returns all of a user's favorites in the given workspace, of the given type.
Results are given in order (The same order as Asana's sidebar).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_favorites_for_user_response = asana.users.get_favorites_for_user(
    user_gid="me",
    resource_type="project",
    workspace="1234",
    opt_pretty=True,
    limit=50,
    offset="eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9",
    opt_fields=["name", "offset", "path", "uri"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_gid: `str`<a id="user_gid-str"></a>

A string identifying a user. This can either be the string \"me\", an email, or the gid of a user.

##### resource_type: `str`<a id="resource_type-str"></a>

The resource type of favorites to be returned.

##### workspace: `str`<a id="workspace-str"></a>

The workspace in which to get favorites.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### limit: `int`<a id="limit-int"></a>

Results per page. The number of objects to return per page. The value must be between 1 and 100.

##### offset: `str`<a id="offset-str"></a>

Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`UsersGetFavoritesForUserResponse`](./asana_python_sdk/pydantic/users_get_favorites_for_user_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{user_gid}/favorites` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.users.get_user_record`<a id="asanausersget_user_record"></a>

Returns the full user record for the single user with the provided ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_record_response = asana.users.get_user_record(
    user_gid="me",
    opt_pretty=True,
    opt_fields=["email", "name", "photo", "photo.image_1024x1024", "photo.image_128x128", "photo.image_21x21", "photo.image_27x27", "photo.image_36x36", "photo.image_60x60", "workspaces", "workspaces.name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_gid: `str`<a id="user_gid-str"></a>

A string identifying a user. This can either be the string \"me\", an email, or the gid of a user.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`UsersGetUserRecordResponse`](./asana_python_sdk/pydantic/users_get_user_record_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{user_gid}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.users.list_multiple_users`<a id="asanauserslist_multiple_users"></a>

Returns the user records for all users in all workspaces and organizations accessible to the authenticated user. Accepts an optional workspace ID parameter.
Results are sorted by user ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_multiple_users_response = asana.users.list_multiple_users(
    workspace="1331",
    team="15627",
    opt_pretty=True,
    limit=50,
    offset="eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9",
    opt_fields=["email", "name", "offset", "path", "photo", "photo.image_1024x1024", "photo.image_128x128", "photo.image_21x21", "photo.image_27x27", "photo.image_36x36", "photo.image_60x60", "uri", "workspaces", "workspaces.name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### workspace: `str`<a id="workspace-str"></a>

The workspace or organization ID to filter users on.

##### team: `str`<a id="team-str"></a>

The team ID to filter users on.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### limit: `int`<a id="limit-int"></a>

Results per page. The number of objects to return per page. The value must be between 1 and 100.

##### offset: `str`<a id="offset-str"></a>

Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`ErrorResponse`](./asana_python_sdk/pydantic/error_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.users.list_team_users`<a id="asanauserslist_team_users"></a>

Returns the compact records for all users that are members of the team.
Results are sorted alphabetically and limited to 2000. For more results use the `/users` endpoint.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_team_users_response = asana.users.list_team_users(
    team_gid="159874",
    opt_pretty=True,
    offset="eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9",
    opt_fields=["email", "name", "photo", "photo.image_1024x1024", "photo.image_128x128", "photo.image_21x21", "photo.image_27x27", "photo.image_36x36", "photo.image_60x60", "workspaces", "workspaces.name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### team_gid: `str`<a id="team_gid-str"></a>

Globally unique identifier for the team.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### offset: `str`<a id="offset-str"></a>

Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`UsersListTeamUsersResponse`](./asana_python_sdk/pydantic/users_list_team_users_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teams/{team_gid}/users` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.users.list_workspace_users`<a id="asanauserslist_workspace_users"></a>

Returns the compact records for all users in the specified workspace or organization.
Results are sorted alphabetically and limited to 2000. For more results use the `/users` endpoint.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_workspace_users_response = asana.users.list_workspace_users(
    workspace_gid="12345",
    opt_pretty=True,
    offset="eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9",
    opt_fields=["email", "name", "photo", "photo.image_1024x1024", "photo.image_128x128", "photo.image_21x21", "photo.image_27x27", "photo.image_36x36", "photo.image_60x60", "workspaces", "workspaces.name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### workspace_gid: `str`<a id="workspace_gid-str"></a>

Globally unique identifier for the workspace or organization.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### offset: `str`<a id="offset-str"></a>

Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`UsersListWorkspaceUsersResponse`](./asana_python_sdk/pydantic/users_list_workspace_users_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workspaces/{workspace_gid}/users` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.webhooks.establish_webhook`<a id="asanawebhooksestablish_webhook"></a>

Establishing a webhook is a two-part process. First, a simple HTTP POST
request initiates the creation similar to creating any other resource.

Next, in the middle of this request comes the confirmation handshake.
When a webhook is created, we will send a test POST to the target with an
`X-Hook-Secret` header. The target must respond with a `200 OK` or `204
No Content` and a matching `X-Hook-Secret` header to confirm that this
webhook subscription is indeed expected. We strongly recommend storing
this secret to be used to verify future webhook event signatures.

The POST request to create the webhook will then return with the status
of the request. If you do not acknowledge the webhook’s confirmation
handshake it will fail to setup, and you will receive an error in
response to your attempt to create it. This means you need to be able to
receive and complete the webhook *while* the POST request is in-flight
(in other words, have a server that can handle requests asynchronously).

Invalid hostnames like localhost will recieve a 403 Forbidden status code.

```
# Request
curl -H "Authorization: Bearer <personal_access_token>" \
-X POST https://app.asana.com/api/1.0/webhooks \
-d "resource=8675309" \
-d "target=https://example.com/receive-webhook/7654"
```

```
# Handshake sent to https://example.com/
POST /receive-webhook/7654
X-Hook-Secret: b537207f20cbfa02357cf448134da559e8bd39d61597dcd5631b8012eae53e81
```

```
# Handshake response sent by example.com
HTTP/1.1 200
X-Hook-Secret: b537207f20cbfa02357cf448134da559e8bd39d61597dcd5631b8012eae53e81
```

```
# Response
HTTP/1.1 201
{
  "data": {
    "gid": "43214",
    "resource": {
      "gid": "8675309",
      "name": "Bugs"
    },
    "target": "https://example.com/receive-webhook/7654",
    "active": false,
    "last_success_at": null,
    "last_failure_at": null,
    "last_failure_content": null
  }
}
```

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
establish_webhook_response = asana.webhooks.establish_webhook(
    data={
        "resource": "12345",
        "target": "https://example.com/receive-webhook/7654?app_specific_param=app_specific_value",
    },
    opt_pretty=True,
    opt_fields=["active", "created_at", "filters", "filters.action", "filters.fields", "filters.resource_subtype", "last_failure_at", "last_failure_content", "last_success_at", "resource", "resource.name", "target"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### data: [`WebhookRequest`](./asana_python_sdk/type/webhook_request.py)<a id="data-webhookrequestasana_python_sdktypewebhook_requestpy"></a>


##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WebhooksEstablishWebhookRequest`](./asana_python_sdk/type/webhooks_establish_webhook_request.py)
The webhook workspace and target.

#### 🔄 Return<a id="🔄-return"></a>

[`WebhooksEstablishWebhookResponse`](./asana_python_sdk/pydantic/webhooks_establish_webhook_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webhooks` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.webhooks.get_webhook_record`<a id="asanawebhooksget_webhook_record"></a>

Returns the full record for the given webhook.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_webhook_record_response = asana.webhooks.get_webhook_record(
    webhook_gid="12345",
    opt_pretty=True,
    opt_fields=["active", "created_at", "filters", "filters.action", "filters.fields", "filters.resource_subtype", "last_failure_at", "last_failure_content", "last_success_at", "resource", "resource.name", "target"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### webhook_gid: `str`<a id="webhook_gid-str"></a>

Globally unique identifier for the webhook.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`WebhooksGetWebhookRecordResponse`](./asana_python_sdk/pydantic/webhooks_get_webhook_record_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webhooks/{webhook_gid}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.webhooks.list_multiple_webhooks`<a id="asanawebhookslist_multiple_webhooks"></a>

Get the compact representation of all webhooks your app has registered for the authenticated user in the given workspace.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_multiple_webhooks_response = asana.webhooks.list_multiple_webhooks(
    workspace="1331",
    opt_pretty=True,
    limit=50,
    offset="eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9",
    resource="51648",
    opt_fields=["active", "created_at", "filters", "filters.action", "filters.fields", "filters.resource_subtype", "last_failure_at", "last_failure_content", "last_success_at", "offset", "path", "resource", "resource.name", "target", "uri"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### workspace: `str`<a id="workspace-str"></a>

The workspace to query for webhooks in.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### limit: `int`<a id="limit-int"></a>

Results per page. The number of objects to return per page. The value must be between 1 and 100.

##### offset: `str`<a id="offset-str"></a>

Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'

##### resource: `str`<a id="resource-str"></a>

Only return webhooks for the given resource.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`WebhooksListMultipleWebhooksResponse`](./asana_python_sdk/pydantic/webhooks_list_multiple_webhooks_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webhooks` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.webhooks.remove_webhook`<a id="asanawebhooksremove_webhook"></a>

This method *permanently* removes a webhook. Note that it may be possible to receive a request that was already in flight after deleting the webhook, but no further requests will be issued.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_webhook_response = asana.webhooks.remove_webhook(
    webhook_gid="12345",
    opt_pretty=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### webhook_gid: `str`<a id="webhook_gid-str"></a>

Globally unique identifier for the webhook.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

#### 🔄 Return<a id="🔄-return"></a>

[`WebhooksRemoveWebhookResponse`](./asana_python_sdk/pydantic/webhooks_remove_webhook_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webhooks/{webhook_gid}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.webhooks.update_webhook_filters`<a id="asanawebhooksupdate_webhook_filters"></a>

An existing webhook's filters can be updated by making a PUT request on the URL for that webhook. Note that the webhook's previous `filters` array will be completely overwritten by the `filters` sent in the PUT request.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_webhook_filters_response = asana.webhooks.update_webhook_filters(
    webhook_gid="12345",
    data={
    },
    opt_pretty=True,
    opt_fields=["active", "created_at", "filters", "filters.action", "filters.fields", "filters.resource_subtype", "last_failure_at", "last_failure_content", "last_success_at", "resource", "resource.name", "target"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### webhook_gid: `str`<a id="webhook_gid-str"></a>

Globally unique identifier for the webhook.

##### data: [`WebhookUpdateRequest`](./asana_python_sdk/type/webhook_update_request.py)<a id="data-webhookupdaterequestasana_python_sdktypewebhook_update_requestpy"></a>


##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WebhooksUpdateWebhookFiltersRequest`](./asana_python_sdk/type/webhooks_update_webhook_filters_request.py)
The updated filters for the webhook.

#### 🔄 Return<a id="🔄-return"></a>

[`WebhooksUpdateWebhookFiltersResponse`](./asana_python_sdk/pydantic/webhooks_update_webhook_filters_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webhooks/{webhook_gid}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.workspace_memberships.get_record_by_id`<a id="asanaworkspace_membershipsget_record_by_id"></a>

Returns the complete workspace record for a single workspace membership.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_record_by_id_response = asana.workspace_memberships.get_record_by_id(
    workspace_membership_gid="12345",
    opt_pretty=True,
    opt_fields=["created_at", "is_active", "is_admin", "is_guest", "user", "user.name", "user_task_list", "user_task_list.name", "user_task_list.owner", "user_task_list.workspace", "vacation_dates", "vacation_dates.end_on", "vacation_dates.start_on", "workspace", "workspace.name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### workspace_membership_gid: `str`<a id="workspace_membership_gid-str"></a>

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`WorkspaceMembershipsGetRecordByIdResponse`](./asana_python_sdk/pydantic/workspace_memberships_get_record_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workspace_memberships/{workspace_membership_gid}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.workspace_memberships.get_user_memberships`<a id="asanaworkspace_membershipsget_user_memberships"></a>

Returns the compact workspace membership records for the user.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_memberships_response = asana.workspace_memberships.get_user_memberships(
    user_gid="me",
    opt_pretty=True,
    limit=50,
    offset="eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9",
    opt_fields=["created_at", "is_active", "is_admin", "is_guest", "offset", "path", "uri", "user", "user.name", "user_task_list", "user_task_list.name", "user_task_list.owner", "user_task_list.workspace", "vacation_dates", "vacation_dates.end_on", "vacation_dates.start_on", "workspace", "workspace.name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_gid: `str`<a id="user_gid-str"></a>

A string identifying a user. This can either be the string \"me\", an email, or the gid of a user.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### limit: `int`<a id="limit-int"></a>

Results per page. The number of objects to return per page. The value must be between 1 and 100.

##### offset: `str`<a id="offset-str"></a>

Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`WorkspaceMembershipsGetUserMembershipsResponse`](./asana_python_sdk/pydantic/workspace_memberships_get_user_memberships_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{user_gid}/workspace_memberships` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.workspace_memberships.list_for_workspace`<a id="asanaworkspace_membershipslist_for_workspace"></a>

Returns the compact workspace membership records for the workspace.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_for_workspace_response = asana.workspace_memberships.list_for_workspace(
    workspace_gid="12345",
    user="me",
    opt_pretty=True,
    limit=50,
    offset="eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9",
    opt_fields=["created_at", "is_active", "is_admin", "is_guest", "offset", "path", "uri", "user", "user.name", "user_task_list", "user_task_list.name", "user_task_list.owner", "user_task_list.workspace", "vacation_dates", "vacation_dates.end_on", "vacation_dates.start_on", "workspace", "workspace.name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### workspace_gid: `str`<a id="workspace_gid-str"></a>

Globally unique identifier for the workspace or organization.

##### user: `str`<a id="user-str"></a>

A string identifying a user. This can either be the string \"me\", an email, or the gid of a user.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### limit: `int`<a id="limit-int"></a>

Results per page. The number of objects to return per page. The value must be between 1 and 100.

##### offset: `str`<a id="offset-str"></a>

Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`WorkspaceMembershipsListForWorkspaceResponse`](./asana_python_sdk/pydantic/workspace_memberships_list_for_workspace_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workspaces/{workspace_gid}/workspace_memberships` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.workspaces.add_user_to_workspace`<a id="asanaworkspacesadd_user_to_workspace"></a>

Add a user to a workspace or organization.
The user can be referenced by their globally unique user ID or their email address. Returns the full user record for the invited user.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_user_to_workspace_response = asana.workspaces.add_user_to_workspace(
    workspace_gid="12345",
    data={
        "user": "12345",
    },
    opt_pretty=True,
    opt_fields=["email", "name", "photo", "photo.image_1024x1024", "photo.image_128x128", "photo.image_21x21", "photo.image_27x27", "photo.image_36x36", "photo.image_60x60"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### workspace_gid: `str`<a id="workspace_gid-str"></a>

Globally unique identifier for the workspace or organization.

##### data: [`WorkspaceAddUserRequest`](./asana_python_sdk/type/workspace_add_user_request.py)<a id="data-workspaceadduserrequestasana_python_sdktypeworkspace_add_user_requestpy"></a>


##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WorkspacesAddUserToWorkspaceRequest`](./asana_python_sdk/type/workspaces_add_user_to_workspace_request.py)
The user to add to the workspace.

#### 🔄 Return<a id="🔄-return"></a>

[`WorkspacesAddUserToWorkspaceResponse`](./asana_python_sdk/pydantic/workspaces_add_user_to_workspace_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workspaces/{workspace_gid}/addUser` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.workspaces.get_workspace_record`<a id="asanaworkspacesget_workspace_record"></a>

Returns the full workspace record for a single workspace.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_workspace_record_response = asana.workspaces.get_workspace_record(
    workspace_gid="12345",
    opt_pretty=True,
    opt_fields=["email_domains", "is_organization", "name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### workspace_gid: `str`<a id="workspace_gid-str"></a>

Globally unique identifier for the workspace or organization.

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`WorkspacesGetWorkspaceRecordResponse`](./asana_python_sdk/pydantic/workspaces_get_workspace_record_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workspaces/{workspace_gid}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.workspaces.list_multiple`<a id="asanaworkspaceslist_multiple"></a>

Returns the compact records for all workspaces visible to the authorized user.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_multiple_response = asana.workspaces.list_multiple(
    opt_pretty=True,
    limit=50,
    offset="eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9",
    opt_fields=["email_domains", "is_organization", "name", "offset", "path", "uri"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### limit: `int`<a id="limit-int"></a>

Results per page. The number of objects to return per page. The value must be between 1 and 100.

##### offset: `str`<a id="offset-str"></a>

Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### 🔄 Return<a id="🔄-return"></a>

[`WorkspacesListMultipleResponse`](./asana_python_sdk/pydantic/workspaces_list_multiple_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workspaces` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.workspaces.remove_user_from_workspace`<a id="asanaworkspacesremove_user_from_workspace"></a>

Remove a user from a workspace or organization.
The user making this call must be an admin in the workspace. The user can be referenced by their globally unique user ID or their email address.
Returns an empty data record.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_user_from_workspace_response = asana.workspaces.remove_user_from_workspace(
    workspace_gid="12345",
    data={
        "user": "12345",
    },
    opt_pretty=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### workspace_gid: `str`<a id="workspace_gid-str"></a>

Globally unique identifier for the workspace or organization.

##### data: [`WorkspaceRemoveUserRequest`](./asana_python_sdk/type/workspace_remove_user_request.py)<a id="data-workspaceremoveuserrequestasana_python_sdktypeworkspace_remove_user_requestpy"></a>


##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WorkspacesRemoveUserFromWorkspaceRequest`](./asana_python_sdk/type/workspaces_remove_user_from_workspace_request.py)
The user to remove from the workspace.

#### 🔄 Return<a id="🔄-return"></a>

[`WorkspacesRemoveUserFromWorkspaceResponse`](./asana_python_sdk/pydantic/workspaces_remove_user_from_workspace_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workspaces/{workspace_gid}/removeUser` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `asana.workspaces.update_workspace_record`<a id="asanaworkspacesupdate_workspace_record"></a>

A specific, existing workspace can be updated by making a PUT request on the URL for that workspace. Only the fields provided in the data block will be updated; any unspecified fields will remain unchanged.
Currently the only field that can be modified for a workspace is its name.
Returns the complete, updated workspace record.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_workspace_record_response = asana.workspaces.update_workspace_record(
    workspace_gid="12345",
    items=None,
    opt_pretty=True,
    opt_fields=["email_domains", "is_organization", "name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### workspace_gid: `str`<a id="workspace_gid-str"></a>

Globally unique identifier for the workspace or organization.

##### items: [`WorkspaceCompact`](./asana_python_sdk/type/workspace_compact.py)<a id="items-workspacecompactasana_python_sdktypeworkspace_compactpy"></a>


##### opt_pretty: `bool`<a id="opt_pretty-bool"></a>

Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.

##### opt_fields: List[`str`]<a id="opt_fields-liststr"></a>

This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WorkspacesUpdateWorkspaceRecordRequest`](./asana_python_sdk/type/workspaces_update_workspace_record_request.py)
The workspace object with all updated properties.

#### 🔄 Return<a id="🔄-return"></a>

[`WorkspacesUpdateWorkspaceRecordResponse`](./asana_python_sdk/pydantic/workspaces_update_workspace_record_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workspaces/{workspace_gid}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
