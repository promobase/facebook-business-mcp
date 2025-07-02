"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .idname import IDNameFields


# Field literal type
TargetingSubscriberUniverseField = Literal[
    "messenger_subscriber_source", "whatsapp_subscriber_pool", "whatsapp_subscriber_source"
]


class TargetingSubscriberUniverseFields(BaseModel):
    """Pydantic model for TargetingSubscriberUniverse fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    messenger_subscriber_source: IDNameFields = Field(None, alias="messenger_subscriber_source")
    whatsapp_subscriber_pool: IDNameFields = Field(None, alias="whatsapp_subscriber_pool")
    whatsapp_subscriber_source: IDNameFields = Field(None, alias="whatsapp_subscriber_source")
