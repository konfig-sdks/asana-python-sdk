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

from asana_python_sdk.model.tasks_get_user_task_list_tasks_response import TasksGetUserTaskListTasksResponse as TasksGetUserTaskListTasksResponseSchema
from asana_python_sdk.model.error_response import ErrorResponse as ErrorResponseSchema

from asana_python_sdk.type.tasks_get_user_task_list_tasks_response import TasksGetUserTaskListTasksResponse
from asana_python_sdk.type.error_response import ErrorResponse

from ...api_client import Dictionary
from asana_python_sdk.pydantic.tasks_get_user_task_list_tasks_response import TasksGetUserTaskListTasksResponse as TasksGetUserTaskListTasksResponsePydantic
from asana_python_sdk.pydantic.error_response import ErrorResponse as ErrorResponsePydantic

# Query params
CompletedSinceSchema = schemas.StrSchema
OptPrettySchema = schemas.BoolSchema


class LimitSchema(
    schemas.IntSchema
):
    pass
OffsetSchema = schemas.StrSchema


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
            def OFFSET(cls):
                return cls("offset")
            
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
            def PATH(cls):
                return cls("path")
            
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
            def URI(cls):
                return cls("uri")
            
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
        'completed_since': typing.Union[CompletedSinceSchema, str, ],
        'opt_pretty': typing.Union[OptPrettySchema, bool, ],
        'limit': typing.Union[LimitSchema, decimal.Decimal, int, ],
        'offset': typing.Union[OffsetSchema, str, ],
        'opt_fields': typing.Union[OptFieldsSchema, list, tuple, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_completed_since = api_client.QueryParameter(
    name="completed_since",
    style=api_client.ParameterStyle.FORM,
    schema=CompletedSinceSchema,
    explode=True,
)
request_query_opt_pretty = api_client.QueryParameter(
    name="opt_pretty",
    style=api_client.ParameterStyle.FORM,
    schema=OptPrettySchema,
    explode=True,
)
request_query_limit = api_client.QueryParameter(
    name="limit",
    style=api_client.ParameterStyle.FORM,
    schema=LimitSchema,
    explode=True,
)
request_query_offset = api_client.QueryParameter(
    name="offset",
    style=api_client.ParameterStyle.FORM,
    schema=OffsetSchema,
    explode=True,
)
request_query_opt_fields = api_client.QueryParameter(
    name="opt_fields",
    style=api_client.ParameterStyle.FORM,
    schema=OptFieldsSchema,
)
# Path params
UserTaskListGidSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'user_task_list_gid': typing.Union[UserTaskListGidSchema, str, ],
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


request_path_user_task_list_gid = api_client.PathParameter(
    name="user_task_list_gid",
    style=api_client.ParameterStyle.SIMPLE,
    schema=UserTaskListGidSchema,
    required=True,
)
SchemaFor200ResponseBodyApplicationJson = TasksGetUserTaskListTasksResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: TasksGetUserTaskListTasksResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: TasksGetUserTaskListTasksResponse


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

    def _get_user_task_list_tasks_mapped_args(
        self,
        user_task_list_gid: str,
        completed_since: typing.Optional[str] = None,
        opt_pretty: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[str] = None,
        opt_fields: typing.Optional[typing.List[str]] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _path_params = {}
        if completed_since is not None:
            _query_params["completed_since"] = completed_since
        if opt_pretty is not None:
            _query_params["opt_pretty"] = opt_pretty
        if limit is not None:
            _query_params["limit"] = limit
        if offset is not None:
            _query_params["offset"] = offset
        if opt_fields is not None:
            _query_params["opt_fields"] = opt_fields
        if user_task_list_gid is not None:
            _path_params["user_task_list_gid"] = user_task_list_gid
        args.query = _query_params
        args.path = _path_params
        return args

    async def _aget_user_task_list_tasks_oapg(
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
        Get tasks from a user task list
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_user_task_list_gid,
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
            request_query_completed_since,
            request_query_opt_pretty,
            request_query_limit,
            request_query_offset,
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
            path_template='/user_task_lists/{user_task_list_gid}/tasks',
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


    def _get_user_task_list_tasks_oapg(
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
        Get tasks from a user task list
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_user_task_list_gid,
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
            request_query_completed_since,
            request_query_opt_pretty,
            request_query_limit,
            request_query_offset,
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
            path_template='/user_task_lists/{user_task_list_gid}/tasks',
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


class GetUserTaskListTasksRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_user_task_list_tasks(
        self,
        user_task_list_gid: str,
        completed_since: typing.Optional[str] = None,
        opt_pretty: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[str] = None,
        opt_fields: typing.Optional[typing.List[str]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_user_task_list_tasks_mapped_args(
            user_task_list_gid=user_task_list_gid,
            completed_since=completed_since,
            opt_pretty=opt_pretty,
            limit=limit,
            offset=offset,
            opt_fields=opt_fields,
        )
        return await self._aget_user_task_list_tasks_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get_user_task_list_tasks(
        self,
        user_task_list_gid: str,
        completed_since: typing.Optional[str] = None,
        opt_pretty: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[str] = None,
        opt_fields: typing.Optional[typing.List[str]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_user_task_list_tasks_mapped_args(
            user_task_list_gid=user_task_list_gid,
            completed_since=completed_since,
            opt_pretty=opt_pretty,
            limit=limit,
            offset=offset,
            opt_fields=opt_fields,
        )
        return self._get_user_task_list_tasks_oapg(
            query_params=args.query,
            path_params=args.path,
        )

class GetUserTaskListTasks(BaseApi):

    async def aget_user_task_list_tasks(
        self,
        user_task_list_gid: str,
        completed_since: typing.Optional[str] = None,
        opt_pretty: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[str] = None,
        opt_fields: typing.Optional[typing.List[str]] = None,
        validate: bool = False,
        **kwargs,
    ) -> TasksGetUserTaskListTasksResponsePydantic:
        raw_response = await self.raw.aget_user_task_list_tasks(
            user_task_list_gid=user_task_list_gid,
            completed_since=completed_since,
            opt_pretty=opt_pretty,
            limit=limit,
            offset=offset,
            opt_fields=opt_fields,
            **kwargs,
        )
        if validate:
            return TasksGetUserTaskListTasksResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(TasksGetUserTaskListTasksResponsePydantic, raw_response.body)
    
    
    def get_user_task_list_tasks(
        self,
        user_task_list_gid: str,
        completed_since: typing.Optional[str] = None,
        opt_pretty: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[str] = None,
        opt_fields: typing.Optional[typing.List[str]] = None,
        validate: bool = False,
    ) -> TasksGetUserTaskListTasksResponsePydantic:
        raw_response = self.raw.get_user_task_list_tasks(
            user_task_list_gid=user_task_list_gid,
            completed_since=completed_since,
            opt_pretty=opt_pretty,
            limit=limit,
            offset=offset,
            opt_fields=opt_fields,
        )
        if validate:
            return TasksGetUserTaskListTasksResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(TasksGetUserTaskListTasksResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        user_task_list_gid: str,
        completed_since: typing.Optional[str] = None,
        opt_pretty: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[str] = None,
        opt_fields: typing.Optional[typing.List[str]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_user_task_list_tasks_mapped_args(
            user_task_list_gid=user_task_list_gid,
            completed_since=completed_since,
            opt_pretty=opt_pretty,
            limit=limit,
            offset=offset,
            opt_fields=opt_fields,
        )
        return await self._aget_user_task_list_tasks_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        user_task_list_gid: str,
        completed_since: typing.Optional[str] = None,
        opt_pretty: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[str] = None,
        opt_fields: typing.Optional[typing.List[str]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_user_task_list_tasks_mapped_args(
            user_task_list_gid=user_task_list_gid,
            completed_since=completed_since,
            opt_pretty=opt_pretty,
            limit=limit,
            offset=offset,
            opt_fields=opt_fields,
        )
        return self._get_user_task_list_tasks_oapg(
            query_params=args.query,
            path_params=args.path,
        )

