operation_parameter_map = {
    '/attachments/{attachment_gid}-DELETE': {
        'parameters': [
            {
                'name': 'attachment_gid'
            },
            {
                'name': 'opt_pretty'
            },
        ]
    },
    '/attachments-GET': {
        'parameters': [
            {
                'name': 'parent'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/attachments/{attachment_gid}-GET': {
        'parameters': [
            {
                'name': 'attachment_gid'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/attachments-POST': {
        'parameters': [
            {
                'name': 'parent'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
            {
                'name': 'resource_subtype'
            },
            {
                'name': 'file'
            },
            {
                'name': 'url'
            },
            {
                'name': 'name'
            },
            {
                'name': 'connect_to_app'
            },
        ]
    },
    '/workspaces/{workspace_gid}/audit_log_events-GET': {
        'parameters': [
            {
                'name': 'workspace_gid'
            },
            {
                'name': 'start_at'
            },
            {
                'name': 'end_at'
            },
            {
                'name': 'event_type'
            },
            {
                'name': 'actor_type'
            },
            {
                'name': 'actor_gid'
            },
            {
                'name': 'resource_gid'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
        ]
    },
    '/batch-POST': {
        'parameters': [
            {
                'name': 'data'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/portfolios/{portfolio_gid}/custom_field_settings-GET': {
        'parameters': [
            {
                'name': 'portfolio_gid'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/projects/{project_gid}/custom_field_settings-GET': {
        'parameters': [
            {
                'name': 'project_gid'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/custom_fields/{custom_field_gid}/enum_options-POST': {
        'parameters': [
            {
                'name': 'custom_field_gid'
            },
            {
                'name': 'data'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/custom_fields-POST': {
        'parameters': [
            {
                'name': 'data'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/custom_fields/{custom_field_gid}-DELETE': {
        'parameters': [
            {
                'name': 'custom_field_gid'
            },
            {
                'name': 'opt_pretty'
            },
        ]
    },
    '/custom_fields/{custom_field_gid}-GET': {
        'parameters': [
            {
                'name': 'custom_field_gid'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/workspaces/{workspace_gid}/custom_fields-GET': {
        'parameters': [
            {
                'name': 'workspace_gid'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/custom_fields/{custom_field_gid}/enum_options/insert-POST': {
        'parameters': [
            {
                'name': 'custom_field_gid'
            },
            {
                'name': 'data'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/enum_options/{enum_option_gid}-PUT': {
        'parameters': [
            {
                'name': 'enum_option_gid'
            },
            {
                'name': 'data'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/custom_fields/{custom_field_gid}-PUT': {
        'parameters': [
            {
                'name': 'custom_field_gid'
            },
            {
                'name': 'data'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/events-GET': {
        'parameters': [
            {
                'name': 'resource'
            },
            {
                'name': 'sync'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/goals/{goal_gid}/addSupportingRelationship-POST': {
        'parameters': [
            {
                'name': 'goal_gid'
            },
            {
                'name': 'data'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/goal_relationships-GET': {
        'parameters': [
            {
                'name': 'supported_goal'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'resource_subtype'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/goal_relationships/{goal_relationship_gid}-GET': {
        'parameters': [
            {
                'name': 'goal_relationship_gid'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/goals/{goal_gid}/removeSupportingRelationship-POST': {
        'parameters': [
            {
                'name': 'goal_gid'
            },
            {
                'name': 'data'
            },
            {
                'name': 'opt_pretty'
            },
        ]
    },
    '/goal_relationships/{goal_relationship_gid}-PUT': {
        'parameters': [
            {
                'name': 'goal_relationship_gid'
            },
            {
                'name': 'data'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/goals/{goal_gid}/addFollowers-POST': {
        'parameters': [
            {
                'name': 'goal_gid'
            },
            {
                'name': 'data'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/goals/{goal_gid}/setMetric-POST': {
        'parameters': [
            {
                'name': 'goal_gid'
            },
            {
                'name': 'data'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/goals-POST': {
        'parameters': [
            {
                'name': 'data'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/goals/{goal_gid}-DELETE': {
        'parameters': [
            {
                'name': 'goal_gid'
            },
            {
                'name': 'opt_pretty'
            },
        ]
    },
    '/goals-GET': {
        'parameters': [
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'portfolio'
            },
            {
                'name': 'project'
            },
            {
                'name': 'task'
            },
            {
                'name': 'is_workspace_level'
            },
            {
                'name': 'team'
            },
            {
                'name': 'workspace'
            },
            {
                'name': 'time_periods'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/goals/{goal_gid}-GET': {
        'parameters': [
            {
                'name': 'goal_gid'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/goals/{goal_gid}/parentGoals-GET': {
        'parameters': [
            {
                'name': 'goal_gid'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/goals/{goal_gid}/removeFollowers-POST': {
        'parameters': [
            {
                'name': 'goal_gid'
            },
            {
                'name': 'data'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/goals/{goal_gid}-PUT': {
        'parameters': [
            {
                'name': 'goal_gid'
            },
            {
                'name': 'data'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/goals/{goal_gid}/setMetricCurrentValue-POST': {
        'parameters': [
            {
                'name': 'goal_gid'
            },
            {
                'name': 'data'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/jobs/{job_gid}-GET': {
        'parameters': [
            {
                'name': 'job_gid'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/memberships-POST': {
        'parameters': [
            {
                'name': 'data'
            },
            {
                'name': 'opt_pretty'
            },
        ]
    },
    '/memberships/{membership_gid}-DELETE': {
        'parameters': [
            {
                'name': 'membership_gid'
            },
            {
                'name': 'opt_pretty'
            },
        ]
    },
    '/memberships/{membership_gid}-GET': {
        'parameters': [
            {
                'name': 'membership_gid'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/memberships-GET': {
        'parameters': [
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'parent'
            },
            {
                'name': 'member'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/organization_exports-POST': {
        'parameters': [
            {
                'name': 'data'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/organization_exports/{organization_export_gid}-GET': {
        'parameters': [
            {
                'name': 'organization_export_gid'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/portfolios/{portfolio_gid}/portfolio_memberships-GET': {
        'parameters': [
            {
                'name': 'portfolio_gid'
            },
            {
                'name': 'user'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/portfolio_memberships/{portfolio_membership_gid}-GET': {
        'parameters': [
            {
                'name': 'portfolio_membership_gid'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/portfolio_memberships-GET': {
        'parameters': [
            {
                'name': 'portfolio'
            },
            {
                'name': 'workspace'
            },
            {
                'name': 'user'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/portfolios/{portfolio_gid}/addCustomFieldSetting-POST': {
        'parameters': [
            {
                'name': 'portfolio_gid'
            },
            {
                'name': 'data'
            },
            {
                'name': 'opt_pretty'
            },
        ]
    },
    '/portfolios/{portfolio_gid}/addMembers-POST': {
        'parameters': [
            {
                'name': 'portfolio_gid'
            },
            {
                'name': 'data'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/portfolios/{portfolio_gid}/addItem-POST': {
        'parameters': [
            {
                'name': 'portfolio_gid'
            },
            {
                'name': 'data'
            },
            {
                'name': 'opt_pretty'
            },
        ]
    },
    '/portfolios-POST': {
        'parameters': [
            {
                'name': 'data'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/portfolios/{portfolio_gid}-DELETE': {
        'parameters': [
            {
                'name': 'portfolio_gid'
            },
            {
                'name': 'opt_pretty'
            },
        ]
    },
    '/portfolios/{portfolio_gid}/items-GET': {
        'parameters': [
            {
                'name': 'portfolio_gid'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/portfolios/{portfolio_gid}-GET': {
        'parameters': [
            {
                'name': 'portfolio_gid'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/portfolios-GET': {
        'parameters': [
            {
                'name': 'workspace'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'owner'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/portfolios/{portfolio_gid}/removeCustomFieldSetting-POST': {
        'parameters': [
            {
                'name': 'portfolio_gid'
            },
            {
                'name': 'data'
            },
            {
                'name': 'opt_pretty'
            },
        ]
    },
    '/portfolios/{portfolio_gid}/removeItem-POST': {
        'parameters': [
            {
                'name': 'portfolio_gid'
            },
            {
                'name': 'data'
            },
            {
                'name': 'opt_pretty'
            },
        ]
    },
    '/portfolios/{portfolio_gid}/removeMembers-POST': {
        'parameters': [
            {
                'name': 'portfolio_gid'
            },
            {
                'name': 'data'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/portfolios/{portfolio_gid}-PUT': {
        'parameters': [
            {
                'name': 'portfolio_gid'
            },
            {
                'name': 'data'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/projects/{project_gid}/project_briefs-POST': {
        'parameters': [
            {
                'name': 'project_gid'
            },
            {
                'name': 'data'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/project_briefs/{project_brief_gid}-GET': {
        'parameters': [
            {
                'name': 'project_brief_gid'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/project_briefs/{project_brief_gid}-DELETE': {
        'parameters': [
            {
                'name': 'project_brief_gid'
            },
            {
                'name': 'opt_pretty'
            },
        ]
    },
    '/project_briefs/{project_brief_gid}-PUT': {
        'parameters': [
            {
                'name': 'project_brief_gid'
            },
            {
                'name': 'data'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/projects/{project_gid}/project_memberships-GET': {
        'parameters': [
            {
                'name': 'project_gid'
            },
            {
                'name': 'user'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/project_memberships/{project_membership_gid}-GET': {
        'parameters': [
            {
                'name': 'project_membership_gid'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/projects/{project_gid}/project_statuses-POST': {
        'parameters': [
            {
                'name': 'project_gid'
            },
            {
                'name': 'data'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/project_statuses/{project_status_gid}-DELETE': {
        'parameters': [
            {
                'name': 'project_status_gid'
            },
            {
                'name': 'opt_pretty'
            },
        ]
    },
    '/projects/{project_gid}/project_statuses-GET': {
        'parameters': [
            {
                'name': 'project_gid'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/project_statuses/{project_status_gid}-GET': {
        'parameters': [
            {
                'name': 'project_status_gid'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/project_templates/{project_template_gid}-DELETE': {
        'parameters': [
            {
                'name': 'project_template_gid'
            },
            {
                'name': 'opt_pretty'
            },
        ]
    },
    '/teams/{team_gid}/project_templates-GET': {
        'parameters': [
            {
                'name': 'team_gid'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/project_templates/{project_template_gid}-GET': {
        'parameters': [
            {
                'name': 'project_template_gid'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/project_templates/{project_template_gid}/instantiateProject-POST': {
        'parameters': [
            {
                'name': 'project_template_gid'
            },
            {
                'name': 'data'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/project_templates-GET': {
        'parameters': [
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'workspace'
            },
            {
                'name': 'team'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/projects/{project_gid}/addCustomFieldSetting-POST': {
        'parameters': [
            {
                'name': 'project_gid'
            },
            {
                'name': 'data'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/projects/{project_gid}/addFollowers-POST': {
        'parameters': [
            {
                'name': 'project_gid'
            },
            {
                'name': 'data'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/projects/{project_gid}/addMembers-POST': {
        'parameters': [
            {
                'name': 'project_gid'
            },
            {
                'name': 'data'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/workspaces/{workspace_gid}/projects-POST': {
        'parameters': [
            {
                'name': 'workspace_gid'
            },
            {
                'name': 'data'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/projects-POST': {
        'parameters': [
            {
                'name': 'data'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/teams/{team_gid}/projects-POST': {
        'parameters': [
            {
                'name': 'team_gid'
            },
            {
                'name': 'data'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/projects/{project_gid}/saveAsTemplate-POST': {
        'parameters': [
            {
                'name': 'project_gid'
            },
            {
                'name': 'data'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/projects/{project_gid}-DELETE': {
        'parameters': [
            {
                'name': 'project_gid'
            },
            {
                'name': 'opt_pretty'
            },
        ]
    },
    '/projects/{project_gid}/duplicate-POST': {
        'parameters': [
            {
                'name': 'project_gid'
            },
            {
                'name': 'data'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/workspaces/{workspace_gid}/projects-GET': {
        'parameters': [
            {
                'name': 'workspace_gid'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'archived'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/projects/{project_gid}-GET': {
        'parameters': [
            {
                'name': 'project_gid'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/projects/{project_gid}/task_counts-GET': {
        'parameters': [
            {
                'name': 'project_gid'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/teams/{team_gid}/projects-GET': {
        'parameters': [
            {
                'name': 'team_gid'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'archived'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/projects-GET': {
        'parameters': [
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'workspace'
            },
            {
                'name': 'team'
            },
            {
                'name': 'archived'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/projects/{project_gid}/removeCustomFieldSetting-POST': {
        'parameters': [
            {
                'name': 'project_gid'
            },
            {
                'name': 'data'
            },
            {
                'name': 'opt_pretty'
            },
        ]
    },
    '/projects/{project_gid}/removeMembers-POST': {
        'parameters': [
            {
                'name': 'project_gid'
            },
            {
                'name': 'data'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/projects/{project_gid}/removeFollowers-POST': {
        'parameters': [
            {
                'name': 'project_gid'
            },
            {
                'name': 'data'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/tasks/{task_gid}/projects-GET': {
        'parameters': [
            {
                'name': 'task_gid'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/projects/{project_gid}-PUT': {
        'parameters': [
            {
                'name': 'project_gid'
            },
            {
                'name': 'data'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/rule_triggers/{rule_trigger_gid}/run-POST': {
        'parameters': [
            {
                'name': 'rule_trigger_gid'
            },
            {
                'name': 'data'
            },
        ]
    },
    '/sections/{section_gid}/addTask-POST': {
        'parameters': [
            {
                'name': 'section_gid'
            },
            {
                'name': 'data'
            },
            {
                'name': 'opt_pretty'
            },
        ]
    },
    '/projects/{project_gid}/sections-POST': {
        'parameters': [
            {
                'name': 'project_gid'
            },
            {
                'name': 'data'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/sections/{section_gid}-DELETE': {
        'parameters': [
            {
                'name': 'section_gid'
            },
            {
                'name': 'opt_pretty'
            },
        ]
    },
    '/sections/{section_gid}-GET': {
        'parameters': [
            {
                'name': 'section_gid'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/projects/{project_gid}/sections-GET': {
        'parameters': [
            {
                'name': 'project_gid'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/projects/{project_gid}/sections/insert-POST': {
        'parameters': [
            {
                'name': 'project_gid'
            },
            {
                'name': 'data'
            },
            {
                'name': 'opt_pretty'
            },
        ]
    },
    '/sections/{section_gid}-PUT': {
        'parameters': [
            {
                'name': 'section_gid'
            },
            {
                'name': 'data'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/status_updates-POST': {
        'parameters': [
            {
                'name': 'data'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/status_updates/{status_update_gid}-DELETE': {
        'parameters': [
            {
                'name': 'status_update_gid'
            },
            {
                'name': 'opt_pretty'
            },
        ]
    },
    '/status_updates-GET': {
        'parameters': [
            {
                'name': 'parent'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'created_since'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/status_updates/{status_update_gid}-GET': {
        'parameters': [
            {
                'name': 'status_update_gid'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/tasks/{task_gid}/stories-POST': {
        'parameters': [
            {
                'name': 'task_gid'
            },
            {
                'name': 'data'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/stories/{story_gid}-DELETE': {
        'parameters': [
            {
                'name': 'story_gid'
            },
            {
                'name': 'opt_pretty'
            },
        ]
    },
    '/stories/{story_gid}-GET': {
        'parameters': [
            {
                'name': 'story_gid'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/tasks/{task_gid}/stories-GET': {
        'parameters': [
            {
                'name': 'task_gid'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/stories/{story_gid}-PUT': {
        'parameters': [
            {
                'name': 'story_gid'
            },
            {
                'name': 'data'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/tags-POST': {
        'parameters': [
            {
                'name': 'data'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/workspaces/{workspace_gid}/tags-POST': {
        'parameters': [
            {
                'name': 'workspace_gid'
            },
            {
                'name': 'data'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/workspaces/{workspace_gid}/tags-GET': {
        'parameters': [
            {
                'name': 'workspace_gid'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/tags/{tag_gid}-GET': {
        'parameters': [
            {
                'name': 'tag_gid'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/tasks/{task_gid}/tags-GET': {
        'parameters': [
            {
                'name': 'task_gid'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/tags-GET': {
        'parameters': [
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'workspace'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/tags/{tag_gid}-DELETE': {
        'parameters': [
            {
                'name': 'tag_gid'
            },
            {
                'name': 'opt_pretty'
            },
        ]
    },
    '/tags/{tag_gid}-PUT': {
        'parameters': [
            {
                'name': 'tag_gid'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/task_templates/{task_template_gid}-DELETE': {
        'parameters': [
            {
                'name': 'task_template_gid'
            },
            {
                'name': 'opt_pretty'
            },
        ]
    },
    '/task_templates/{task_template_gid}-GET': {
        'parameters': [
            {
                'name': 'task_template_gid'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/task_templates/{task_template_gid}/instantiateTask-POST': {
        'parameters': [
            {
                'name': 'task_template_gid'
            },
            {
                'name': 'data'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/task_templates-GET': {
        'parameters': [
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'project'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/tasks/{task_gid}/addFollowers-POST': {
        'parameters': [
            {
                'name': 'task_gid'
            },
            {
                'name': 'data'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/tasks/{task_gid}/addProject-POST': {
        'parameters': [
            {
                'name': 'task_gid'
            },
            {
                'name': 'data'
            },
            {
                'name': 'opt_pretty'
            },
        ]
    },
    '/tasks/{task_gid}/addTag-POST': {
        'parameters': [
            {
                'name': 'task_gid'
            },
            {
                'name': 'data'
            },
            {
                'name': 'opt_pretty'
            },
        ]
    },
    '/tasks-POST': {
        'parameters': [
            {
                'name': 'data'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/tasks/{task_gid}/subtasks-POST': {
        'parameters': [
            {
                'name': 'task_gid'
            },
            {
                'name': 'data'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/tasks/{task_gid}-DELETE': {
        'parameters': [
            {
                'name': 'task_gid'
            },
            {
                'name': 'opt_pretty'
            },
        ]
    },
    '/tasks/{task_gid}/duplicate-POST': {
        'parameters': [
            {
                'name': 'task_gid'
            },
            {
                'name': 'data'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/tasks/{task_gid}/dependencies-GET': {
        'parameters': [
            {
                'name': 'task_gid'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/workspaces/{workspace_gid}/tasks/custom_id/{custom_id}-GET': {
        'parameters': [
            {
                'name': 'workspace_gid'
            },
            {
                'name': 'custom_id'
            },
        ]
    },
    '/tasks/{task_gid}/dependents-GET': {
        'parameters': [
            {
                'name': 'task_gid'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/tasks-GET': {
        'parameters': [
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'assignee'
            },
            {
                'name': 'project'
            },
            {
                'name': 'section'
            },
            {
                'name': 'workspace'
            },
            {
                'name': 'completed_since'
            },
            {
                'name': 'modified_since'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/tags/{tag_gid}/tasks-GET': {
        'parameters': [
            {
                'name': 'tag_gid'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/sections/{section_gid}/tasks-GET': {
        'parameters': [
            {
                'name': 'section_gid'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'completed_since'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/tasks/{task_gid}/subtasks-GET': {
        'parameters': [
            {
                'name': 'task_gid'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/tasks/{task_gid}-GET': {
        'parameters': [
            {
                'name': 'task_gid'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/projects/{project_gid}/tasks-GET': {
        'parameters': [
            {
                'name': 'project_gid'
            },
            {
                'name': 'completed_since'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/user_task_lists/{user_task_list_gid}/tasks-GET': {
        'parameters': [
            {
                'name': 'user_task_list_gid'
            },
            {
                'name': 'completed_since'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/tasks/{task_gid}/removeFollowers-POST': {
        'parameters': [
            {
                'name': 'task_gid'
            },
            {
                'name': 'data'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/tasks/{task_gid}/removeProject-POST': {
        'parameters': [
            {
                'name': 'task_gid'
            },
            {
                'name': 'data'
            },
            {
                'name': 'opt_pretty'
            },
        ]
    },
    '/tasks/{task_gid}/removeTag-POST': {
        'parameters': [
            {
                'name': 'task_gid'
            },
            {
                'name': 'data'
            },
            {
                'name': 'opt_pretty'
            },
        ]
    },
    '/workspaces/{workspace_gid}/tasks/search-GET': {
        'parameters': [
            {
                'name': 'workspace_gid'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'text'
            },
            {
                'name': 'resource_subtype'
            },
            {
                'name': 'assignee.any'
            },
            {
                'name': 'assignee.not'
            },
            {
                'name': 'portfolios.any'
            },
            {
                'name': 'projects.any'
            },
            {
                'name': 'projects.not'
            },
            {
                'name': 'projects.all'
            },
            {
                'name': 'sections.any'
            },
            {
                'name': 'sections.not'
            },
            {
                'name': 'sections.all'
            },
            {
                'name': 'tags.any'
            },
            {
                'name': 'tags.not'
            },
            {
                'name': 'tags.all'
            },
            {
                'name': 'teams.any'
            },
            {
                'name': 'followers.not'
            },
            {
                'name': 'created_by.any'
            },
            {
                'name': 'created_by.not'
            },
            {
                'name': 'assigned_by.any'
            },
            {
                'name': 'assigned_by.not'
            },
            {
                'name': 'liked_by.not'
            },
            {
                'name': 'commented_on_by.not'
            },
            {
                'name': 'due_on.before'
            },
            {
                'name': 'due_on.after'
            },
            {
                'name': 'due_on'
            },
            {
                'name': 'due_at.before'
            },
            {
                'name': 'due_at.after'
            },
            {
                'name': 'start_on.before'
            },
            {
                'name': 'start_on.after'
            },
            {
                'name': 'start_on'
            },
            {
                'name': 'created_on.before'
            },
            {
                'name': 'created_on.after'
            },
            {
                'name': 'created_on'
            },
            {
                'name': 'created_at.before'
            },
            {
                'name': 'created_at.after'
            },
            {
                'name': 'completed_on.before'
            },
            {
                'name': 'completed_on.after'
            },
            {
                'name': 'completed_on'
            },
            {
                'name': 'completed_at.before'
            },
            {
                'name': 'completed_at.after'
            },
            {
                'name': 'modified_on.before'
            },
            {
                'name': 'modified_on.after'
            },
            {
                'name': 'modified_on'
            },
            {
                'name': 'modified_at.before'
            },
            {
                'name': 'modified_at.after'
            },
            {
                'name': 'is_blocking'
            },
            {
                'name': 'is_blocked'
            },
            {
                'name': 'has_attachment'
            },
            {
                'name': 'completed'
            },
            {
                'name': 'is_subtask'
            },
            {
                'name': 'sort_by'
            },
            {
                'name': 'sort_ascending'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/tasks/{task_gid}/addDependencies-POST': {
        'parameters': [
            {
                'name': 'task_gid'
            },
            {
                'name': 'data'
            },
            {
                'name': 'opt_pretty'
            },
        ]
    },
    '/tasks/{task_gid}/setParent-POST': {
        'parameters': [
            {
                'name': 'task_gid'
            },
            {
                'name': 'data'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/tasks/{task_gid}/addDependents-POST': {
        'parameters': [
            {
                'name': 'task_gid'
            },
            {
                'name': 'data'
            },
            {
                'name': 'opt_pretty'
            },
        ]
    },
    '/tasks/{task_gid}/removeDependencies-POST': {
        'parameters': [
            {
                'name': 'task_gid'
            },
            {
                'name': 'data'
            },
            {
                'name': 'opt_pretty'
            },
        ]
    },
    '/tasks/{task_gid}/removeDependents-POST': {
        'parameters': [
            {
                'name': 'task_gid'
            },
            {
                'name': 'data'
            },
            {
                'name': 'opt_pretty'
            },
        ]
    },
    '/tasks/{task_gid}-PUT': {
        'parameters': [
            {
                'name': 'task_gid'
            },
            {
                'name': 'data'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/teams/{team_gid}/team_memberships-GET': {
        'parameters': [
            {
                'name': 'team_gid'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/team_memberships-GET': {
        'parameters': [
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'team'
            },
            {
                'name': 'user'
            },
            {
                'name': 'workspace'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/team_memberships/{team_membership_gid}-GET': {
        'parameters': [
            {
                'name': 'team_membership_gid'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/users/{user_gid}/team_memberships-GET': {
        'parameters': [
            {
                'name': 'user_gid'
            },
            {
                'name': 'workspace'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/teams/{team_gid}/addUser-POST': {
        'parameters': [
            {
                'name': 'team_gid'
            },
            {
                'name': 'data'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/teams-POST': {
        'parameters': [
            {
                'name': 'data'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/teams/{team_gid}-GET': {
        'parameters': [
            {
                'name': 'team_gid'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/users/{user_gid}/teams-GET': {
        'parameters': [
            {
                'name': 'user_gid'
            },
            {
                'name': 'organization'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/workspaces/{workspace_gid}/teams-GET': {
        'parameters': [
            {
                'name': 'workspace_gid'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/teams/{team_gid}/removeUser-POST': {
        'parameters': [
            {
                'name': 'team_gid'
            },
            {
                'name': 'data'
            },
            {
                'name': 'opt_pretty'
            },
        ]
    },
    '/teams/{team_gid}-PUT': {
        'parameters': [
            {
                'name': 'team_gid'
            },
            {
                'name': 'data'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/time_periods-GET': {
        'parameters': [
            {
                'name': 'workspace'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'start_on'
            },
            {
                'name': 'end_on'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/time_periods/{time_period_gid}-GET': {
        'parameters': [
            {
                'name': 'time_period_gid'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/tasks/{task_gid}/time_tracking_entries-POST': {
        'parameters': [
            {
                'name': 'task_gid'
            },
            {
                'name': 'data'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/time_tracking_entries/{time_tracking_entry_gid}-DELETE': {
        'parameters': [
            {
                'name': 'time_tracking_entry_gid'
            },
            {
                'name': 'opt_pretty'
            },
        ]
    },
    '/tasks/{task_gid}/time_tracking_entries-GET': {
        'parameters': [
            {
                'name': 'task_gid'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/time_tracking_entries/{time_tracking_entry_gid}-GET': {
        'parameters': [
            {
                'name': 'time_tracking_entry_gid'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/time_tracking_entries/{time_tracking_entry_gid}-PUT': {
        'parameters': [
            {
                'name': 'time_tracking_entry_gid'
            },
            {
                'name': 'data'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/workspaces/{workspace_gid}/typeahead-GET': {
        'parameters': [
            {
                'name': 'workspace_gid'
            },
            {
                'name': 'resource_type'
            },
            {
                'name': 'type'
            },
            {
                'name': 'query'
            },
            {
                'name': 'count'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/user_task_lists/{user_task_list_gid}-GET': {
        'parameters': [
            {
                'name': 'user_task_list_gid'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/users/{user_gid}/user_task_list-GET': {
        'parameters': [
            {
                'name': 'user_gid'
            },
            {
                'name': 'workspace'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/users/{user_gid}/favorites-GET': {
        'parameters': [
            {
                'name': 'user_gid'
            },
            {
                'name': 'resource_type'
            },
            {
                'name': 'workspace'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/users/{user_gid}-GET': {
        'parameters': [
            {
                'name': 'user_gid'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/users-GET': {
        'parameters': [
            {
                'name': 'workspace'
            },
            {
                'name': 'team'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/teams/{team_gid}/users-GET': {
        'parameters': [
            {
                'name': 'team_gid'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/workspaces/{workspace_gid}/users-GET': {
        'parameters': [
            {
                'name': 'workspace_gid'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/webhooks-POST': {
        'parameters': [
            {
                'name': 'data'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/webhooks/{webhook_gid}-GET': {
        'parameters': [
            {
                'name': 'webhook_gid'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/webhooks-GET': {
        'parameters': [
            {
                'name': 'workspace'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'resource'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/webhooks/{webhook_gid}-DELETE': {
        'parameters': [
            {
                'name': 'webhook_gid'
            },
            {
                'name': 'opt_pretty'
            },
        ]
    },
    '/webhooks/{webhook_gid}-PUT': {
        'parameters': [
            {
                'name': 'webhook_gid'
            },
            {
                'name': 'data'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/workspace_memberships/{workspace_membership_gid}-GET': {
        'parameters': [
            {
                'name': 'workspace_membership_gid'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/users/{user_gid}/workspace_memberships-GET': {
        'parameters': [
            {
                'name': 'user_gid'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/workspaces/{workspace_gid}/workspace_memberships-GET': {
        'parameters': [
            {
                'name': 'workspace_gid'
            },
            {
                'name': 'user'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/workspaces/{workspace_gid}/addUser-POST': {
        'parameters': [
            {
                'name': 'workspace_gid'
            },
            {
                'name': 'data'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/workspaces/{workspace_gid}-GET': {
        'parameters': [
            {
                'name': 'workspace_gid'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/workspaces-GET': {
        'parameters': [
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
    '/workspaces/{workspace_gid}/removeUser-POST': {
        'parameters': [
            {
                'name': 'workspace_gid'
            },
            {
                'name': 'data'
            },
            {
                'name': 'opt_pretty'
            },
        ]
    },
    '/workspaces/{workspace_gid}-PUT': {
        'parameters': [
            {
                'name': 'workspace_gid'
            },
            {
                'name': 'items'
            },
            {
                'name': 'opt_pretty'
            },
            {
                'name': 'opt_fields'
            },
        ]
    },
};