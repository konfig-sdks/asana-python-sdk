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


class ProjectUpdateRequest(
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
                        schemas.DictSchema
                    ):
                    
                    
                        class MetaOapg:
                            additional_properties = schemas.StrSchema
                        
                        def __getitem__(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        def get_item_oapg(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                            return super().get_item_oapg(name)
                    
                        def __new__(
                            cls,
                            *args: typing.Union[dict, frozendict.frozendict, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[MetaOapg.additional_properties, str, ],
                        ) -> 'custom_fields':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                                **kwargs,
                            )
                    followers = schemas.StrSchema
                    
                    
                    class owner(
                        schemas.StrBase,
                        schemas.NoneBase,
                        schemas.Schema,
                        schemas.NoneStrMixin
                    ):
                    
                    
                        def __new__(
                            cls,
                            *args: typing.Union[None, str, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'owner':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                            )
                    team = schemas.StrSchema
                    __annotations__ = {
                        "custom_fields": custom_fields,
                        "followers": followers,
                        "owner": owner,
                        "team": team,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["custom_fields"]) -> MetaOapg.properties.custom_fields: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["followers"]) -> MetaOapg.properties.followers: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["owner"]) -> MetaOapg.properties.owner: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["team"]) -> MetaOapg.properties.team: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["custom_fields", "followers", "owner", "team", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["custom_fields"]) -> typing.Union[MetaOapg.properties.custom_fields, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["followers"]) -> typing.Union[MetaOapg.properties.followers, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["owner"]) -> typing.Union[MetaOapg.properties.owner, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["team"]) -> typing.Union[MetaOapg.properties.team, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["custom_fields", "followers", "owner", "team", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                custom_fields: typing.Union[MetaOapg.properties.custom_fields, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
                followers: typing.Union[MetaOapg.properties.followers, str, schemas.Unset] = schemas.unset,
                owner: typing.Union[MetaOapg.properties.owner, None, str, schemas.Unset] = schemas.unset,
                team: typing.Union[MetaOapg.properties.team, str, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_1':
                return super().__new__(
                    cls,
                    *args,
                    custom_fields=custom_fields,
                    followers=followers,
                    owner=owner,
                    team=team,
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
    ) -> 'ProjectUpdateRequest':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from asana_python_sdk.model.project_base import ProjectBase
