# coding: utf-8

"""
    Asana

    This is the interface for interacting with the [Asana Platform](https://developers.asana.com). Our API reference is generated from our [OpenAPI spec](https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml).

    The version of the OpenAPI document: 1.0
    Created by: https://asana.com/support
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel


class AttachmentRequest(BaseModel):
    # Required identifier of the parent task, project, or project_brief, as a string. 
    parent: str = Field(alias='parent')

    # The type of the attachment. Must be one of the given values. If not specified, a file attachment of type `asana` will be assumed. Note that if the value of `resource_subtype` is `external`, a `parent`, `name`, and `url` must also be provided. 
    resource_subtype: typing.Optional[Literal["asana", "dropbox", "gdrive", "onedrive", "box", "vimeo", "external"]] = Field(None, alias='resource_subtype')

    # Required for `asana` attachments. 
    file: typing.Optional[typing.IO] = Field(None, alias='file')

    # The URL of the external resource being attached. Required for attachments of type `external`. 
    url: typing.Optional[str] = Field(None, alias='url')

    # The name of the external resource being attached. Required for attachments of type `external`. 
    name: typing.Optional[str] = Field(None, alias='name')

    # *Optional*. Only relevant for external attachments with a parent task. A boolean indicating whether the current app should be connected with the attachment for the purposes of showing an app components widget. Requires the app to have been added to a project the parent task is in. 
    connect_to_app: typing.Optional[bool] = Field(None, alias='connect_to_app')
    class Config:
        arbitrary_types_allowed = True
