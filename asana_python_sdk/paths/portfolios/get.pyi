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

from asana_python_sdk.model.portfolios_list_multiple_portfolios_response import PortfoliosListMultiplePortfoliosResponse as PortfoliosListMultiplePortfoliosResponseSchema
from asana_python_sdk.model.error_response import ErrorResponse as ErrorResponseSchema

from asana_python_sdk.type.portfolios_list_multiple_portfolios_response import PortfoliosListMultiplePortfoliosResponse
from asana_python_sdk.type.error_response import ErrorResponse

from ...api_client import Dictionary
from asana_python_sdk.pydantic.error_response import ErrorResponse as ErrorResponsePydantic
from asana_python_sdk.pydantic.portfolios_list_multiple_portfolios_response import PortfoliosListMultiplePortfoliosResponse as PortfoliosListMultiplePortfoliosResponsePydantic

# Query params
OptPrettySchema = schemas.BoolSchema


class LimitSchema(
    schemas.IntSchema
):
    pass
OffsetSchema = schemas.StrSchema
WorkspaceSchema = schemas.StrSchema
OwnerSchema = schemas.StrSchema


class OptFieldsSchema(
    schemas.ListSchema
):


    class MetaOapg:
        
        
        class items(
            schemas.EnumBase,
            schemas.StrSchema
        ):
            
            @schemas.classproperty
            def COLOR(cls):
                return cls("color")
            
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
            def CURRENT_STATUS_UPDATE(cls):
                return cls("current_status_update")
            
            @schemas.classproperty
            def CURRENT_STATUS_UPDATE_RESOURCE_SUBTYPE(cls):
                return cls("current_status_update.resource_subtype")
            
            @schemas.classproperty
            def CURRENT_STATUS_UPDATE_TITLE(cls):
                return cls("current_status_update.title")
            
            @schemas.classproperty
            def CUSTOM_FIELD_SETTINGS(cls):
                return cls("custom_field_settings")
            
            @schemas.classproperty
            def CUSTOM_FIELD_SETTINGS_CUSTOM_FIELD(cls):
                return cls("custom_field_settings.custom_field")
            
            @schemas.classproperty
            def CUSTOM_FIELD_SETTINGS_CUSTOM_FIELD_ASANA_CREATED_FIELD(cls):
                return cls("custom_field_settings.custom_field.asana_created_field")
            
            @schemas.classproperty
            def CUSTOM_FIELD_SETTINGS_CUSTOM_FIELD_CREATED_BY(cls):
                return cls("custom_field_settings.custom_field.created_by")
            
            @schemas.classproperty
            def CUSTOM_FIELD_SETTINGS_CUSTOM_FIELD_CREATED_BY_NAME(cls):
                return cls("custom_field_settings.custom_field.created_by.name")
            
            @schemas.classproperty
            def CUSTOM_FIELD_SETTINGS_CUSTOM_FIELD_CURRENCY_CODE(cls):
                return cls("custom_field_settings.custom_field.currency_code")
            
            @schemas.classproperty
            def CUSTOM_FIELD_SETTINGS_CUSTOM_FIELD_CUSTOM_LABEL(cls):
                return cls("custom_field_settings.custom_field.custom_label")
            
            @schemas.classproperty
            def CUSTOM_FIELD_SETTINGS_CUSTOM_FIELD_CUSTOM_LABEL_POSITION(cls):
                return cls("custom_field_settings.custom_field.custom_label_position")
            
            @schemas.classproperty
            def CUSTOM_FIELD_SETTINGS_CUSTOM_FIELD_DATE_VALUE(cls):
                return cls("custom_field_settings.custom_field.date_value")
            
            @schemas.classproperty
            def CUSTOM_FIELD_SETTINGS_CUSTOM_FIELD_DATE_VALUE_DATE(cls):
                return cls("custom_field_settings.custom_field.date_value.date")
            
            @schemas.classproperty
            def CUSTOM_FIELD_SETTINGS_CUSTOM_FIELD_DATE_VALUE_DATE_TIME(cls):
                return cls("custom_field_settings.custom_field.date_value.date_time")
            
            @schemas.classproperty
            def CUSTOM_FIELD_SETTINGS_CUSTOM_FIELD_DESCRIPTION(cls):
                return cls("custom_field_settings.custom_field.description")
            
            @schemas.classproperty
            def CUSTOM_FIELD_SETTINGS_CUSTOM_FIELD_DISPLAY_VALUE(cls):
                return cls("custom_field_settings.custom_field.display_value")
            
            @schemas.classproperty
            def CUSTOM_FIELD_SETTINGS_CUSTOM_FIELD_ENABLED(cls):
                return cls("custom_field_settings.custom_field.enabled")
            
            @schemas.classproperty
            def CUSTOM_FIELD_SETTINGS_CUSTOM_FIELD_ENUM_OPTIONS(cls):
                return cls("custom_field_settings.custom_field.enum_options")
            
            @schemas.classproperty
            def CUSTOM_FIELD_SETTINGS_CUSTOM_FIELD_ENUM_OPTIONS_COLOR(cls):
                return cls("custom_field_settings.custom_field.enum_options.color")
            
            @schemas.classproperty
            def CUSTOM_FIELD_SETTINGS_CUSTOM_FIELD_ENUM_OPTIONS_ENABLED(cls):
                return cls("custom_field_settings.custom_field.enum_options.enabled")
            
            @schemas.classproperty
            def CUSTOM_FIELD_SETTINGS_CUSTOM_FIELD_ENUM_OPTIONS_NAME(cls):
                return cls("custom_field_settings.custom_field.enum_options.name")
            
            @schemas.classproperty
            def CUSTOM_FIELD_SETTINGS_CUSTOM_FIELD_ENUM_VALUE(cls):
                return cls("custom_field_settings.custom_field.enum_value")
            
            @schemas.classproperty
            def CUSTOM_FIELD_SETTINGS_CUSTOM_FIELD_ENUM_VALUE_COLOR(cls):
                return cls("custom_field_settings.custom_field.enum_value.color")
            
            @schemas.classproperty
            def CUSTOM_FIELD_SETTINGS_CUSTOM_FIELD_ENUM_VALUE_ENABLED(cls):
                return cls("custom_field_settings.custom_field.enum_value.enabled")
            
            @schemas.classproperty
            def CUSTOM_FIELD_SETTINGS_CUSTOM_FIELD_ENUM_VALUE_NAME(cls):
                return cls("custom_field_settings.custom_field.enum_value.name")
            
            @schemas.classproperty
            def CUSTOM_FIELD_SETTINGS_CUSTOM_FIELD_FORMAT(cls):
                return cls("custom_field_settings.custom_field.format")
            
            @schemas.classproperty
            def CUSTOM_FIELD_SETTINGS_CUSTOM_FIELD_HAS_NOTIFICATIONS_ENABLED(cls):
                return cls("custom_field_settings.custom_field.has_notifications_enabled")
            
            @schemas.classproperty
            def CUSTOM_FIELD_SETTINGS_CUSTOM_FIELD_ID_PREFIX(cls):
                return cls("custom_field_settings.custom_field.id_prefix")
            
            @schemas.classproperty
            def CUSTOM_FIELD_SETTINGS_CUSTOM_FIELD_IS_FORMULA_FIELD(cls):
                return cls("custom_field_settings.custom_field.is_formula_field")
            
            @schemas.classproperty
            def CUSTOM_FIELD_SETTINGS_CUSTOM_FIELD_IS_GLOBAL_TO_WORKSPACE(cls):
                return cls("custom_field_settings.custom_field.is_global_to_workspace")
            
            @schemas.classproperty
            def CUSTOM_FIELD_SETTINGS_CUSTOM_FIELD_IS_VALUE_READ_ONLY(cls):
                return cls("custom_field_settings.custom_field.is_value_read_only")
            
            @schemas.classproperty
            def CUSTOM_FIELD_SETTINGS_CUSTOM_FIELD_MULTI_ENUM_VALUES(cls):
                return cls("custom_field_settings.custom_field.multi_enum_values")
            
            @schemas.classproperty
            def CUSTOM_FIELD_SETTINGS_CUSTOM_FIELD_MULTI_ENUM_VALUES_COLOR(cls):
                return cls("custom_field_settings.custom_field.multi_enum_values.color")
            
            @schemas.classproperty
            def CUSTOM_FIELD_SETTINGS_CUSTOM_FIELD_MULTI_ENUM_VALUES_ENABLED(cls):
                return cls("custom_field_settings.custom_field.multi_enum_values.enabled")
            
            @schemas.classproperty
            def CUSTOM_FIELD_SETTINGS_CUSTOM_FIELD_MULTI_ENUM_VALUES_NAME(cls):
                return cls("custom_field_settings.custom_field.multi_enum_values.name")
            
            @schemas.classproperty
            def CUSTOM_FIELD_SETTINGS_CUSTOM_FIELD_NAME(cls):
                return cls("custom_field_settings.custom_field.name")
            
            @schemas.classproperty
            def CUSTOM_FIELD_SETTINGS_CUSTOM_FIELD_NUMBER_VALUE(cls):
                return cls("custom_field_settings.custom_field.number_value")
            
            @schemas.classproperty
            def CUSTOM_FIELD_SETTINGS_CUSTOM_FIELD_PEOPLE_VALUE(cls):
                return cls("custom_field_settings.custom_field.people_value")
            
            @schemas.classproperty
            def CUSTOM_FIELD_SETTINGS_CUSTOM_FIELD_PEOPLE_VALUE_NAME(cls):
                return cls("custom_field_settings.custom_field.people_value.name")
            
            @schemas.classproperty
            def CUSTOM_FIELD_SETTINGS_CUSTOM_FIELD_PRECISION(cls):
                return cls("custom_field_settings.custom_field.precision")
            
            @schemas.classproperty
            def CUSTOM_FIELD_SETTINGS_CUSTOM_FIELD_REPRESENTATION_TYPE(cls):
                return cls("custom_field_settings.custom_field.representation_type")
            
            @schemas.classproperty
            def CUSTOM_FIELD_SETTINGS_CUSTOM_FIELD_RESOURCE_SUBTYPE(cls):
                return cls("custom_field_settings.custom_field.resource_subtype")
            
            @schemas.classproperty
            def CUSTOM_FIELD_SETTINGS_CUSTOM_FIELD_TEXT_VALUE(cls):
                return cls("custom_field_settings.custom_field.text_value")
            
            @schemas.classproperty
            def CUSTOM_FIELD_SETTINGS_CUSTOM_FIELD_TYPE(cls):
                return cls("custom_field_settings.custom_field.type")
            
            @schemas.classproperty
            def CUSTOM_FIELD_SETTINGS_IS_IMPORTANT(cls):
                return cls("custom_field_settings.is_important")
            
            @schemas.classproperty
            def CUSTOM_FIELD_SETTINGS_PARENT(cls):
                return cls("custom_field_settings.parent")
            
            @schemas.classproperty
            def CUSTOM_FIELD_SETTINGS_PARENT_NAME(cls):
                return cls("custom_field_settings.parent.name")
            
            @schemas.classproperty
            def CUSTOM_FIELD_SETTINGS_PROJECT(cls):
                return cls("custom_field_settings.project")
            
            @schemas.classproperty
            def CUSTOM_FIELD_SETTINGS_PROJECT_NAME(cls):
                return cls("custom_field_settings.project.name")
            
            @schemas.classproperty
            def CUSTOM_FIELDS(cls):
                return cls("custom_fields")
            
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
            def CUSTOM_FIELDS_ID_PREFIX(cls):
                return cls("custom_fields.id_prefix")
            
            @schemas.classproperty
            def CUSTOM_FIELDS_IS_FORMULA_FIELD(cls):
                return cls("custom_fields.is_formula_field")
            
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
            def DUE_ON(cls):
                return cls("due_on")
            
            @schemas.classproperty
            def MEMBERS(cls):
                return cls("members")
            
            @schemas.classproperty
            def MEMBERS_NAME(cls):
                return cls("members.name")
            
            @schemas.classproperty
            def NAME(cls):
                return cls("name")
            
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
            def PERMALINK_URL(cls):
                return cls("permalink_url")
            
            @schemas.classproperty
            def PROJECT_TEMPLATES(cls):
                return cls("project_templates")
            
            @schemas.classproperty
            def PROJECT_TEMPLATES_NAME(cls):
                return cls("project_templates.name")
            
            @schemas.classproperty
            def PUBLIC(cls):
                return cls("public")
            
            @schemas.classproperty
            def START_ON(cls):
                return cls("start_on")
            
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
        'workspace': typing.Union[WorkspaceSchema, str, ],
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'opt_pretty': typing.Union[OptPrettySchema, bool, ],
        'limit': typing.Union[LimitSchema, decimal.Decimal, int, ],
        'offset': typing.Union[OffsetSchema, str, ],
        'owner': typing.Union[OwnerSchema, str, ],
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
request_query_workspace = api_client.QueryParameter(
    name="workspace",
    style=api_client.ParameterStyle.FORM,
    schema=WorkspaceSchema,
    required=True,
    explode=True,
)
request_query_owner = api_client.QueryParameter(
    name="owner",
    style=api_client.ParameterStyle.FORM,
    schema=OwnerSchema,
    explode=True,
)
request_query_opt_fields = api_client.QueryParameter(
    name="opt_fields",
    style=api_client.ParameterStyle.FORM,
    schema=OptFieldsSchema,
)
SchemaFor200ResponseBodyApplicationJson = PortfoliosListMultiplePortfoliosResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: PortfoliosListMultiplePortfoliosResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: PortfoliosListMultiplePortfoliosResponse


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

    def _list_multiple_portfolios_mapped_args(
        self,
        workspace: str,
        opt_pretty: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[str] = None,
        owner: typing.Optional[str] = None,
        opt_fields: typing.Optional[typing.List[str]] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if opt_pretty is not None:
            _query_params["opt_pretty"] = opt_pretty
        if limit is not None:
            _query_params["limit"] = limit
        if offset is not None:
            _query_params["offset"] = offset
        if workspace is not None:
            _query_params["workspace"] = workspace
        if owner is not None:
            _query_params["owner"] = owner
        if opt_fields is not None:
            _query_params["opt_fields"] = opt_fields
        args.query = _query_params
        return args

    async def _alist_multiple_portfolios_oapg(
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
        Get multiple portfolios
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_opt_pretty,
            request_query_limit,
            request_query_offset,
            request_query_workspace,
            request_query_owner,
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
            path_template='/portfolios',
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


    def _list_multiple_portfolios_oapg(
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
        Get multiple portfolios
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_opt_pretty,
            request_query_limit,
            request_query_offset,
            request_query_workspace,
            request_query_owner,
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
            path_template='/portfolios',
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


class ListMultiplePortfoliosRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def alist_multiple_portfolios(
        self,
        workspace: str,
        opt_pretty: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[str] = None,
        owner: typing.Optional[str] = None,
        opt_fields: typing.Optional[typing.List[str]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_multiple_portfolios_mapped_args(
            workspace=workspace,
            opt_pretty=opt_pretty,
            limit=limit,
            offset=offset,
            owner=owner,
            opt_fields=opt_fields,
        )
        return await self._alist_multiple_portfolios_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def list_multiple_portfolios(
        self,
        workspace: str,
        opt_pretty: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[str] = None,
        owner: typing.Optional[str] = None,
        opt_fields: typing.Optional[typing.List[str]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_multiple_portfolios_mapped_args(
            workspace=workspace,
            opt_pretty=opt_pretty,
            limit=limit,
            offset=offset,
            owner=owner,
            opt_fields=opt_fields,
        )
        return self._list_multiple_portfolios_oapg(
            query_params=args.query,
        )

class ListMultiplePortfolios(BaseApi):

    async def alist_multiple_portfolios(
        self,
        workspace: str,
        opt_pretty: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[str] = None,
        owner: typing.Optional[str] = None,
        opt_fields: typing.Optional[typing.List[str]] = None,
        validate: bool = False,
        **kwargs,
    ) -> PortfoliosListMultiplePortfoliosResponsePydantic:
        raw_response = await self.raw.alist_multiple_portfolios(
            workspace=workspace,
            opt_pretty=opt_pretty,
            limit=limit,
            offset=offset,
            owner=owner,
            opt_fields=opt_fields,
            **kwargs,
        )
        if validate:
            return PortfoliosListMultiplePortfoliosResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(PortfoliosListMultiplePortfoliosResponsePydantic, raw_response.body)
    
    
    def list_multiple_portfolios(
        self,
        workspace: str,
        opt_pretty: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[str] = None,
        owner: typing.Optional[str] = None,
        opt_fields: typing.Optional[typing.List[str]] = None,
        validate: bool = False,
    ) -> PortfoliosListMultiplePortfoliosResponsePydantic:
        raw_response = self.raw.list_multiple_portfolios(
            workspace=workspace,
            opt_pretty=opt_pretty,
            limit=limit,
            offset=offset,
            owner=owner,
            opt_fields=opt_fields,
        )
        if validate:
            return PortfoliosListMultiplePortfoliosResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(PortfoliosListMultiplePortfoliosResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        workspace: str,
        opt_pretty: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[str] = None,
        owner: typing.Optional[str] = None,
        opt_fields: typing.Optional[typing.List[str]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_multiple_portfolios_mapped_args(
            workspace=workspace,
            opt_pretty=opt_pretty,
            limit=limit,
            offset=offset,
            owner=owner,
            opt_fields=opt_fields,
        )
        return await self._alist_multiple_portfolios_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        workspace: str,
        opt_pretty: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[str] = None,
        owner: typing.Optional[str] = None,
        opt_fields: typing.Optional[typing.List[str]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_multiple_portfolios_mapped_args(
            workspace=workspace,
            opt_pretty=opt_pretty,
            limit=limit,
            offset=offset,
            owner=owner,
            opt_fields=opt_fields,
        )
        return self._list_multiple_portfolios_oapg(
            query_params=args.query,
        )

