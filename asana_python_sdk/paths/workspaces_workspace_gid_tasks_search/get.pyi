# coding: utf-8

"""
    Asana

    This is the interface for interacting with the [Asana Platform](https://developers.asana.com). Our API reference is generated from our [OpenAPI spec] (https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml).

    The version of the OpenAPI document: 1.0
    Created by: https://asana.com/support
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from asana_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from asana_python_sdk.api_response import AsyncGeneratorResponse
from asana_python_sdk import api_client, exceptions
from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from asana_python_sdk import schemas  # noqa: F401

from asana_python_sdk.model.tasks_search_in_workspace_response import TasksSearchInWorkspaceResponse as TasksSearchInWorkspaceResponseSchema
from asana_python_sdk.model.error_response import ErrorResponse as ErrorResponseSchema

from asana_python_sdk.type.tasks_search_in_workspace_response import TasksSearchInWorkspaceResponse
from asana_python_sdk.type.error_response import ErrorResponse

from ...api_client import Dictionary
from asana_python_sdk.pydantic.error_response import ErrorResponse as ErrorResponsePydantic
from asana_python_sdk.pydantic.tasks_search_in_workspace_response import TasksSearchInWorkspaceResponse as TasksSearchInWorkspaceResponsePydantic

# Query params
OptPrettySchema = schemas.BoolSchema
TextSchema = schemas.StrSchema


class ResourceSubtypeSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def DEFAULT_TASK(cls):
        return cls("default_task")
    
    @schemas.classproperty
    def MILESTONE(cls):
        return cls("milestone")
AssigneeAnySchema = schemas.StrSchema
AssigneeNotSchema = schemas.StrSchema
PortfoliosAnySchema = schemas.StrSchema
ProjectsAnySchema = schemas.StrSchema
ProjectsNotSchema = schemas.StrSchema
ProjectsAllSchema = schemas.StrSchema
SectionsAnySchema = schemas.StrSchema
SectionsNotSchema = schemas.StrSchema
SectionsAllSchema = schemas.StrSchema
TagsAnySchema = schemas.StrSchema
TagsNotSchema = schemas.StrSchema
TagsAllSchema = schemas.StrSchema
TeamsAnySchema = schemas.StrSchema
FollowersNotSchema = schemas.StrSchema
CreatedByAnySchema = schemas.StrSchema
CreatedByNotSchema = schemas.StrSchema
AssignedByAnySchema = schemas.StrSchema
AssignedByNotSchema = schemas.StrSchema
LikedByNotSchema = schemas.StrSchema
CommentedOnByNotSchema = schemas.StrSchema
DueOnBeforeSchema = schemas.DateSchema
DueOnAfterSchema = schemas.DateSchema


class DueOnSchema(
    schemas.DateBase,
    schemas.StrBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneStrMixin
):


    class MetaOapg:
        format = 'date'


    def __new__(
        cls,
        *args: typing.Union[None, str, date, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'DueOnSchema':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
        )
DueAtBeforeSchema = schemas.DateTimeSchema
DueAtAfterSchema = schemas.DateTimeSchema
StartOnBeforeSchema = schemas.DateSchema
StartOnAfterSchema = schemas.DateSchema


class StartOnSchema(
    schemas.DateBase,
    schemas.StrBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneStrMixin
):


    class MetaOapg:
        format = 'date'


    def __new__(
        cls,
        *args: typing.Union[None, str, date, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'StartOnSchema':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
        )
CreatedOnBeforeSchema = schemas.DateSchema
CreatedOnAfterSchema = schemas.DateSchema


class CreatedOnSchema(
    schemas.DateBase,
    schemas.StrBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneStrMixin
):


    class MetaOapg:
        format = 'date'


    def __new__(
        cls,
        *args: typing.Union[None, str, date, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'CreatedOnSchema':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
        )
CreatedAtBeforeSchema = schemas.DateTimeSchema
CreatedAtAfterSchema = schemas.DateTimeSchema
CompletedOnBeforeSchema = schemas.DateSchema
CompletedOnAfterSchema = schemas.DateSchema


class CompletedOnSchema(
    schemas.DateBase,
    schemas.StrBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneStrMixin
):


    class MetaOapg:
        format = 'date'


    def __new__(
        cls,
        *args: typing.Union[None, str, date, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'CompletedOnSchema':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
        )
CompletedAtBeforeSchema = schemas.DateTimeSchema
CompletedAtAfterSchema = schemas.DateTimeSchema
ModifiedOnBeforeSchema = schemas.DateSchema
ModifiedOnAfterSchema = schemas.DateSchema


class ModifiedOnSchema(
    schemas.DateBase,
    schemas.StrBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneStrMixin
):


    class MetaOapg:
        format = 'date'


    def __new__(
        cls,
        *args: typing.Union[None, str, date, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'ModifiedOnSchema':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
        )
ModifiedAtBeforeSchema = schemas.DateTimeSchema
ModifiedAtAfterSchema = schemas.DateTimeSchema
IsBlockingSchema = schemas.BoolSchema
IsBlockedSchema = schemas.BoolSchema
HasAttachmentSchema = schemas.BoolSchema
CompletedSchema = schemas.BoolSchema
IsSubtaskSchema = schemas.BoolSchema


class SortBySchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def DUE_DATE(cls):
        return cls("due_date")
    
    @schemas.classproperty
    def CREATED_AT(cls):
        return cls("created_at")
    
    @schemas.classproperty
    def COMPLETED_AT(cls):
        return cls("completed_at")
    
    @schemas.classproperty
    def LIKES(cls):
        return cls("likes")
    
    @schemas.classproperty
    def MODIFIED_AT(cls):
        return cls("modified_at")
SortAscendingSchema = schemas.BoolSchema


class OptFieldsSchema(
    schemas.ListSchema
):


    class MetaOapg:
        
        
        class items(
            schemas.EnumBase,
            schemas.StrSchema
        ):
            
            @schemas.classproperty
            def ACTUAL_TIME_MINUTES(cls):
                return cls("actual_time_minutes")
            
            @schemas.classproperty
            def APPROVAL_STATUS(cls):
                return cls("approval_status")
            
            @schemas.classproperty
            def ASSIGNEE(cls):
                return cls("assignee")
            
            @schemas.classproperty
            def ASSIGNEE_NAME(cls):
                return cls("assignee.name")
            
            @schemas.classproperty
            def ASSIGNEE_SECTION(cls):
                return cls("assignee_section")
            
            @schemas.classproperty
            def ASSIGNEE_SECTION_NAME(cls):
                return cls("assignee_section.name")
            
            @schemas.classproperty
            def ASSIGNEE_STATUS(cls):
                return cls("assignee_status")
            
            @schemas.classproperty
            def COMPLETED(cls):
                return cls("completed")
            
            @schemas.classproperty
            def COMPLETED_AT(cls):
                return cls("completed_at")
            
            @schemas.classproperty
            def COMPLETED_BY(cls):
                return cls("completed_by")
            
            @schemas.classproperty
            def COMPLETED_BY_NAME(cls):
                return cls("completed_by.name")
            
            @schemas.classproperty
            def CREATED_AT(cls):
                return cls("created_at")
            
            @schemas.classproperty
            def CREATED_BY(cls):
                return cls("created_by")
            
            @schemas.classproperty
            def CUSTOM_FIELDS(cls):
                return cls("custom_fields")
            
            @schemas.classproperty
            def CUSTOM_FIELDS_ASANA_CREATED_FIELD(cls):
                return cls("custom_fields.asana_created_field")
            
            @schemas.classproperty
            def CUSTOM_FIELDS_CREATED_BY(cls):
                return cls("custom_fields.created_by")
            
            @schemas.classproperty
            def CUSTOM_FIELDS_CREATED_BY_NAME(cls):
                return cls("custom_fields.created_by.name")
            
            @schemas.classproperty
            def CUSTOM_FIELDS_CURRENCY_CODE(cls):
                return cls("custom_fields.currency_code")
            
            @schemas.classproperty
            def CUSTOM_FIELDS_CUSTOM_LABEL(cls):
                return cls("custom_fields.custom_label")
            
            @schemas.classproperty
            def CUSTOM_FIELDS_CUSTOM_LABEL_POSITION(cls):
                return cls("custom_fields.custom_label_position")
            
            @schemas.classproperty
            def CUSTOM_FIELDS_DATE_VALUE(cls):
                return cls("custom_fields.date_value")
            
            @schemas.classproperty
            def CUSTOM_FIELDS_DATE_VALUE_DATE(cls):
                return cls("custom_fields.date_value.date")
            
            @schemas.classproperty
            def CUSTOM_FIELDS_DATE_VALUE_DATE_TIME(cls):
                return cls("custom_fields.date_value.date_time")
            
            @schemas.classproperty
            def CUSTOM_FIELDS_DESCRIPTION(cls):
                return cls("custom_fields.description")
            
            @schemas.classproperty
            def CUSTOM_FIELDS_DISPLAY_VALUE(cls):
                return cls("custom_fields.display_value")
            
            @schemas.classproperty
            def CUSTOM_FIELDS_ENABLED(cls):
                return cls("custom_fields.enabled")
            
            @schemas.classproperty
            def CUSTOM_FIELDS_ENUM_OPTIONS(cls):
                return cls("custom_fields.enum_options")
            
            @schemas.classproperty
            def CUSTOM_FIELDS_ENUM_OPTIONS_COLOR(cls):
                return cls("custom_fields.enum_options.color")
            
            @schemas.classproperty
            def CUSTOM_FIELDS_ENUM_OPTIONS_ENABLED(cls):
                return cls("custom_fields.enum_options.enabled")
            
            @schemas.classproperty
            def CUSTOM_FIELDS_ENUM_OPTIONS_NAME(cls):
                return cls("custom_fields.enum_options.name")
            
            @schemas.classproperty
            def CUSTOM_FIELDS_ENUM_VALUE(cls):
                return cls("custom_fields.enum_value")
            
            @schemas.classproperty
            def CUSTOM_FIELDS_ENUM_VALUE_COLOR(cls):
                return cls("custom_fields.enum_value.color")
            
            @schemas.classproperty
            def CUSTOM_FIELDS_ENUM_VALUE_ENABLED(cls):
                return cls("custom_fields.enum_value.enabled")
            
            @schemas.classproperty
            def CUSTOM_FIELDS_ENUM_VALUE_NAME(cls):
                return cls("custom_fields.enum_value.name")
            
            @schemas.classproperty
            def CUSTOM_FIELDS_FORMAT(cls):
                return cls("custom_fields.format")
            
            @schemas.classproperty
            def CUSTOM_FIELDS_HAS_NOTIFICATIONS_ENABLED(cls):
                return cls("custom_fields.has_notifications_enabled")
            
            @schemas.classproperty
            def CUSTOM_FIELDS_ID_PREFIX(cls):
                return cls("custom_fields.id_prefix")
            
            @schemas.classproperty
            def CUSTOM_FIELDS_IS_FORMULA_FIELD(cls):
                return cls("custom_fields.is_formula_field")
            
            @schemas.classproperty
            def CUSTOM_FIELDS_IS_GLOBAL_TO_WORKSPACE(cls):
                return cls("custom_fields.is_global_to_workspace")
            
            @schemas.classproperty
            def CUSTOM_FIELDS_IS_VALUE_READ_ONLY(cls):
                return cls("custom_fields.is_value_read_only")
            
            @schemas.classproperty
            def CUSTOM_FIELDS_MULTI_ENUM_VALUES(cls):
                return cls("custom_fields.multi_enum_values")
            
            @schemas.classproperty
            def CUSTOM_FIELDS_MULTI_ENUM_VALUES_COLOR(cls):
                return cls("custom_fields.multi_enum_values.color")
            
            @schemas.classproperty
            def CUSTOM_FIELDS_MULTI_ENUM_VALUES_ENABLED(cls):
                return cls("custom_fields.multi_enum_values.enabled")
            
            @schemas.classproperty
            def CUSTOM_FIELDS_MULTI_ENUM_VALUES_NAME(cls):
                return cls("custom_fields.multi_enum_values.name")
            
            @schemas.classproperty
            def CUSTOM_FIELDS_NAME(cls):
                return cls("custom_fields.name")
            
            @schemas.classproperty
            def CUSTOM_FIELDS_NUMBER_VALUE(cls):
                return cls("custom_fields.number_value")
            
            @schemas.classproperty
            def CUSTOM_FIELDS_PEOPLE_VALUE(cls):
                return cls("custom_fields.people_value")
            
            @schemas.classproperty
            def CUSTOM_FIELDS_PEOPLE_VALUE_NAME(cls):
                return cls("custom_fields.people_value.name")
            
            @schemas.classproperty
            def CUSTOM_FIELDS_PRECISION(cls):
                return cls("custom_fields.precision")
            
            @schemas.classproperty
            def CUSTOM_FIELDS_REPRESENTATION_TYPE(cls):
                return cls("custom_fields.representation_type")
            
            @schemas.classproperty
            def CUSTOM_FIELDS_RESOURCE_SUBTYPE(cls):
                return cls("custom_fields.resource_subtype")
            
            @schemas.classproperty
            def CUSTOM_FIELDS_TEXT_VALUE(cls):
                return cls("custom_fields.text_value")
            
            @schemas.classproperty
            def CUSTOM_FIELDS_TYPE(cls):
                return cls("custom_fields.type")
            
            @schemas.classproperty
            def DEPENDENCIES(cls):
                return cls("dependencies")
            
            @schemas.classproperty
            def DEPENDENTS(cls):
                return cls("dependents")
            
            @schemas.classproperty
            def DUE_AT(cls):
                return cls("due_at")
            
            @schemas.classproperty
            def DUE_ON(cls):
                return cls("due_on")
            
            @schemas.classproperty
            def EXTERNAL(cls):
                return cls("external")
            
            @schemas.classproperty
            def EXTERNAL_DATA(cls):
                return cls("external.data")
            
            @schemas.classproperty
            def FOLLOWERS(cls):
                return cls("followers")
            
            @schemas.classproperty
            def FOLLOWERS_NAME(cls):
                return cls("followers.name")
            
            @schemas.classproperty
            def HEARTED(cls):
                return cls("hearted")
            
            @schemas.classproperty
            def HEARTS(cls):
                return cls("hearts")
            
            @schemas.classproperty
            def HEARTS_USER(cls):
                return cls("hearts.user")
            
            @schemas.classproperty
            def HEARTS_USER_NAME(cls):
                return cls("hearts.user.name")
            
            @schemas.classproperty
            def HTML_NOTES(cls):
                return cls("html_notes")
            
            @schemas.classproperty
            def IS_RENDERED_AS_SEPARATOR(cls):
                return cls("is_rendered_as_separator")
            
            @schemas.classproperty
            def LIKED(cls):
                return cls("liked")
            
            @schemas.classproperty
            def LIKES(cls):
                return cls("likes")
            
            @schemas.classproperty
            def LIKES_USER(cls):
                return cls("likes.user")
            
            @schemas.classproperty
            def LIKES_USER_NAME(cls):
                return cls("likes.user.name")
            
            @schemas.classproperty
            def MEMBERSHIPS(cls):
                return cls("memberships")
            
            @schemas.classproperty
            def MEMBERSHIPS_PROJECT(cls):
                return cls("memberships.project")
            
            @schemas.classproperty
            def MEMBERSHIPS_PROJECT_NAME(cls):
                return cls("memberships.project.name")
            
            @schemas.classproperty
            def MEMBERSHIPS_SECTION(cls):
                return cls("memberships.section")
            
            @schemas.classproperty
            def MEMBERSHIPS_SECTION_NAME(cls):
                return cls("memberships.section.name")
            
            @schemas.classproperty
            def MODIFIED_AT(cls):
                return cls("modified_at")
            
            @schemas.classproperty
            def NAME(cls):
                return cls("name")
            
            @schemas.classproperty
            def NOTES(cls):
                return cls("notes")
            
            @schemas.classproperty
            def NUM_HEARTS(cls):
                return cls("num_hearts")
            
            @schemas.classproperty
            def NUM_LIKES(cls):
                return cls("num_likes")
            
            @schemas.classproperty
            def NUM_SUBTASKS(cls):
                return cls("num_subtasks")
            
            @schemas.classproperty
            def PARENT(cls):
                return cls("parent")
            
            @schemas.classproperty
            def PARENT_CREATED_BY(cls):
                return cls("parent.created_by")
            
            @schemas.classproperty
            def PARENT_NAME(cls):
                return cls("parent.name")
            
            @schemas.classproperty
            def PARENT_RESOURCE_SUBTYPE(cls):
                return cls("parent.resource_subtype")
            
            @schemas.classproperty
            def PERMALINK_URL(cls):
                return cls("permalink_url")
            
            @schemas.classproperty
            def PROJECTS(cls):
                return cls("projects")
            
            @schemas.classproperty
            def PROJECTS_NAME(cls):
                return cls("projects.name")
            
            @schemas.classproperty
            def RESOURCE_SUBTYPE(cls):
                return cls("resource_subtype")
            
            @schemas.classproperty
            def START_AT(cls):
                return cls("start_at")
            
            @schemas.classproperty
            def START_ON(cls):
                return cls("start_on")
            
            @schemas.classproperty
            def TAGS(cls):
                return cls("tags")
            
            @schemas.classproperty
            def TAGS_NAME(cls):
                return cls("tags.name")
            
            @schemas.classproperty
            def WORKSPACE(cls):
                return cls("workspace")
            
            @schemas.classproperty
            def WORKSPACE_NAME(cls):
                return cls("workspace.name")

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'OptFieldsSchema':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'opt_pretty': typing.Union[OptPrettySchema, bool, ],
        'text': typing.Union[TextSchema, str, ],
        'resource_subtype': typing.Union[ResourceSubtypeSchema, str, ],
        'assignee.any': typing.Union[AssigneeAnySchema, str, ],
        'assignee.not': typing.Union[AssigneeNotSchema, str, ],
        'portfolios.any': typing.Union[PortfoliosAnySchema, str, ],
        'projects.any': typing.Union[ProjectsAnySchema, str, ],
        'projects.not': typing.Union[ProjectsNotSchema, str, ],
        'projects.all': typing.Union[ProjectsAllSchema, str, ],
        'sections.any': typing.Union[SectionsAnySchema, str, ],
        'sections.not': typing.Union[SectionsNotSchema, str, ],
        'sections.all': typing.Union[SectionsAllSchema, str, ],
        'tags.any': typing.Union[TagsAnySchema, str, ],
        'tags.not': typing.Union[TagsNotSchema, str, ],
        'tags.all': typing.Union[TagsAllSchema, str, ],
        'teams.any': typing.Union[TeamsAnySchema, str, ],
        'followers.not': typing.Union[FollowersNotSchema, str, ],
        'created_by.any': typing.Union[CreatedByAnySchema, str, ],
        'created_by.not': typing.Union[CreatedByNotSchema, str, ],
        'assigned_by.any': typing.Union[AssignedByAnySchema, str, ],
        'assigned_by.not': typing.Union[AssignedByNotSchema, str, ],
        'liked_by.not': typing.Union[LikedByNotSchema, str, ],
        'commented_on_by.not': typing.Union[CommentedOnByNotSchema, str, ],
        'due_on.before': typing.Union[DueOnBeforeSchema, str, date, ],
        'due_on.after': typing.Union[DueOnAfterSchema, str, date, ],
        'due_on': typing.Union[DueOnSchema, None, str, date, ],
        'due_at.before': typing.Union[DueAtBeforeSchema, str, datetime, ],
        'due_at.after': typing.Union[DueAtAfterSchema, str, datetime, ],
        'start_on.before': typing.Union[StartOnBeforeSchema, str, date, ],
        'start_on.after': typing.Union[StartOnAfterSchema, str, date, ],
        'start_on': typing.Union[StartOnSchema, None, str, date, ],
        'created_on.before': typing.Union[CreatedOnBeforeSchema, str, date, ],
        'created_on.after': typing.Union[CreatedOnAfterSchema, str, date, ],
        'created_on': typing.Union[CreatedOnSchema, None, str, date, ],
        'created_at.before': typing.Union[CreatedAtBeforeSchema, str, datetime, ],
        'created_at.after': typing.Union[CreatedAtAfterSchema, str, datetime, ],
        'completed_on.before': typing.Union[CompletedOnBeforeSchema, str, date, ],
        'completed_on.after': typing.Union[CompletedOnAfterSchema, str, date, ],
        'completed_on': typing.Union[CompletedOnSchema, None, str, date, ],
        'completed_at.before': typing.Union[CompletedAtBeforeSchema, str, datetime, ],
        'completed_at.after': typing.Union[CompletedAtAfterSchema, str, datetime, ],
        'modified_on.before': typing.Union[ModifiedOnBeforeSchema, str, date, ],
        'modified_on.after': typing.Union[ModifiedOnAfterSchema, str, date, ],
        'modified_on': typing.Union[ModifiedOnSchema, None, str, date, ],
        'modified_at.before': typing.Union[ModifiedAtBeforeSchema, str, datetime, ],
        'modified_at.after': typing.Union[ModifiedAtAfterSchema, str, datetime, ],
        'is_blocking': typing.Union[IsBlockingSchema, bool, ],
        'is_blocked': typing.Union[IsBlockedSchema, bool, ],
        'has_attachment': typing.Union[HasAttachmentSchema, bool, ],
        'completed': typing.Union[CompletedSchema, bool, ],
        'is_subtask': typing.Union[IsSubtaskSchema, bool, ],
        'sort_by': typing.Union[SortBySchema, str, ],
        'sort_ascending': typing.Union[SortAscendingSchema, bool, ],
        'opt_fields': typing.Union[OptFieldsSchema, list, tuple, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_opt_pretty = api_client.QueryParameter(
    name="opt_pretty",
    style=api_client.ParameterStyle.FORM,
    schema=OptPrettySchema,
    explode=True,
)
request_query_text = api_client.QueryParameter(
    name="text",
    style=api_client.ParameterStyle.FORM,
    schema=TextSchema,
    explode=True,
)
request_query_resource_subtype = api_client.QueryParameter(
    name="resource_subtype",
    style=api_client.ParameterStyle.FORM,
    schema=ResourceSubtypeSchema,
    explode=True,
)
request_query_assignee_any = api_client.QueryParameter(
    name="assignee.any",
    style=api_client.ParameterStyle.FORM,
    schema=AssigneeAnySchema,
    explode=True,
)
request_query_assignee_not = api_client.QueryParameter(
    name="assignee.not",
    style=api_client.ParameterStyle.FORM,
    schema=AssigneeNotSchema,
    explode=True,
)
request_query_portfolios_any = api_client.QueryParameter(
    name="portfolios.any",
    style=api_client.ParameterStyle.FORM,
    schema=PortfoliosAnySchema,
    explode=True,
)
request_query_projects_any = api_client.QueryParameter(
    name="projects.any",
    style=api_client.ParameterStyle.FORM,
    schema=ProjectsAnySchema,
    explode=True,
)
request_query_projects_not = api_client.QueryParameter(
    name="projects.not",
    style=api_client.ParameterStyle.FORM,
    schema=ProjectsNotSchema,
    explode=True,
)
request_query_projects_all = api_client.QueryParameter(
    name="projects.all",
    style=api_client.ParameterStyle.FORM,
    schema=ProjectsAllSchema,
    explode=True,
)
request_query_sections_any = api_client.QueryParameter(
    name="sections.any",
    style=api_client.ParameterStyle.FORM,
    schema=SectionsAnySchema,
    explode=True,
)
request_query_sections_not = api_client.QueryParameter(
    name="sections.not",
    style=api_client.ParameterStyle.FORM,
    schema=SectionsNotSchema,
    explode=True,
)
request_query_sections_all = api_client.QueryParameter(
    name="sections.all",
    style=api_client.ParameterStyle.FORM,
    schema=SectionsAllSchema,
    explode=True,
)
request_query_tags_any = api_client.QueryParameter(
    name="tags.any",
    style=api_client.ParameterStyle.FORM,
    schema=TagsAnySchema,
    explode=True,
)
request_query_tags_not = api_client.QueryParameter(
    name="tags.not",
    style=api_client.ParameterStyle.FORM,
    schema=TagsNotSchema,
    explode=True,
)
request_query_tags_all = api_client.QueryParameter(
    name="tags.all",
    style=api_client.ParameterStyle.FORM,
    schema=TagsAllSchema,
    explode=True,
)
request_query_teams_any = api_client.QueryParameter(
    name="teams.any",
    style=api_client.ParameterStyle.FORM,
    schema=TeamsAnySchema,
    explode=True,
)
request_query_followers_not = api_client.QueryParameter(
    name="followers.not",
    style=api_client.ParameterStyle.FORM,
    schema=FollowersNotSchema,
    explode=True,
)
request_query_created_by_any = api_client.QueryParameter(
    name="created_by.any",
    style=api_client.ParameterStyle.FORM,
    schema=CreatedByAnySchema,
    explode=True,
)
request_query_created_by_not = api_client.QueryParameter(
    name="created_by.not",
    style=api_client.ParameterStyle.FORM,
    schema=CreatedByNotSchema,
    explode=True,
)
request_query_assigned_by_any = api_client.QueryParameter(
    name="assigned_by.any",
    style=api_client.ParameterStyle.FORM,
    schema=AssignedByAnySchema,
    explode=True,
)
request_query_assigned_by_not = api_client.QueryParameter(
    name="assigned_by.not",
    style=api_client.ParameterStyle.FORM,
    schema=AssignedByNotSchema,
    explode=True,
)
request_query_liked_by_not = api_client.QueryParameter(
    name="liked_by.not",
    style=api_client.ParameterStyle.FORM,
    schema=LikedByNotSchema,
    explode=True,
)
request_query_commented_on_by_not = api_client.QueryParameter(
    name="commented_on_by.not",
    style=api_client.ParameterStyle.FORM,
    schema=CommentedOnByNotSchema,
    explode=True,
)
request_query_due_on_before = api_client.QueryParameter(
    name="due_on.before",
    style=api_client.ParameterStyle.FORM,
    schema=DueOnBeforeSchema,
    explode=True,
)
request_query_due_on_after = api_client.QueryParameter(
    name="due_on.after",
    style=api_client.ParameterStyle.FORM,
    schema=DueOnAfterSchema,
    explode=True,
)
request_query_due_on = api_client.QueryParameter(
    name="due_on",
    style=api_client.ParameterStyle.FORM,
    schema=DueOnSchema,
    explode=True,
)
request_query_due_at_before = api_client.QueryParameter(
    name="due_at.before",
    style=api_client.ParameterStyle.FORM,
    schema=DueAtBeforeSchema,
    explode=True,
)
request_query_due_at_after = api_client.QueryParameter(
    name="due_at.after",
    style=api_client.ParameterStyle.FORM,
    schema=DueAtAfterSchema,
    explode=True,
)
request_query_start_on_before = api_client.QueryParameter(
    name="start_on.before",
    style=api_client.ParameterStyle.FORM,
    schema=StartOnBeforeSchema,
    explode=True,
)
request_query_start_on_after = api_client.QueryParameter(
    name="start_on.after",
    style=api_client.ParameterStyle.FORM,
    schema=StartOnAfterSchema,
    explode=True,
)
request_query_start_on = api_client.QueryParameter(
    name="start_on",
    style=api_client.ParameterStyle.FORM,
    schema=StartOnSchema,
    explode=True,
)
request_query_created_on_before = api_client.QueryParameter(
    name="created_on.before",
    style=api_client.ParameterStyle.FORM,
    schema=CreatedOnBeforeSchema,
    explode=True,
)
request_query_created_on_after = api_client.QueryParameter(
    name="created_on.after",
    style=api_client.ParameterStyle.FORM,
    schema=CreatedOnAfterSchema,
    explode=True,
)
request_query_created_on = api_client.QueryParameter(
    name="created_on",
    style=api_client.ParameterStyle.FORM,
    schema=CreatedOnSchema,
    explode=True,
)
request_query_created_at_before = api_client.QueryParameter(
    name="created_at.before",
    style=api_client.ParameterStyle.FORM,
    schema=CreatedAtBeforeSchema,
    explode=True,
)
request_query_created_at_after = api_client.QueryParameter(
    name="created_at.after",
    style=api_client.ParameterStyle.FORM,
    schema=CreatedAtAfterSchema,
    explode=True,
)
request_query_completed_on_before = api_client.QueryParameter(
    name="completed_on.before",
    style=api_client.ParameterStyle.FORM,
    schema=CompletedOnBeforeSchema,
    explode=True,
)
request_query_completed_on_after = api_client.QueryParameter(
    name="completed_on.after",
    style=api_client.ParameterStyle.FORM,
    schema=CompletedOnAfterSchema,
    explode=True,
)
request_query_completed_on = api_client.QueryParameter(
    name="completed_on",
    style=api_client.ParameterStyle.FORM,
    schema=CompletedOnSchema,
    explode=True,
)
request_query_completed_at_before = api_client.QueryParameter(
    name="completed_at.before",
    style=api_client.ParameterStyle.FORM,
    schema=CompletedAtBeforeSchema,
    explode=True,
)
request_query_completed_at_after = api_client.QueryParameter(
    name="completed_at.after",
    style=api_client.ParameterStyle.FORM,
    schema=CompletedAtAfterSchema,
    explode=True,
)
request_query_modified_on_before = api_client.QueryParameter(
    name="modified_on.before",
    style=api_client.ParameterStyle.FORM,
    schema=ModifiedOnBeforeSchema,
    explode=True,
)
request_query_modified_on_after = api_client.QueryParameter(
    name="modified_on.after",
    style=api_client.ParameterStyle.FORM,
    schema=ModifiedOnAfterSchema,
    explode=True,
)
request_query_modified_on = api_client.QueryParameter(
    name="modified_on",
    style=api_client.ParameterStyle.FORM,
    schema=ModifiedOnSchema,
    explode=True,
)
request_query_modified_at_before = api_client.QueryParameter(
    name="modified_at.before",
    style=api_client.ParameterStyle.FORM,
    schema=ModifiedAtBeforeSchema,
    explode=True,
)
request_query_modified_at_after = api_client.QueryParameter(
    name="modified_at.after",
    style=api_client.ParameterStyle.FORM,
    schema=ModifiedAtAfterSchema,
    explode=True,
)
request_query_is_blocking = api_client.QueryParameter(
    name="is_blocking",
    style=api_client.ParameterStyle.FORM,
    schema=IsBlockingSchema,
    explode=True,
)
request_query_is_blocked = api_client.QueryParameter(
    name="is_blocked",
    style=api_client.ParameterStyle.FORM,
    schema=IsBlockedSchema,
    explode=True,
)
request_query_has_attachment = api_client.QueryParameter(
    name="has_attachment",
    style=api_client.ParameterStyle.FORM,
    schema=HasAttachmentSchema,
    explode=True,
)
request_query_completed = api_client.QueryParameter(
    name="completed",
    style=api_client.ParameterStyle.FORM,
    schema=CompletedSchema,
    explode=True,
)
request_query_is_subtask = api_client.QueryParameter(
    name="is_subtask",
    style=api_client.ParameterStyle.FORM,
    schema=IsSubtaskSchema,
    explode=True,
)
request_query_sort_by = api_client.QueryParameter(
    name="sort_by",
    style=api_client.ParameterStyle.FORM,
    schema=SortBySchema,
    explode=True,
)
request_query_sort_ascending = api_client.QueryParameter(
    name="sort_ascending",
    style=api_client.ParameterStyle.FORM,
    schema=SortAscendingSchema,
    explode=True,
)
request_query_opt_fields = api_client.QueryParameter(
    name="opt_fields",
    style=api_client.ParameterStyle.FORM,
    schema=OptFieldsSchema,
)
# Path params
WorkspaceGidSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'workspace_gid': typing.Union[WorkspaceGidSchema, str, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_workspace_gid = api_client.PathParameter(
    name="workspace_gid",
    style=api_client.ParameterStyle.SIMPLE,
    schema=WorkspaceGidSchema,
    required=True,
)
SchemaFor200ResponseBodyApplicationJson = TasksSearchInWorkspaceResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: TasksSearchInWorkspaceResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: TasksSearchInWorkspaceResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor400ResponseBodyApplicationJson = ErrorResponseSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: ErrorResponse


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: ErrorResponse


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
    },
)
SchemaFor401ResponseBodyApplicationJson = ErrorResponseSchema


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: ErrorResponse


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: ErrorResponse


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationJson),
    },
)
SchemaFor403ResponseBodyApplicationJson = ErrorResponseSchema


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    body: ErrorResponse


@dataclass
class ApiResponseFor403Async(api_client.AsyncApiResponse):
    body: ErrorResponse


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
    response_cls_async=ApiResponseFor403Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor403ResponseBodyApplicationJson),
    },
)
SchemaFor404ResponseBodyApplicationJson = ErrorResponseSchema


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    body: ErrorResponse


@dataclass
class ApiResponseFor404Async(api_client.AsyncApiResponse):
    body: ErrorResponse


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    response_cls_async=ApiResponseFor404Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor404ResponseBodyApplicationJson),
    },
)
SchemaFor500ResponseBodyApplicationJson = ErrorResponseSchema


@dataclass
class ApiResponseFor500(api_client.ApiResponse):
    body: ErrorResponse


@dataclass
class ApiResponseFor500Async(api_client.AsyncApiResponse):
    body: ErrorResponse


_response_for_500 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor500,
    response_cls_async=ApiResponseFor500Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor500ResponseBodyApplicationJson),
    },
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _search_in_workspace_mapped_args(
        self,
        workspace_gid: str,
        opt_pretty: typing.Optional[bool] = None,
        text: typing.Optional[str] = None,
        resource_subtype: typing.Optional[str] = None,
        assignee_any: typing.Optional[str] = None,
        assignee_not: typing.Optional[str] = None,
        portfolios_any: typing.Optional[str] = None,
        projects_any: typing.Optional[str] = None,
        projects_not: typing.Optional[str] = None,
        projects_all: typing.Optional[str] = None,
        sections_any: typing.Optional[str] = None,
        sections_not: typing.Optional[str] = None,
        sections_all: typing.Optional[str] = None,
        tags_any: typing.Optional[str] = None,
        tags_not: typing.Optional[str] = None,
        tags_all: typing.Optional[str] = None,
        teams_any: typing.Optional[str] = None,
        followers_not: typing.Optional[str] = None,
        created_by_any: typing.Optional[str] = None,
        created_by_not: typing.Optional[str] = None,
        assigned_by_any: typing.Optional[str] = None,
        assigned_by_not: typing.Optional[str] = None,
        liked_by_not: typing.Optional[str] = None,
        commented_on_by_not: typing.Optional[str] = None,
        due_on_before: typing.Optional[date] = None,
        due_on_after: typing.Optional[date] = None,
        due_on: typing.Optional[typing.Optional[date]] = None,
        due_at_before: typing.Optional[datetime] = None,
        due_at_after: typing.Optional[datetime] = None,
        start_on_before: typing.Optional[date] = None,
        start_on_after: typing.Optional[date] = None,
        start_on: typing.Optional[typing.Optional[date]] = None,
        created_on_before: typing.Optional[date] = None,
        created_on_after: typing.Optional[date] = None,
        created_on: typing.Optional[typing.Optional[date]] = None,
        created_at_before: typing.Optional[datetime] = None,
        created_at_after: typing.Optional[datetime] = None,
        completed_on_before: typing.Optional[date] = None,
        completed_on_after: typing.Optional[date] = None,
        completed_on: typing.Optional[typing.Optional[date]] = None,
        completed_at_before: typing.Optional[datetime] = None,
        completed_at_after: typing.Optional[datetime] = None,
        modified_on_before: typing.Optional[date] = None,
        modified_on_after: typing.Optional[date] = None,
        modified_on: typing.Optional[typing.Optional[date]] = None,
        modified_at_before: typing.Optional[datetime] = None,
        modified_at_after: typing.Optional[datetime] = None,
        is_blocking: typing.Optional[bool] = None,
        is_blocked: typing.Optional[bool] = None,
        has_attachment: typing.Optional[bool] = None,
        completed: typing.Optional[bool] = None,
        is_subtask: typing.Optional[bool] = None,
        sort_by: typing.Optional[str] = None,
        sort_ascending: typing.Optional[bool] = None,
        opt_fields: typing.Optional[typing.List[str]] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _path_params = {}
        if opt_pretty is not None:
            _query_params["opt_pretty"] = opt_pretty
        if text is not None:
            _query_params["text"] = text
        if resource_subtype is not None:
            _query_params["resource_subtype"] = resource_subtype
        if assignee_any is not None:
            _query_params["assignee.any"] = assignee_any
        if assignee_not is not None:
            _query_params["assignee.not"] = assignee_not
        if portfolios_any is not None:
            _query_params["portfolios.any"] = portfolios_any
        if projects_any is not None:
            _query_params["projects.any"] = projects_any
        if projects_not is not None:
            _query_params["projects.not"] = projects_not
        if projects_all is not None:
            _query_params["projects.all"] = projects_all
        if sections_any is not None:
            _query_params["sections.any"] = sections_any
        if sections_not is not None:
            _query_params["sections.not"] = sections_not
        if sections_all is not None:
            _query_params["sections.all"] = sections_all
        if tags_any is not None:
            _query_params["tags.any"] = tags_any
        if tags_not is not None:
            _query_params["tags.not"] = tags_not
        if tags_all is not None:
            _query_params["tags.all"] = tags_all
        if teams_any is not None:
            _query_params["teams.any"] = teams_any
        if followers_not is not None:
            _query_params["followers.not"] = followers_not
        if created_by_any is not None:
            _query_params["created_by.any"] = created_by_any
        if created_by_not is not None:
            _query_params["created_by.not"] = created_by_not
        if assigned_by_any is not None:
            _query_params["assigned_by.any"] = assigned_by_any
        if assigned_by_not is not None:
            _query_params["assigned_by.not"] = assigned_by_not
        if liked_by_not is not None:
            _query_params["liked_by.not"] = liked_by_not
        if commented_on_by_not is not None:
            _query_params["commented_on_by.not"] = commented_on_by_not
        if due_on_before is not None:
            _query_params["due_on.before"] = due_on_before
        if due_on_after is not None:
            _query_params["due_on.after"] = due_on_after
        if due_on is not None:
            _query_params["due_on"] = due_on
        if due_at_before is not None:
            _query_params["due_at.before"] = due_at_before
        if due_at_after is not None:
            _query_params["due_at.after"] = due_at_after
        if start_on_before is not None:
            _query_params["start_on.before"] = start_on_before
        if start_on_after is not None:
            _query_params["start_on.after"] = start_on_after
        if start_on is not None:
            _query_params["start_on"] = start_on
        if created_on_before is not None:
            _query_params["created_on.before"] = created_on_before
        if created_on_after is not None:
            _query_params["created_on.after"] = created_on_after
        if created_on is not None:
            _query_params["created_on"] = created_on
        if created_at_before is not None:
            _query_params["created_at.before"] = created_at_before
        if created_at_after is not None:
            _query_params["created_at.after"] = created_at_after
        if completed_on_before is not None:
            _query_params["completed_on.before"] = completed_on_before
        if completed_on_after is not None:
            _query_params["completed_on.after"] = completed_on_after
        if completed_on is not None:
            _query_params["completed_on"] = completed_on
        if completed_at_before is not None:
            _query_params["completed_at.before"] = completed_at_before
        if completed_at_after is not None:
            _query_params["completed_at.after"] = completed_at_after
        if modified_on_before is not None:
            _query_params["modified_on.before"] = modified_on_before
        if modified_on_after is not None:
            _query_params["modified_on.after"] = modified_on_after
        if modified_on is not None:
            _query_params["modified_on"] = modified_on
        if modified_at_before is not None:
            _query_params["modified_at.before"] = modified_at_before
        if modified_at_after is not None:
            _query_params["modified_at.after"] = modified_at_after
        if is_blocking is not None:
            _query_params["is_blocking"] = is_blocking
        if is_blocked is not None:
            _query_params["is_blocked"] = is_blocked
        if has_attachment is not None:
            _query_params["has_attachment"] = has_attachment
        if completed is not None:
            _query_params["completed"] = completed
        if is_subtask is not None:
            _query_params["is_subtask"] = is_subtask
        if sort_by is not None:
            _query_params["sort_by"] = sort_by
        if sort_ascending is not None:
            _query_params["sort_ascending"] = sort_ascending
        if opt_fields is not None:
            _query_params["opt_fields"] = opt_fields
        if workspace_gid is not None:
            _path_params["workspace_gid"] = workspace_gid
        args.query = _query_params
        args.path = _path_params
        return args

    async def _asearch_in_workspace_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Search tasks in a workspace
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_workspace_gid,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_opt_pretty,
            request_query_text,
            request_query_resource_subtype,
            request_query_assignee_any,
            request_query_assignee_not,
            request_query_portfolios_any,
            request_query_projects_any,
            request_query_projects_not,
            request_query_projects_all,
            request_query_sections_any,
            request_query_sections_not,
            request_query_sections_all,
            request_query_tags_any,
            request_query_tags_not,
            request_query_tags_all,
            request_query_teams_any,
            request_query_followers_not,
            request_query_created_by_any,
            request_query_created_by_not,
            request_query_assigned_by_any,
            request_query_assigned_by_not,
            request_query_liked_by_not,
            request_query_commented_on_by_not,
            request_query_due_on_before,
            request_query_due_on_after,
            request_query_due_on,
            request_query_due_at_before,
            request_query_due_at_after,
            request_query_start_on_before,
            request_query_start_on_after,
            request_query_start_on,
            request_query_created_on_before,
            request_query_created_on_after,
            request_query_created_on,
            request_query_created_at_before,
            request_query_created_at_after,
            request_query_completed_on_before,
            request_query_completed_on_after,
            request_query_completed_on,
            request_query_completed_at_before,
            request_query_completed_at_after,
            request_query_modified_on_before,
            request_query_modified_on_after,
            request_query_modified_on,
            request_query_modified_at_before,
            request_query_modified_at_after,
            request_query_is_blocking,
            request_query_is_blocked,
            request_query_has_attachment,
            request_query_completed,
            request_query_is_subtask,
            request_query_sort_by,
            request_query_sort_ascending,
            request_query_opt_fields,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/workspaces/{workspace_gid}/tasks/search',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _search_in_workspace_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Search tasks in a workspace
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_workspace_gid,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_opt_pretty,
            request_query_text,
            request_query_resource_subtype,
            request_query_assignee_any,
            request_query_assignee_not,
            request_query_portfolios_any,
            request_query_projects_any,
            request_query_projects_not,
            request_query_projects_all,
            request_query_sections_any,
            request_query_sections_not,
            request_query_sections_all,
            request_query_tags_any,
            request_query_tags_not,
            request_query_tags_all,
            request_query_teams_any,
            request_query_followers_not,
            request_query_created_by_any,
            request_query_created_by_not,
            request_query_assigned_by_any,
            request_query_assigned_by_not,
            request_query_liked_by_not,
            request_query_commented_on_by_not,
            request_query_due_on_before,
            request_query_due_on_after,
            request_query_due_on,
            request_query_due_at_before,
            request_query_due_at_after,
            request_query_start_on_before,
            request_query_start_on_after,
            request_query_start_on,
            request_query_created_on_before,
            request_query_created_on_after,
            request_query_created_on,
            request_query_created_at_before,
            request_query_created_at_after,
            request_query_completed_on_before,
            request_query_completed_on_after,
            request_query_completed_on,
            request_query_completed_at_before,
            request_query_completed_at_after,
            request_query_modified_on_before,
            request_query_modified_on_after,
            request_query_modified_on,
            request_query_modified_at_before,
            request_query_modified_at_after,
            request_query_is_blocking,
            request_query_is_blocked,
            request_query_has_attachment,
            request_query_completed,
            request_query_is_subtask,
            request_query_sort_by,
            request_query_sort_ascending,
            request_query_opt_fields,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/workspaces/{workspace_gid}/tasks/search',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class SearchInWorkspaceRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def asearch_in_workspace(
        self,
        workspace_gid: str,
        opt_pretty: typing.Optional[bool] = None,
        text: typing.Optional[str] = None,
        resource_subtype: typing.Optional[str] = None,
        assignee_any: typing.Optional[str] = None,
        assignee_not: typing.Optional[str] = None,
        portfolios_any: typing.Optional[str] = None,
        projects_any: typing.Optional[str] = None,
        projects_not: typing.Optional[str] = None,
        projects_all: typing.Optional[str] = None,
        sections_any: typing.Optional[str] = None,
        sections_not: typing.Optional[str] = None,
        sections_all: typing.Optional[str] = None,
        tags_any: typing.Optional[str] = None,
        tags_not: typing.Optional[str] = None,
        tags_all: typing.Optional[str] = None,
        teams_any: typing.Optional[str] = None,
        followers_not: typing.Optional[str] = None,
        created_by_any: typing.Optional[str] = None,
        created_by_not: typing.Optional[str] = None,
        assigned_by_any: typing.Optional[str] = None,
        assigned_by_not: typing.Optional[str] = None,
        liked_by_not: typing.Optional[str] = None,
        commented_on_by_not: typing.Optional[str] = None,
        due_on_before: typing.Optional[date] = None,
        due_on_after: typing.Optional[date] = None,
        due_on: typing.Optional[typing.Optional[date]] = None,
        due_at_before: typing.Optional[datetime] = None,
        due_at_after: typing.Optional[datetime] = None,
        start_on_before: typing.Optional[date] = None,
        start_on_after: typing.Optional[date] = None,
        start_on: typing.Optional[typing.Optional[date]] = None,
        created_on_before: typing.Optional[date] = None,
        created_on_after: typing.Optional[date] = None,
        created_on: typing.Optional[typing.Optional[date]] = None,
        created_at_before: typing.Optional[datetime] = None,
        created_at_after: typing.Optional[datetime] = None,
        completed_on_before: typing.Optional[date] = None,
        completed_on_after: typing.Optional[date] = None,
        completed_on: typing.Optional[typing.Optional[date]] = None,
        completed_at_before: typing.Optional[datetime] = None,
        completed_at_after: typing.Optional[datetime] = None,
        modified_on_before: typing.Optional[date] = None,
        modified_on_after: typing.Optional[date] = None,
        modified_on: typing.Optional[typing.Optional[date]] = None,
        modified_at_before: typing.Optional[datetime] = None,
        modified_at_after: typing.Optional[datetime] = None,
        is_blocking: typing.Optional[bool] = None,
        is_blocked: typing.Optional[bool] = None,
        has_attachment: typing.Optional[bool] = None,
        completed: typing.Optional[bool] = None,
        is_subtask: typing.Optional[bool] = None,
        sort_by: typing.Optional[str] = None,
        sort_ascending: typing.Optional[bool] = None,
        opt_fields: typing.Optional[typing.List[str]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._search_in_workspace_mapped_args(
            workspace_gid=workspace_gid,
            opt_pretty=opt_pretty,
            text=text,
            resource_subtype=resource_subtype,
            assignee_any=assignee_any,
            assignee_not=assignee_not,
            portfolios_any=portfolios_any,
            projects_any=projects_any,
            projects_not=projects_not,
            projects_all=projects_all,
            sections_any=sections_any,
            sections_not=sections_not,
            sections_all=sections_all,
            tags_any=tags_any,
            tags_not=tags_not,
            tags_all=tags_all,
            teams_any=teams_any,
            followers_not=followers_not,
            created_by_any=created_by_any,
            created_by_not=created_by_not,
            assigned_by_any=assigned_by_any,
            assigned_by_not=assigned_by_not,
            liked_by_not=liked_by_not,
            commented_on_by_not=commented_on_by_not,
            due_on_before=due_on_before,
            due_on_after=due_on_after,
            due_on=due_on,
            due_at_before=due_at_before,
            due_at_after=due_at_after,
            start_on_before=start_on_before,
            start_on_after=start_on_after,
            start_on=start_on,
            created_on_before=created_on_before,
            created_on_after=created_on_after,
            created_on=created_on,
            created_at_before=created_at_before,
            created_at_after=created_at_after,
            completed_on_before=completed_on_before,
            completed_on_after=completed_on_after,
            completed_on=completed_on,
            completed_at_before=completed_at_before,
            completed_at_after=completed_at_after,
            modified_on_before=modified_on_before,
            modified_on_after=modified_on_after,
            modified_on=modified_on,
            modified_at_before=modified_at_before,
            modified_at_after=modified_at_after,
            is_blocking=is_blocking,
            is_blocked=is_blocked,
            has_attachment=has_attachment,
            completed=completed,
            is_subtask=is_subtask,
            sort_by=sort_by,
            sort_ascending=sort_ascending,
            opt_fields=opt_fields,
        )
        return await self._asearch_in_workspace_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def search_in_workspace(
        self,
        workspace_gid: str,
        opt_pretty: typing.Optional[bool] = None,
        text: typing.Optional[str] = None,
        resource_subtype: typing.Optional[str] = None,
        assignee_any: typing.Optional[str] = None,
        assignee_not: typing.Optional[str] = None,
        portfolios_any: typing.Optional[str] = None,
        projects_any: typing.Optional[str] = None,
        projects_not: typing.Optional[str] = None,
        projects_all: typing.Optional[str] = None,
        sections_any: typing.Optional[str] = None,
        sections_not: typing.Optional[str] = None,
        sections_all: typing.Optional[str] = None,
        tags_any: typing.Optional[str] = None,
        tags_not: typing.Optional[str] = None,
        tags_all: typing.Optional[str] = None,
        teams_any: typing.Optional[str] = None,
        followers_not: typing.Optional[str] = None,
        created_by_any: typing.Optional[str] = None,
        created_by_not: typing.Optional[str] = None,
        assigned_by_any: typing.Optional[str] = None,
        assigned_by_not: typing.Optional[str] = None,
        liked_by_not: typing.Optional[str] = None,
        commented_on_by_not: typing.Optional[str] = None,
        due_on_before: typing.Optional[date] = None,
        due_on_after: typing.Optional[date] = None,
        due_on: typing.Optional[typing.Optional[date]] = None,
        due_at_before: typing.Optional[datetime] = None,
        due_at_after: typing.Optional[datetime] = None,
        start_on_before: typing.Optional[date] = None,
        start_on_after: typing.Optional[date] = None,
        start_on: typing.Optional[typing.Optional[date]] = None,
        created_on_before: typing.Optional[date] = None,
        created_on_after: typing.Optional[date] = None,
        created_on: typing.Optional[typing.Optional[date]] = None,
        created_at_before: typing.Optional[datetime] = None,
        created_at_after: typing.Optional[datetime] = None,
        completed_on_before: typing.Optional[date] = None,
        completed_on_after: typing.Optional[date] = None,
        completed_on: typing.Optional[typing.Optional[date]] = None,
        completed_at_before: typing.Optional[datetime] = None,
        completed_at_after: typing.Optional[datetime] = None,
        modified_on_before: typing.Optional[date] = None,
        modified_on_after: typing.Optional[date] = None,
        modified_on: typing.Optional[typing.Optional[date]] = None,
        modified_at_before: typing.Optional[datetime] = None,
        modified_at_after: typing.Optional[datetime] = None,
        is_blocking: typing.Optional[bool] = None,
        is_blocked: typing.Optional[bool] = None,
        has_attachment: typing.Optional[bool] = None,
        completed: typing.Optional[bool] = None,
        is_subtask: typing.Optional[bool] = None,
        sort_by: typing.Optional[str] = None,
        sort_ascending: typing.Optional[bool] = None,
        opt_fields: typing.Optional[typing.List[str]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._search_in_workspace_mapped_args(
            workspace_gid=workspace_gid,
            opt_pretty=opt_pretty,
            text=text,
            resource_subtype=resource_subtype,
            assignee_any=assignee_any,
            assignee_not=assignee_not,
            portfolios_any=portfolios_any,
            projects_any=projects_any,
            projects_not=projects_not,
            projects_all=projects_all,
            sections_any=sections_any,
            sections_not=sections_not,
            sections_all=sections_all,
            tags_any=tags_any,
            tags_not=tags_not,
            tags_all=tags_all,
            teams_any=teams_any,
            followers_not=followers_not,
            created_by_any=created_by_any,
            created_by_not=created_by_not,
            assigned_by_any=assigned_by_any,
            assigned_by_not=assigned_by_not,
            liked_by_not=liked_by_not,
            commented_on_by_not=commented_on_by_not,
            due_on_before=due_on_before,
            due_on_after=due_on_after,
            due_on=due_on,
            due_at_before=due_at_before,
            due_at_after=due_at_after,
            start_on_before=start_on_before,
            start_on_after=start_on_after,
            start_on=start_on,
            created_on_before=created_on_before,
            created_on_after=created_on_after,
            created_on=created_on,
            created_at_before=created_at_before,
            created_at_after=created_at_after,
            completed_on_before=completed_on_before,
            completed_on_after=completed_on_after,
            completed_on=completed_on,
            completed_at_before=completed_at_before,
            completed_at_after=completed_at_after,
            modified_on_before=modified_on_before,
            modified_on_after=modified_on_after,
            modified_on=modified_on,
            modified_at_before=modified_at_before,
            modified_at_after=modified_at_after,
            is_blocking=is_blocking,
            is_blocked=is_blocked,
            has_attachment=has_attachment,
            completed=completed,
            is_subtask=is_subtask,
            sort_by=sort_by,
            sort_ascending=sort_ascending,
            opt_fields=opt_fields,
        )
        return self._search_in_workspace_oapg(
            query_params=args.query,
            path_params=args.path,
        )

class SearchInWorkspace(BaseApi):

    async def asearch_in_workspace(
        self,
        workspace_gid: str,
        opt_pretty: typing.Optional[bool] = None,
        text: typing.Optional[str] = None,
        resource_subtype: typing.Optional[str] = None,
        assignee_any: typing.Optional[str] = None,
        assignee_not: typing.Optional[str] = None,
        portfolios_any: typing.Optional[str] = None,
        projects_any: typing.Optional[str] = None,
        projects_not: typing.Optional[str] = None,
        projects_all: typing.Optional[str] = None,
        sections_any: typing.Optional[str] = None,
        sections_not: typing.Optional[str] = None,
        sections_all: typing.Optional[str] = None,
        tags_any: typing.Optional[str] = None,
        tags_not: typing.Optional[str] = None,
        tags_all: typing.Optional[str] = None,
        teams_any: typing.Optional[str] = None,
        followers_not: typing.Optional[str] = None,
        created_by_any: typing.Optional[str] = None,
        created_by_not: typing.Optional[str] = None,
        assigned_by_any: typing.Optional[str] = None,
        assigned_by_not: typing.Optional[str] = None,
        liked_by_not: typing.Optional[str] = None,
        commented_on_by_not: typing.Optional[str] = None,
        due_on_before: typing.Optional[date] = None,
        due_on_after: typing.Optional[date] = None,
        due_on: typing.Optional[typing.Optional[date]] = None,
        due_at_before: typing.Optional[datetime] = None,
        due_at_after: typing.Optional[datetime] = None,
        start_on_before: typing.Optional[date] = None,
        start_on_after: typing.Optional[date] = None,
        start_on: typing.Optional[typing.Optional[date]] = None,
        created_on_before: typing.Optional[date] = None,
        created_on_after: typing.Optional[date] = None,
        created_on: typing.Optional[typing.Optional[date]] = None,
        created_at_before: typing.Optional[datetime] = None,
        created_at_after: typing.Optional[datetime] = None,
        completed_on_before: typing.Optional[date] = None,
        completed_on_after: typing.Optional[date] = None,
        completed_on: typing.Optional[typing.Optional[date]] = None,
        completed_at_before: typing.Optional[datetime] = None,
        completed_at_after: typing.Optional[datetime] = None,
        modified_on_before: typing.Optional[date] = None,
        modified_on_after: typing.Optional[date] = None,
        modified_on: typing.Optional[typing.Optional[date]] = None,
        modified_at_before: typing.Optional[datetime] = None,
        modified_at_after: typing.Optional[datetime] = None,
        is_blocking: typing.Optional[bool] = None,
        is_blocked: typing.Optional[bool] = None,
        has_attachment: typing.Optional[bool] = None,
        completed: typing.Optional[bool] = None,
        is_subtask: typing.Optional[bool] = None,
        sort_by: typing.Optional[str] = None,
        sort_ascending: typing.Optional[bool] = None,
        opt_fields: typing.Optional[typing.List[str]] = None,
        validate: bool = False,
        **kwargs,
    ) -> TasksSearchInWorkspaceResponsePydantic:
        raw_response = await self.raw.asearch_in_workspace(
            workspace_gid=workspace_gid,
            opt_pretty=opt_pretty,
            text=text,
            resource_subtype=resource_subtype,
            assignee_any=assignee_any,
            assignee_not=assignee_not,
            portfolios_any=portfolios_any,
            projects_any=projects_any,
            projects_not=projects_not,
            projects_all=projects_all,
            sections_any=sections_any,
            sections_not=sections_not,
            sections_all=sections_all,
            tags_any=tags_any,
            tags_not=tags_not,
            tags_all=tags_all,
            teams_any=teams_any,
            followers_not=followers_not,
            created_by_any=created_by_any,
            created_by_not=created_by_not,
            assigned_by_any=assigned_by_any,
            assigned_by_not=assigned_by_not,
            liked_by_not=liked_by_not,
            commented_on_by_not=commented_on_by_not,
            due_on_before=due_on_before,
            due_on_after=due_on_after,
            due_on=due_on,
            due_at_before=due_at_before,
            due_at_after=due_at_after,
            start_on_before=start_on_before,
            start_on_after=start_on_after,
            start_on=start_on,
            created_on_before=created_on_before,
            created_on_after=created_on_after,
            created_on=created_on,
            created_at_before=created_at_before,
            created_at_after=created_at_after,
            completed_on_before=completed_on_before,
            completed_on_after=completed_on_after,
            completed_on=completed_on,
            completed_at_before=completed_at_before,
            completed_at_after=completed_at_after,
            modified_on_before=modified_on_before,
            modified_on_after=modified_on_after,
            modified_on=modified_on,
            modified_at_before=modified_at_before,
            modified_at_after=modified_at_after,
            is_blocking=is_blocking,
            is_blocked=is_blocked,
            has_attachment=has_attachment,
            completed=completed,
            is_subtask=is_subtask,
            sort_by=sort_by,
            sort_ascending=sort_ascending,
            opt_fields=opt_fields,
            **kwargs,
        )
        if validate:
            return TasksSearchInWorkspaceResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(TasksSearchInWorkspaceResponsePydantic, raw_response.body)
    
    
    def search_in_workspace(
        self,
        workspace_gid: str,
        opt_pretty: typing.Optional[bool] = None,
        text: typing.Optional[str] = None,
        resource_subtype: typing.Optional[str] = None,
        assignee_any: typing.Optional[str] = None,
        assignee_not: typing.Optional[str] = None,
        portfolios_any: typing.Optional[str] = None,
        projects_any: typing.Optional[str] = None,
        projects_not: typing.Optional[str] = None,
        projects_all: typing.Optional[str] = None,
        sections_any: typing.Optional[str] = None,
        sections_not: typing.Optional[str] = None,
        sections_all: typing.Optional[str] = None,
        tags_any: typing.Optional[str] = None,
        tags_not: typing.Optional[str] = None,
        tags_all: typing.Optional[str] = None,
        teams_any: typing.Optional[str] = None,
        followers_not: typing.Optional[str] = None,
        created_by_any: typing.Optional[str] = None,
        created_by_not: typing.Optional[str] = None,
        assigned_by_any: typing.Optional[str] = None,
        assigned_by_not: typing.Optional[str] = None,
        liked_by_not: typing.Optional[str] = None,
        commented_on_by_not: typing.Optional[str] = None,
        due_on_before: typing.Optional[date] = None,
        due_on_after: typing.Optional[date] = None,
        due_on: typing.Optional[typing.Optional[date]] = None,
        due_at_before: typing.Optional[datetime] = None,
        due_at_after: typing.Optional[datetime] = None,
        start_on_before: typing.Optional[date] = None,
        start_on_after: typing.Optional[date] = None,
        start_on: typing.Optional[typing.Optional[date]] = None,
        created_on_before: typing.Optional[date] = None,
        created_on_after: typing.Optional[date] = None,
        created_on: typing.Optional[typing.Optional[date]] = None,
        created_at_before: typing.Optional[datetime] = None,
        created_at_after: typing.Optional[datetime] = None,
        completed_on_before: typing.Optional[date] = None,
        completed_on_after: typing.Optional[date] = None,
        completed_on: typing.Optional[typing.Optional[date]] = None,
        completed_at_before: typing.Optional[datetime] = None,
        completed_at_after: typing.Optional[datetime] = None,
        modified_on_before: typing.Optional[date] = None,
        modified_on_after: typing.Optional[date] = None,
        modified_on: typing.Optional[typing.Optional[date]] = None,
        modified_at_before: typing.Optional[datetime] = None,
        modified_at_after: typing.Optional[datetime] = None,
        is_blocking: typing.Optional[bool] = None,
        is_blocked: typing.Optional[bool] = None,
        has_attachment: typing.Optional[bool] = None,
        completed: typing.Optional[bool] = None,
        is_subtask: typing.Optional[bool] = None,
        sort_by: typing.Optional[str] = None,
        sort_ascending: typing.Optional[bool] = None,
        opt_fields: typing.Optional[typing.List[str]] = None,
        validate: bool = False,
    ) -> TasksSearchInWorkspaceResponsePydantic:
        raw_response = self.raw.search_in_workspace(
            workspace_gid=workspace_gid,
            opt_pretty=opt_pretty,
            text=text,
            resource_subtype=resource_subtype,
            assignee_any=assignee_any,
            assignee_not=assignee_not,
            portfolios_any=portfolios_any,
            projects_any=projects_any,
            projects_not=projects_not,
            projects_all=projects_all,
            sections_any=sections_any,
            sections_not=sections_not,
            sections_all=sections_all,
            tags_any=tags_any,
            tags_not=tags_not,
            tags_all=tags_all,
            teams_any=teams_any,
            followers_not=followers_not,
            created_by_any=created_by_any,
            created_by_not=created_by_not,
            assigned_by_any=assigned_by_any,
            assigned_by_not=assigned_by_not,
            liked_by_not=liked_by_not,
            commented_on_by_not=commented_on_by_not,
            due_on_before=due_on_before,
            due_on_after=due_on_after,
            due_on=due_on,
            due_at_before=due_at_before,
            due_at_after=due_at_after,
            start_on_before=start_on_before,
            start_on_after=start_on_after,
            start_on=start_on,
            created_on_before=created_on_before,
            created_on_after=created_on_after,
            created_on=created_on,
            created_at_before=created_at_before,
            created_at_after=created_at_after,
            completed_on_before=completed_on_before,
            completed_on_after=completed_on_after,
            completed_on=completed_on,
            completed_at_before=completed_at_before,
            completed_at_after=completed_at_after,
            modified_on_before=modified_on_before,
            modified_on_after=modified_on_after,
            modified_on=modified_on,
            modified_at_before=modified_at_before,
            modified_at_after=modified_at_after,
            is_blocking=is_blocking,
            is_blocked=is_blocked,
            has_attachment=has_attachment,
            completed=completed,
            is_subtask=is_subtask,
            sort_by=sort_by,
            sort_ascending=sort_ascending,
            opt_fields=opt_fields,
        )
        if validate:
            return TasksSearchInWorkspaceResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(TasksSearchInWorkspaceResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        workspace_gid: str,
        opt_pretty: typing.Optional[bool] = None,
        text: typing.Optional[str] = None,
        resource_subtype: typing.Optional[str] = None,
        assignee_any: typing.Optional[str] = None,
        assignee_not: typing.Optional[str] = None,
        portfolios_any: typing.Optional[str] = None,
        projects_any: typing.Optional[str] = None,
        projects_not: typing.Optional[str] = None,
        projects_all: typing.Optional[str] = None,
        sections_any: typing.Optional[str] = None,
        sections_not: typing.Optional[str] = None,
        sections_all: typing.Optional[str] = None,
        tags_any: typing.Optional[str] = None,
        tags_not: typing.Optional[str] = None,
        tags_all: typing.Optional[str] = None,
        teams_any: typing.Optional[str] = None,
        followers_not: typing.Optional[str] = None,
        created_by_any: typing.Optional[str] = None,
        created_by_not: typing.Optional[str] = None,
        assigned_by_any: typing.Optional[str] = None,
        assigned_by_not: typing.Optional[str] = None,
        liked_by_not: typing.Optional[str] = None,
        commented_on_by_not: typing.Optional[str] = None,
        due_on_before: typing.Optional[date] = None,
        due_on_after: typing.Optional[date] = None,
        due_on: typing.Optional[typing.Optional[date]] = None,
        due_at_before: typing.Optional[datetime] = None,
        due_at_after: typing.Optional[datetime] = None,
        start_on_before: typing.Optional[date] = None,
        start_on_after: typing.Optional[date] = None,
        start_on: typing.Optional[typing.Optional[date]] = None,
        created_on_before: typing.Optional[date] = None,
        created_on_after: typing.Optional[date] = None,
        created_on: typing.Optional[typing.Optional[date]] = None,
        created_at_before: typing.Optional[datetime] = None,
        created_at_after: typing.Optional[datetime] = None,
        completed_on_before: typing.Optional[date] = None,
        completed_on_after: typing.Optional[date] = None,
        completed_on: typing.Optional[typing.Optional[date]] = None,
        completed_at_before: typing.Optional[datetime] = None,
        completed_at_after: typing.Optional[datetime] = None,
        modified_on_before: typing.Optional[date] = None,
        modified_on_after: typing.Optional[date] = None,
        modified_on: typing.Optional[typing.Optional[date]] = None,
        modified_at_before: typing.Optional[datetime] = None,
        modified_at_after: typing.Optional[datetime] = None,
        is_blocking: typing.Optional[bool] = None,
        is_blocked: typing.Optional[bool] = None,
        has_attachment: typing.Optional[bool] = None,
        completed: typing.Optional[bool] = None,
        is_subtask: typing.Optional[bool] = None,
        sort_by: typing.Optional[str] = None,
        sort_ascending: typing.Optional[bool] = None,
        opt_fields: typing.Optional[typing.List[str]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._search_in_workspace_mapped_args(
            workspace_gid=workspace_gid,
            opt_pretty=opt_pretty,
            text=text,
            resource_subtype=resource_subtype,
            assignee_any=assignee_any,
            assignee_not=assignee_not,
            portfolios_any=portfolios_any,
            projects_any=projects_any,
            projects_not=projects_not,
            projects_all=projects_all,
            sections_any=sections_any,
            sections_not=sections_not,
            sections_all=sections_all,
            tags_any=tags_any,
            tags_not=tags_not,
            tags_all=tags_all,
            teams_any=teams_any,
            followers_not=followers_not,
            created_by_any=created_by_any,
            created_by_not=created_by_not,
            assigned_by_any=assigned_by_any,
            assigned_by_not=assigned_by_not,
            liked_by_not=liked_by_not,
            commented_on_by_not=commented_on_by_not,
            due_on_before=due_on_before,
            due_on_after=due_on_after,
            due_on=due_on,
            due_at_before=due_at_before,
            due_at_after=due_at_after,
            start_on_before=start_on_before,
            start_on_after=start_on_after,
            start_on=start_on,
            created_on_before=created_on_before,
            created_on_after=created_on_after,
            created_on=created_on,
            created_at_before=created_at_before,
            created_at_after=created_at_after,
            completed_on_before=completed_on_before,
            completed_on_after=completed_on_after,
            completed_on=completed_on,
            completed_at_before=completed_at_before,
            completed_at_after=completed_at_after,
            modified_on_before=modified_on_before,
            modified_on_after=modified_on_after,
            modified_on=modified_on,
            modified_at_before=modified_at_before,
            modified_at_after=modified_at_after,
            is_blocking=is_blocking,
            is_blocked=is_blocked,
            has_attachment=has_attachment,
            completed=completed,
            is_subtask=is_subtask,
            sort_by=sort_by,
            sort_ascending=sort_ascending,
            opt_fields=opt_fields,
        )
        return await self._asearch_in_workspace_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        workspace_gid: str,
        opt_pretty: typing.Optional[bool] = None,
        text: typing.Optional[str] = None,
        resource_subtype: typing.Optional[str] = None,
        assignee_any: typing.Optional[str] = None,
        assignee_not: typing.Optional[str] = None,
        portfolios_any: typing.Optional[str] = None,
        projects_any: typing.Optional[str] = None,
        projects_not: typing.Optional[str] = None,
        projects_all: typing.Optional[str] = None,
        sections_any: typing.Optional[str] = None,
        sections_not: typing.Optional[str] = None,
        sections_all: typing.Optional[str] = None,
        tags_any: typing.Optional[str] = None,
        tags_not: typing.Optional[str] = None,
        tags_all: typing.Optional[str] = None,
        teams_any: typing.Optional[str] = None,
        followers_not: typing.Optional[str] = None,
        created_by_any: typing.Optional[str] = None,
        created_by_not: typing.Optional[str] = None,
        assigned_by_any: typing.Optional[str] = None,
        assigned_by_not: typing.Optional[str] = None,
        liked_by_not: typing.Optional[str] = None,
        commented_on_by_not: typing.Optional[str] = None,
        due_on_before: typing.Optional[date] = None,
        due_on_after: typing.Optional[date] = None,
        due_on: typing.Optional[typing.Optional[date]] = None,
        due_at_before: typing.Optional[datetime] = None,
        due_at_after: typing.Optional[datetime] = None,
        start_on_before: typing.Optional[date] = None,
        start_on_after: typing.Optional[date] = None,
        start_on: typing.Optional[typing.Optional[date]] = None,
        created_on_before: typing.Optional[date] = None,
        created_on_after: typing.Optional[date] = None,
        created_on: typing.Optional[typing.Optional[date]] = None,
        created_at_before: typing.Optional[datetime] = None,
        created_at_after: typing.Optional[datetime] = None,
        completed_on_before: typing.Optional[date] = None,
        completed_on_after: typing.Optional[date] = None,
        completed_on: typing.Optional[typing.Optional[date]] = None,
        completed_at_before: typing.Optional[datetime] = None,
        completed_at_after: typing.Optional[datetime] = None,
        modified_on_before: typing.Optional[date] = None,
        modified_on_after: typing.Optional[date] = None,
        modified_on: typing.Optional[typing.Optional[date]] = None,
        modified_at_before: typing.Optional[datetime] = None,
        modified_at_after: typing.Optional[datetime] = None,
        is_blocking: typing.Optional[bool] = None,
        is_blocked: typing.Optional[bool] = None,
        has_attachment: typing.Optional[bool] = None,
        completed: typing.Optional[bool] = None,
        is_subtask: typing.Optional[bool] = None,
        sort_by: typing.Optional[str] = None,
        sort_ascending: typing.Optional[bool] = None,
        opt_fields: typing.Optional[typing.List[str]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._search_in_workspace_mapped_args(
            workspace_gid=workspace_gid,
            opt_pretty=opt_pretty,
            text=text,
            resource_subtype=resource_subtype,
            assignee_any=assignee_any,
            assignee_not=assignee_not,
            portfolios_any=portfolios_any,
            projects_any=projects_any,
            projects_not=projects_not,
            projects_all=projects_all,
            sections_any=sections_any,
            sections_not=sections_not,
            sections_all=sections_all,
            tags_any=tags_any,
            tags_not=tags_not,
            tags_all=tags_all,
            teams_any=teams_any,
            followers_not=followers_not,
            created_by_any=created_by_any,
            created_by_not=created_by_not,
            assigned_by_any=assigned_by_any,
            assigned_by_not=assigned_by_not,
            liked_by_not=liked_by_not,
            commented_on_by_not=commented_on_by_not,
            due_on_before=due_on_before,
            due_on_after=due_on_after,
            due_on=due_on,
            due_at_before=due_at_before,
            due_at_after=due_at_after,
            start_on_before=start_on_before,
            start_on_after=start_on_after,
            start_on=start_on,
            created_on_before=created_on_before,
            created_on_after=created_on_after,
            created_on=created_on,
            created_at_before=created_at_before,
            created_at_after=created_at_after,
            completed_on_before=completed_on_before,
            completed_on_after=completed_on_after,
            completed_on=completed_on,
            completed_at_before=completed_at_before,
            completed_at_after=completed_at_after,
            modified_on_before=modified_on_before,
            modified_on_after=modified_on_after,
            modified_on=modified_on,
            modified_at_before=modified_at_before,
            modified_at_after=modified_at_after,
            is_blocking=is_blocking,
            is_blocked=is_blocked,
            has_attachment=has_attachment,
            completed=completed,
            is_subtask=is_subtask,
            sort_by=sort_by,
            sort_ascending=sort_ascending,
            opt_fields=opt_fields,
        )
        return self._search_in_workspace_oapg(
            query_params=args.query,
            path_params=args.path,
        )

