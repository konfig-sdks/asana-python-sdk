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


class TeamRequest(
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
                    description = schemas.StrSchema
                    html_description = schemas.StrSchema
                    organization = schemas.StrSchema
                    
                    
                    class visibility(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                        
                        @schemas.classproperty
                        def SECRET(cls):
                            return cls("secret")
                        
                        @schemas.classproperty
                        def REQUEST_TO_JOIN(cls):
                            return cls("request_to_join")
                        
                        @schemas.classproperty
                        def PUBLIC(cls):
                            return cls("public")
                    
                    
                    class edit_team_name_or_description_access_level(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                        
                        @schemas.classproperty
                        def ALL_TEAM_MEMBERS(cls):
                            return cls("all_team_members")
                        
                        @schemas.classproperty
                        def ONLY_TEAM_ADMINS(cls):
                            return cls("only_team_admins")
                    
                    
                    class edit_team_visibility_or_trash_team_access_level(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                        
                        @schemas.classproperty
                        def ALL_TEAM_MEMBERS(cls):
                            return cls("all_team_members")
                        
                        @schemas.classproperty
                        def ONLY_TEAM_ADMINS(cls):
                            return cls("only_team_admins")
                    
                    
                    class member_invite_management_access_level(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                        
                        @schemas.classproperty
                        def ALL_TEAM_MEMBERS(cls):
                            return cls("all_team_members")
                        
                        @schemas.classproperty
                        def ONLY_TEAM_ADMINS(cls):
                            return cls("only_team_admins")
                    
                    
                    class guest_invite_management_access_level(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                        
                        @schemas.classproperty
                        def ALL_TEAM_MEMBERS(cls):
                            return cls("all_team_members")
                        
                        @schemas.classproperty
                        def ONLY_TEAM_ADMINS(cls):
                            return cls("only_team_admins")
                    
                    
                    class join_request_management_access_level(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                        
                        @schemas.classproperty
                        def ALL_TEAM_MEMBERS(cls):
                            return cls("all_team_members")
                        
                        @schemas.classproperty
                        def ONLY_TEAM_ADMINS(cls):
                            return cls("only_team_admins")
                    
                    
                    class team_member_removal_access_level(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                        
                        @schemas.classproperty
                        def ALL_TEAM_MEMBERS(cls):
                            return cls("all_team_members")
                        
                        @schemas.classproperty
                        def ONLY_TEAM_ADMINS(cls):
                            return cls("only_team_admins")
                    __annotations__ = {
                        "description": description,
                        "html_description": html_description,
                        "organization": organization,
                        "visibility": visibility,
                        "edit_team_name_or_description_access_level": edit_team_name_or_description_access_level,
                        "edit_team_visibility_or_trash_team_access_level": edit_team_visibility_or_trash_team_access_level,
                        "member_invite_management_access_level": member_invite_management_access_level,
                        "guest_invite_management_access_level": guest_invite_management_access_level,
                        "join_request_management_access_level": join_request_management_access_level,
                        "team_member_removal_access_level": team_member_removal_access_level,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["html_description"]) -> MetaOapg.properties.html_description: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["organization"]) -> MetaOapg.properties.organization: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["visibility"]) -> MetaOapg.properties.visibility: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["edit_team_name_or_description_access_level"]) -> MetaOapg.properties.edit_team_name_or_description_access_level: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["edit_team_visibility_or_trash_team_access_level"]) -> MetaOapg.properties.edit_team_visibility_or_trash_team_access_level: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["member_invite_management_access_level"]) -> MetaOapg.properties.member_invite_management_access_level: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["guest_invite_management_access_level"]) -> MetaOapg.properties.guest_invite_management_access_level: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["join_request_management_access_level"]) -> MetaOapg.properties.join_request_management_access_level: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["team_member_removal_access_level"]) -> MetaOapg.properties.team_member_removal_access_level: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "html_description", "organization", "visibility", "edit_team_name_or_description_access_level", "edit_team_visibility_or_trash_team_access_level", "member_invite_management_access_level", "guest_invite_management_access_level", "join_request_management_access_level", "team_member_removal_access_level", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["html_description"]) -> typing.Union[MetaOapg.properties.html_description, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["organization"]) -> typing.Union[MetaOapg.properties.organization, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["visibility"]) -> typing.Union[MetaOapg.properties.visibility, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["edit_team_name_or_description_access_level"]) -> typing.Union[MetaOapg.properties.edit_team_name_or_description_access_level, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["edit_team_visibility_or_trash_team_access_level"]) -> typing.Union[MetaOapg.properties.edit_team_visibility_or_trash_team_access_level, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["member_invite_management_access_level"]) -> typing.Union[MetaOapg.properties.member_invite_management_access_level, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["guest_invite_management_access_level"]) -> typing.Union[MetaOapg.properties.guest_invite_management_access_level, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["join_request_management_access_level"]) -> typing.Union[MetaOapg.properties.join_request_management_access_level, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["team_member_removal_access_level"]) -> typing.Union[MetaOapg.properties.team_member_removal_access_level, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "html_description", "organization", "visibility", "edit_team_name_or_description_access_level", "edit_team_visibility_or_trash_team_access_level", "member_invite_management_access_level", "guest_invite_management_access_level", "join_request_management_access_level", "team_member_removal_access_level", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
                html_description: typing.Union[MetaOapg.properties.html_description, str, schemas.Unset] = schemas.unset,
                organization: typing.Union[MetaOapg.properties.organization, str, schemas.Unset] = schemas.unset,
                visibility: typing.Union[MetaOapg.properties.visibility, str, schemas.Unset] = schemas.unset,
                edit_team_name_or_description_access_level: typing.Union[MetaOapg.properties.edit_team_name_or_description_access_level, str, schemas.Unset] = schemas.unset,
                edit_team_visibility_or_trash_team_access_level: typing.Union[MetaOapg.properties.edit_team_visibility_or_trash_team_access_level, str, schemas.Unset] = schemas.unset,
                member_invite_management_access_level: typing.Union[MetaOapg.properties.member_invite_management_access_level, str, schemas.Unset] = schemas.unset,
                guest_invite_management_access_level: typing.Union[MetaOapg.properties.guest_invite_management_access_level, str, schemas.Unset] = schemas.unset,
                join_request_management_access_level: typing.Union[MetaOapg.properties.join_request_management_access_level, str, schemas.Unset] = schemas.unset,
                team_member_removal_access_level: typing.Union[MetaOapg.properties.team_member_removal_access_level, str, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_1':
                return super().__new__(
                    cls,
                    *args,
                    description=description,
                    html_description=html_description,
                    organization=organization,
                    visibility=visibility,
                    edit_team_name_or_description_access_level=edit_team_name_or_description_access_level,
                    edit_team_visibility_or_trash_team_access_level=edit_team_visibility_or_trash_team_access_level,
                    member_invite_management_access_level=member_invite_management_access_level,
                    guest_invite_management_access_level=guest_invite_management_access_level,
                    join_request_management_access_level=join_request_management_access_level,
                    team_member_removal_access_level=team_member_removal_access_level,
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
                TeamCompact,
                cls.all_of_1,
            ]


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TeamRequest':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from asana_python_sdk.model.team_compact import TeamCompact
