"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field


class AdCreativeLinkDataMoment_type(str, Enum):
    """AdCreativeLinkDataMoment_type enum values."""

    FB_LIVE_SHOPPING = "FB_LIVE_SHOPPING"
    IG_LIVE_SHOPPING = "IG_LIVE_SHOPPING"


# Field literal type
AdCreativeLinkDataMomentField = Literal["id", "type"]


class AdCreativeLinkDataMomentFields(BaseModel):
    """Pydantic model for AdCreativeLinkDataMoment fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    id: str = Field(None, alias="id")
    type: dict[str, Any] = Field(None, alias="type")
