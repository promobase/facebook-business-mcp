"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
WhatsAppPaymentCapabilitiesField = Literal["is_enabled", "payment_capability_details"]


class WhatsAppPaymentCapabilitiesFields(BaseModel):
    """Pydantic model for WhatsAppPaymentCapabilities fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    is_enabled: bool = Field(None, alias="is_enabled")
    payment_capability_details: list[dict[str, Any]] = Field(
        None, alias="payment_capability_details"
    )
