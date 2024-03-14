# coding: utf-8

"""
    Asana

    This is the interface for interacting with the [Asana Platform](https://developers.asana.com). Our API reference is generated from our [OpenAPI spec](https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml).

    The version of the OpenAPI document: 1.0
    Created by: https://asana.com/support
"""

from asana_python_sdk.paths.webhooks.post import EstablishWebhookRaw
from asana_python_sdk.paths.webhooks_webhook_gid.get import GetWebhookRecordRaw
from asana_python_sdk.paths.webhooks.get import ListMultipleWebhooksRaw
from asana_python_sdk.paths.webhooks_webhook_gid.delete import RemoveWebhookRaw
from asana_python_sdk.paths.webhooks_webhook_gid.put import UpdateWebhookFiltersRaw


class WebhooksApiRaw(
    EstablishWebhookRaw,
    GetWebhookRecordRaw,
    ListMultipleWebhooksRaw,
    RemoveWebhookRaw,
    UpdateWebhookFiltersRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
