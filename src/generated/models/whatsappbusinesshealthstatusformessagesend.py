"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .whatsappbusinesshealthstatus import WhatsAppBusinessHealthStatusFields


# Field literal type
WhatsAppBusinessHealthStatusForMessageSendField = Literal["can_send_message", "entities"]


class WhatsAppBusinessHealthStatusForMessageSendFields(BaseModel):
    """Pydantic model for WhatsAppBusinessHealthStatusForMessageSend fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    can_send_message: str = Field(None, alias="can_send_message")
    entities: list[WhatsAppBusinessHealthStatusFields] = Field(None, alias="entities")
