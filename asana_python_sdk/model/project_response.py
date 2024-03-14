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


class ProjectResponse(
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
                    
                    
                    class custom_fields(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            @staticmethod
                            def items() -> typing.Type['CustomFieldCompact']:
                                return CustomFieldCompact
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple['CustomFieldCompact'], typing.List['CustomFieldCompact']],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'custom_fields':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> 'CustomFieldCompact':
                            return super().__getitem__(i)
                    completed = schemas.BoolSchema
                    
                    
                    class completed_at(
                        schemas.DateTimeBase,
                        schemas.StrBase,
                        schemas.NoneBase,
                        schemas.Schema,
                        schemas.NoneStrMixin
                    ):
                    
                    
                        class MetaOapg:
                            format = 'date-time'
                    
                    
                        def __new__(
                            cls,
                            *args: typing.Union[None, str, datetime, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'completed_at':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                            )
                    
                    
                    class completed_by(
                        schemas.ComposedSchema,
                    ):
                    
                    
                        class MetaOapg:
                            all_of_1 = schemas.AnyTypeSchema
                            
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
                        ) -> 'completed_by':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                                **kwargs,
                            )
                    
                    
                    class followers(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            @staticmethod
                            def items() -> typing.Type['UserCompact']:
                                return UserCompact
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple['UserCompact'], typing.List['UserCompact']],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'followers':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> 'UserCompact':
                            return super().__getitem__(i)
                    
                    
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
                    
                    
                    class team(
                        schemas.ComposedSchema,
                    ):
                    
                    
                        class MetaOapg:
                            all_of_1 = schemas.DictSchema
                            
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
                        ) -> 'team':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                                **kwargs,
                            )
                    
                    
                    class icon(
                        schemas.EnumBase,
                        schemas.StrBase,
                        schemas.NoneBase,
                        schemas.Schema,
                        schemas.NoneStrMixin
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "list": "LIST",
                                "board": "BOARD",
                                "timeline": "TIMELINE",
                                "calendar": "CALENDAR",
                                "rocket": "ROCKET",
                                "people": "PEOPLE",
                                "graph": "GRAPH",
                                "star": "STAR",
                                "bug": "BUG",
                                "light_bulb": "LIGHT_BULB",
                                "globe": "GLOBE",
                                "gear": "GEAR",
                                "notebook": "NOTEBOOK",
                                "computer": "COMPUTER",
                                "check": "CHECK",
                                "target": "TARGET",
                                "html": "HTML",
                                "megaphone": "MEGAPHONE",
                                "chat_bubbles": "CHAT_BUBBLES",
                                "briefcase": "BRIEFCASE",
                                "page_layout": "PAGE_LAYOUT",
                                "mountain_flag": "MOUNTAIN_FLAG",
                                "puzzle": "PUZZLE",
                                "presentation": "PRESENTATION",
                                "line_and_symbols": "LINE_AND_SYMBOLS",
                                "speed_dial": "SPEED_DIAL",
                                "ribbon": "RIBBON",
                                "shoe": "SHOE",
                                "shopping_basket": "SHOPPING_BASKET",
                                "map": "MAP",
                                "ticket": "TICKET",
                                "coins": "COINS",
                            }
                        
                        @schemas.classproperty
                        def LIST(cls):
                            return cls("list")
                        
                        @schemas.classproperty
                        def BOARD(cls):
                            return cls("board")
                        
                        @schemas.classproperty
                        def TIMELINE(cls):
                            return cls("timeline")
                        
                        @schemas.classproperty
                        def CALENDAR(cls):
                            return cls("calendar")
                        
                        @schemas.classproperty
                        def ROCKET(cls):
                            return cls("rocket")
                        
                        @schemas.classproperty
                        def PEOPLE(cls):
                            return cls("people")
                        
                        @schemas.classproperty
                        def GRAPH(cls):
                            return cls("graph")
                        
                        @schemas.classproperty
                        def STAR(cls):
                            return cls("star")
                        
                        @schemas.classproperty
                        def BUG(cls):
                            return cls("bug")
                        
                        @schemas.classproperty
                        def LIGHT_BULB(cls):
                            return cls("light_bulb")
                        
                        @schemas.classproperty
                        def GLOBE(cls):
                            return cls("globe")
                        
                        @schemas.classproperty
                        def GEAR(cls):
                            return cls("gear")
                        
                        @schemas.classproperty
                        def NOTEBOOK(cls):
                            return cls("notebook")
                        
                        @schemas.classproperty
                        def COMPUTER(cls):
                            return cls("computer")
                        
                        @schemas.classproperty
                        def CHECK(cls):
                            return cls("check")
                        
                        @schemas.classproperty
                        def TARGET(cls):
                            return cls("target")
                        
                        @schemas.classproperty
                        def HTML(cls):
                            return cls("html")
                        
                        @schemas.classproperty
                        def MEGAPHONE(cls):
                            return cls("megaphone")
                        
                        @schemas.classproperty
                        def CHAT_BUBBLES(cls):
                            return cls("chat_bubbles")
                        
                        @schemas.classproperty
                        def BRIEFCASE(cls):
                            return cls("briefcase")
                        
                        @schemas.classproperty
                        def PAGE_LAYOUT(cls):
                            return cls("page_layout")
                        
                        @schemas.classproperty
                        def MOUNTAIN_FLAG(cls):
                            return cls("mountain_flag")
                        
                        @schemas.classproperty
                        def PUZZLE(cls):
                            return cls("puzzle")
                        
                        @schemas.classproperty
                        def PRESENTATION(cls):
                            return cls("presentation")
                        
                        @schemas.classproperty
                        def LINE_AND_SYMBOLS(cls):
                            return cls("line_and_symbols")
                        
                        @schemas.classproperty
                        def SPEED_DIAL(cls):
                            return cls("speed_dial")
                        
                        @schemas.classproperty
                        def RIBBON(cls):
                            return cls("ribbon")
                        
                        @schemas.classproperty
                        def SHOE(cls):
                            return cls("shoe")
                        
                        @schemas.classproperty
                        def SHOPPING_BASKET(cls):
                            return cls("shopping_basket")
                        
                        @schemas.classproperty
                        def MAP(cls):
                            return cls("map")
                        
                        @schemas.classproperty
                        def TICKET(cls):
                            return cls("ticket")
                        
                        @schemas.classproperty
                        def COINS(cls):
                            return cls("coins")
                    
                    
                        def __new__(
                            cls,
                            *args: typing.Union[None, str, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'icon':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                            )
                    permalink_url = schemas.StrSchema
                    
                    
                    class project_brief(
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
                                    ProjectBriefCompact,
                                    cls.all_of_1,
                                ]
                    
                    
                        def __new__(
                            cls,
                            *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'project_brief':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                                **kwargs,
                            )
                    
                    
                    class created_from_template(
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
                                    ProjectTemplateCompact,
                                    cls.all_of_1,
                                ]
                    
                    
                        def __new__(
                            cls,
                            *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'created_from_template':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                                **kwargs,
                            )
                    
                    
                    class workspace(
                        schemas.ComposedSchema,
                    ):
                    
                    
                        class MetaOapg:
                            all_of_1 = schemas.DictSchema
                            
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
                                    WorkspaceCompact,
                                    cls.all_of_1,
                                ]
                    
                    
                        def __new__(
                            cls,
                            *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'workspace':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                                **kwargs,
                            )
                    __annotations__ = {
                        "custom_fields": custom_fields,
                        "completed": completed,
                        "completed_at": completed_at,
                        "completed_by": completed_by,
                        "followers": followers,
                        "owner": owner,
                        "team": team,
                        "icon": icon,
                        "permalink_url": permalink_url,
                        "project_brief": project_brief,
                        "created_from_template": created_from_template,
                        "workspace": workspace,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["custom_fields"]) -> MetaOapg.properties.custom_fields: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["completed"]) -> MetaOapg.properties.completed: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["completed_at"]) -> MetaOapg.properties.completed_at: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["completed_by"]) -> MetaOapg.properties.completed_by: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["followers"]) -> MetaOapg.properties.followers: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["owner"]) -> MetaOapg.properties.owner: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["team"]) -> MetaOapg.properties.team: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["icon"]) -> MetaOapg.properties.icon: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["permalink_url"]) -> MetaOapg.properties.permalink_url: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["project_brief"]) -> MetaOapg.properties.project_brief: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["created_from_template"]) -> MetaOapg.properties.created_from_template: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["workspace"]) -> MetaOapg.properties.workspace: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["custom_fields", "completed", "completed_at", "completed_by", "followers", "owner", "team", "icon", "permalink_url", "project_brief", "created_from_template", "workspace", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["custom_fields"]) -> typing.Union[MetaOapg.properties.custom_fields, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["completed"]) -> typing.Union[MetaOapg.properties.completed, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["completed_at"]) -> typing.Union[MetaOapg.properties.completed_at, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["completed_by"]) -> typing.Union[MetaOapg.properties.completed_by, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["followers"]) -> typing.Union[MetaOapg.properties.followers, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["owner"]) -> typing.Union[MetaOapg.properties.owner, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["team"]) -> typing.Union[MetaOapg.properties.team, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["icon"]) -> typing.Union[MetaOapg.properties.icon, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["permalink_url"]) -> typing.Union[MetaOapg.properties.permalink_url, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["project_brief"]) -> typing.Union[MetaOapg.properties.project_brief, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["created_from_template"]) -> typing.Union[MetaOapg.properties.created_from_template, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["workspace"]) -> typing.Union[MetaOapg.properties.workspace, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["custom_fields", "completed", "completed_at", "completed_by", "followers", "owner", "team", "icon", "permalink_url", "project_brief", "created_from_template", "workspace", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                custom_fields: typing.Union[MetaOapg.properties.custom_fields, list, tuple, schemas.Unset] = schemas.unset,
                completed: typing.Union[MetaOapg.properties.completed, bool, schemas.Unset] = schemas.unset,
                completed_at: typing.Union[MetaOapg.properties.completed_at, None, str, datetime, schemas.Unset] = schemas.unset,
                completed_by: typing.Union[MetaOapg.properties.completed_by, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
                followers: typing.Union[MetaOapg.properties.followers, list, tuple, schemas.Unset] = schemas.unset,
                owner: typing.Union[MetaOapg.properties.owner, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
                team: typing.Union[MetaOapg.properties.team, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
                icon: typing.Union[MetaOapg.properties.icon, None, str, schemas.Unset] = schemas.unset,
                permalink_url: typing.Union[MetaOapg.properties.permalink_url, str, schemas.Unset] = schemas.unset,
                project_brief: typing.Union[MetaOapg.properties.project_brief, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
                created_from_template: typing.Union[MetaOapg.properties.created_from_template, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
                workspace: typing.Union[MetaOapg.properties.workspace, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_1':
                return super().__new__(
                    cls,
                    *args,
                    custom_fields=custom_fields,
                    completed=completed,
                    completed_at=completed_at,
                    completed_by=completed_by,
                    followers=followers,
                    owner=owner,
                    team=team,
                    icon=icon,
                    permalink_url=permalink_url,
                    project_brief=project_brief,
                    created_from_template=created_from_template,
                    workspace=workspace,
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
                ProjectBase,
                cls.all_of_1,
            ]


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ProjectResponse':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from asana_python_sdk.model.custom_field_compact import CustomFieldCompact
from asana_python_sdk.model.project_base import ProjectBase
from asana_python_sdk.model.project_brief_compact import ProjectBriefCompact
from asana_python_sdk.model.project_template_compact import ProjectTemplateCompact
from asana_python_sdk.model.team_compact import TeamCompact
from asana_python_sdk.model.user_compact import UserCompact
from asana_python_sdk.model.workspace_compact import WorkspaceCompact
