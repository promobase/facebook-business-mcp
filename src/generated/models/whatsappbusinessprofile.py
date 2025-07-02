"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
WhatsAppBusinessProfileField = Literal["id", "name_verification", "whatsapp_business_api_data"]


class WhatsAppBusinessProfileFields(BaseModel):
    """Pydantic model for WhatsAppBusinessProfile fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    id: str = Field(None, alias="id")
    name_verification: dict[str, Any] = Field(None, alias="name_verification")
    whatsapp_business_api_data: dict[str, Any] = Field(None, alias="whatsapp_business_api_data")
