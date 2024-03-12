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


class ProjectTemplateBase(
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
                    public = schemas.BoolSchema
                    
                    
                    class owner(
                        schemas.ComposedSchema,
                    ):
                    
                    
                        class MetaOapg:
                            
                            
                            class all_of_1(
                                schemas.DictBase,
                                schemas.NoneBase,
                                schemas.Schema,
                                schemas.NoneFrozenDictMixin
                            ):
                            
                            
                                def __new__(
                                    cls,
                                    *args: typing.Union[dict, frozendict.frozendict, None, ],
                                    _configuration: typing.Optional[schemas.Configuration] = None,
                                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                                ) -> 'all_of_1':
                                    return super().__new__(
                                        cls,
                                        *args,
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
                                    UserCompact,
                                    cls.all_of_1,
                                ]
                    
                    
                        def __new__(
                            cls,
                            *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'owner':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                                **kwargs,
                            )
                
                    @staticmethod
                    def team() -> typing.Type['TeamCompact']:
                        return TeamCompact
                    
                    
                    class requested_dates(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            @staticmethod
                            def items() -> typing.Type['DateVariableCompact']:
                                return DateVariableCompact
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple['DateVariableCompact'], typing.List['DateVariableCompact']],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'requested_dates':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> 'DateVariableCompact':
                            return super().__getitem__(i)
                    
                    
                    class color(
                        schemas.EnumBase,
                        schemas.StrBase,
                        schemas.NoneBase,
                        schemas.Schema,
                        schemas.NoneStrMixin
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "dark-pink": "DARKPINK",
                                "dark-green": "DARKGREEN",
                                "dark-blue": "DARKBLUE",
                                "dark-red": "DARKRED",
                                "dark-teal": "DARKTEAL",
                                "dark-brown": "DARKBROWN",
                                "dark-orange": "DARKORANGE",
                                "dark-purple": "DARKPURPLE",
                                "dark-warm-gray": "DARKWARMGRAY",
                                "light-pink": "LIGHTPINK",
                                "light-green": "LIGHTGREEN",
                                "light-blue": "LIGHTBLUE",
                                "light-red": "LIGHTRED",
                                "light-teal": "LIGHTTEAL",
                                "light-brown": "LIGHTBROWN",
                                "light-orange": "LIGHTORANGE",
                                "light-purple": "LIGHTPURPLE",
                                "light-warm-gray": "LIGHTWARMGRAY",
                                None: "NONE",
                            }
                        
                        @schemas.classproperty
                        def DARKPINK(cls):
                            return cls("dark-pink")
                        
                        @schemas.classproperty
                        def DARKGREEN(cls):
                            return cls("dark-green")
                        
                        @schemas.classproperty
                        def DARKBLUE(cls):
                            return cls("dark-blue")
                        
                        @schemas.classproperty
                        def DARKRED(cls):
                            return cls("dark-red")
                        
                        @schemas.classproperty
                        def DARKTEAL(cls):
                            return cls("dark-teal")
                        
                        @schemas.classproperty
                        def DARKBROWN(cls):
                            return cls("dark-brown")
                        
                        @schemas.classproperty
                        def DARKORANGE(cls):
                            return cls("dark-orange")
                        
                        @schemas.classproperty
                        def DARKPURPLE(cls):
                            return cls("dark-purple")
                        
                        @schemas.classproperty
                        def DARKWARMGRAY(cls):
                            return cls("dark-warm-gray")
                        
                        @schemas.classproperty
                        def LIGHTPINK(cls):
                            return cls("light-pink")
                        
                        @schemas.classproperty
                        def LIGHTGREEN(cls):
                            return cls("light-green")
                        
                        @schemas.classproperty
                        def LIGHTBLUE(cls):
                            return cls("light-blue")
                        
                        @schemas.classproperty
                        def LIGHTRED(cls):
                            return cls("light-red")
                        
                        @schemas.classproperty
                        def LIGHTTEAL(cls):
                            return cls("light-teal")
                        
                        @schemas.classproperty
                        def LIGHTBROWN(cls):
                            return cls("light-brown")
                        
                        @schemas.classproperty
                        def LIGHTORANGE(cls):
                            return cls("light-orange")
                        
                        @schemas.classproperty
                        def LIGHTPURPLE(cls):
                            return cls("light-purple")
                        
                        @schemas.classproperty
                        def LIGHTWARMGRAY(cls):
                            return cls("light-warm-gray")
                        
                        @schemas.classproperty
                        def NONE(cls):
                            return cls(None)
                    
                    
                        def __new__(
                            cls,
                            *args: typing.Union[None, str, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'color':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                            )
                    
                    
                    class requested_roles(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            @staticmethod
                            def items() -> typing.Type['TemplateRole']:
                                return TemplateRole
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple['TemplateRole'], typing.List['TemplateRole']],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'requested_roles':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> 'TemplateRole':
                            return super().__getitem__(i)
                    __annotations__ = {
                        "description": description,
                        "html_description": html_description,
                        "public": public,
                        "owner": owner,
                        "team": team,
                        "requested_dates": requested_dates,
                        "color": color,
                        "requested_roles": requested_roles,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["html_description"]) -> MetaOapg.properties.html_description: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["public"]) -> MetaOapg.properties.public: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["owner"]) -> MetaOapg.properties.owner: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["team"]) -> 'TeamCompact': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["requested_dates"]) -> MetaOapg.properties.requested_dates: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["color"]) -> MetaOapg.properties.color: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["requested_roles"]) -> MetaOapg.properties.requested_roles: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "html_description", "public", "owner", "team", "requested_dates", "color", "requested_roles", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["html_description"]) -> typing.Union[MetaOapg.properties.html_description, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["public"]) -> typing.Union[MetaOapg.properties.public, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["owner"]) -> typing.Union[MetaOapg.properties.owner, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["team"]) -> typing.Union['TeamCompact', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["requested_dates"]) -> typing.Union[MetaOapg.properties.requested_dates, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["color"]) -> typing.Union[MetaOapg.properties.color, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["requested_roles"]) -> typing.Union[MetaOapg.properties.requested_roles, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "html_description", "public", "owner", "team", "requested_dates", "color", "requested_roles", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
                html_description: typing.Union[MetaOapg.properties.html_description, str, schemas.Unset] = schemas.unset,
                public: typing.Union[MetaOapg.properties.public, bool, schemas.Unset] = schemas.unset,
                owner: typing.Union[MetaOapg.properties.owner, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
                team: typing.Union['TeamCompact', schemas.Unset] = schemas.unset,
                requested_dates: typing.Union[MetaOapg.properties.requested_dates, list, tuple, schemas.Unset] = schemas.unset,
                color: typing.Union[MetaOapg.properties.color, None, str, schemas.Unset] = schemas.unset,
                requested_roles: typing.Union[MetaOapg.properties.requested_roles, list, tuple, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_1':
                return super().__new__(
                    cls,
                    *args,
                    description=description,
                    html_description=html_description,
                    public=public,
                    owner=owner,
                    team=team,
                    requested_dates=requested_dates,
                    color=color,
                    requested_roles=requested_roles,
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
                ProjectTemplateCompact,
                cls.all_of_1,
            ]


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ProjectTemplateBase':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from asana_python_sdk.model.date_variable_compact import DateVariableCompact
from asana_python_sdk.model.project_template_compact import ProjectTemplateCompact
from asana_python_sdk.model.team_compact import TeamCompact
from asana_python_sdk.model.template_role import TemplateRole
from asana_python_sdk.model.user_compact import UserCompact