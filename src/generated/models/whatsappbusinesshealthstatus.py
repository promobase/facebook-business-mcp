"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
WhatsAppBusinessHealthStatusField = Literal[
    "additional_info", "can_send_message", "entity_type", "errors", "id"
]


class WhatsAppBusinessHealthStatusFields(BaseModel):
    """Pydantic model for WhatsAppBusinessHealthStatus fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    additional_info: list[str] = Field(None, alias="additional_info")
    can_send_message: str = Field(None, alias="can_send_message")
    entity_type: str = Field(None, alias="entity_type")
    errors: list[dict[str, Any]] = Field(None, alias="errors")
    id: str = Field(None, alias="id")
