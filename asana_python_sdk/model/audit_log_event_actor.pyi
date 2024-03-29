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


class AuditLogEventActor(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The entity that triggered the event. Will typically be a user.
    """


    class MetaOapg:
        
        class properties:
            
            
            class actor_type(
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
            gid = schemas.StrSchema
            name = schemas.StrSchema
            email = schemas.StrSchema
            __annotations__ = {
                "actor_type": actor_type,
                "gid": gid,
                "name": name,
                "email": email,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["actor_type"]) -> MetaOapg.properties.actor_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gid"]) -> MetaOapg.properties.gid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["actor_type", "gid", "name", "email", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["actor_type"]) -> typing.Union[MetaOapg.properties.actor_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gid"]) -> typing.Union[MetaOapg.properties.gid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> typing.Union[MetaOapg.properties.email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["actor_type", "gid", "name", "email", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        actor_type: typing.Union[MetaOapg.properties.actor_type, str, schemas.Unset] = schemas.unset,
        gid: typing.Union[MetaOapg.properties.gid, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        email: typing.Union[MetaOapg.properties.email, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AuditLogEventActor':
        return super().__new__(
            cls,
            *args,
            actor_type=actor_type,
            gid=gid,
            name=name,
            email=email,
            _configuration=_configuration,
            **kwargs,
        )
