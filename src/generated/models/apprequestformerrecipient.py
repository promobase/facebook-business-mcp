"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AppRequestFormerRecipientField = Literal["id", "recipient_id"]


class AppRequestFormerRecipientFields(BaseModel):
    """Pydantic model for AppRequestFormerRecipient fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    id: str = Field(None, alias="id")
    recipient_id: str = Field(None, alias="recipient_id")
