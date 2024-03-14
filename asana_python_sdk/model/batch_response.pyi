# coding: utf-8

"""
    Asana

    This is the interface for interacting with the [Asana Platform](https://developers.asana.com). Our API reference is generated from our [OpenAPI spec](https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml).

    The version of the OpenAPI document: 1.0
    Created by: https://asana.com/support
"""

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


class BatchResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    A response object returned from a batch request.
    """


    class MetaOapg:
        
        class properties:
            status_code = schemas.IntSchema
            headers = schemas.DictSchema
            body = schemas.DictSchema
            __annotations__ = {
                "status_code": status_code,
                "headers": headers,
                "body": body,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status_code"]) -> MetaOapg.properties.status_code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["headers"]) -> MetaOapg.properties.headers: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["body"]) -> MetaOapg.properties.body: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["status_code", "headers", "body", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status_code"]) -> typing.Union[MetaOapg.properties.status_code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["headers"]) -> typing.Union[MetaOapg.properties.headers, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["body"]) -> typing.Union[MetaOapg.properties.body, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["status_code", "headers", "body", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        status_code: typing.Union[MetaOapg.properties.status_code, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        headers: typing.Union[MetaOapg.properties.headers, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        body: typing.Union[MetaOapg.properties.body, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BatchResponse':
        return super().__new__(
            cls,
            *args,
            status_code=status_code,
            headers=headers,
            body=body,
            _configuration=_configuration,
            **kwargs,
        )
