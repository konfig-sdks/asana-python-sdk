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


class ProjectMembershipNormalResponse(
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
                    def user() -> typing.Type['UserCompact']:
                        return UserCompact
                
                    @staticmethod
                    def project() -> typing.Type['ProjectCompact']:
                        return ProjectCompact
                    resource_type = schemas.StrSchema
                    
                    
                    class write_access(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "full_write": "FULL_WRITE",
                                "comment_only": "COMMENT_ONLY",
                            }
                        
                        @schemas.classproperty
                        def FULL_WRITE(cls):
                            return cls("full_write")
                        
                        @schemas.classproperty
                        def COMMENT_ONLY(cls):
                            return cls("comment_only")
                    __annotations__ = {
                        "user": user,
                        "project": project,
                        "resource_type": resource_type,
                        "write_access": write_access,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["user"]) -> 'UserCompact': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["project"]) -> 'ProjectCompact': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["resource_type"]) -> MetaOapg.properties.resource_type: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["write_access"]) -> MetaOapg.properties.write_access: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["user", "project", "resource_type", "write_access", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["user"]) -> typing.Union['UserCompact', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["project"]) -> typing.Union['ProjectCompact', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["resource_type"]) -> typing.Union[MetaOapg.properties.resource_type, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["write_access"]) -> typing.Union[MetaOapg.properties.write_access, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["user", "project", "resource_type", "write_access", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                user: typing.Union['UserCompact', schemas.Unset] = schemas.unset,
                project: typing.Union['ProjectCompact', schemas.Unset] = schemas.unset,
                resource_type: typing.Union[MetaOapg.properties.resource_type, str, schemas.Unset] = schemas.unset,
                write_access: typing.Union[MetaOapg.properties.write_access, str, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_1':
                return super().__new__(
                    cls,
                    *args,
                    user=user,
                    project=project,
                    resource_type=resource_type,
                    write_access=write_access,
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
                ProjectMembershipCompact,
                cls.all_of_1,
            ]


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ProjectMembershipNormalResponse':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from asana_python_sdk.model.project_compact import ProjectCompact
from asana_python_sdk.model.project_membership_compact import ProjectMembershipCompact
from asana_python_sdk.model.user_compact import UserCompact
