# coding: utf-8

"""
    Asana

    This is the interface for interacting with the [Asana Platform](https://developers.asana.com). Our API reference is generated from our [OpenAPI spec](https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml).

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

from asana_python_sdk.model.audit_log_api_get_audit_log_events_response import AuditLogApiGetAuditLogEventsResponse as AuditLogApiGetAuditLogEventsResponseSchema
from asana_python_sdk.model.error_response import ErrorResponse as ErrorResponseSchema

from asana_python_sdk.type.error_response import ErrorResponse
from asana_python_sdk.type.audit_log_api_get_audit_log_events_response import AuditLogApiGetAuditLogEventsResponse

from ...api_client import Dictionary
from asana_python_sdk.pydantic.error_response import ErrorResponse as ErrorResponsePydantic
from asana_python_sdk.pydantic.audit_log_api_get_audit_log_events_response import AuditLogApiGetAuditLogEventsResponse as AuditLogApiGetAuditLogEventsResponsePydantic

# Query params
StartAtSchema = schemas.DateTimeSchema
EndAtSchema = schemas.DateTimeSchema
EventTypeSchema = schemas.StrSchema


class ActorTypeSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def USER(cls):
        return cls("user")
    
    @schemas.classproperty
    def ASANA(cls):
        return cls("asana")
    
    @schemas.classproperty
    def ASANA_SUPPORT(cls):
        return cls("asana_support")
    
    @schemas.classproperty
    def ANONYMOUS(cls):
        return cls("anonymous")
    
    @schemas.classproperty
    def EXTERNAL_ADMINISTRATOR(cls):
        return cls("external_administrator")
ActorGidSchema = schemas.StrSchema
ResourceGidSchema = schemas.StrSchema


class LimitSchema(
    schemas.IntSchema
):
    pass
OffsetSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'start_at': typing.Union[StartAtSchema, str, datetime, ],
        'end_at': typing.Union[EndAtSchema, str, datetime, ],
        'event_type': typing.Union[EventTypeSchema, str, ],
        'actor_type': typing.Union[ActorTypeSchema, str, ],
        'actor_gid': typing.Union[ActorGidSchema, str, ],
        'resource_gid': typing.Union[ResourceGidSchema, str, ],
        'limit': typing.Union[LimitSchema, decimal.Decimal, int, ],
        'offset': typing.Union[OffsetSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_start_at = api_client.QueryParameter(
    name="start_at",
    style=api_client.ParameterStyle.FORM,
    schema=StartAtSchema,
    explode=True,
)
request_query_end_at = api_client.QueryParameter(
    name="end_at",
    style=api_client.ParameterStyle.FORM,
    schema=EndAtSchema,
    explode=True,
)
request_query_event_type = api_client.QueryParameter(
    name="event_type",
    style=api_client.ParameterStyle.FORM,
    schema=EventTypeSchema,
    explode=True,
)
request_query_actor_type = api_client.QueryParameter(
    name="actor_type",
    style=api_client.ParameterStyle.FORM,
    schema=ActorTypeSchema,
    explode=True,
)
request_query_actor_gid = api_client.QueryParameter(
    name="actor_gid",
    style=api_client.ParameterStyle.FORM,
    schema=ActorGidSchema,
    explode=True,
)
request_query_resource_gid = api_client.QueryParameter(
    name="resource_gid",
    style=api_client.ParameterStyle.FORM,
    schema=ResourceGidSchema,
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
SchemaFor200ResponseBodyApplicationJson = AuditLogApiGetAuditLogEventsResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: AuditLogApiGetAuditLogEventsResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: AuditLogApiGetAuditLogEventsResponse


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

    def _get_audit_log_events_mapped_args(
        self,
        workspace_gid: str,
        start_at: typing.Optional[datetime] = None,
        end_at: typing.Optional[datetime] = None,
        event_type: typing.Optional[str] = None,
        actor_type: typing.Optional[str] = None,
        actor_gid: typing.Optional[str] = None,
        resource_gid: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _path_params = {}
        if start_at is not None:
            _query_params["start_at"] = start_at
        if end_at is not None:
            _query_params["end_at"] = end_at
        if event_type is not None:
            _query_params["event_type"] = event_type
        if actor_type is not None:
            _query_params["actor_type"] = actor_type
        if actor_gid is not None:
            _query_params["actor_gid"] = actor_gid
        if resource_gid is not None:
            _query_params["resource_gid"] = resource_gid
        if limit is not None:
            _query_params["limit"] = limit
        if offset is not None:
            _query_params["offset"] = offset
        if workspace_gid is not None:
            _path_params["workspace_gid"] = workspace_gid
        args.query = _query_params
        args.path = _path_params
        return args

    async def _aget_audit_log_events_oapg(
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
        Get audit log events
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
            request_query_start_at,
            request_query_end_at,
            request_query_event_type,
            request_query_actor_type,
            request_query_actor_gid,
            request_query_resource_gid,
            request_query_limit,
            request_query_offset,
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
            path_template='/workspaces/{workspace_gid}/audit_log_events',
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


    def _get_audit_log_events_oapg(
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
        Get audit log events
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
            request_query_start_at,
            request_query_end_at,
            request_query_event_type,
            request_query_actor_type,
            request_query_actor_gid,
            request_query_resource_gid,
            request_query_limit,
            request_query_offset,
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
            path_template='/workspaces/{workspace_gid}/audit_log_events',
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


class GetAuditLogEventsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_audit_log_events(
        self,
        workspace_gid: str,
        start_at: typing.Optional[datetime] = None,
        end_at: typing.Optional[datetime] = None,
        event_type: typing.Optional[str] = None,
        actor_type: typing.Optional[str] = None,
        actor_gid: typing.Optional[str] = None,
        resource_gid: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_audit_log_events_mapped_args(
            workspace_gid=workspace_gid,
            start_at=start_at,
            end_at=end_at,
            event_type=event_type,
            actor_type=actor_type,
            actor_gid=actor_gid,
            resource_gid=resource_gid,
            limit=limit,
            offset=offset,
        )
        return await self._aget_audit_log_events_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get_audit_log_events(
        self,
        workspace_gid: str,
        start_at: typing.Optional[datetime] = None,
        end_at: typing.Optional[datetime] = None,
        event_type: typing.Optional[str] = None,
        actor_type: typing.Optional[str] = None,
        actor_gid: typing.Optional[str] = None,
        resource_gid: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_audit_log_events_mapped_args(
            workspace_gid=workspace_gid,
            start_at=start_at,
            end_at=end_at,
            event_type=event_type,
            actor_type=actor_type,
            actor_gid=actor_gid,
            resource_gid=resource_gid,
            limit=limit,
            offset=offset,
        )
        return self._get_audit_log_events_oapg(
            query_params=args.query,
            path_params=args.path,
        )

class GetAuditLogEvents(BaseApi):

    async def aget_audit_log_events(
        self,
        workspace_gid: str,
        start_at: typing.Optional[datetime] = None,
        end_at: typing.Optional[datetime] = None,
        event_type: typing.Optional[str] = None,
        actor_type: typing.Optional[str] = None,
        actor_gid: typing.Optional[str] = None,
        resource_gid: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> AuditLogApiGetAuditLogEventsResponsePydantic:
        raw_response = await self.raw.aget_audit_log_events(
            workspace_gid=workspace_gid,
            start_at=start_at,
            end_at=end_at,
            event_type=event_type,
            actor_type=actor_type,
            actor_gid=actor_gid,
            resource_gid=resource_gid,
            limit=limit,
            offset=offset,
            **kwargs,
        )
        if validate:
            return AuditLogApiGetAuditLogEventsResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(AuditLogApiGetAuditLogEventsResponsePydantic, raw_response.body)
    
    
    def get_audit_log_events(
        self,
        workspace_gid: str,
        start_at: typing.Optional[datetime] = None,
        end_at: typing.Optional[datetime] = None,
        event_type: typing.Optional[str] = None,
        actor_type: typing.Optional[str] = None,
        actor_gid: typing.Optional[str] = None,
        resource_gid: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[str] = None,
        validate: bool = False,
    ) -> AuditLogApiGetAuditLogEventsResponsePydantic:
        raw_response = self.raw.get_audit_log_events(
            workspace_gid=workspace_gid,
            start_at=start_at,
            end_at=end_at,
            event_type=event_type,
            actor_type=actor_type,
            actor_gid=actor_gid,
            resource_gid=resource_gid,
            limit=limit,
            offset=offset,
        )
        if validate:
            return AuditLogApiGetAuditLogEventsResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(AuditLogApiGetAuditLogEventsResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        workspace_gid: str,
        start_at: typing.Optional[datetime] = None,
        end_at: typing.Optional[datetime] = None,
        event_type: typing.Optional[str] = None,
        actor_type: typing.Optional[str] = None,
        actor_gid: typing.Optional[str] = None,
        resource_gid: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_audit_log_events_mapped_args(
            workspace_gid=workspace_gid,
            start_at=start_at,
            end_at=end_at,
            event_type=event_type,
            actor_type=actor_type,
            actor_gid=actor_gid,
            resource_gid=resource_gid,
            limit=limit,
            offset=offset,
        )
        return await self._aget_audit_log_events_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        workspace_gid: str,
        start_at: typing.Optional[datetime] = None,
        end_at: typing.Optional[datetime] = None,
        event_type: typing.Optional[str] = None,
        actor_type: typing.Optional[str] = None,
        actor_gid: typing.Optional[str] = None,
        resource_gid: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_audit_log_events_mapped_args(
            workspace_gid=workspace_gid,
            start_at=start_at,
            end_at=end_at,
            event_type=event_type,
            actor_type=actor_type,
            actor_gid=actor_gid,
            resource_gid=resource_gid,
            limit=limit,
            offset=offset,
        )
        return self._get_audit_log_events_oapg(
            query_params=args.query,
            path_params=args.path,
        )

