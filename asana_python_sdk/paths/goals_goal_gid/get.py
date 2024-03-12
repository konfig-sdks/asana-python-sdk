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

from asana_python_sdk.model.goals_get_goal_record_response import GoalsGetGoalRecordResponse as GoalsGetGoalRecordResponseSchema
from asana_python_sdk.model.error_response import ErrorResponse as ErrorResponseSchema

from asana_python_sdk.type.goals_get_goal_record_response import GoalsGetGoalRecordResponse
from asana_python_sdk.type.error_response import ErrorResponse

from ...api_client import Dictionary
from asana_python_sdk.pydantic.error_response import ErrorResponse as ErrorResponsePydantic
from asana_python_sdk.pydantic.goals_get_goal_record_response import GoalsGetGoalRecordResponse as GoalsGetGoalRecordResponsePydantic

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
                    "current_status_update": "CURRENT_STATUS_UPDATE",
                    "current_status_update.resource_subtype": "CURRENT_STATUS_UPDATE_RESOURCE_SUBTYPE",
                    "current_status_update.title": "CURRENT_STATUS_UPDATE_TITLE",
                    "due_on": "DUE_ON",
                    "followers": "FOLLOWERS",
                    "followers.name": "FOLLOWERS_NAME",
                    "html_notes": "HTML_NOTES",
                    "is_workspace_level": "IS_WORKSPACE_LEVEL",
                    "liked": "LIKED",
                    "likes": "LIKES",
                    "likes.user": "LIKES_USER",
                    "likes.user.name": "LIKES_USER_NAME",
                    "metric": "METRIC",
                    "metric.can_manage": "METRIC_CAN_MANAGE",
                    "metric.currency_code": "METRIC_CURRENCY_CODE",
                    "metric.current_display_value": "METRIC_CURRENT_DISPLAY_VALUE",
                    "metric.current_number_value": "METRIC_CURRENT_NUMBER_VALUE",
                    "metric.initial_number_value": "METRIC_INITIAL_NUMBER_VALUE",
                    "metric.precision": "METRIC_PRECISION",
                    "metric.progress_source": "METRIC_PROGRESS_SOURCE",
                    "metric.resource_subtype": "METRIC_RESOURCE_SUBTYPE",
                    "metric.target_number_value": "METRIC_TARGET_NUMBER_VALUE",
                    "metric.unit": "METRIC_UNIT",
                    "name": "NAME",
                    "notes": "NOTES",
                    "num_likes": "NUM_LIKES",
                    "owner": "OWNER",
                    "owner.name": "OWNER_NAME",
                    "start_on": "START_ON",
                    "status": "STATUS",
                    "team": "TEAM",
                    "team.name": "TEAM_NAME",
                    "time_period": "TIME_PERIOD",
                    "time_period.display_name": "TIME_PERIOD_DISPLAY_NAME",
                    "time_period.end_on": "TIME_PERIOD_END_ON",
                    "time_period.period": "TIME_PERIOD_PERIOD",
                    "time_period.start_on": "TIME_PERIOD_START_ON",
                    "workspace": "WORKSPACE",
                    "workspace.name": "WORKSPACE_NAME",
                }
            
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
            def OWNER(cls):
                return cls("owner")
            
            @schemas.classproperty
            def OWNER_NAME(cls):
                return cls("owner.name")
            
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
GoalGidSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'goal_gid': typing.Union[GoalGidSchema, str, ],
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


request_path_goal_gid = api_client.PathParameter(
    name="goal_gid",
    style=api_client.ParameterStyle.SIMPLE,
    schema=GoalGidSchema,
    required=True,
)
_auth = [
    'oauth2',
    'personalAccessToken',
]
SchemaFor200ResponseBodyApplicationJson = GoalsGetGoalRecordResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: GoalsGetGoalRecordResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: GoalsGetGoalRecordResponse


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
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
    '401': _response_for_401,
    '402': _response_for_402,
    '403': _response_for_403,
    '404': _response_for_404,
    '500': _response_for_500,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _get_goal_record_mapped_args(
        self,
        goal_gid: str,
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
        if goal_gid is not None:
            _path_params["goal_gid"] = goal_gid
        args.query = _query_params
        args.path = _path_params
        return args

    async def _aget_goal_record_oapg(
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
        Get a goal
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_goal_gid,
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
            path_template='/goals/{goal_gid}',
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


    def _get_goal_record_oapg(
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
        Get a goal
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_goal_gid,
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
            path_template='/goals/{goal_gid}',
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


class GetGoalRecordRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_goal_record(
        self,
        goal_gid: str,
        opt_pretty: typing.Optional[bool] = None,
        opt_fields: typing.Optional[typing.List[str]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_goal_record_mapped_args(
            goal_gid=goal_gid,
            opt_pretty=opt_pretty,
            opt_fields=opt_fields,
        )
        return await self._aget_goal_record_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get_goal_record(
        self,
        goal_gid: str,
        opt_pretty: typing.Optional[bool] = None,
        opt_fields: typing.Optional[typing.List[str]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_goal_record_mapped_args(
            goal_gid=goal_gid,
            opt_pretty=opt_pretty,
            opt_fields=opt_fields,
        )
        return self._get_goal_record_oapg(
            query_params=args.query,
            path_params=args.path,
        )

class GetGoalRecord(BaseApi):

    async def aget_goal_record(
        self,
        goal_gid: str,
        opt_pretty: typing.Optional[bool] = None,
        opt_fields: typing.Optional[typing.List[str]] = None,
        validate: bool = False,
        **kwargs,
    ) -> GoalsGetGoalRecordResponsePydantic:
        raw_response = await self.raw.aget_goal_record(
            goal_gid=goal_gid,
            opt_pretty=opt_pretty,
            opt_fields=opt_fields,
            **kwargs,
        )
        if validate:
            return GoalsGetGoalRecordResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(GoalsGetGoalRecordResponsePydantic, raw_response.body)
    
    
    def get_goal_record(
        self,
        goal_gid: str,
        opt_pretty: typing.Optional[bool] = None,
        opt_fields: typing.Optional[typing.List[str]] = None,
        validate: bool = False,
    ) -> GoalsGetGoalRecordResponsePydantic:
        raw_response = self.raw.get_goal_record(
            goal_gid=goal_gid,
            opt_pretty=opt_pretty,
            opt_fields=opt_fields,
        )
        if validate:
            return GoalsGetGoalRecordResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(GoalsGetGoalRecordResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        goal_gid: str,
        opt_pretty: typing.Optional[bool] = None,
        opt_fields: typing.Optional[typing.List[str]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_goal_record_mapped_args(
            goal_gid=goal_gid,
            opt_pretty=opt_pretty,
            opt_fields=opt_fields,
        )
        return await self._aget_goal_record_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        goal_gid: str,
        opt_pretty: typing.Optional[bool] = None,
        opt_fields: typing.Optional[typing.List[str]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_goal_record_mapped_args(
            goal_gid=goal_gid,
            opt_pretty=opt_pretty,
            opt_fields=opt_fields,
        )
        return self._get_goal_record_oapg(
            query_params=args.query,
            path_params=args.path,
        )

