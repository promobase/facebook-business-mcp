"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdLightAdgroupField = Literal["adset_id", "id"]


class AdLightAdgroupFields(BaseModel):
    """Pydantic model for AdLightAdgroup fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    adset_id: str = Field(None, alias="adset_id")
    id: str = Field(None, alias="id")
