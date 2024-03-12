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


class ProjectMembershipCompact(
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
                    def parent() -> typing.Type['ProjectCompact']:
                        return ProjectCompact
                
                    @staticmethod
                    def member() -> typing.Type['MemberCompact']:
                        return MemberCompact
                    
                    
                    class access_level(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "admin": "ADMIN",
                                "editor": "EDITOR",
                                "commenter": "COMMENTER",
                                "viewer": "VIEWER",
                            }
                        
                        @schemas.classproperty
                        def ADMIN(cls):
                            return cls("admin")
                        
                        @schemas.classproperty
                        def EDITOR(cls):
                            return cls("editor")
                        
                        @schemas.classproperty
                        def COMMENTER(cls):
                            return cls("commenter")
                        
                        @schemas.classproperty
                        def VIEWER(cls):
                            return cls("viewer")
                    __annotations__ = {
                        "parent": parent,
                        "member": member,
                        "access_level": access_level,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["parent"]) -> 'ProjectCompact': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["member"]) -> 'MemberCompact': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["access_level"]) -> MetaOapg.properties.access_level: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["parent", "member", "access_level", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["parent"]) -> typing.Union['ProjectCompact', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["member"]) -> typing.Union['MemberCompact', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["access_level"]) -> typing.Union[MetaOapg.properties.access_level, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["parent", "member", "access_level", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                parent: typing.Union['ProjectCompact', schemas.Unset] = schemas.unset,
                member: typing.Union['MemberCompact', schemas.Unset] = schemas.unset,
                access_level: typing.Union[MetaOapg.properties.access_level, str, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_1':
                return super().__new__(
                    cls,
                    *args,
                    parent=parent,
                    member=member,
                    access_level=access_level,
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
    ) -> 'ProjectMembershipCompact':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from asana_python_sdk.model.asana_resource import AsanaResource
from asana_python_sdk.model.member_compact import MemberCompact
from asana_python_sdk.model.project_compact import ProjectCompact
