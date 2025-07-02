"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdCreativeDestinationSpecField = Literal["destination_type"]


class AdCreativeDestinationSpecFields(BaseModel):
    """Pydantic model for AdCreativeDestinationSpec fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    destination_type: str = Field(None, alias="destination_type")
