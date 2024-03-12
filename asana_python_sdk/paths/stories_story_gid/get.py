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

from asana_python_sdk.model.stories_get_full_record_response import StoriesGetFullRecordResponse as StoriesGetFullRecordResponseSchema
from asana_python_sdk.model.error_response import ErrorResponse as ErrorResponseSchema

from asana_python_sdk.type.stories_get_full_record_response import StoriesGetFullRecordResponse
from asana_python_sdk.type.error_response import ErrorResponse

from ...api_client import Dictionary
from asana_python_sdk.pydantic.error_response import ErrorResponse as ErrorResponsePydantic
from asana_python_sdk.pydantic.stories_get_full_record_response import StoriesGetFullRecordResponse as StoriesGetFullRecordResponsePydantic

from . import path

# Query params
OptPrettySchema = schemas.BoolSchema


class OptFieldsSchema(
    schemas.ListSchema
):


    class MetaOapg:
        
        
        class items(
            schemas.EnumBase,
            schemas.StrSchema
        ):
        
        
            class MetaOapg:
                enum_value_to_name = {
                    "assignee": "ASSIGNEE",
                    "assignee.name": "ASSIGNEE_NAME",
                    "created_at": "CREATED_AT",
                    "created_by": "CREATED_BY",
                    "created_by.name": "CREATED_BY_NAME",
                    "custom_field": "CUSTOM_FIELD",
                    "custom_field.date_value": "CUSTOM_FIELD_DATE_VALUE",
                    "custom_field.date_value.date": "CUSTOM_FIELD_DATE_VALUE_DATE",
                    "custom_field.date_value.date_time": "CUSTOM_FIELD_DATE_VALUE_DATE_TIME",
                    "custom_field.display_value": "CUSTOM_FIELD_DISPLAY_VALUE",
                    "custom_field.enabled": "CUSTOM_FIELD_ENABLED",
                    "custom_field.enum_options": "CUSTOM_FIELD_ENUM_OPTIONS",
                    "custom_field.enum_options.color": "CUSTOM_FIELD_ENUM_OPTIONS_COLOR",
                    "custom_field.enum_options.enabled": "CUSTOM_FIELD_ENUM_OPTIONS_ENABLED",
                    "custom_field.enum_options.name": "CUSTOM_FIELD_ENUM_OPTIONS_NAME",
                    "custom_field.enum_value": "CUSTOM_FIELD_ENUM_VALUE",
                    "custom_field.enum_value.color": "CUSTOM_FIELD_ENUM_VALUE_COLOR",
                    "custom_field.enum_value.enabled": "CUSTOM_FIELD_ENUM_VALUE_ENABLED",
                    "custom_field.enum_value.name": "CUSTOM_FIELD_ENUM_VALUE_NAME",
                    "custom_field.id_prefix": "CUSTOM_FIELD_ID_PREFIX",
                    "custom_field.is_formula_field": "CUSTOM_FIELD_IS_FORMULA_FIELD",
                    "custom_field.multi_enum_values": "CUSTOM_FIELD_MULTI_ENUM_VALUES",
                    "custom_field.multi_enum_values.color": "CUSTOM_FIELD_MULTI_ENUM_VALUES_COLOR",
                    "custom_field.multi_enum_values.enabled": "CUSTOM_FIELD_MULTI_ENUM_VALUES_ENABLED",
                    "custom_field.multi_enum_values.name": "CUSTOM_FIELD_MULTI_ENUM_VALUES_NAME",
                    "custom_field.name": "CUSTOM_FIELD_NAME",
                    "custom_field.number_value": "CUSTOM_FIELD_NUMBER_VALUE",
                    "custom_field.representation_type": "CUSTOM_FIELD_REPRESENTATION_TYPE",
                    "custom_field.resource_subtype": "CUSTOM_FIELD_RESOURCE_SUBTYPE",
                    "custom_field.text_value": "CUSTOM_FIELD_TEXT_VALUE",
                    "custom_field.type": "CUSTOM_FIELD_TYPE",
                    "dependency": "DEPENDENCY",
                    "dependency.created_by": "DEPENDENCY_CREATED_BY",
                    "dependency.name": "DEPENDENCY_NAME",
                    "dependency.resource_subtype": "DEPENDENCY_RESOURCE_SUBTYPE",
                    "duplicate_of": "DUPLICATE_OF",
                    "duplicate_of.created_by": "DUPLICATE_OF_CREATED_BY",
                    "duplicate_of.name": "DUPLICATE_OF_NAME",
                    "duplicate_of.resource_subtype": "DUPLICATE_OF_RESOURCE_SUBTYPE",
                    "duplicated_from": "DUPLICATED_FROM",
                    "duplicated_from.created_by": "DUPLICATED_FROM_CREATED_BY",
                    "duplicated_from.name": "DUPLICATED_FROM_NAME",
                    "duplicated_from.resource_subtype": "DUPLICATED_FROM_RESOURCE_SUBTYPE",
                    "follower": "FOLLOWER",
                    "follower.name": "FOLLOWER_NAME",
                    "hearted": "HEARTED",
                    "hearts": "HEARTS",
                    "hearts.user": "HEARTS_USER",
                    "hearts.user.name": "HEARTS_USER_NAME",
                    "html_text": "HTML_TEXT",
                    "is_editable": "IS_EDITABLE",
                    "is_edited": "IS_EDITED",
                    "is_pinned": "IS_PINNED",
                    "liked": "LIKED",
                    "likes": "LIKES",
                    "likes.user": "LIKES_USER",
                    "likes.user.name": "LIKES_USER_NAME",
                    "new_approval_status": "NEW_APPROVAL_STATUS",
                    "new_date_value": "NEW_DATE_VALUE",
                    "new_dates": "NEW_DATES",
                    "new_dates.due_at": "NEW_DATES_DUE_AT",
                    "new_dates.due_on": "NEW_DATES_DUE_ON",
                    "new_dates.start_on": "NEW_DATES_START_ON",
                    "new_enum_value": "NEW_ENUM_VALUE",
                    "new_enum_value.color": "NEW_ENUM_VALUE_COLOR",
                    "new_enum_value.enabled": "NEW_ENUM_VALUE_ENABLED",
                    "new_enum_value.name": "NEW_ENUM_VALUE_NAME",
                    "new_multi_enum_values": "NEW_MULTI_ENUM_VALUES",
                    "new_multi_enum_values.color": "NEW_MULTI_ENUM_VALUES_COLOR",
                    "new_multi_enum_values.enabled": "NEW_MULTI_ENUM_VALUES_ENABLED",
                    "new_multi_enum_values.name": "NEW_MULTI_ENUM_VALUES_NAME",
                    "new_name": "NEW_NAME",
                    "new_number_value": "NEW_NUMBER_VALUE",
                    "new_people_value": "NEW_PEOPLE_VALUE",
                    "new_people_value.name": "NEW_PEOPLE_VALUE_NAME",
                    "new_resource_subtype": "NEW_RESOURCE_SUBTYPE",
                    "new_section": "NEW_SECTION",
                    "new_section.name": "NEW_SECTION_NAME",
                    "new_text_value": "NEW_TEXT_VALUE",
                    "num_hearts": "NUM_HEARTS",
                    "num_likes": "NUM_LIKES",
                    "old_approval_status": "OLD_APPROVAL_STATUS",
                    "old_date_value": "OLD_DATE_VALUE",
                    "old_dates": "OLD_DATES",
                    "old_dates.due_at": "OLD_DATES_DUE_AT",
                    "old_dates.due_on": "OLD_DATES_DUE_ON",
                    "old_dates.start_on": "OLD_DATES_START_ON",
                    "old_enum_value": "OLD_ENUM_VALUE",
                    "old_enum_value.color": "OLD_ENUM_VALUE_COLOR",
                    "old_enum_value.enabled": "OLD_ENUM_VALUE_ENABLED",
                    "old_enum_value.name": "OLD_ENUM_VALUE_NAME",
                    "old_multi_enum_values": "OLD_MULTI_ENUM_VALUES",
                    "old_multi_enum_values.color": "OLD_MULTI_ENUM_VALUES_COLOR",
                    "old_multi_enum_values.enabled": "OLD_MULTI_ENUM_VALUES_ENABLED",
                    "old_multi_enum_values.name": "OLD_MULTI_ENUM_VALUES_NAME",
                    "old_name": "OLD_NAME",
                    "old_number_value": "OLD_NUMBER_VALUE",
                    "old_people_value": "OLD_PEOPLE_VALUE",
                    "old_people_value.name": "OLD_PEOPLE_VALUE_NAME",
                    "old_resource_subtype": "OLD_RESOURCE_SUBTYPE",
                    "old_section": "OLD_SECTION",
                    "old_section.name": "OLD_SECTION_NAME",
                    "old_text_value": "OLD_TEXT_VALUE",
                    "previews": "PREVIEWS",
                    "previews.fallback": "PREVIEWS_FALLBACK",
                    "previews.footer": "PREVIEWS_FOOTER",
                    "previews.header": "PREVIEWS_HEADER",
                    "previews.header_link": "PREVIEWS_HEADER_LINK",
                    "previews.html_text": "PREVIEWS_HTML_TEXT",
                    "previews.text": "PREVIEWS_TEXT",
                    "previews.title": "PREVIEWS_TITLE",
                    "previews.title_link": "PREVIEWS_TITLE_LINK",
                    "project": "PROJECT",
                    "project.name": "PROJECT_NAME",
                    "resource_subtype": "RESOURCE_SUBTYPE",
                    "source": "SOURCE",
                    "sticker_name": "STICKER_NAME",
                    "story": "STORY",
                    "story.created_at": "STORY_CREATED_AT",
                    "story.created_by": "STORY_CREATED_BY",
                    "story.created_by.name": "STORY_CREATED_BY_NAME",
                    "story.resource_subtype": "STORY_RESOURCE_SUBTYPE",
                    "story.text": "STORY_TEXT",
                    "tag": "TAG",
                    "tag.name": "TAG_NAME",
                    "target": "TARGET",
                    "target.created_by": "TARGET_CREATED_BY",
                    "target.name": "TARGET_NAME",
                    "target.resource_subtype": "TARGET_RESOURCE_SUBTYPE",
                    "task": "TASK",
                    "task.created_by": "TASK_CREATED_BY",
                    "task.name": "TASK_NAME",
                    "task.resource_subtype": "TASK_RESOURCE_SUBTYPE",
                    "text": "TEXT",
                    "type": "TYPE",
                }
            
            @schemas.classproperty
            def ASSIGNEE(cls):
                return cls("assignee")
            
            @schemas.classproperty
            def ASSIGNEE_NAME(cls):
                return cls("assignee.name")
            
            @schemas.classproperty
            def CREATED_AT(cls):
                return cls("created_at")
            
            @schemas.classproperty
            def CREATED_BY(cls):
                return cls("created_by")
            
            @schemas.classproperty
            def CREATED_BY_NAME(cls):
                return cls("created_by.name")
            
            @schemas.classproperty
            def CUSTOM_FIELD(cls):
                return cls("custom_field")
            
            @schemas.classproperty
            def CUSTOM_FIELD_DATE_VALUE(cls):
                return cls("custom_field.date_value")
            
            @schemas.classproperty
            def CUSTOM_FIELD_DATE_VALUE_DATE(cls):
                return cls("custom_field.date_value.date")
            
            @schemas.classproperty
            def CUSTOM_FIELD_DATE_VALUE_DATE_TIME(cls):
                return cls("custom_field.date_value.date_time")
            
            @schemas.classproperty
            def CUSTOM_FIELD_DISPLAY_VALUE(cls):
                return cls("custom_field.display_value")
            
            @schemas.classproperty
            def CUSTOM_FIELD_ENABLED(cls):
                return cls("custom_field.enabled")
            
            @schemas.classproperty
            def CUSTOM_FIELD_ENUM_OPTIONS(cls):
                return cls("custom_field.enum_options")
            
            @schemas.classproperty
            def CUSTOM_FIELD_ENUM_OPTIONS_COLOR(cls):
                return cls("custom_field.enum_options.color")
            
            @schemas.classproperty
            def CUSTOM_FIELD_ENUM_OPTIONS_ENABLED(cls):
                return cls("custom_field.enum_options.enabled")
            
            @schemas.classproperty
            def CUSTOM_FIELD_ENUM_OPTIONS_NAME(cls):
                return cls("custom_field.enum_options.name")
            
            @schemas.classproperty
            def CUSTOM_FIELD_ENUM_VALUE(cls):
                return cls("custom_field.enum_value")
            
            @schemas.classproperty
            def CUSTOM_FIELD_ENUM_VALUE_COLOR(cls):
                return cls("custom_field.enum_value.color")
            
            @schemas.classproperty
            def CUSTOM_FIELD_ENUM_VALUE_ENABLED(cls):
                return cls("custom_field.enum_value.enabled")
            
            @schemas.classproperty
            def CUSTOM_FIELD_ENUM_VALUE_NAME(cls):
                return cls("custom_field.enum_value.name")
            
            @schemas.classproperty
            def CUSTOM_FIELD_ID_PREFIX(cls):
                return cls("custom_field.id_prefix")
            
            @schemas.classproperty
            def CUSTOM_FIELD_IS_FORMULA_FIELD(cls):
                return cls("custom_field.is_formula_field")
            
            @schemas.classproperty
            def CUSTOM_FIELD_MULTI_ENUM_VALUES(cls):
                return cls("custom_field.multi_enum_values")
            
            @schemas.classproperty
            def CUSTOM_FIELD_MULTI_ENUM_VALUES_COLOR(cls):
                return cls("custom_field.multi_enum_values.color")
            
            @schemas.classproperty
            def CUSTOM_FIELD_MULTI_ENUM_VALUES_ENABLED(cls):
                return cls("custom_field.multi_enum_values.enabled")
            
            @schemas.classproperty
            def CUSTOM_FIELD_MULTI_ENUM_VALUES_NAME(cls):
                return cls("custom_field.multi_enum_values.name")
            
            @schemas.classproperty
            def CUSTOM_FIELD_NAME(cls):
                return cls("custom_field.name")
            
            @schemas.classproperty
            def CUSTOM_FIELD_NUMBER_VALUE(cls):
                return cls("custom_field.number_value")
            
            @schemas.classproperty
            def CUSTOM_FIELD_REPRESENTATION_TYPE(cls):
                return cls("custom_field.representation_type")
            
            @schemas.classproperty
            def CUSTOM_FIELD_RESOURCE_SUBTYPE(cls):
                return cls("custom_field.resource_subtype")
            
            @schemas.classproperty
            def CUSTOM_FIELD_TEXT_VALUE(cls):
                return cls("custom_field.text_value")
            
            @schemas.classproperty
            def CUSTOM_FIELD_TYPE(cls):
                return cls("custom_field.type")
            
            @schemas.classproperty
            def DEPENDENCY(cls):
                return cls("dependency")
            
            @schemas.classproperty
            def DEPENDENCY_CREATED_BY(cls):
                return cls("dependency.created_by")
            
            @schemas.classproperty
            def DEPENDENCY_NAME(cls):
                return cls("dependency.name")
            
            @schemas.classproperty
            def DEPENDENCY_RESOURCE_SUBTYPE(cls):
                return cls("dependency.resource_subtype")
            
            @schemas.classproperty
            def DUPLICATE_OF(cls):
                return cls("duplicate_of")
            
            @schemas.classproperty
            def DUPLICATE_OF_CREATED_BY(cls):
                return cls("duplicate_of.created_by")
            
            @schemas.classproperty
            def DUPLICATE_OF_NAME(cls):
                return cls("duplicate_of.name")
            
            @schemas.classproperty
            def DUPLICATE_OF_RESOURCE_SUBTYPE(cls):
                return cls("duplicate_of.resource_subtype")
            
            @schemas.classproperty
            def DUPLICATED_FROM(cls):
                return cls("duplicated_from")
            
            @schemas.classproperty
            def DUPLICATED_FROM_CREATED_BY(cls):
                return cls("duplicated_from.created_by")
            
            @schemas.classproperty
            def DUPLICATED_FROM_NAME(cls):
                return cls("duplicated_from.name")
            
            @schemas.classproperty
            def DUPLICATED_FROM_RESOURCE_SUBTYPE(cls):
                return cls("duplicated_from.resource_subtype")
            
            @schemas.classproperty
            def FOLLOWER(cls):
                return cls("follower")
            
            @schemas.classproperty
            def FOLLOWER_NAME(cls):
                return cls("follower.name")
            
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
            def HTML_TEXT(cls):
                return cls("html_text")
            
            @schemas.classproperty
            def IS_EDITABLE(cls):
                return cls("is_editable")
            
            @schemas.classproperty
            def IS_EDITED(cls):
                return cls("is_edited")
            
            @schemas.classproperty
            def IS_PINNED(cls):
                return cls("is_pinned")
            
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
            def NEW_APPROVAL_STATUS(cls):
                return cls("new_approval_status")
            
            @schemas.classproperty
            def NEW_DATE_VALUE(cls):
                return cls("new_date_value")
            
            @schemas.classproperty
            def NEW_DATES(cls):
                return cls("new_dates")
            
            @schemas.classproperty
            def NEW_DATES_DUE_AT(cls):
                return cls("new_dates.due_at")
            
            @schemas.classproperty
            def NEW_DATES_DUE_ON(cls):
                return cls("new_dates.due_on")
            
            @schemas.classproperty
            def NEW_DATES_START_ON(cls):
                return cls("new_dates.start_on")
            
            @schemas.classproperty
            def NEW_ENUM_VALUE(cls):
                return cls("new_enum_value")
            
            @schemas.classproperty
            def NEW_ENUM_VALUE_COLOR(cls):
                return cls("new_enum_value.color")
            
            @schemas.classproperty
            def NEW_ENUM_VALUE_ENABLED(cls):
                return cls("new_enum_value.enabled")
            
            @schemas.classproperty
            def NEW_ENUM_VALUE_NAME(cls):
                return cls("new_enum_value.name")
            
            @schemas.classproperty
            def NEW_MULTI_ENUM_VALUES(cls):
                return cls("new_multi_enum_values")
            
            @schemas.classproperty
            def NEW_MULTI_ENUM_VALUES_COLOR(cls):
                return cls("new_multi_enum_values.color")
            
            @schemas.classproperty
            def NEW_MULTI_ENUM_VALUES_ENABLED(cls):
                return cls("new_multi_enum_values.enabled")
            
            @schemas.classproperty
            def NEW_MULTI_ENUM_VALUES_NAME(cls):
                return cls("new_multi_enum_values.name")
            
            @schemas.classproperty
            def NEW_NAME(cls):
                return cls("new_name")
            
            @schemas.classproperty
            def NEW_NUMBER_VALUE(cls):
                return cls("new_number_value")
            
            @schemas.classproperty
            def NEW_PEOPLE_VALUE(cls):
                return cls("new_people_value")
            
            @schemas.classproperty
            def NEW_PEOPLE_VALUE_NAME(cls):
                return cls("new_people_value.name")
            
            @schemas.classproperty
            def NEW_RESOURCE_SUBTYPE(cls):
                return cls("new_resource_subtype")
            
            @schemas.classproperty
            def NEW_SECTION(cls):
                return cls("new_section")
            
            @schemas.classproperty
            def NEW_SECTION_NAME(cls):
                return cls("new_section.name")
            
            @schemas.classproperty
            def NEW_TEXT_VALUE(cls):
                return cls("new_text_value")
            
            @schemas.classproperty
            def NUM_HEARTS(cls):
                return cls("num_hearts")
            
            @schemas.classproperty
            def NUM_LIKES(cls):
                return cls("num_likes")
            
            @schemas.classproperty
            def OLD_APPROVAL_STATUS(cls):
                return cls("old_approval_status")
            
            @schemas.classproperty
            def OLD_DATE_VALUE(cls):
                return cls("old_date_value")
            
            @schemas.classproperty
            def OLD_DATES(cls):
                return cls("old_dates")
            
            @schemas.classproperty
            def OLD_DATES_DUE_AT(cls):
                return cls("old_dates.due_at")
            
            @schemas.classproperty
            def OLD_DATES_DUE_ON(cls):
                return cls("old_dates.due_on")
            
            @schemas.classproperty
            def OLD_DATES_START_ON(cls):
                return cls("old_dates.start_on")
            
            @schemas.classproperty
            def OLD_ENUM_VALUE(cls):
                return cls("old_enum_value")
            
            @schemas.classproperty
            def OLD_ENUM_VALUE_COLOR(cls):
                return cls("old_enum_value.color")
            
            @schemas.classproperty
            def OLD_ENUM_VALUE_ENABLED(cls):
                return cls("old_enum_value.enabled")
            
            @schemas.classproperty
            def OLD_ENUM_VALUE_NAME(cls):
                return cls("old_enum_value.name")
            
            @schemas.classproperty
            def OLD_MULTI_ENUM_VALUES(cls):
                return cls("old_multi_enum_values")
            
            @schemas.classproperty
            def OLD_MULTI_ENUM_VALUES_COLOR(cls):
                return cls("old_multi_enum_values.color")
            
            @schemas.classproperty
            def OLD_MULTI_ENUM_VALUES_ENABLED(cls):
                return cls("old_multi_enum_values.enabled")
            
            @schemas.classproperty
            def OLD_MULTI_ENUM_VALUES_NAME(cls):
                return cls("old_multi_enum_values.name")
            
            @schemas.classproperty
            def OLD_NAME(cls):
                return cls("old_name")
            
            @schemas.classproperty
            def OLD_NUMBER_VALUE(cls):
                return cls("old_number_value")
            
            @schemas.classproperty
            def OLD_PEOPLE_VALUE(cls):
                return cls("old_people_value")
            
            @schemas.classproperty
            def OLD_PEOPLE_VALUE_NAME(cls):
                return cls("old_people_value.name")
            
            @schemas.classproperty
            def OLD_RESOURCE_SUBTYPE(cls):
                return cls("old_resource_subtype")
            
            @schemas.classproperty
            def OLD_SECTION(cls):
                return cls("old_section")
            
            @schemas.classproperty
            def OLD_SECTION_NAME(cls):
                return cls("old_section.name")
            
            @schemas.classproperty
            def OLD_TEXT_VALUE(cls):
                return cls("old_text_value")
            
            @schemas.classproperty
            def PREVIEWS(cls):
                return cls("previews")
            
            @schemas.classproperty
            def PREVIEWS_FALLBACK(cls):
                return cls("previews.fallback")
            
            @schemas.classproperty
            def PREVIEWS_FOOTER(cls):
                return cls("previews.footer")
            
            @schemas.classproperty
            def PREVIEWS_HEADER(cls):
                return cls("previews.header")
            
            @schemas.classproperty
            def PREVIEWS_HEADER_LINK(cls):
                return cls("previews.header_link")
            
            @schemas.classproperty
            def PREVIEWS_HTML_TEXT(cls):
                return cls("previews.html_text")
            
            @schemas.classproperty
            def PREVIEWS_TEXT(cls):
                return cls("previews.text")
            
            @schemas.classproperty
            def PREVIEWS_TITLE(cls):
                return cls("previews.title")
            
            @schemas.classproperty
            def PREVIEWS_TITLE_LINK(cls):
                return cls("previews.title_link")
            
            @schemas.classproperty
            def PROJECT(cls):
                return cls("project")
            
            @schemas.classproperty
            def PROJECT_NAME(cls):
                return cls("project.name")
            
            @schemas.classproperty
            def RESOURCE_SUBTYPE(cls):
                return cls("resource_subtype")
            
            @schemas.classproperty
            def SOURCE(cls):
                return cls("source")
            
            @schemas.classproperty
            def STICKER_NAME(cls):
                return cls("sticker_name")
            
            @schemas.classproperty
            def STORY(cls):
                return cls("story")
            
            @schemas.classproperty
            def STORY_CREATED_AT(cls):
                return cls("story.created_at")
            
            @schemas.classproperty
            def STORY_CREATED_BY(cls):
                return cls("story.created_by")
            
            @schemas.classproperty
            def STORY_CREATED_BY_NAME(cls):
                return cls("story.created_by.name")
            
            @schemas.classproperty
            def STORY_RESOURCE_SUBTYPE(cls):
                return cls("story.resource_subtype")
            
            @schemas.classproperty
            def STORY_TEXT(cls):
                return cls("story.text")
            
            @schemas.classproperty
            def TAG(cls):
                return cls("tag")
            
            @schemas.classproperty
            def TAG_NAME(cls):
                return cls("tag.name")
            
            @schemas.classproperty
            def TARGET(cls):
                return cls("target")
            
            @schemas.classproperty
            def TARGET_CREATED_BY(cls):
                return cls("target.created_by")
            
            @schemas.classproperty
            def TARGET_NAME(cls):
                return cls("target.name")
            
            @schemas.classproperty
            def TARGET_RESOURCE_SUBTYPE(cls):
                return cls("target.resource_subtype")
            
            @schemas.classproperty
            def TASK(cls):
                return cls("task")
            
            @schemas.classproperty
            def TASK_CREATED_BY(cls):
                return cls("task.created_by")
            
            @schemas.classproperty
            def TASK_NAME(cls):
                return cls("task.name")
            
            @schemas.classproperty
            def TASK_RESOURCE_SUBTYPE(cls):
                return cls("task.resource_subtype")
            
            @schemas.classproperty
            def TEXT(cls):
                return cls("text")
            
            @schemas.classproperty
            def TYPE(cls):
                return cls("type")

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
request_query_opt_fields = api_client.QueryParameter(
    name="opt_fields",
    style=api_client.ParameterStyle.FORM,
    schema=OptFieldsSchema,
)
# Path params
StoryGidSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'story_gid': typing.Union[StoryGidSchema, str, ],
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


request_path_story_gid = api_client.PathParameter(
    name="story_gid",
    style=api_client.ParameterStyle.SIMPLE,
    schema=StoryGidSchema,
    required=True,
)
_auth = [
    'oauth2',
    'personalAccessToken',
]
SchemaFor200ResponseBodyApplicationJson = StoriesGetFullRecordResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: StoriesGetFullRecordResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: StoriesGetFullRecordResponse


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
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
    '401': _response_for_401,
    '403': _response_for_403,
    '404': _response_for_404,
    '500': _response_for_500,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _get_full_record_mapped_args(
        self,
        story_gid: str,
        opt_pretty: typing.Optional[bool] = None,
        opt_fields: typing.Optional[typing.List[str]] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _path_params = {}
        if opt_pretty is not None:
            _query_params["opt_pretty"] = opt_pretty
        if opt_fields is not None:
            _query_params["opt_fields"] = opt_fields
        if story_gid is not None:
            _path_params["story_gid"] = story_gid
        args.query = _query_params
        args.path = _path_params
        return args

    async def _aget_full_record_oapg(
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
        Get a story
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_story_gid,
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
            path_template='/stories/{story_gid}',
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


    def _get_full_record_oapg(
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
        Get a story
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_story_gid,
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
            path_template='/stories/{story_gid}',
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


class GetFullRecordRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_full_record(
        self,
        story_gid: str,
        opt_pretty: typing.Optional[bool] = None,
        opt_fields: typing.Optional[typing.List[str]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_full_record_mapped_args(
            story_gid=story_gid,
            opt_pretty=opt_pretty,
            opt_fields=opt_fields,
        )
        return await self._aget_full_record_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get_full_record(
        self,
        story_gid: str,
        opt_pretty: typing.Optional[bool] = None,
        opt_fields: typing.Optional[typing.List[str]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_full_record_mapped_args(
            story_gid=story_gid,
            opt_pretty=opt_pretty,
            opt_fields=opt_fields,
        )
        return self._get_full_record_oapg(
            query_params=args.query,
            path_params=args.path,
        )

class GetFullRecord(BaseApi):

    async def aget_full_record(
        self,
        story_gid: str,
        opt_pretty: typing.Optional[bool] = None,
        opt_fields: typing.Optional[typing.List[str]] = None,
        validate: bool = False,
        **kwargs,
    ) -> StoriesGetFullRecordResponsePydantic:
        raw_response = await self.raw.aget_full_record(
            story_gid=story_gid,
            opt_pretty=opt_pretty,
            opt_fields=opt_fields,
            **kwargs,
        )
        if validate:
            return StoriesGetFullRecordResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(StoriesGetFullRecordResponsePydantic, raw_response.body)
    
    
    def get_full_record(
        self,
        story_gid: str,
        opt_pretty: typing.Optional[bool] = None,
        opt_fields: typing.Optional[typing.List[str]] = None,
        validate: bool = False,
    ) -> StoriesGetFullRecordResponsePydantic:
        raw_response = self.raw.get_full_record(
            story_gid=story_gid,
            opt_pretty=opt_pretty,
            opt_fields=opt_fields,
        )
        if validate:
            return StoriesGetFullRecordResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(StoriesGetFullRecordResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        story_gid: str,
        opt_pretty: typing.Optional[bool] = None,
        opt_fields: typing.Optional[typing.List[str]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_full_record_mapped_args(
            story_gid=story_gid,
            opt_pretty=opt_pretty,
            opt_fields=opt_fields,
        )
        return await self._aget_full_record_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        story_gid: str,
        opt_pretty: typing.Optional[bool] = None,
        opt_fields: typing.Optional[typing.List[str]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_full_record_mapped_args(
            story_gid=story_gid,
            opt_pretty=opt_pretty,
            opt_fields=opt_fields,
        )
        return self._get_full_record_oapg(
            query_params=args.query,
            path_params=args.path,
        )

