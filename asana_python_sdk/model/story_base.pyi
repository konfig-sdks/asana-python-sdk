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


class StoryBase(
    schemas.ComposedSchema,
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        
        class all_of_1(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                
                class properties:
                    created_at = schemas.DateTimeSchema
                    resource_subtype = schemas.StrSchema
                    text = schemas.StrSchema
                    html_text = schemas.StrSchema
                    is_pinned = schemas.BoolSchema
                    
                    
                    class sticker_name(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                        
                        @schemas.classproperty
                        def GREEN_CHECKMARK(cls):
                            return cls("green_checkmark")
                        
                        @schemas.classproperty
                        def PEOPLE_DANCING(cls):
                            return cls("people_dancing")
                        
                        @schemas.classproperty
                        def DANCING_UNICORN(cls):
                            return cls("dancing_unicorn")
                        
                        @schemas.classproperty
                        def HEART(cls):
                            return cls("heart")
                        
                        @schemas.classproperty
                        def PARTY_POPPER(cls):
                            return cls("party_popper")
                        
                        @schemas.classproperty
                        def PEOPLE_WAVING_FLAGS(cls):
                            return cls("people_waving_flags")
                        
                        @schemas.classproperty
                        def SPLASHING_NARWHAL(cls):
                            return cls("splashing_narwhal")
                        
                        @schemas.classproperty
                        def TROPHY(cls):
                            return cls("trophy")
                        
                        @schemas.classproperty
                        def YETI_RIDING_UNICORN(cls):
                            return cls("yeti_riding_unicorn")
                        
                        @schemas.classproperty
                        def CELEBRATING_PEOPLE(cls):
                            return cls("celebrating_people")
                        
                        @schemas.classproperty
                        def DETERMINED_CLIMBERS(cls):
                            return cls("determined_climbers")
                        
                        @schemas.classproperty
                        def PHOENIX_SPREADING_LOVE(cls):
                            return cls("phoenix_spreading_love")
                    __annotations__ = {
                        "created_at": created_at,
                        "resource_subtype": resource_subtype,
                        "text": text,
                        "html_text": html_text,
                        "is_pinned": is_pinned,
                        "sticker_name": sticker_name,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["resource_subtype"]) -> MetaOapg.properties.resource_subtype: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["text"]) -> MetaOapg.properties.text: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["html_text"]) -> MetaOapg.properties.html_text: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["is_pinned"]) -> MetaOapg.properties.is_pinned: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["sticker_name"]) -> MetaOapg.properties.sticker_name: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["created_at", "resource_subtype", "text", "html_text", "is_pinned", "sticker_name", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> typing.Union[MetaOapg.properties.created_at, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["resource_subtype"]) -> typing.Union[MetaOapg.properties.resource_subtype, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["text"]) -> typing.Union[MetaOapg.properties.text, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["html_text"]) -> typing.Union[MetaOapg.properties.html_text, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["is_pinned"]) -> typing.Union[MetaOapg.properties.is_pinned, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["sticker_name"]) -> typing.Union[MetaOapg.properties.sticker_name, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["created_at", "resource_subtype", "text", "html_text", "is_pinned", "sticker_name", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                created_at: typing.Union[MetaOapg.properties.created_at, str, datetime, schemas.Unset] = schemas.unset,
                resource_subtype: typing.Union[MetaOapg.properties.resource_subtype, str, schemas.Unset] = schemas.unset,
                text: typing.Union[MetaOapg.properties.text, str, schemas.Unset] = schemas.unset,
                html_text: typing.Union[MetaOapg.properties.html_text, str, schemas.Unset] = schemas.unset,
                is_pinned: typing.Union[MetaOapg.properties.is_pinned, bool, schemas.Unset] = schemas.unset,
                sticker_name: typing.Union[MetaOapg.properties.sticker_name, str, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_1':
                return super().__new__(
                    cls,
                    *args,
                    created_at=created_at,
                    resource_subtype=resource_subtype,
                    text=text,
                    html_text=html_text,
                    is_pinned=is_pinned,
                    sticker_name=sticker_name,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        @classmethod
        @functools.lru_cache()
        def all_of(cls):
            # we need this here to make our import statements work
            # we must store _composed_schemas in here so the code is only run
            # when we invoke this method. If we kept this at the class
            # level we would get an error because the class level
            # code would be run when this module is imported, and these composed
            # classes don't exist yet because their module has not finished
            # loading
            return [
                AsanaResource,
                cls.all_of_1,
            ]


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'StoryBase':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from asana_python_sdk.model.asana_resource import AsanaResource
