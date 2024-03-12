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


class WorkspaceMembershipResponse(
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
                
                    @staticmethod
                    def user_task_list() -> typing.Type['UserTaskListCompact']:
                        return UserTaskListCompact
                    is_active = schemas.BoolSchema
                    is_admin = schemas.BoolSchema
                    is_guest = schemas.BoolSchema
                    
                    
                    class vacation_dates(
                        schemas.DictBase,
                        schemas.NoneBase,
                        schemas.Schema,
                        schemas.NoneFrozenDictMixin
                    ):
                    
                    
                        class MetaOapg:
                            
                            class properties:
                                start_on = schemas.StrSchema
                                
                                
                                class end_on(
                                    schemas.StrBase,
                                    schemas.NoneBase,
                                    schemas.Schema,
                                    schemas.NoneStrMixin
                                ):
                                
                                
                                    def __new__(
                                        cls,
                                        *args: typing.Union[None, str, ],
                                        _configuration: typing.Optional[schemas.Configuration] = None,
                                    ) -> 'end_on':
                                        return super().__new__(
                                            cls,
                                            *args,
                                            _configuration=_configuration,
                                        )
                                __annotations__ = {
                                    "start_on": start_on,
                                    "end_on": end_on,
                                }
                    
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["start_on"]) -> MetaOapg.properties.start_on: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["end_on"]) -> MetaOapg.properties.end_on: ...
                        
                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                        
                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["start_on", "end_on", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["start_on"]) -> typing.Union[MetaOapg.properties.start_on, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["end_on"]) -> typing.Union[MetaOapg.properties.end_on, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                        
                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["start_on", "end_on", ], str]):
                            return super().get_item_oapg(name)
                        
                    
                        def __new__(
                            cls,
                            *args: typing.Union[dict, frozendict.frozendict, None, ],
                            start_on: typing.Union[MetaOapg.properties.start_on, str, schemas.Unset] = schemas.unset,
                            end_on: typing.Union[MetaOapg.properties.end_on, None, str, schemas.Unset] = schemas.unset,
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'vacation_dates':
                            return super().__new__(
                                cls,
                                *args,
                                start_on=start_on,
                                end_on=end_on,
                                _configuration=_configuration,
                                **kwargs,
                            )
                    created_at = schemas.DateTimeSchema
                    __annotations__ = {
                        "user_task_list": user_task_list,
                        "is_active": is_active,
                        "is_admin": is_admin,
                        "is_guest": is_guest,
                        "vacation_dates": vacation_dates,
                        "created_at": created_at,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["user_task_list"]) -> 'UserTaskListCompact': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["is_active"]) -> MetaOapg.properties.is_active: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["is_admin"]) -> MetaOapg.properties.is_admin: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["is_guest"]) -> MetaOapg.properties.is_guest: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["vacation_dates"]) -> MetaOapg.properties.vacation_dates: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["user_task_list", "is_active", "is_admin", "is_guest", "vacation_dates", "created_at", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["user_task_list"]) -> typing.Union['UserTaskListCompact', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["is_active"]) -> typing.Union[MetaOapg.properties.is_active, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["is_admin"]) -> typing.Union[MetaOapg.properties.is_admin, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["is_guest"]) -> typing.Union[MetaOapg.properties.is_guest, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["vacation_dates"]) -> typing.Union[MetaOapg.properties.vacation_dates, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> typing.Union[MetaOapg.properties.created_at, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["user_task_list", "is_active", "is_admin", "is_guest", "vacation_dates", "created_at", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                user_task_list: typing.Union['UserTaskListCompact', schemas.Unset] = schemas.unset,
                is_active: typing.Union[MetaOapg.properties.is_active, bool, schemas.Unset] = schemas.unset,
                is_admin: typing.Union[MetaOapg.properties.is_admin, bool, schemas.Unset] = schemas.unset,
                is_guest: typing.Union[MetaOapg.properties.is_guest, bool, schemas.Unset] = schemas.unset,
                vacation_dates: typing.Union[MetaOapg.properties.vacation_dates, dict, frozendict.frozendict, None, schemas.Unset] = schemas.unset,
                created_at: typing.Union[MetaOapg.properties.created_at, str, datetime, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_1':
                return super().__new__(
                    cls,
                    *args,
                    user_task_list=user_task_list,
                    is_active=is_active,
                    is_admin=is_admin,
                    is_guest=is_guest,
                    vacation_dates=vacation_dates,
                    created_at=created_at,
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
                WorkspaceMembershipCompact,
                cls.all_of_1,
            ]


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'WorkspaceMembershipResponse':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from asana_python_sdk.model.user_task_list_compact import UserTaskListCompact
from asana_python_sdk.model.workspace_membership_compact import WorkspaceMembershipCompact