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

from asana_python_sdk.model.attachment_request import AttachmentRequest as AttachmentRequestSchema
from asana_python_sdk.model.attachments_upload_attachment_response import AttachmentsUploadAttachmentResponse as AttachmentsUploadAttachmentResponseSchema
from asana_python_sdk.model.error_response import ErrorResponse as ErrorResponseSchema

from asana_python_sdk.type.attachments_upload_attachment_response import AttachmentsUploadAttachmentResponse
from asana_python_sdk.type.error_response import ErrorResponse
from asana_python_sdk.type.attachment_request import AttachmentRequest

from ...api_client import Dictionary
from asana_python_sdk.pydantic.attachment_request import AttachmentRequest as AttachmentRequestPydantic
from asana_python_sdk.pydantic.attachments_upload_attachment_response import AttachmentsUploadAttachmentResponse as AttachmentsUploadAttachmentResponsePydantic
from asana_python_sdk.pydantic.error_response import ErrorResponse as ErrorResponsePydantic

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
                    "connected_to_app": "CONNECTED_TO_APP",
                    "created_at": "CREATED_AT",
                    "download_url": "DOWNLOAD_URL",
                    "host": "HOST",
                    "name": "NAME",
                    "parent": "PARENT",
                    "parent.created_by": "PARENT_CREATED_BY",
                    "parent.name": "PARENT_NAME",
                    "parent.resource_subtype": "PARENT_RESOURCE_SUBTYPE",
                    "permanent_url": "PERMANENT_URL",
                    "resource_subtype": "RESOURCE_SUBTYPE",
                    "size": "SIZE",
                    "view_url": "VIEW_URL",
                }
            
            @schemas.classproperty
            def CONNECTED_TO_APP(cls):
                return cls("connected_to_app")
            
            @schemas.classproperty
            def CREATED_AT(cls):
                return cls("created_at")
            
            @schemas.classproperty
            def DOWNLOAD_URL(cls):
                return cls("download_url")
            
            @schemas.classproperty
            def HOST(cls):
                return cls("host")
            
            @schemas.classproperty
            def NAME(cls):
                return cls("name")
            
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
            def PERMANENT_URL(cls):
                return cls("permanent_url")
            
            @schemas.classproperty
            def RESOURCE_SUBTYPE(cls):
                return cls("resource_subtype")
            
            @schemas.classproperty
            def SIZE(cls):
                return cls("size")
            
            @schemas.classproperty
            def VIEW_URL(cls):
                return cls("view_url")

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
# body param
SchemaForRequestBodyMultipartFormData = AttachmentRequestSchema


request_body_attachment_request = api_client.RequestBody(
    content={
        'multipart/form-data': api_client.MediaType(
            schema=SchemaForRequestBodyMultipartFormData),
    },
)
_auth = [
    'oauth2',
    'personalAccessToken',
]
SchemaFor200ResponseBodyApplicationJson = AttachmentsUploadAttachmentResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: AttachmentsUploadAttachmentResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: AttachmentsUploadAttachmentResponse


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

    def _upload_attachment_mapped_args(
        self,
        parent: str,
        opt_pretty: typing.Optional[bool] = None,
        opt_fields: typing.Optional[typing.List[str]] = None,
        resource_subtype: typing.Optional[str] = None,
        file: typing.Optional[typing.IO] = None,
        url: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        connect_to_app: typing.Optional[bool] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _body = {}
        if resource_subtype is not None:
            _body["resource_subtype"] = resource_subtype
        if file is not None:
            _body["file"] = file
        if parent is not None:
            _body["parent"] = parent
        if url is not None:
            _body["url"] = url
        if name is not None:
            _body["name"] = name
        if connect_to_app is not None:
            _body["connect_to_app"] = connect_to_app
        args.body = _body
        if opt_pretty is not None:
            _query_params["opt_pretty"] = opt_pretty
        if opt_fields is not None:
            _query_params["opt_fields"] = opt_fields
        args.query = _query_params
        return args

    async def _aupload_attachment_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'multipart/form-data',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Upload an attachment
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
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
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/attachments',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_attachment_request.serialize(body, content_type)
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


    def _upload_attachment_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'multipart/form-data',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Upload an attachment
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
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
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/attachments',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_attachment_request.serialize(body, content_type)
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


class UploadAttachmentRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aupload_attachment(
        self,
        parent: str,
        opt_pretty: typing.Optional[bool] = None,
        opt_fields: typing.Optional[typing.List[str]] = None,
        resource_subtype: typing.Optional[str] = None,
        file: typing.Optional[typing.IO] = None,
        url: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        connect_to_app: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._upload_attachment_mapped_args(
            parent=parent,
            opt_pretty=opt_pretty,
            opt_fields=opt_fields,
            resource_subtype=resource_subtype,
            file=file,
            url=url,
            name=name,
            connect_to_app=connect_to_app,
        )
        return await self._aupload_attachment_oapg(
            body=args.body,
            query_params=args.query,
            **kwargs,
        )
    
    def upload_attachment(
        self,
        parent: str,
        opt_pretty: typing.Optional[bool] = None,
        opt_fields: typing.Optional[typing.List[str]] = None,
        resource_subtype: typing.Optional[str] = None,
        file: typing.Optional[typing.IO] = None,
        url: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        connect_to_app: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._upload_attachment_mapped_args(
            parent=parent,
            opt_pretty=opt_pretty,
            opt_fields=opt_fields,
            resource_subtype=resource_subtype,
            file=file,
            url=url,
            name=name,
            connect_to_app=connect_to_app,
        )
        return self._upload_attachment_oapg(
            body=args.body,
            query_params=args.query,
        )

class UploadAttachment(BaseApi):

    async def aupload_attachment(
        self,
        parent: str,
        opt_pretty: typing.Optional[bool] = None,
        opt_fields: typing.Optional[typing.List[str]] = None,
        resource_subtype: typing.Optional[str] = None,
        file: typing.Optional[typing.IO] = None,
        url: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        connect_to_app: typing.Optional[bool] = None,
        validate: bool = False,
        **kwargs,
    ) -> AttachmentsUploadAttachmentResponsePydantic:
        raw_response = await self.raw.aupload_attachment(
            parent=parent,
            opt_pretty=opt_pretty,
            opt_fields=opt_fields,
            resource_subtype=resource_subtype,
            file=file,
            url=url,
            name=name,
            connect_to_app=connect_to_app,
            **kwargs,
        )
        if validate:
            return AttachmentsUploadAttachmentResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(AttachmentsUploadAttachmentResponsePydantic, raw_response.body)
    
    
    def upload_attachment(
        self,
        parent: str,
        opt_pretty: typing.Optional[bool] = None,
        opt_fields: typing.Optional[typing.List[str]] = None,
        resource_subtype: typing.Optional[str] = None,
        file: typing.Optional[typing.IO] = None,
        url: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        connect_to_app: typing.Optional[bool] = None,
        validate: bool = False,
    ) -> AttachmentsUploadAttachmentResponsePydantic:
        raw_response = self.raw.upload_attachment(
            parent=parent,
            opt_pretty=opt_pretty,
            opt_fields=opt_fields,
            resource_subtype=resource_subtype,
            file=file,
            url=url,
            name=name,
            connect_to_app=connect_to_app,
        )
        if validate:
            return AttachmentsUploadAttachmentResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(AttachmentsUploadAttachmentResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        parent: str,
        opt_pretty: typing.Optional[bool] = None,
        opt_fields: typing.Optional[typing.List[str]] = None,
        resource_subtype: typing.Optional[str] = None,
        file: typing.Optional[typing.IO] = None,
        url: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        connect_to_app: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._upload_attachment_mapped_args(
            parent=parent,
            opt_pretty=opt_pretty,
            opt_fields=opt_fields,
            resource_subtype=resource_subtype,
            file=file,
            url=url,
            name=name,
            connect_to_app=connect_to_app,
        )
        return await self._aupload_attachment_oapg(
            body=args.body,
            query_params=args.query,
            **kwargs,
        )
    
    def post(
        self,
        parent: str,
        opt_pretty: typing.Optional[bool] = None,
        opt_fields: typing.Optional[typing.List[str]] = None,
        resource_subtype: typing.Optional[str] = None,
        file: typing.Optional[typing.IO] = None,
        url: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        connect_to_app: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._upload_attachment_mapped_args(
            parent=parent,
            opt_pretty=opt_pretty,
            opt_fields=opt_fields,
            resource_subtype=resource_subtype,
            file=file,
            url=url,
            name=name,
            connect_to_app=connect_to_app,
        )
        return self._upload_attachment_oapg(
            body=args.body,
            query_params=args.query,
        )

