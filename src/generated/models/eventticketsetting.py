"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
EventTicketSettingField = Literal["id", "ticket_delivery_type"]


class EventTicketSettingFields(BaseModel):
    """Pydantic model for EventTicketSetting fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    id: str = Field(None, alias="id")
    ticket_delivery_type: str = Field(None, alias="ticket_delivery_type")
