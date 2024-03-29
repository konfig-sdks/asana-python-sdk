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


class TaskTemplateRecipe(
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
                    
                    
                    class memberships(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            @staticmethod
                            def items() -> typing.Type['ProjectCompact']:
                                return ProjectCompact
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple['ProjectCompact'], typing.List['ProjectCompact']],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'memberships':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> 'ProjectCompact':
                            return super().__getitem__(i)
                    
                    
                    class relative_start_on(
                        schemas.IntBase,
                        schemas.NoneBase,
                        schemas.Schema,
                        schemas.NoneDecimalMixin
                    ):
                    
                    
                        def __new__(
                            cls,
                            *args: typing.Union[None, decimal.Decimal, int, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'relative_start_on':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                            )
                    
                    
                    class relative_due_on(
                        schemas.IntBase,
                        schemas.NoneBase,
                        schemas.Schema,
                        schemas.NoneDecimalMixin
                    ):
                    
                    
                        def __new__(
                            cls,
                            *args: typing.Union[None, decimal.Decimal, int, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'relative_due_on':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                            )
                    
                    
                    class due_time(
                        schemas.StrBase,
                        schemas.NoneBase,
                        schemas.Schema,
                        schemas.NoneStrMixin
                    ):
                    
                    
                        def __new__(
                            cls,
                            *args: typing.Union[None, str, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'due_time':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                            )
                    
                    
                    class dependencies(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            @staticmethod
                            def items() -> typing.Type['TaskTemplateRecipeCompact']:
                                return TaskTemplateRecipeCompact
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple['TaskTemplateRecipeCompact'], typing.List['TaskTemplateRecipeCompact']],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'dependencies':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> 'TaskTemplateRecipeCompact':
                            return super().__getitem__(i)
                    
                    
                    class dependents(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            @staticmethod
                            def items() -> typing.Type['TaskTemplateRecipeCompact']:
                                return TaskTemplateRecipeCompact
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple['TaskTemplateRecipeCompact'], typing.List['TaskTemplateRecipeCompact']],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'dependents':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> 'TaskTemplateRecipeCompact':
                            return super().__getitem__(i)
                    
                    
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
                    
                    
                    class attachments(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            @staticmethod
                            def items() -> typing.Type['AttachmentCompact']:
                                return AttachmentCompact
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple['AttachmentCompact'], typing.List['AttachmentCompact']],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'attachments':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> 'AttachmentCompact':
                            return super().__getitem__(i)
                    
                    
                    class subtasks(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            @staticmethod
                            def items() -> typing.Type['TaskTemplateRecipeCompact']:
                                return TaskTemplateRecipeCompact
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple['TaskTemplateRecipeCompact'], typing.List['TaskTemplateRecipeCompact']],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'subtasks':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> 'TaskTemplateRecipeCompact':
                            return super().__getitem__(i)
                    
                    
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
                    __annotations__ = {
                        "description": description,
                        "html_description": html_description,
                        "memberships": memberships,
                        "relative_start_on": relative_start_on,
                        "relative_due_on": relative_due_on,
                        "due_time": due_time,
                        "dependencies": dependencies,
                        "dependents": dependents,
                        "followers": followers,
                        "attachments": attachments,
                        "subtasks": subtasks,
                        "custom_fields": custom_fields,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["html_description"]) -> MetaOapg.properties.html_description: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["memberships"]) -> MetaOapg.properties.memberships: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["relative_start_on"]) -> MetaOapg.properties.relative_start_on: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["relative_due_on"]) -> MetaOapg.properties.relative_due_on: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["due_time"]) -> MetaOapg.properties.due_time: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["dependencies"]) -> MetaOapg.properties.dependencies: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["dependents"]) -> MetaOapg.properties.dependents: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["followers"]) -> MetaOapg.properties.followers: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["attachments"]) -> MetaOapg.properties.attachments: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["subtasks"]) -> MetaOapg.properties.subtasks: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["custom_fields"]) -> MetaOapg.properties.custom_fields: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "html_description", "memberships", "relative_start_on", "relative_due_on", "due_time", "dependencies", "dependents", "followers", "attachments", "subtasks", "custom_fields", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["html_description"]) -> typing.Union[MetaOapg.properties.html_description, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["memberships"]) -> typing.Union[MetaOapg.properties.memberships, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["relative_start_on"]) -> typing.Union[MetaOapg.properties.relative_start_on, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["relative_due_on"]) -> typing.Union[MetaOapg.properties.relative_due_on, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["due_time"]) -> typing.Union[MetaOapg.properties.due_time, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["dependencies"]) -> typing.Union[MetaOapg.properties.dependencies, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["dependents"]) -> typing.Union[MetaOapg.properties.dependents, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["followers"]) -> typing.Union[MetaOapg.properties.followers, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["attachments"]) -> typing.Union[MetaOapg.properties.attachments, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["subtasks"]) -> typing.Union[MetaOapg.properties.subtasks, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["custom_fields"]) -> typing.Union[MetaOapg.properties.custom_fields, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "html_description", "memberships", "relative_start_on", "relative_due_on", "due_time", "dependencies", "dependents", "followers", "attachments", "subtasks", "custom_fields", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
                html_description: typing.Union[MetaOapg.properties.html_description, str, schemas.Unset] = schemas.unset,
                memberships: typing.Union[MetaOapg.properties.memberships, list, tuple, schemas.Unset] = schemas.unset,
                relative_start_on: typing.Union[MetaOapg.properties.relative_start_on, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                relative_due_on: typing.Union[MetaOapg.properties.relative_due_on, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                due_time: typing.Union[MetaOapg.properties.due_time, None, str, schemas.Unset] = schemas.unset,
                dependencies: typing.Union[MetaOapg.properties.dependencies, list, tuple, schemas.Unset] = schemas.unset,
                dependents: typing.Union[MetaOapg.properties.dependents, list, tuple, schemas.Unset] = schemas.unset,
                followers: typing.Union[MetaOapg.properties.followers, list, tuple, schemas.Unset] = schemas.unset,
                attachments: typing.Union[MetaOapg.properties.attachments, list, tuple, schemas.Unset] = schemas.unset,
                subtasks: typing.Union[MetaOapg.properties.subtasks, list, tuple, schemas.Unset] = schemas.unset,
                custom_fields: typing.Union[MetaOapg.properties.custom_fields, list, tuple, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_1':
                return super().__new__(
                    cls,
                    *args,
                    description=description,
                    html_description=html_description,
                    memberships=memberships,
                    relative_start_on=relative_start_on,
                    relative_due_on=relative_due_on,
                    due_time=due_time,
                    dependencies=dependencies,
                    dependents=dependents,
                    followers=followers,
                    attachments=attachments,
                    subtasks=subtasks,
                    custom_fields=custom_fields,
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
                TaskTemplateRecipeCompact,
                cls.all_of_1,
            ]


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TaskTemplateRecipe':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from asana_python_sdk.model.attachment_compact import AttachmentCompact
from asana_python_sdk.model.custom_field_compact import CustomFieldCompact
from asana_python_sdk.model.project_compact import ProjectCompact
from asana_python_sdk.model.task_template_recipe_compact import TaskTemplateRecipeCompact
from asana_python_sdk.model.user_compact import UserCompact
