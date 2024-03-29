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


class ProjectDuplicateRequestScheduleDates(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    A dictionary of options to auto-shift dates. `task_dates` must be included to use this option. Requires either `start_on` or `due_on`, but not both.
    """


    class MetaOapg:
        required = {
            "should_skip_weekends",
        }
        
        class properties:
            should_skip_weekends = schemas.BoolSchema
            due_on = schemas.StrSchema
            start_on = schemas.StrSchema
            __annotations__ = {
                "should_skip_weekends": should_skip_weekends,
                "due_on": due_on,
                "start_on": start_on,
            }
    
    should_skip_weekends: MetaOapg.properties.should_skip_weekends
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["should_skip_weekends"]) -> MetaOapg.properties.should_skip_weekends: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["due_on"]) -> MetaOapg.properties.due_on: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["start_on"]) -> MetaOapg.properties.start_on: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["should_skip_weekends", "due_on", "start_on", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["should_skip_weekends"]) -> MetaOapg.properties.should_skip_weekends: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["due_on"]) -> typing.Union[MetaOapg.properties.due_on, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["start_on"]) -> typing.Union[MetaOapg.properties.start_on, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["should_skip_weekends", "due_on", "start_on", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        should_skip_weekends: typing.Union[MetaOapg.properties.should_skip_weekends, bool, ],
        due_on: typing.Union[MetaOapg.properties.due_on, str, schemas.Unset] = schemas.unset,
        start_on: typing.Union[MetaOapg.properties.start_on, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ProjectDuplicateRequestScheduleDates':
        return super().__new__(
            cls,
            *args,
            should_skip_weekends=should_skip_weekends,
            due_on=due_on,
            start_on=start_on,
            _configuration=_configuration,
            **kwargs,
        )
