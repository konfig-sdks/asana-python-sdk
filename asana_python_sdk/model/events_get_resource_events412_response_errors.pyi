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


class EventsGetResourceEvents412ResponseErrors(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['EventsGetResourceEvents412ResponseErrorsItem']:
            return EventsGetResourceEvents412ResponseErrorsItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['EventsGetResourceEvents412ResponseErrorsItem'], typing.List['EventsGetResourceEvents412ResponseErrorsItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'EventsGetResourceEvents412ResponseErrors':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'EventsGetResourceEvents412ResponseErrorsItem':
        return super().__getitem__(i)

from asana_python_sdk.model.events_get_resource_events412_response_errors_item import EventsGetResourceEvents412ResponseErrorsItem
