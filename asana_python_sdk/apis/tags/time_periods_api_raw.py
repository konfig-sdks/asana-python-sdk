# coding: utf-8

"""
    Asana

    This is the interface for interacting with the [Asana Platform](https://developers.asana.com). Our API reference is generated from our [OpenAPI spec] (https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml).

    The version of the OpenAPI document: 1.0
    Created by: https://asana.com/support
"""

from asana_python_sdk.paths.time_periods.get import GetCompactTimePeriodsRaw
from asana_python_sdk.paths.time_periods_time_period_gid.get import GetFullRecordRaw


class TimePeriodsApiRaw(
    GetCompactTimePeriodsRaw,
    GetFullRecordRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass