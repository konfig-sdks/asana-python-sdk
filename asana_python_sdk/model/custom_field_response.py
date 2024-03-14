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


class CustomFieldResponse(
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
                    
                    
                    class representation_type(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "text": "TEXT",
                                "enum": "ENUM",
                                "multi_enum": "MULTI_ENUM",
                                "number": "NUMBER",
                                "date": "DATE",
                                "people": "PEOPLE",
                                "formula": "FORMULA",
                                "custom_id": "CUSTOM_ID",
                            }
                        
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
                    is_value_read_only = schemas.BoolSchema
                    
                    
                    class created_by(
                        schemas.ComposedSchema,
                    ):
                    
                    
                        class MetaOapg:
                            all_of_1 = schemas.AnyTypeSchema
                            
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
                                    UserCompact,
                                    cls.all_of_1,
                                ]
                    
                    
                        def __new__(
                            cls,
                            *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'created_by':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                                **kwargs,
                            )
                    
                    
                    class people_value(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            @staticmethod
                            def items() -> typing.Type['UserCompact']:
                                return UserCompact
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple['UserCompact'], typing.List['UserCompact']],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'people_value':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> 'UserCompact':
                            return super().__getitem__(i)
                    __annotations__ = {
                        "representation_type": representation_type,
                        "id_prefix": id_prefix,
                        "is_formula_field": is_formula_field,
                        "is_value_read_only": is_value_read_only,
                        "created_by": created_by,
                        "people_value": people_value,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["representation_type"]) -> MetaOapg.properties.representation_type: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["id_prefix"]) -> MetaOapg.properties.id_prefix: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["is_formula_field"]) -> MetaOapg.properties.is_formula_field: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["is_value_read_only"]) -> MetaOapg.properties.is_value_read_only: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["created_by"]) -> MetaOapg.properties.created_by: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["people_value"]) -> MetaOapg.properties.people_value: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["representation_type", "id_prefix", "is_formula_field", "is_value_read_only", "created_by", "people_value", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["representation_type"]) -> typing.Union[MetaOapg.properties.representation_type, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["id_prefix"]) -> typing.Union[MetaOapg.properties.id_prefix, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["is_formula_field"]) -> typing.Union[MetaOapg.properties.is_formula_field, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["is_value_read_only"]) -> typing.Union[MetaOapg.properties.is_value_read_only, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["created_by"]) -> typing.Union[MetaOapg.properties.created_by, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["people_value"]) -> typing.Union[MetaOapg.properties.people_value, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["representation_type", "id_prefix", "is_formula_field", "is_value_read_only", "created_by", "people_value", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                representation_type: typing.Union[MetaOapg.properties.representation_type, str, schemas.Unset] = schemas.unset,
                id_prefix: typing.Union[MetaOapg.properties.id_prefix, None, str, schemas.Unset] = schemas.unset,
                is_formula_field: typing.Union[MetaOapg.properties.is_formula_field, bool, schemas.Unset] = schemas.unset,
                is_value_read_only: typing.Union[MetaOapg.properties.is_value_read_only, bool, schemas.Unset] = schemas.unset,
                created_by: typing.Union[MetaOapg.properties.created_by, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
                people_value: typing.Union[MetaOapg.properties.people_value, list, tuple, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_1':
                return super().__new__(
                    cls,
                    *args,
                    representation_type=representation_type,
                    id_prefix=id_prefix,
                    is_formula_field=is_formula_field,
                    is_value_read_only=is_value_read_only,
                    created_by=created_by,
                    people_value=people_value,
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
                CustomFieldBase,
                cls.all_of_1,
            ]


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CustomFieldResponse':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from asana_python_sdk.model.custom_field_base import CustomFieldBase
from asana_python_sdk.model.user_compact import UserCompact
