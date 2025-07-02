"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdCreativeWhatsAppChannelSpecField = Literal["channel_id", "channel_url"]


class AdCreativeWhatsAppChannelSpecFields(BaseModel):
    """Pydantic model for AdCreativeWhatsAppChannelSpec fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    channel_id: str = Field(None, alias="channel_id")
    channel_url: str = Field(None, alias="channel_url")
