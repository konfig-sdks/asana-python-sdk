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


class WebhookResponse(
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
                    last_failure_at = schemas.DateTimeSchema
                    last_failure_content = schemas.StrSchema
                    last_success_at = schemas.DateTimeSchema
                    
                    
                    class filters(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            
                            class items(
                                schemas.ComposedSchema,
                            ):
                            
                            
                                class MetaOapg:
                                    all_of_1 = schemas.AnyTypeSchema
                                    all_of_2 = schemas.DictSchema
                                    
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
                                            WebhookFilter,
                                            cls.all_of_1,
                                            cls.all_of_2,
                                        ]
                            
                            
                                def __new__(
                                    cls,
                                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                                    _configuration: typing.Optional[schemas.Configuration] = None,
                                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                                ) -> 'items':
                                    return super().__new__(
                                        cls,
                                        *args,
                                        _configuration=_configuration,
                                        **kwargs,
                                    )
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'filters':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> MetaOapg.items:
                            return super().__getitem__(i)
                    __annotations__ = {
                        "created_at": created_at,
                        "last_failure_at": last_failure_at,
                        "last_failure_content": last_failure_content,
                        "last_success_at": last_success_at,
                        "filters": filters,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["last_failure_at"]) -> MetaOapg.properties.last_failure_at: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["last_failure_content"]) -> MetaOapg.properties.last_failure_content: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["last_success_at"]) -> MetaOapg.properties.last_success_at: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["filters"]) -> MetaOapg.properties.filters: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["created_at", "last_failure_at", "last_failure_content", "last_success_at", "filters", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> typing.Union[MetaOapg.properties.created_at, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["last_failure_at"]) -> typing.Union[MetaOapg.properties.last_failure_at, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["last_failure_content"]) -> typing.Union[MetaOapg.properties.last_failure_content, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["last_success_at"]) -> typing.Union[MetaOapg.properties.last_success_at, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["filters"]) -> typing.Union[MetaOapg.properties.filters, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["created_at", "last_failure_at", "last_failure_content", "last_success_at", "filters", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                created_at: typing.Union[MetaOapg.properties.created_at, str, datetime, schemas.Unset] = schemas.unset,
                last_failure_at: typing.Union[MetaOapg.properties.last_failure_at, str, datetime, schemas.Unset] = schemas.unset,
                last_failure_content: typing.Union[MetaOapg.properties.last_failure_content, str, schemas.Unset] = schemas.unset,
                last_success_at: typing.Union[MetaOapg.properties.last_success_at, str, datetime, schemas.Unset] = schemas.unset,
                filters: typing.Union[MetaOapg.properties.filters, list, tuple, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_1':
                return super().__new__(
                    cls,
                    *args,
                    created_at=created_at,
                    last_failure_at=last_failure_at,
                    last_failure_content=last_failure_content,
                    last_success_at=last_success_at,
                    filters=filters,
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
                WebhookCompact,
                cls.all_of_1,
            ]


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'WebhookResponse':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from asana_python_sdk.model.webhook_compact import WebhookCompact
from asana_python_sdk.model.webhook_filter import WebhookFilter
