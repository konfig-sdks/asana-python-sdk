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


class RequiredSectionRequest(TypedDict):
    # The text to be displayed as the section name. This cannot be an empty string.
    name: str

class OptionalSectionRequest(TypedDict, total=False):
    # An existing section within this project before which the added section should be inserted. Cannot be provided together with insert_after.
    insert_before: str

    # An existing section within this project after which the added section should be inserted. Cannot be provided together with insert_before.
    insert_after: str

class SectionRequest(RequiredSectionRequest, OptionalSectionRequest):
    pass
