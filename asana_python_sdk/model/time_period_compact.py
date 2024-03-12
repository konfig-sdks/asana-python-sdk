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


class TimePeriodCompact(
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
                    end_on = schemas.StrSchema
                    start_on = schemas.StrSchema
                    
                    
                    class period(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "FY": "FY",
                                "H1": "H1",
                                "H2": "H2",
                                "Q1": "Q1",
                                "Q2": "Q2",
                                "Q3": "Q3",
                                "Q4": "Q4",
                            }
                        
                        @schemas.classproperty
                        def FY(cls):
                            return cls("FY")
                        
                        @schemas.classproperty
                        def H1(cls):
                            return cls("H1")
                        
                        @schemas.classproperty
                        def H2(cls):
                            return cls("H2")
                        
                        @schemas.classproperty
                        def Q1(cls):
                            return cls("Q1")
                        
                        @schemas.classproperty
                        def Q2(cls):
                            return cls("Q2")
                        
                        @schemas.classproperty
                        def Q3(cls):
                            return cls("Q3")
                        
                        @schemas.classproperty
                        def Q4(cls):
                            return cls("Q4")
                    display_name = schemas.StrSchema
                    __annotations__ = {
                        "end_on": end_on,
                        "start_on": start_on,
                        "period": period,
                        "display_name": display_name,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["end_on"]) -> MetaOapg.properties.end_on: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["start_on"]) -> MetaOapg.properties.start_on: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["period"]) -> MetaOapg.properties.period: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["display_name"]) -> MetaOapg.properties.display_name: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["end_on", "start_on", "period", "display_name", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["end_on"]) -> typing.Union[MetaOapg.properties.end_on, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["start_on"]) -> typing.Union[MetaOapg.properties.start_on, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["period"]) -> typing.Union[MetaOapg.properties.period, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["display_name"]) -> typing.Union[MetaOapg.properties.display_name, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["end_on", "start_on", "period", "display_name", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                end_on: typing.Union[MetaOapg.properties.end_on, str, schemas.Unset] = schemas.unset,
                start_on: typing.Union[MetaOapg.properties.start_on, str, schemas.Unset] = schemas.unset,
                period: typing.Union[MetaOapg.properties.period, str, schemas.Unset] = schemas.unset,
                display_name: typing.Union[MetaOapg.properties.display_name, str, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_1':
                return super().__new__(
                    cls,
                    *args,
                    end_on=end_on,
                    start_on=start_on,
                    period=period,
                    display_name=display_name,
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
    ) -> 'TimePeriodCompact':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from asana_python_sdk.model.asana_resource import AsanaResource