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

from asana_python_sdk.model.teams_get_user_teams_response import TeamsGetUserTeamsResponse as TeamsGetUserTeamsResponseSchema
from asana_python_sdk.model.error_response import ErrorResponse as ErrorResponseSchema

from asana_python_sdk.type.teams_get_user_teams_response import TeamsGetUserTeamsResponse
from asana_python_sdk.type.error_response import ErrorResponse

from ...api_client import Dictionary
from asana_python_sdk.pydantic.teams_get_user_teams_response import TeamsGetUserTeamsResponse as TeamsGetUserTeamsResponsePydantic
from asana_python_sdk.pydantic.error_response import ErrorResponse as ErrorResponsePydantic

# Query params
OptPrettySchema = schemas.BoolSchema


class LimitSchema(
    schemas.IntSchema
):
    pass
OffsetSchema = schemas.StrSchema
OrganizationSchema = schemas.StrSchema


class OptFieldsSchema(
    schemas.ListSchema
):


    class MetaOapg:
        
        
        class items(
            schemas.EnumBase,
            schemas.StrSchema
        ):
            
            @schemas.classproperty
            def DESCRIPTION(cls):
                return cls("description")
            
            @schemas.classproperty
            def EDIT_TEAM_NAME_OR_DESCRIPTION_ACCESS_LEVEL(cls):
                return cls("edit_team_name_or_description_access_level")
            
            @schemas.classproperty
            def EDIT_TEAM_VISIBILITY_OR_TRASH_TEAM_ACCESS_LEVEL(cls):
                return cls("edit_team_visibility_or_trash_team_access_level")
            
            @schemas.classproperty
            def GUEST_INVITE_MANAGEMENT_ACCESS_LEVEL(cls):
                return cls("guest_invite_management_access_level")
            
            @schemas.classproperty
            def HTML_DESCRIPTION(cls):
                return cls("html_description")
            
            @schemas.classproperty
            def JOIN_REQUEST_MANAGEMENT_ACCESS_LEVEL(cls):
                return cls("join_request_management_access_level")
            
            @schemas.classproperty
            def MEMBER_INVITE_MANAGEMENT_ACCESS_LEVEL(cls):
                return cls("member_invite_management_access_level")
            
            @schemas.classproperty
            def NAME(cls):
                return cls("name")
            
            @schemas.classproperty
            def OFFSET(cls):
                return cls("offset")
            
            @schemas.classproperty
            def ORGANIZATION(cls):
                return cls("organization")
            
            @schemas.classproperty
            def ORGANIZATION_NAME(cls):
                return cls("organization.name")
            
            @schemas.classproperty
            def PATH(cls):
                return cls("path")
            
            @schemas.classproperty
            def PERMALINK_URL(cls):
                return cls("permalink_url")
            
            @schemas.classproperty
            def TEAM_MEMBER_REMOVAL_ACCESS_LEVEL(cls):
                return cls("team_member_removal_access_level")
            
            @schemas.classproperty
            def URI(cls):
                return cls("uri")
            
            @schemas.classproperty
            def VISIBILITY(cls):
                return cls("visibility")

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
        'organization': typing.Union[OrganizationSchema, str, ],
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'opt_pretty': typing.Union[OptPrettySchema, bool, ],
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
request_query_organization = api_client.QueryParameter(
    name="organization",
    style=api_client.ParameterStyle.FORM,
    schema=OrganizationSchema,
    required=True,
    explode=True,
)
request_query_opt_fields = api_client.QueryParameter(
    name="opt_fields",
    style=api_client.ParameterStyle.FORM,
    schema=OptFieldsSchema,
)
# Path params
UserGidSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'user_gid': typing.Union[UserGidSchema, str, ],
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


request_path_user_gid = api_client.PathParameter(
    name="user_gid",
    style=api_client.ParameterStyle.SIMPLE,
    schema=UserGidSchema,
    required=True,
)
SchemaFor200ResponseBodyApplicationJson = TeamsGetUserTeamsResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: TeamsGetUserTeamsResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: TeamsGetUserTeamsResponse


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

    def _get_user_teams_mapped_args(
        self,
        user_gid: str,
        organization: str,
        opt_pretty: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[str] = None,
        opt_fields: typing.Optional[typing.List[str]] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _path_params = {}
        if opt_pretty is not None:
            _query_params["opt_pretty"] = opt_pretty
        if limit is not None:
            _query_params["limit"] = limit
        if offset is not None:
            _query_params["offset"] = offset
        if organization is not None:
            _query_params["organization"] = organization
        if opt_fields is not None:
            _query_params["opt_fields"] = opt_fields
        if user_gid is not None:
            _path_params["user_gid"] = user_gid
        args.query = _query_params
        args.path = _path_params
        return args

    async def _aget_user_teams_oapg(
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
        Get teams for a user
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_user_gid,
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
            request_query_limit,
            request_query_offset,
            request_query_organization,
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
            path_template='/users/{user_gid}/teams',
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


    def _get_user_teams_oapg(
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
        Get teams for a user
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_user_gid,
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
            request_query_limit,
            request_query_offset,
            request_query_organization,
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
            path_template='/users/{user_gid}/teams',
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


class GetUserTeamsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_user_teams(
        self,
        user_gid: str,
        organization: str,
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
        args = self._get_user_teams_mapped_args(
            user_gid=user_gid,
            organization=organization,
            opt_pretty=opt_pretty,
            limit=limit,
            offset=offset,
            opt_fields=opt_fields,
        )
        return await self._aget_user_teams_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get_user_teams(
        self,
        user_gid: str,
        organization: str,
        opt_pretty: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[str] = None,
        opt_fields: typing.Optional[typing.List[str]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_user_teams_mapped_args(
            user_gid=user_gid,
            organization=organization,
            opt_pretty=opt_pretty,
            limit=limit,
            offset=offset,
            opt_fields=opt_fields,
        )
        return self._get_user_teams_oapg(
            query_params=args.query,
            path_params=args.path,
        )

class GetUserTeams(BaseApi):

    async def aget_user_teams(
        self,
        user_gid: str,
        organization: str,
        opt_pretty: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[str] = None,
        opt_fields: typing.Optional[typing.List[str]] = None,
        validate: bool = False,
        **kwargs,
    ) -> TeamsGetUserTeamsResponsePydantic:
        raw_response = await self.raw.aget_user_teams(
            user_gid=user_gid,
            organization=organization,
            opt_pretty=opt_pretty,
            limit=limit,
            offset=offset,
            opt_fields=opt_fields,
            **kwargs,
        )
        if validate:
            return TeamsGetUserTeamsResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(TeamsGetUserTeamsResponsePydantic, raw_response.body)
    
    
    def get_user_teams(
        self,
        user_gid: str,
        organization: str,
        opt_pretty: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[str] = None,
        opt_fields: typing.Optional[typing.List[str]] = None,
        validate: bool = False,
    ) -> TeamsGetUserTeamsResponsePydantic:
        raw_response = self.raw.get_user_teams(
            user_gid=user_gid,
            organization=organization,
            opt_pretty=opt_pretty,
            limit=limit,
            offset=offset,
            opt_fields=opt_fields,
        )
        if validate:
            return TeamsGetUserTeamsResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(TeamsGetUserTeamsResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        user_gid: str,
        organization: str,
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
        args = self._get_user_teams_mapped_args(
            user_gid=user_gid,
            organization=organization,
            opt_pretty=opt_pretty,
            limit=limit,
            offset=offset,
            opt_fields=opt_fields,
        )
        return await self._aget_user_teams_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        user_gid: str,
        organization: str,
        opt_pretty: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[str] = None,
        opt_fields: typing.Optional[typing.List[str]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_user_teams_mapped_args(
            user_gid=user_gid,
            organization=organization,
            opt_pretty=opt_pretty,
            limit=limit,
            offset=offset,
            opt_fields=opt_fields,
        )
        return self._get_user_teams_oapg(
            query_params=args.query,
            path_params=args.path,
        )

