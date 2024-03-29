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


class ProjectBase(
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
                    archived = schemas.BoolSchema
                    
                    
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
                                "none": "NONE",
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
                            return cls("none")
                        
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
                    created_at = schemas.DateTimeSchema
                    
                    
                    class current_status(
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
                                    ProjectStatusResponse,
                                    cls.all_of_1,
                                ]
                    
                    
                        def __new__(
                            cls,
                            *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'current_status':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                                **kwargs,
                            )
                    
                    
                    class current_status_update(
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
                                    StatusUpdateCompact,
                                    cls.all_of_1,
                                ]
                    
                    
                        def __new__(
                            cls,
                            *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'current_status_update':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                                **kwargs,
                            )
                    
                    
                    class custom_field_settings(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            @staticmethod
                            def items() -> typing.Type['CustomFieldSettingResponse']:
                                return CustomFieldSettingResponse
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple['CustomFieldSettingResponse'], typing.List['CustomFieldSettingResponse']],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'custom_field_settings':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> 'CustomFieldSettingResponse':
                            return super().__getitem__(i)
                    
                    
                    class default_view(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                        
                        @schemas.classproperty
                        def LIST(cls):
                            return cls("list")
                        
                        @schemas.classproperty
                        def BOARD(cls):
                            return cls("board")
                        
                        @schemas.classproperty
                        def CALENDAR(cls):
                            return cls("calendar")
                        
                        @schemas.classproperty
                        def TIMELINE(cls):
                            return cls("timeline")
                    
                    
                    class due_date(
                        schemas.DateBase,
                        schemas.StrBase,
                        schemas.NoneBase,
                        schemas.Schema,
                        schemas.NoneStrMixin
                    ):
                    
                    
                        class MetaOapg:
                            format = 'date'
                    
                    
                        def __new__(
                            cls,
                            *args: typing.Union[None, str, date, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'due_date':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                            )
                    
                    
                    class due_on(
                        schemas.DateBase,
                        schemas.StrBase,
                        schemas.NoneBase,
                        schemas.Schema,
                        schemas.NoneStrMixin
                    ):
                    
                    
                        class MetaOapg:
                            format = 'date'
                    
                    
                        def __new__(
                            cls,
                            *args: typing.Union[None, str, date, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'due_on':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                            )
                    html_notes = schemas.StrSchema
                    
                    
                    class members(
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
                        ) -> 'members':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> 'UserCompact':
                            return super().__getitem__(i)
                    modified_at = schemas.DateTimeSchema
                    notes = schemas.StrSchema
                    public = schemas.BoolSchema
                    
                    
                    class start_on(
                        schemas.DateBase,
                        schemas.StrBase,
                        schemas.NoneBase,
                        schemas.Schema,
                        schemas.NoneStrMixin
                    ):
                    
                    
                        class MetaOapg:
                            format = 'date'
                    
                    
                        def __new__(
                            cls,
                            *args: typing.Union[None, str, date, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'start_on':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                            )
                    
                    
                    class default_access_level(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                        
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
                    
                    
                    class minimum_access_level_for_customization(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                        
                        @schemas.classproperty
                        def ADMIN(cls):
                            return cls("admin")
                        
                        @schemas.classproperty
                        def EDITOR(cls):
                            return cls("editor")
                    
                    
                    class minimum_access_level_for_sharing(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                        
                        @schemas.classproperty
                        def ADMIN(cls):
                            return cls("admin")
                        
                        @schemas.classproperty
                        def EDITOR(cls):
                            return cls("editor")
                    __annotations__ = {
                        "archived": archived,
                        "color": color,
                        "created_at": created_at,
                        "current_status": current_status,
                        "current_status_update": current_status_update,
                        "custom_field_settings": custom_field_settings,
                        "default_view": default_view,
                        "due_date": due_date,
                        "due_on": due_on,
                        "html_notes": html_notes,
                        "members": members,
                        "modified_at": modified_at,
                        "notes": notes,
                        "public": public,
                        "start_on": start_on,
                        "default_access_level": default_access_level,
                        "minimum_access_level_for_customization": minimum_access_level_for_customization,
                        "minimum_access_level_for_sharing": minimum_access_level_for_sharing,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["archived"]) -> MetaOapg.properties.archived: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["color"]) -> MetaOapg.properties.color: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["current_status"]) -> MetaOapg.properties.current_status: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["current_status_update"]) -> MetaOapg.properties.current_status_update: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["custom_field_settings"]) -> MetaOapg.properties.custom_field_settings: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["default_view"]) -> MetaOapg.properties.default_view: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["due_date"]) -> MetaOapg.properties.due_date: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["due_on"]) -> MetaOapg.properties.due_on: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["html_notes"]) -> MetaOapg.properties.html_notes: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["members"]) -> MetaOapg.properties.members: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["modified_at"]) -> MetaOapg.properties.modified_at: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["notes"]) -> MetaOapg.properties.notes: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["public"]) -> MetaOapg.properties.public: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["start_on"]) -> MetaOapg.properties.start_on: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["default_access_level"]) -> MetaOapg.properties.default_access_level: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["minimum_access_level_for_customization"]) -> MetaOapg.properties.minimum_access_level_for_customization: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["minimum_access_level_for_sharing"]) -> MetaOapg.properties.minimum_access_level_for_sharing: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["archived", "color", "created_at", "current_status", "current_status_update", "custom_field_settings", "default_view", "due_date", "due_on", "html_notes", "members", "modified_at", "notes", "public", "start_on", "default_access_level", "minimum_access_level_for_customization", "minimum_access_level_for_sharing", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["archived"]) -> typing.Union[MetaOapg.properties.archived, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["color"]) -> typing.Union[MetaOapg.properties.color, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> typing.Union[MetaOapg.properties.created_at, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["current_status"]) -> typing.Union[MetaOapg.properties.current_status, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["current_status_update"]) -> typing.Union[MetaOapg.properties.current_status_update, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["custom_field_settings"]) -> typing.Union[MetaOapg.properties.custom_field_settings, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["default_view"]) -> typing.Union[MetaOapg.properties.default_view, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["due_date"]) -> typing.Union[MetaOapg.properties.due_date, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["due_on"]) -> typing.Union[MetaOapg.properties.due_on, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["html_notes"]) -> typing.Union[MetaOapg.properties.html_notes, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["members"]) -> typing.Union[MetaOapg.properties.members, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["modified_at"]) -> typing.Union[MetaOapg.properties.modified_at, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["notes"]) -> typing.Union[MetaOapg.properties.notes, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["public"]) -> typing.Union[MetaOapg.properties.public, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["start_on"]) -> typing.Union[MetaOapg.properties.start_on, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["default_access_level"]) -> typing.Union[MetaOapg.properties.default_access_level, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["minimum_access_level_for_customization"]) -> typing.Union[MetaOapg.properties.minimum_access_level_for_customization, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["minimum_access_level_for_sharing"]) -> typing.Union[MetaOapg.properties.minimum_access_level_for_sharing, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["archived", "color", "created_at", "current_status", "current_status_update", "custom_field_settings", "default_view", "due_date", "due_on", "html_notes", "members", "modified_at", "notes", "public", "start_on", "default_access_level", "minimum_access_level_for_customization", "minimum_access_level_for_sharing", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                archived: typing.Union[MetaOapg.properties.archived, bool, schemas.Unset] = schemas.unset,
                color: typing.Union[MetaOapg.properties.color, None, str, schemas.Unset] = schemas.unset,
                created_at: typing.Union[MetaOapg.properties.created_at, str, datetime, schemas.Unset] = schemas.unset,
                current_status: typing.Union[MetaOapg.properties.current_status, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
                current_status_update: typing.Union[MetaOapg.properties.current_status_update, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
                custom_field_settings: typing.Union[MetaOapg.properties.custom_field_settings, list, tuple, schemas.Unset] = schemas.unset,
                default_view: typing.Union[MetaOapg.properties.default_view, str, schemas.Unset] = schemas.unset,
                due_date: typing.Union[MetaOapg.properties.due_date, None, str, date, schemas.Unset] = schemas.unset,
                due_on: typing.Union[MetaOapg.properties.due_on, None, str, date, schemas.Unset] = schemas.unset,
                html_notes: typing.Union[MetaOapg.properties.html_notes, str, schemas.Unset] = schemas.unset,
                members: typing.Union[MetaOapg.properties.members, list, tuple, schemas.Unset] = schemas.unset,
                modified_at: typing.Union[MetaOapg.properties.modified_at, str, datetime, schemas.Unset] = schemas.unset,
                notes: typing.Union[MetaOapg.properties.notes, str, schemas.Unset] = schemas.unset,
                public: typing.Union[MetaOapg.properties.public, bool, schemas.Unset] = schemas.unset,
                start_on: typing.Union[MetaOapg.properties.start_on, None, str, date, schemas.Unset] = schemas.unset,
                default_access_level: typing.Union[MetaOapg.properties.default_access_level, str, schemas.Unset] = schemas.unset,
                minimum_access_level_for_customization: typing.Union[MetaOapg.properties.minimum_access_level_for_customization, str, schemas.Unset] = schemas.unset,
                minimum_access_level_for_sharing: typing.Union[MetaOapg.properties.minimum_access_level_for_sharing, str, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_1':
                return super().__new__(
                    cls,
                    *args,
                    archived=archived,
                    color=color,
                    created_at=created_at,
                    current_status=current_status,
                    current_status_update=current_status_update,
                    custom_field_settings=custom_field_settings,
                    default_view=default_view,
                    due_date=due_date,
                    due_on=due_on,
                    html_notes=html_notes,
                    members=members,
                    modified_at=modified_at,
                    notes=notes,
                    public=public,
                    start_on=start_on,
                    default_access_level=default_access_level,
                    minimum_access_level_for_customization=minimum_access_level_for_customization,
                    minimum_access_level_for_sharing=minimum_access_level_for_sharing,
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
                ProjectCompact,
                cls.all_of_1,
            ]


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ProjectBase':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from asana_python_sdk.model.custom_field_setting_response import CustomFieldSettingResponse
from asana_python_sdk.model.project_compact import ProjectCompact
from asana_python_sdk.model.project_status_response import ProjectStatusResponse
from asana_python_sdk.model.status_update_compact import StatusUpdateCompact
from asana_python_sdk.model.user_compact import UserCompact
