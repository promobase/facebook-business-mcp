"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
WhatsappSubscribedAppsInfoField = Literal["page_whatsapp_number", "subscribed_apps"]


class WhatsappSubscribedAppsInfoFields(BaseModel):
    """Pydantic model for WhatsappSubscribedAppsInfo fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    page_whatsapp_number: str = Field(None, alias="page_whatsapp_number")
    subscribed_apps: list[dict[str, Any]] = Field(None, alias="subscribed_apps")
