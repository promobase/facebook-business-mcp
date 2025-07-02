"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdDefaultValuesField = Literal["campaign_group"]


class AdDefaultValuesFields(BaseModel):
    """Pydantic model for AdDefaultValues fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    campaign_group: dict[str, Any] = Field(None, alias="campaign_group")
