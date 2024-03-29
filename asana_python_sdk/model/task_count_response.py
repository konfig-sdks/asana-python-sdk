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


class TaskCountResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    A response object returned from the task count endpoint.
    """


    class MetaOapg:
        
        class properties:
            num_tasks = schemas.IntSchema
            num_incomplete_tasks = schemas.IntSchema
            num_completed_tasks = schemas.IntSchema
            num_milestones = schemas.IntSchema
            num_incomplete_milestones = schemas.IntSchema
            num_completed_milestones = schemas.IntSchema
            __annotations__ = {
                "num_tasks": num_tasks,
                "num_incomplete_tasks": num_incomplete_tasks,
                "num_completed_tasks": num_completed_tasks,
                "num_milestones": num_milestones,
                "num_incomplete_milestones": num_incomplete_milestones,
                "num_completed_milestones": num_completed_milestones,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["num_tasks"]) -> MetaOapg.properties.num_tasks: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["num_incomplete_tasks"]) -> MetaOapg.properties.num_incomplete_tasks: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["num_completed_tasks"]) -> MetaOapg.properties.num_completed_tasks: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["num_milestones"]) -> MetaOapg.properties.num_milestones: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["num_incomplete_milestones"]) -> MetaOapg.properties.num_incomplete_milestones: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["num_completed_milestones"]) -> MetaOapg.properties.num_completed_milestones: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["num_tasks", "num_incomplete_tasks", "num_completed_tasks", "num_milestones", "num_incomplete_milestones", "num_completed_milestones", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["num_tasks"]) -> typing.Union[MetaOapg.properties.num_tasks, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["num_incomplete_tasks"]) -> typing.Union[MetaOapg.properties.num_incomplete_tasks, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["num_completed_tasks"]) -> typing.Union[MetaOapg.properties.num_completed_tasks, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["num_milestones"]) -> typing.Union[MetaOapg.properties.num_milestones, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["num_incomplete_milestones"]) -> typing.Union[MetaOapg.properties.num_incomplete_milestones, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["num_completed_milestones"]) -> typing.Union[MetaOapg.properties.num_completed_milestones, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["num_tasks", "num_incomplete_tasks", "num_completed_tasks", "num_milestones", "num_incomplete_milestones", "num_completed_milestones", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        num_tasks: typing.Union[MetaOapg.properties.num_tasks, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        num_incomplete_tasks: typing.Union[MetaOapg.properties.num_incomplete_tasks, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        num_completed_tasks: typing.Union[MetaOapg.properties.num_completed_tasks, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        num_milestones: typing.Union[MetaOapg.properties.num_milestones, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        num_incomplete_milestones: typing.Union[MetaOapg.properties.num_incomplete_milestones, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        num_completed_milestones: typing.Union[MetaOapg.properties.num_completed_milestones, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TaskCountResponse':
        return super().__new__(
            cls,
            *args,
            num_tasks=num_tasks,
            num_incomplete_tasks=num_incomplete_tasks,
            num_completed_tasks=num_completed_tasks,
            num_milestones=num_milestones,
            num_incomplete_milestones=num_incomplete_milestones,
            num_completed_milestones=num_completed_milestones,
            _configuration=_configuration,
            **kwargs,
        )
