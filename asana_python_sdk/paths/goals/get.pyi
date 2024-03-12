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

from asana_python_sdk.model.goals_get_compact_records_response import GoalsGetCompactRecordsResponse as GoalsGetCompactRecordsResponseSchema
from asana_python_sdk.model.error_response import ErrorResponse as ErrorResponseSchema

from asana_python_sdk.type.goals_get_compact_records_response import GoalsGetCompactRecordsResponse
from asana_python_sdk.type.error_response import ErrorResponse

from ...api_client import Dictionary
from asana_python_sdk.pydantic.error_response import ErrorResponse as ErrorResponsePydantic
from asana_python_sdk.pydantic.goals_get_compact_records_response import GoalsGetCompactRecordsResponse as GoalsGetCompactRecordsResponsePydantic

# Query params
OptPrettySchema = schemas.BoolSchema
PortfolioSchema = schemas.StrSchema
ProjectSchema = schemas.StrSchema
TaskSchema = schemas.StrSchema
IsWorkspaceLevelSchema = schemas.BoolSchema
TeamSchema = schemas.StrSchema
WorkspaceSchema = schemas.StrSchema


class TimePeriodsSchema(
    schemas.ListSchema
):


    class MetaOapg:
        items = schemas.StrSchema

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'TimePeriodsSchema':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)


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
            def CURRENT_STATUS_UPDATE(cls):
                return cls("current_status_update")
            
            @schemas.classproperty
            def CURRENT_STATUS_UPDATE_RESOURCE_SUBTYPE(cls):
                return cls("current_status_update.resource_subtype")
            
            @schemas.classproperty
            def CURRENT_STATUS_UPDATE_TITLE(cls):
                return cls("current_status_update.title")
            
            @schemas.classproperty
            def DUE_ON(cls):
                return cls("due_on")
            
            @schemas.classproperty
            def FOLLOWERS(cls):
                return cls("followers")
            
            @schemas.classproperty
            def FOLLOWERS_NAME(cls):
                return cls("followers.name")
            
            @schemas.classproperty
            def HTML_NOTES(cls):
                return cls("html_notes")
            
            @schemas.classproperty
            def IS_WORKSPACE_LEVEL(cls):
                return cls("is_workspace_level")
            
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
            def METRIC(cls):
                return cls("metric")
            
            @schemas.classproperty
            def METRIC_CAN_MANAGE(cls):
                return cls("metric.can_manage")
            
            @schemas.classproperty
            def METRIC_CURRENCY_CODE(cls):
                return cls("metric.currency_code")
            
            @schemas.classproperty
            def METRIC_CURRENT_DISPLAY_VALUE(cls):
                return cls("metric.current_display_value")
            
            @schemas.classproperty
            def METRIC_CURRENT_NUMBER_VALUE(cls):
                return cls("metric.current_number_value")
            
            @schemas.classproperty
            def METRIC_INITIAL_NUMBER_VALUE(cls):
                return cls("metric.initial_number_value")
            
            @schemas.classproperty
            def METRIC_PRECISION(cls):
                return cls("metric.precision")
            
            @schemas.classproperty
            def METRIC_PROGRESS_SOURCE(cls):
                return cls("metric.progress_source")
            
            @schemas.classproperty
            def METRIC_RESOURCE_SUBTYPE(cls):
                return cls("metric.resource_subtype")
            
            @schemas.classproperty
            def METRIC_TARGET_NUMBER_VALUE(cls):
                return cls("metric.target_number_value")
            
            @schemas.classproperty
            def METRIC_UNIT(cls):
                return cls("metric.unit")
            
            @schemas.classproperty
            def NAME(cls):
                return cls("name")
            
            @schemas.classproperty
            def NOTES(cls):
                return cls("notes")
            
            @schemas.classproperty
            def NUM_LIKES(cls):
                return cls("num_likes")
            
            @schemas.classproperty
            def OFFSET(cls):
                return cls("offset")
            
            @schemas.classproperty
            def OWNER(cls):
                return cls("owner")
            
            @schemas.classproperty
            def OWNER_NAME(cls):
                return cls("owner.name")
            
            @schemas.classproperty
            def PATH(cls):
                return cls("path")
            
            @schemas.classproperty
            def START_ON(cls):
                return cls("start_on")
            
            @schemas.classproperty
            def STATUS(cls):
                return cls("status")
            
            @schemas.classproperty
            def TEAM(cls):
                return cls("team")
            
            @schemas.classproperty
            def TEAM_NAME(cls):
                return cls("team.name")
            
            @schemas.classproperty
            def TIME_PERIOD(cls):
                return cls("time_period")
            
            @schemas.classproperty
            def TIME_PERIOD_DISPLAY_NAME(cls):
                return cls("time_period.display_name")
            
            @schemas.classproperty
            def TIME_PERIOD_END_ON(cls):
                return cls("time_period.end_on")
            
            @schemas.classproperty
            def TIME_PERIOD_PERIOD(cls):
                return cls("time_period.period")
            
            @schemas.classproperty
            def TIME_PERIOD_START_ON(cls):
                return cls("time_period.start_on")
            
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
        'opt_pretty': typing.Union[OptPrettySchema, bool, ],
        'portfolio': typing.Union[PortfolioSchema, str, ],
        'project': typing.Union[ProjectSchema, str, ],
        'task': typing.Union[TaskSchema, str, ],
        'is_workspace_level': typing.Union[IsWorkspaceLevelSchema, bool, ],
        'team': typing.Union[TeamSchema, str, ],
        'workspace': typing.Union[WorkspaceSchema, str, ],
        'time_periods': typing.Union[TimePeriodsSchema, list, tuple, ],
        'limit': typing.Union[LimitSchema, decimal.Decimal, int, ],
        'offset': typing.Union[OffsetSchema, str, ],
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
request_query_portfolio = api_client.QueryParameter(
    name="portfolio",
    style=api_client.ParameterStyle.FORM,
    schema=PortfolioSchema,
    explode=True,
)
request_query_project = api_client.QueryParameter(
    name="project",
    style=api_client.ParameterStyle.FORM,
    schema=ProjectSchema,
    explode=True,
)
request_query_task = api_client.QueryParameter(
    name="task",
    style=api_client.ParameterStyle.FORM,
    schema=TaskSchema,
    explode=True,
)
request_query_is_workspace_level = api_client.QueryParameter(
    name="is_workspace_level",
    style=api_client.ParameterStyle.FORM,
    schema=IsWorkspaceLevelSchema,
    explode=True,
)
request_query_team = api_client.QueryParameter(
    name="team",
    style=api_client.ParameterStyle.FORM,
    schema=TeamSchema,
    explode=True,
)
request_query_workspace = api_client.QueryParameter(
    name="workspace",
    style=api_client.ParameterStyle.FORM,
    schema=WorkspaceSchema,
    explode=True,
)
request_query_time_periods = api_client.QueryParameter(
    name="time_periods",
    style=api_client.ParameterStyle.FORM,
    schema=TimePeriodsSchema,
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
SchemaFor200ResponseBodyApplicationJson = GoalsGetCompactRecordsResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: GoalsGetCompactRecordsResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: GoalsGetCompactRecordsResponse


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
SchemaFor402ResponseBodyApplicationJson = ErrorResponseSchema


@dataclass
class ApiResponseFor402(api_client.ApiResponse):
    body: ErrorResponse


@dataclass
class ApiResponseFor402Async(api_client.AsyncApiResponse):
    body: ErrorResponse


_response_for_402 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor402,
    response_cls_async=ApiResponseFor402Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor402ResponseBodyApplicationJson),
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

    def _get_compact_records_mapped_args(
        self,
        opt_pretty: typing.Optional[bool] = None,
        portfolio: typing.Optional[str] = None,
        project: typing.Optional[str] = None,
        task: typing.Optional[str] = None,
        is_workspace_level: typing.Optional[bool] = None,
        team: typing.Optional[str] = None,
        workspace: typing.Optional[str] = None,
        time_periods: typing.Optional[typing.List[str]] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[str] = None,
        opt_fields: typing.Optional[typing.List[str]] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if opt_pretty is not None:
            _query_params["opt_pretty"] = opt_pretty
        if portfolio is not None:
            _query_params["portfolio"] = portfolio
        if project is not None:
            _query_params["project"] = project
        if task is not None:
            _query_params["task"] = task
        if is_workspace_level is not None:
            _query_params["is_workspace_level"] = is_workspace_level
        if team is not None:
            _query_params["team"] = team
        if workspace is not None:
            _query_params["workspace"] = workspace
        if time_periods is not None:
            _query_params["time_periods"] = time_periods
        if limit is not None:
            _query_params["limit"] = limit
        if offset is not None:
            _query_params["offset"] = offset
        if opt_fields is not None:
            _query_params["opt_fields"] = opt_fields
        args.query = _query_params
        return args

    async def _aget_compact_records_oapg(
        self,
            query_params: typing.Optional[dict] = {},
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
        Get goals
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_opt_pretty,
            request_query_portfolio,
            request_query_project,
            request_query_task,
            request_query_is_workspace_level,
            request_query_team,
            request_query_workspace,
            request_query_time_periods,
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
            path_template='/goals',
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


    def _get_compact_records_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Get goals
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_opt_pretty,
            request_query_portfolio,
            request_query_project,
            request_query_task,
            request_query_is_workspace_level,
            request_query_team,
            request_query_workspace,
            request_query_time_periods,
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
            path_template='/goals',
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


class GetCompactRecordsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_compact_records(
        self,
        opt_pretty: typing.Optional[bool] = None,
        portfolio: typing.Optional[str] = None,
        project: typing.Optional[str] = None,
        task: typing.Optional[str] = None,
        is_workspace_level: typing.Optional[bool] = None,
        team: typing.Optional[str] = None,
        workspace: typing.Optional[str] = None,
        time_periods: typing.Optional[typing.List[str]] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[str] = None,
        opt_fields: typing.Optional[typing.List[str]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_compact_records_mapped_args(
            opt_pretty=opt_pretty,
            portfolio=portfolio,
            project=project,
            task=task,
            is_workspace_level=is_workspace_level,
            team=team,
            workspace=workspace,
            time_periods=time_periods,
            limit=limit,
            offset=offset,
            opt_fields=opt_fields,
        )
        return await self._aget_compact_records_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get_compact_records(
        self,
        opt_pretty: typing.Optional[bool] = None,
        portfolio: typing.Optional[str] = None,
        project: typing.Optional[str] = None,
        task: typing.Optional[str] = None,
        is_workspace_level: typing.Optional[bool] = None,
        team: typing.Optional[str] = None,
        workspace: typing.Optional[str] = None,
        time_periods: typing.Optional[typing.List[str]] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[str] = None,
        opt_fields: typing.Optional[typing.List[str]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_compact_records_mapped_args(
            opt_pretty=opt_pretty,
            portfolio=portfolio,
            project=project,
            task=task,
            is_workspace_level=is_workspace_level,
            team=team,
            workspace=workspace,
            time_periods=time_periods,
            limit=limit,
            offset=offset,
            opt_fields=opt_fields,
        )
        return self._get_compact_records_oapg(
            query_params=args.query,
        )

class GetCompactRecords(BaseApi):

    async def aget_compact_records(
        self,
        opt_pretty: typing.Optional[bool] = None,
        portfolio: typing.Optional[str] = None,
        project: typing.Optional[str] = None,
        task: typing.Optional[str] = None,
        is_workspace_level: typing.Optional[bool] = None,
        team: typing.Optional[str] = None,
        workspace: typing.Optional[str] = None,
        time_periods: typing.Optional[typing.List[str]] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[str] = None,
        opt_fields: typing.Optional[typing.List[str]] = None,
        validate: bool = False,
        **kwargs,
    ) -> GoalsGetCompactRecordsResponsePydantic:
        raw_response = await self.raw.aget_compact_records(
            opt_pretty=opt_pretty,
            portfolio=portfolio,
            project=project,
            task=task,
            is_workspace_level=is_workspace_level,
            team=team,
            workspace=workspace,
            time_periods=time_periods,
            limit=limit,
            offset=offset,
            opt_fields=opt_fields,
            **kwargs,
        )
        if validate:
            return GoalsGetCompactRecordsResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(GoalsGetCompactRecordsResponsePydantic, raw_response.body)
    
    
    def get_compact_records(
        self,
        opt_pretty: typing.Optional[bool] = None,
        portfolio: typing.Optional[str] = None,
        project: typing.Optional[str] = None,
        task: typing.Optional[str] = None,
        is_workspace_level: typing.Optional[bool] = None,
        team: typing.Optional[str] = None,
        workspace: typing.Optional[str] = None,
        time_periods: typing.Optional[typing.List[str]] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[str] = None,
        opt_fields: typing.Optional[typing.List[str]] = None,
        validate: bool = False,
    ) -> GoalsGetCompactRecordsResponsePydantic:
        raw_response = self.raw.get_compact_records(
            opt_pretty=opt_pretty,
            portfolio=portfolio,
            project=project,
            task=task,
            is_workspace_level=is_workspace_level,
            team=team,
            workspace=workspace,
            time_periods=time_periods,
            limit=limit,
            offset=offset,
            opt_fields=opt_fields,
        )
        if validate:
            return GoalsGetCompactRecordsResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(GoalsGetCompactRecordsResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        opt_pretty: typing.Optional[bool] = None,
        portfolio: typing.Optional[str] = None,
        project: typing.Optional[str] = None,
        task: typing.Optional[str] = None,
        is_workspace_level: typing.Optional[bool] = None,
        team: typing.Optional[str] = None,
        workspace: typing.Optional[str] = None,
        time_periods: typing.Optional[typing.List[str]] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[str] = None,
        opt_fields: typing.Optional[typing.List[str]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_compact_records_mapped_args(
            opt_pretty=opt_pretty,
            portfolio=portfolio,
            project=project,
            task=task,
            is_workspace_level=is_workspace_level,
            team=team,
            workspace=workspace,
            time_periods=time_periods,
            limit=limit,
            offset=offset,
            opt_fields=opt_fields,
        )
        return await self._aget_compact_records_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        opt_pretty: typing.Optional[bool] = None,
        portfolio: typing.Optional[str] = None,
        project: typing.Optional[str] = None,
        task: typing.Optional[str] = None,
        is_workspace_level: typing.Optional[bool] = None,
        team: typing.Optional[str] = None,
        workspace: typing.Optional[str] = None,
        time_periods: typing.Optional[typing.List[str]] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[str] = None,
        opt_fields: typing.Optional[typing.List[str]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_compact_records_mapped_args(
            opt_pretty=opt_pretty,
            portfolio=portfolio,
            project=project,
            task=task,
            is_workspace_level=is_workspace_level,
            team=team,
            workspace=workspace,
            time_periods=time_periods,
            limit=limit,
            offset=offset,
            opt_fields=opt_fields,
        )
        return self._get_compact_records_oapg(
            query_params=args.query,
        )

