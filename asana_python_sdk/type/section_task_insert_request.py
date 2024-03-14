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


class RequiredSectionTaskInsertRequest(TypedDict):
    # The task to add to this section.
    task: str

class OptionalSectionTaskInsertRequest(TypedDict, total=False):
    # An existing task within this section before which the added task should be inserted. Cannot be provided together with insert_after.
    insert_before: str

    # An existing task within this section after which the added task should be inserted. Cannot be provided together with insert_before.
    insert_after: str

class SectionTaskInsertRequest(RequiredSectionTaskInsertRequest, OptionalSectionTaskInsertRequest):
    pass
