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


class SectionTaskInsertRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "task",
        }
        
        class properties:
            task = schemas.StrSchema
            insert_before = schemas.StrSchema
            insert_after = schemas.StrSchema
            __annotations__ = {
                "task": task,
                "insert_before": insert_before,
                "insert_after": insert_after,
            }
    
    task: MetaOapg.properties.task
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["task"]) -> MetaOapg.properties.task: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["insert_before"]) -> MetaOapg.properties.insert_before: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["insert_after"]) -> MetaOapg.properties.insert_after: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["task", "insert_before", "insert_after", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["task"]) -> MetaOapg.properties.task: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["insert_before"]) -> typing.Union[MetaOapg.properties.insert_before, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["insert_after"]) -> typing.Union[MetaOapg.properties.insert_after, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["task", "insert_before", "insert_after", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        task: typing.Union[MetaOapg.properties.task, str, ],
        insert_before: typing.Union[MetaOapg.properties.insert_before, str, schemas.Unset] = schemas.unset,
        insert_after: typing.Union[MetaOapg.properties.insert_after, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SectionTaskInsertRequest':
        return super().__new__(
            cls,
            *args,
            task=task,
            insert_before=insert_before,
            insert_after=insert_after,
            _configuration=_configuration,
            **kwargs,
        )
