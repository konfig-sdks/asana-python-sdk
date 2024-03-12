# coding: utf-8

"""
    Asana

    This is the interface for interacting with the [Asana Platform](https://developers.asana.com). Our API reference is generated from our [OpenAPI spec] (https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml).

    The version of the OpenAPI document: 1.0
    Created by: https://asana.com/support
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel


class Preview(BaseModel):
    # Text to display as the title.
    title: typing.Optional[str] = Field(None, alias='title')

    # Some fallback text to display if unable to display the full preview.
    fallback: typing.Optional[str] = Field(None, alias='fallback')

    # Text to display in the footer.
    footer: typing.Optional[str] = Field(None, alias='footer')

    # Text to display in the header.
    header: typing.Optional[str] = Field(None, alias='header')

    # Where the header will link to.
    header_link: typing.Optional[str] = Field(None, alias='header_link')

    # HTML formatted text for the body of the preview.
    html_text: typing.Optional[str] = Field(None, alias='html_text')

    # Text for the body of the preview.
    text: typing.Optional[str] = Field(None, alias='text')

    # Where to title will link to.
    title_link: typing.Optional[str] = Field(None, alias='title_link')
    class Config:
        arbitrary_types_allowed = True
