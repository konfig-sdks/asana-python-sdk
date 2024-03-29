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


class JobCompact(
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
                    resource_subtype = schemas.StrSchema
                    
                    
                    class status(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "not_started": "NOT_STARTED",
                                "in_progress": "IN_PROGRESS",
                                "succeeded": "SUCCEEDED",
                                "failed": "FAILED",
                            }
                        
                        @schemas.classproperty
                        def NOT_STARTED(cls):
                            return cls("not_started")
                        
                        @schemas.classproperty
                        def IN_PROGRESS(cls):
                            return cls("in_progress")
                        
                        @schemas.classproperty
                        def SUCCEEDED(cls):
                            return cls("succeeded")
                        
                        @schemas.classproperty
                        def FAILED(cls):
                            return cls("failed")
                
                    @staticmethod
                    def new_project() -> typing.Type['ProjectCompact']:
                        return ProjectCompact
                    
                    
                    class new_task(
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
                                    TaskCompact,
                                    cls.all_of_1,
                                ]
                    
                    
                        def __new__(
                            cls,
                            *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'new_task':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                                **kwargs,
                            )
                
                    @staticmethod
                    def new_project_template() -> typing.Type['ProjectTemplateCompact']:
                        return ProjectTemplateCompact
                    __annotations__ = {
                        "resource_subtype": resource_subtype,
                        "status": status,
                        "new_project": new_project,
                        "new_task": new_task,
                        "new_project_template": new_project_template,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["resource_subtype"]) -> MetaOapg.properties.resource_subtype: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["new_project"]) -> 'ProjectCompact': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["new_task"]) -> MetaOapg.properties.new_task: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["new_project_template"]) -> 'ProjectTemplateCompact': ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["resource_subtype", "status", "new_project", "new_task", "new_project_template", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["resource_subtype"]) -> typing.Union[MetaOapg.properties.resource_subtype, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["new_project"]) -> typing.Union['ProjectCompact', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["new_task"]) -> typing.Union[MetaOapg.properties.new_task, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["new_project_template"]) -> typing.Union['ProjectTemplateCompact', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["resource_subtype", "status", "new_project", "new_task", "new_project_template", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                resource_subtype: typing.Union[MetaOapg.properties.resource_subtype, str, schemas.Unset] = schemas.unset,
                status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
                new_project: typing.Union['ProjectCompact', schemas.Unset] = schemas.unset,
                new_task: typing.Union[MetaOapg.properties.new_task, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
                new_project_template: typing.Union['ProjectTemplateCompact', schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_1':
                return super().__new__(
                    cls,
                    *args,
                    resource_subtype=resource_subtype,
                    status=status,
                    new_project=new_project,
                    new_task=new_task,
                    new_project_template=new_project_template,
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
    ) -> 'JobCompact':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from asana_python_sdk.model.asana_resource import AsanaResource
from asana_python_sdk.model.project_compact import ProjectCompact
from asana_python_sdk.model.project_template_compact import ProjectTemplateCompact
from asana_python_sdk.model.task_compact import TaskCompact
