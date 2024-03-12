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

from asana_python_sdk.model.projects_add_custom_field_setting_request import ProjectsAddCustomFieldSettingRequest as ProjectsAddCustomFieldSettingRequestSchema
from asana_python_sdk.model.projects_add_custom_field_setting_response import ProjectsAddCustomFieldSettingResponse as ProjectsAddCustomFieldSettingResponseSchema
from asana_python_sdk.model.add_custom_field_setting_request import AddCustomFieldSettingRequest as AddCustomFieldSettingRequestSchema
from asana_python_sdk.model.error_response import ErrorResponse as ErrorResponseSchema

from asana_python_sdk.type.add_custom_field_setting_request import AddCustomFieldSettingRequest
from asana_python_sdk.type.projects_add_custom_field_setting_request import ProjectsAddCustomFieldSettingRequest
from asana_python_sdk.type.projects_add_custom_field_setting_response import ProjectsAddCustomFieldSettingResponse
from asana_python_sdk.type.error_response import ErrorResponse

from ...api_client import Dictionary
from asana_python_sdk.pydantic.error_response import ErrorResponse as ErrorResponsePydantic
from asana_python_sdk.pydantic.projects_add_custom_field_setting_response import ProjectsAddCustomFieldSettingResponse as ProjectsAddCustomFieldSettingResponsePydantic
from asana_python_sdk.pydantic.add_custom_field_setting_request import AddCustomFieldSettingRequest as AddCustomFieldSettingRequestPydantic
from asana_python_sdk.pydantic.projects_add_custom_field_setting_request import ProjectsAddCustomFieldSettingRequest as ProjectsAddCustomFieldSettingRequestPydantic

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
            
            @schemas.classproperty
            def CUSTOM_FIELD(cls):
                return cls("custom_field")
            
            @schemas.classproperty
            def CUSTOM_FIELD_ASANA_CREATED_FIELD(cls):
                return cls("custom_field.asana_created_field")
            
            @schemas.classproperty
            def CUSTOM_FIELD_CREATED_BY(cls):
                return cls("custom_field.created_by")
            
            @schemas.classproperty
            def CUSTOM_FIELD_CREATED_BY_NAME(cls):
                return cls("custom_field.created_by.name")
            
            @schemas.classproperty
            def CUSTOM_FIELD_CURRENCY_CODE(cls):
                return cls("custom_field.currency_code")
            
            @schemas.classproperty
            def CUSTOM_FIELD_CUSTOM_LABEL(cls):
                return cls("custom_field.custom_label")
            
            @schemas.classproperty
            def CUSTOM_FIELD_CUSTOM_LABEL_POSITION(cls):
                return cls("custom_field.custom_label_position")
            
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
            def CUSTOM_FIELD_DESCRIPTION(cls):
                return cls("custom_field.description")
            
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
            def CUSTOM_FIELD_FORMAT(cls):
                return cls("custom_field.format")
            
            @schemas.classproperty
            def CUSTOM_FIELD_HAS_NOTIFICATIONS_ENABLED(cls):
                return cls("custom_field.has_notifications_enabled")
            
            @schemas.classproperty
            def CUSTOM_FIELD_ID_PREFIX(cls):
                return cls("custom_field.id_prefix")
            
            @schemas.classproperty
            def CUSTOM_FIELD_IS_FORMULA_FIELD(cls):
                return cls("custom_field.is_formula_field")
            
            @schemas.classproperty
            def CUSTOM_FIELD_IS_GLOBAL_TO_WORKSPACE(cls):
                return cls("custom_field.is_global_to_workspace")
            
            @schemas.classproperty
            def CUSTOM_FIELD_IS_VALUE_READ_ONLY(cls):
                return cls("custom_field.is_value_read_only")
            
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
            def CUSTOM_FIELD_PEOPLE_VALUE(cls):
                return cls("custom_field.people_value")
            
            @schemas.classproperty
            def CUSTOM_FIELD_PEOPLE_VALUE_NAME(cls):
                return cls("custom_field.people_value.name")
            
            @schemas.classproperty
            def CUSTOM_FIELD_PRECISION(cls):
                return cls("custom_field.precision")
            
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
            def IS_IMPORTANT(cls):
                return cls("is_important")
            
            @schemas.classproperty
            def PARENT(cls):
                return cls("parent")
            
            @schemas.classproperty
            def PARENT_NAME(cls):
                return cls("parent.name")
            
            @schemas.classproperty
            def PROJECT(cls):
                return cls("project")
            
            @schemas.classproperty
            def PROJECT_NAME(cls):
                return cls("project.name")

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
ProjectGidSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'project_gid': typing.Union[ProjectGidSchema, str, ],
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


request_path_project_gid = api_client.PathParameter(
    name="project_gid",
    style=api_client.ParameterStyle.SIMPLE,
    schema=ProjectGidSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = ProjectsAddCustomFieldSettingRequestSchema


request_body_projects_add_custom_field_setting_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
SchemaFor200ResponseBodyApplicationJson = ProjectsAddCustomFieldSettingResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: ProjectsAddCustomFieldSettingResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: ProjectsAddCustomFieldSettingResponse


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

    def _add_custom_field_setting_mapped_args(
        self,
        project_gid: str,
        data: typing.Optional[AddCustomFieldSettingRequest] = None,
        opt_pretty: typing.Optional[bool] = None,
        opt_fields: typing.Optional[typing.List[str]] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _path_params = {}
        _body = {}
        if data is not None:
            _body["data"] = data
        args.body = _body
        if opt_pretty is not None:
            _query_params["opt_pretty"] = opt_pretty
        if opt_fields is not None:
            _query_params["opt_fields"] = opt_fields
        if project_gid is not None:
            _path_params["project_gid"] = project_gid
        args.query = _query_params
        args.path = _path_params
        return args

    async def _aadd_custom_field_setting_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Add a custom field to a project
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_project_gid,
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
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/projects/{project_gid}/addCustomFieldSetting',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_projects_add_custom_field_setting_request.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
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


    def _add_custom_field_setting_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Add a custom field to a project
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_project_gid,
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
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/projects/{project_gid}/addCustomFieldSetting',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_projects_add_custom_field_setting_request.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
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


class AddCustomFieldSettingRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aadd_custom_field_setting(
        self,
        project_gid: str,
        data: typing.Optional[AddCustomFieldSettingRequest] = None,
        opt_pretty: typing.Optional[bool] = None,
        opt_fields: typing.Optional[typing.List[str]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._add_custom_field_setting_mapped_args(
            project_gid=project_gid,
            data=data,
            opt_pretty=opt_pretty,
            opt_fields=opt_fields,
        )
        return await self._aadd_custom_field_setting_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def add_custom_field_setting(
        self,
        project_gid: str,
        data: typing.Optional[AddCustomFieldSettingRequest] = None,
        opt_pretty: typing.Optional[bool] = None,
        opt_fields: typing.Optional[typing.List[str]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._add_custom_field_setting_mapped_args(
            project_gid=project_gid,
            data=data,
            opt_pretty=opt_pretty,
            opt_fields=opt_fields,
        )
        return self._add_custom_field_setting_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
        )

class AddCustomFieldSetting(BaseApi):

    async def aadd_custom_field_setting(
        self,
        project_gid: str,
        data: typing.Optional[AddCustomFieldSettingRequest] = None,
        opt_pretty: typing.Optional[bool] = None,
        opt_fields: typing.Optional[typing.List[str]] = None,
        validate: bool = False,
        **kwargs,
    ) -> ProjectsAddCustomFieldSettingResponsePydantic:
        raw_response = await self.raw.aadd_custom_field_setting(
            project_gid=project_gid,
            data=data,
            opt_pretty=opt_pretty,
            opt_fields=opt_fields,
            **kwargs,
        )
        if validate:
            return ProjectsAddCustomFieldSettingResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(ProjectsAddCustomFieldSettingResponsePydantic, raw_response.body)
    
    
    def add_custom_field_setting(
        self,
        project_gid: str,
        data: typing.Optional[AddCustomFieldSettingRequest] = None,
        opt_pretty: typing.Optional[bool] = None,
        opt_fields: typing.Optional[typing.List[str]] = None,
        validate: bool = False,
    ) -> ProjectsAddCustomFieldSettingResponsePydantic:
        raw_response = self.raw.add_custom_field_setting(
            project_gid=project_gid,
            data=data,
            opt_pretty=opt_pretty,
            opt_fields=opt_fields,
        )
        if validate:
            return ProjectsAddCustomFieldSettingResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(ProjectsAddCustomFieldSettingResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        project_gid: str,
        data: typing.Optional[AddCustomFieldSettingRequest] = None,
        opt_pretty: typing.Optional[bool] = None,
        opt_fields: typing.Optional[typing.List[str]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._add_custom_field_setting_mapped_args(
            project_gid=project_gid,
            data=data,
            opt_pretty=opt_pretty,
            opt_fields=opt_fields,
        )
        return await self._aadd_custom_field_setting_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        project_gid: str,
        data: typing.Optional[AddCustomFieldSettingRequest] = None,
        opt_pretty: typing.Optional[bool] = None,
        opt_fields: typing.Optional[typing.List[str]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._add_custom_field_setting_mapped_args(
            project_gid=project_gid,
            data=data,
            opt_pretty=opt_pretty,
            opt_fields=opt_fields,
        )
        return self._add_custom_field_setting_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
        )

