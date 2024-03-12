# coding: utf-8

"""
    Asana

    This is the interface for interacting with the [Asana Platform](https://developers.asana.com). Our API reference is generated from our [OpenAPI spec] (https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml).

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


class CustomFieldCompact(
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
                    name = schemas.StrSchema
                    
                    
                    class resource_subtype(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                        
                        @schemas.classproperty
                        def TEXT(cls):
                            return cls("text")
                        
                        @schemas.classproperty
                        def ENUM(cls):
                            return cls("enum")
                        
                        @schemas.classproperty
                        def MULTI_ENUM(cls):
                            return cls("multi_enum")
                        
                        @schemas.classproperty
                        def NUMBER(cls):
                            return cls("number")
                        
                        @schemas.classproperty
                        def DATE(cls):
                            return cls("date")
                        
                        @schemas.classproperty
                        def PEOPLE(cls):
                            return cls("people")
                    
                    
                    class type(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                        
                        @schemas.classproperty
                        def TEXT(cls):
                            return cls("text")
                        
                        @schemas.classproperty
                        def ENUM(cls):
                            return cls("enum")
                        
                        @schemas.classproperty
                        def MULTI_ENUM(cls):
                            return cls("multi_enum")
                        
                        @schemas.classproperty
                        def NUMBER(cls):
                            return cls("number")
                        
                        @schemas.classproperty
                        def DATE(cls):
                            return cls("date")
                        
                        @schemas.classproperty
                        def PEOPLE(cls):
                            return cls("people")
                    
                    
                    class enum_options(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            @staticmethod
                            def items() -> typing.Type['EnumOption']:
                                return EnumOption
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple['EnumOption'], typing.List['EnumOption']],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'enum_options':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> 'EnumOption':
                            return super().__getitem__(i)
                    enabled = schemas.BoolSchema
                    
                    
                    class representation_type(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                        
                        @schemas.classproperty
                        def TEXT(cls):
                            return cls("text")
                        
                        @schemas.classproperty
                        def ENUM(cls):
                            return cls("enum")
                        
                        @schemas.classproperty
                        def MULTI_ENUM(cls):
                            return cls("multi_enum")
                        
                        @schemas.classproperty
                        def NUMBER(cls):
                            return cls("number")
                        
                        @schemas.classproperty
                        def DATE(cls):
                            return cls("date")
                        
                        @schemas.classproperty
                        def PEOPLE(cls):
                            return cls("people")
                        
                        @schemas.classproperty
                        def FORMULA(cls):
                            return cls("formula")
                        
                        @schemas.classproperty
                        def CUSTOM_ID(cls):
                            return cls("custom_id")
                    
                    
                    class id_prefix(
                        schemas.StrBase,
                        schemas.NoneBase,
                        schemas.Schema,
                        schemas.NoneStrMixin
                    ):
                    
                    
                        def __new__(
                            cls,
                            *args: typing.Union[None, str, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'id_prefix':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                            )
                    is_formula_field = schemas.BoolSchema
                    
                    
                    class date_value(
                        schemas.DictBase,
                        schemas.NoneBase,
                        schemas.Schema,
                        schemas.NoneFrozenDictMixin
                    ):
                    
                    
                        class MetaOapg:
                            
                            class properties:
                                date = schemas.StrSchema
                                date_time = schemas.StrSchema
                                __annotations__ = {
                                    "date": date,
                                    "date_time": date_time,
                                }
                    
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["date"]) -> MetaOapg.properties.date: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["date_time"]) -> MetaOapg.properties.date_time: ...
                        
                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                        
                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["date", "date_time", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["date"]) -> typing.Union[MetaOapg.properties.date, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["date_time"]) -> typing.Union[MetaOapg.properties.date_time, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                        
                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["date", "date_time", ], str]):
                            return super().get_item_oapg(name)
                        
                    
                        def __new__(
                            cls,
                            *args: typing.Union[dict, frozendict.frozendict, None, ],
                            date: typing.Union[MetaOapg.properties.date, str, schemas.Unset] = schemas.unset,
                            date_time: typing.Union[MetaOapg.properties.date_time, str, schemas.Unset] = schemas.unset,
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'date_value':
                            return super().__new__(
                                cls,
                                *args,
                                date=date,
                                date_time=date_time,
                                _configuration=_configuration,
                                **kwargs,
                            )
                    
                    
                    class enum_value(
                        schemas.ComposedSchema,
                    ):
                    
                    
                        class MetaOapg:
                            
                            
                            class all_of_1(
                                schemas.DictBase,
                                schemas.NoneBase,
                                schemas.Schema,
                                schemas.NoneFrozenDictMixin
                            ):
                            
                            
                                def __new__(
                                    cls,
                                    *args: typing.Union[dict, frozendict.frozendict, None, ],
                                    _configuration: typing.Optional[schemas.Configuration] = None,
                                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                                ) -> 'all_of_1':
                                    return super().__new__(
                                        cls,
                                        *args,
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
                                    EnumOption,
                                    cls.all_of_1,
                                ]
                    
                    
                        def __new__(
                            cls,
                            *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'enum_value':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                                **kwargs,
                            )
                    
                    
                    class multi_enum_values(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            @staticmethod
                            def items() -> typing.Type['EnumOption']:
                                return EnumOption
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple['EnumOption'], typing.List['EnumOption']],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'multi_enum_values':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> 'EnumOption':
                            return super().__getitem__(i)
                    
                    
                    class number_value(
                        schemas.NumberBase,
                        schemas.NoneBase,
                        schemas.Schema,
                        schemas.NoneDecimalMixin
                    ):
                    
                    
                        def __new__(
                            cls,
                            *args: typing.Union[None, decimal.Decimal, int, float, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'number_value':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                            )
                    
                    
                    class text_value(
                        schemas.StrBase,
                        schemas.NoneBase,
                        schemas.Schema,
                        schemas.NoneStrMixin
                    ):
                    
                    
                        def __new__(
                            cls,
                            *args: typing.Union[None, str, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'text_value':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                            )
                    
                    
                    class display_value(
                        schemas.StrBase,
                        schemas.NoneBase,
                        schemas.Schema,
                        schemas.NoneStrMixin
                    ):
                    
                    
                        def __new__(
                            cls,
                            *args: typing.Union[None, str, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'display_value':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                            )
                    __annotations__ = {
                        "name": name,
                        "resource_subtype": resource_subtype,
                        "type": type,
                        "enum_options": enum_options,
                        "enabled": enabled,
                        "representation_type": representation_type,
                        "id_prefix": id_prefix,
                        "is_formula_field": is_formula_field,
                        "date_value": date_value,
                        "enum_value": enum_value,
                        "multi_enum_values": multi_enum_values,
                        "number_value": number_value,
                        "text_value": text_value,
                        "display_value": display_value,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["resource_subtype"]) -> MetaOapg.properties.resource_subtype: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["enum_options"]) -> MetaOapg.properties.enum_options: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["enabled"]) -> MetaOapg.properties.enabled: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["representation_type"]) -> MetaOapg.properties.representation_type: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["id_prefix"]) -> MetaOapg.properties.id_prefix: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["is_formula_field"]) -> MetaOapg.properties.is_formula_field: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["date_value"]) -> MetaOapg.properties.date_value: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["enum_value"]) -> MetaOapg.properties.enum_value: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["multi_enum_values"]) -> MetaOapg.properties.multi_enum_values: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["number_value"]) -> MetaOapg.properties.number_value: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["text_value"]) -> MetaOapg.properties.text_value: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["display_value"]) -> MetaOapg.properties.display_value: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "resource_subtype", "type", "enum_options", "enabled", "representation_type", "id_prefix", "is_formula_field", "date_value", "enum_value", "multi_enum_values", "number_value", "text_value", "display_value", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["resource_subtype"]) -> typing.Union[MetaOapg.properties.resource_subtype, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["enum_options"]) -> typing.Union[MetaOapg.properties.enum_options, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["enabled"]) -> typing.Union[MetaOapg.properties.enabled, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["representation_type"]) -> typing.Union[MetaOapg.properties.representation_type, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["id_prefix"]) -> typing.Union[MetaOapg.properties.id_prefix, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["is_formula_field"]) -> typing.Union[MetaOapg.properties.is_formula_field, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["date_value"]) -> typing.Union[MetaOapg.properties.date_value, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["enum_value"]) -> typing.Union[MetaOapg.properties.enum_value, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["multi_enum_values"]) -> typing.Union[MetaOapg.properties.multi_enum_values, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["number_value"]) -> typing.Union[MetaOapg.properties.number_value, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["text_value"]) -> typing.Union[MetaOapg.properties.text_value, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["display_value"]) -> typing.Union[MetaOapg.properties.display_value, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "resource_subtype", "type", "enum_options", "enabled", "representation_type", "id_prefix", "is_formula_field", "date_value", "enum_value", "multi_enum_values", "number_value", "text_value", "display_value", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
                resource_subtype: typing.Union[MetaOapg.properties.resource_subtype, str, schemas.Unset] = schemas.unset,
                type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
                enum_options: typing.Union[MetaOapg.properties.enum_options, list, tuple, schemas.Unset] = schemas.unset,
                enabled: typing.Union[MetaOapg.properties.enabled, bool, schemas.Unset] = schemas.unset,
                representation_type: typing.Union[MetaOapg.properties.representation_type, str, schemas.Unset] = schemas.unset,
                id_prefix: typing.Union[MetaOapg.properties.id_prefix, None, str, schemas.Unset] = schemas.unset,
                is_formula_field: typing.Union[MetaOapg.properties.is_formula_field, bool, schemas.Unset] = schemas.unset,
                date_value: typing.Union[MetaOapg.properties.date_value, dict, frozendict.frozendict, None, schemas.Unset] = schemas.unset,
                enum_value: typing.Union[MetaOapg.properties.enum_value, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
                multi_enum_values: typing.Union[MetaOapg.properties.multi_enum_values, list, tuple, schemas.Unset] = schemas.unset,
                number_value: typing.Union[MetaOapg.properties.number_value, None, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
                text_value: typing.Union[MetaOapg.properties.text_value, None, str, schemas.Unset] = schemas.unset,
                display_value: typing.Union[MetaOapg.properties.display_value, None, str, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_1':
                return super().__new__(
                    cls,
                    *args,
                    name=name,
                    resource_subtype=resource_subtype,
                    type=type,
                    enum_options=enum_options,
                    enabled=enabled,
                    representation_type=representation_type,
                    id_prefix=id_prefix,
                    is_formula_field=is_formula_field,
                    date_value=date_value,
                    enum_value=enum_value,
                    multi_enum_values=multi_enum_values,
                    number_value=number_value,
                    text_value=text_value,
                    display_value=display_value,
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
    ) -> 'CustomFieldCompact':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from asana_python_sdk.model.asana_resource import AsanaResource
from asana_python_sdk.model.enum_option import EnumOption
