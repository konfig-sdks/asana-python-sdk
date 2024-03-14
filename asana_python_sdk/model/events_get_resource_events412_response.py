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


class EventsGetResourceEvents412Response(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def errors() -> typing.Type['EventsGetResourceEvents412ResponseErrors']:
                return EventsGetResourceEvents412ResponseErrors
            sync = schemas.StrSchema
            __annotations__ = {
                "errors": errors,
                "sync": sync,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["errors"]) -> 'EventsGetResourceEvents412ResponseErrors': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sync"]) -> MetaOapg.properties.sync: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["errors", "sync", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["errors"]) -> typing.Union['EventsGetResourceEvents412ResponseErrors', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sync"]) -> typing.Union[MetaOapg.properties.sync, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["errors", "sync", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        errors: typing.Union['EventsGetResourceEvents412ResponseErrors', schemas.Unset] = schemas.unset,
        sync: typing.Union[MetaOapg.properties.sync, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EventsGetResourceEvents412Response':
        return super().__new__(
            cls,
            *args,
            errors=errors,
            sync=sync,
            _configuration=_configuration,
            **kwargs,
        )

from asana_python_sdk.model.events_get_resource_events412_response_errors import EventsGetResourceEvents412ResponseErrors
