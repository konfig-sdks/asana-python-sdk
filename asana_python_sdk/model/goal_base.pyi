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


class GoalBase(
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
                    html_notes = schemas.StrSchema
                    notes = schemas.StrSchema
                    
                    
                    class due_on(
                        schemas.StrBase,
                        schemas.NoneBase,
                        schemas.Schema,
                        schemas.NoneStrMixin
                    ):
                    
                    
                        def __new__(
                            cls,
                            *args: typing.Union[None, str, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'due_on':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                            )
                    
                    
                    class start_on(
                        schemas.StrBase,
                        schemas.NoneBase,
                        schemas.Schema,
                        schemas.NoneStrMixin
                    ):
                    
                    
                        def __new__(
                            cls,
                            *args: typing.Union[None, str, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'start_on':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                            )
                    is_workspace_level = schemas.BoolSchema
                    liked = schemas.BoolSchema
                    __annotations__ = {
                        "name": name,
                        "html_notes": html_notes,
                        "notes": notes,
                        "due_on": due_on,
                        "start_on": start_on,
                        "is_workspace_level": is_workspace_level,
                        "liked": liked,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["html_notes"]) -> MetaOapg.properties.html_notes: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["notes"]) -> MetaOapg.properties.notes: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["due_on"]) -> MetaOapg.properties.due_on: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["start_on"]) -> MetaOapg.properties.start_on: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["is_workspace_level"]) -> MetaOapg.properties.is_workspace_level: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["liked"]) -> MetaOapg.properties.liked: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "html_notes", "notes", "due_on", "start_on", "is_workspace_level", "liked", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["html_notes"]) -> typing.Union[MetaOapg.properties.html_notes, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["notes"]) -> typing.Union[MetaOapg.properties.notes, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["due_on"]) -> typing.Union[MetaOapg.properties.due_on, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["start_on"]) -> typing.Union[MetaOapg.properties.start_on, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["is_workspace_level"]) -> typing.Union[MetaOapg.properties.is_workspace_level, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["liked"]) -> typing.Union[MetaOapg.properties.liked, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "html_notes", "notes", "due_on", "start_on", "is_workspace_level", "liked", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
                html_notes: typing.Union[MetaOapg.properties.html_notes, str, schemas.Unset] = schemas.unset,
                notes: typing.Union[MetaOapg.properties.notes, str, schemas.Unset] = schemas.unset,
                due_on: typing.Union[MetaOapg.properties.due_on, None, str, schemas.Unset] = schemas.unset,
                start_on: typing.Union[MetaOapg.properties.start_on, None, str, schemas.Unset] = schemas.unset,
                is_workspace_level: typing.Union[MetaOapg.properties.is_workspace_level, bool, schemas.Unset] = schemas.unset,
                liked: typing.Union[MetaOapg.properties.liked, bool, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_1':
                return super().__new__(
                    cls,
                    *args,
                    name=name,
                    html_notes=html_notes,
                    notes=notes,
                    due_on=due_on,
                    start_on=start_on,
                    is_workspace_level=is_workspace_level,
                    liked=liked,
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
    ) -> 'GoalBase':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from asana_python_sdk.model.asana_resource import AsanaResource
