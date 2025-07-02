"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .idname import IDNameFields


# Field literal type
TargetingMarketingMessageChannelsField = Literal["whatsapp"]


class TargetingMarketingMessageChannelsFields(BaseModel):
    """Pydantic model for TargetingMarketingMessageChannels fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    whatsapp: IDNameFields = Field(None, alias="whatsapp")
