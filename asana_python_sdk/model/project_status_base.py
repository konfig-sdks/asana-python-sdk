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


class ProjectStatusBase(
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
                    text = schemas.StrSchema
                    html_text = schemas.StrSchema
                    
                    
                    class color(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "green": "GREEN",
                                "yellow": "YELLOW",
                                "red": "RED",
                                "blue": "BLUE",
                                "complete": "COMPLETE",
                            }
                        
                        @schemas.classproperty
                        def GREEN(cls):
                            return cls("green")
                        
                        @schemas.classproperty
                        def YELLOW(cls):
                            return cls("yellow")
                        
                        @schemas.classproperty
                        def RED(cls):
                            return cls("red")
                        
                        @schemas.classproperty
                        def BLUE(cls):
                            return cls("blue")
                        
                        @schemas.classproperty
                        def COMPLETE(cls):
                            return cls("complete")
                    __annotations__ = {
                        "text": text,
                        "html_text": html_text,
                        "color": color,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["text"]) -> MetaOapg.properties.text: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["html_text"]) -> MetaOapg.properties.html_text: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["color"]) -> MetaOapg.properties.color: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["text", "html_text", "color", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["text"]) -> typing.Union[MetaOapg.properties.text, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["html_text"]) -> typing.Union[MetaOapg.properties.html_text, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["color"]) -> typing.Union[MetaOapg.properties.color, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["text", "html_text", "color", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                text: typing.Union[MetaOapg.properties.text, str, schemas.Unset] = schemas.unset,
                html_text: typing.Union[MetaOapg.properties.html_text, str, schemas.Unset] = schemas.unset,
                color: typing.Union[MetaOapg.properties.color, str, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_1':
                return super().__new__(
                    cls,
                    *args,
                    text=text,
                    html_text=html_text,
                    color=color,
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
                ProjectStatusCompact,
                cls.all_of_1,
            ]


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ProjectStatusBase':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from asana_python_sdk.model.project_status_compact import ProjectStatusCompact
