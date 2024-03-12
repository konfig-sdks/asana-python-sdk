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


class GoalMetricBase(
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
                    
                    
                    class resource_subtype(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                        
                        @schemas.classproperty
                        def NUMBER(cls):
                            return cls("number")
                    precision = schemas.IntSchema
                    
                    
                    class unit(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                        
                        @schemas.classproperty
                        def NONE(cls):
                            return cls("none")
                        
                        @schemas.classproperty
                        def CURRENCY(cls):
                            return cls("currency")
                        
                        @schemas.classproperty
                        def PERCENTAGE(cls):
                            return cls("percentage")
                    
                    
                    class currency_code(
                        schemas.StrBase,
                        schemas.NoneBase,
                        schemas.Schema,
                        schemas.NoneStrMixin
                    ):
                    
                    
                        def __new__(
                            cls,
                            *args: typing.Union[None, str, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'currency_code':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                            )
                    initial_number_value = schemas.NumberSchema
                    target_number_value = schemas.NumberSchema
                    current_number_value = schemas.NumberSchema
                    current_display_value = schemas.StrSchema
                    
                    
                    class progress_source(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                        
                        @schemas.classproperty
                        def MANUAL(cls):
                            return cls("manual")
                        
                        @schemas.classproperty
                        def SUBGOAL_PROGRESS(cls):
                            return cls("subgoal_progress")
                        
                        @schemas.classproperty
                        def PROJECT_TASK_COMPLETION(cls):
                            return cls("project_task_completion")
                        
                        @schemas.classproperty
                        def PROJECT_MILESTONE_COMPLETION(cls):
                            return cls("project_milestone_completion")
                        
                        @schemas.classproperty
                        def TASK_COMPLETION(cls):
                            return cls("task_completion")
                        
                        @schemas.classproperty
                        def EXTERNAL(cls):
                            return cls("external")
                    __annotations__ = {
                        "resource_subtype": resource_subtype,
                        "precision": precision,
                        "unit": unit,
                        "currency_code": currency_code,
                        "initial_number_value": initial_number_value,
                        "target_number_value": target_number_value,
                        "current_number_value": current_number_value,
                        "current_display_value": current_display_value,
                        "progress_source": progress_source,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["resource_subtype"]) -> MetaOapg.properties.resource_subtype: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["precision"]) -> MetaOapg.properties.precision: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["unit"]) -> MetaOapg.properties.unit: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["currency_code"]) -> MetaOapg.properties.currency_code: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["initial_number_value"]) -> MetaOapg.properties.initial_number_value: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["target_number_value"]) -> MetaOapg.properties.target_number_value: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["current_number_value"]) -> MetaOapg.properties.current_number_value: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["current_display_value"]) -> MetaOapg.properties.current_display_value: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["progress_source"]) -> MetaOapg.properties.progress_source: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["resource_subtype", "precision", "unit", "currency_code", "initial_number_value", "target_number_value", "current_number_value", "current_display_value", "progress_source", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["resource_subtype"]) -> typing.Union[MetaOapg.properties.resource_subtype, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["precision"]) -> typing.Union[MetaOapg.properties.precision, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["unit"]) -> typing.Union[MetaOapg.properties.unit, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["currency_code"]) -> typing.Union[MetaOapg.properties.currency_code, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["initial_number_value"]) -> typing.Union[MetaOapg.properties.initial_number_value, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["target_number_value"]) -> typing.Union[MetaOapg.properties.target_number_value, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["current_number_value"]) -> typing.Union[MetaOapg.properties.current_number_value, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["current_display_value"]) -> typing.Union[MetaOapg.properties.current_display_value, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["progress_source"]) -> typing.Union[MetaOapg.properties.progress_source, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["resource_subtype", "precision", "unit", "currency_code", "initial_number_value", "target_number_value", "current_number_value", "current_display_value", "progress_source", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                resource_subtype: typing.Union[MetaOapg.properties.resource_subtype, str, schemas.Unset] = schemas.unset,
                precision: typing.Union[MetaOapg.properties.precision, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                unit: typing.Union[MetaOapg.properties.unit, str, schemas.Unset] = schemas.unset,
                currency_code: typing.Union[MetaOapg.properties.currency_code, None, str, schemas.Unset] = schemas.unset,
                initial_number_value: typing.Union[MetaOapg.properties.initial_number_value, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
                target_number_value: typing.Union[MetaOapg.properties.target_number_value, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
                current_number_value: typing.Union[MetaOapg.properties.current_number_value, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
                current_display_value: typing.Union[MetaOapg.properties.current_display_value, str, schemas.Unset] = schemas.unset,
                progress_source: typing.Union[MetaOapg.properties.progress_source, str, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_1':
                return super().__new__(
                    cls,
                    *args,
                    resource_subtype=resource_subtype,
                    precision=precision,
                    unit=unit,
                    currency_code=currency_code,
                    initial_number_value=initial_number_value,
                    target_number_value=target_number_value,
                    current_number_value=current_number_value,
                    current_display_value=current_display_value,
                    progress_source=progress_source,
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
    ) -> 'GoalMetricBase':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from asana_python_sdk.model.asana_resource import AsanaResource
