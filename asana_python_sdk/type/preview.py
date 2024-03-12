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


class RequiredPreview(TypedDict):
    pass

class OptionalPreview(TypedDict, total=False):
    # Text to display as the title.
    title: str

    # Some fallback text to display if unable to display the full preview.
    fallback: str

    # Text to display in the footer.
    footer: str

    # Text to display in the header.
    header: str

    # Where the header will link to.
    header_link: str

    # HTML formatted text for the body of the preview.
    html_text: str

    # Text for the body of the preview.
    text: str

    # Where to title will link to.
    title_link: str

class Preview(RequiredPreview, OptionalPreview):
    pass
