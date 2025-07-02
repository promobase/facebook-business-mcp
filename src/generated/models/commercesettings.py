"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
CommerceSettingsField = Literal["inventory", "total_inventory"]


class CommerceSettingsFields(BaseModel):
    """Pydantic model for CommerceSettings fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    inventory: int = Field(None, alias="inventory")
    total_inventory: int = Field(None, alias="total_inventory")
