"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
IGBoostMediaAdField = Literal["ad_id", "ad_status"]


class IGBoostMediaAdFields(BaseModel):
    """Pydantic model for IGBoostMediaAd fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    ad_id: str = Field(None, alias="ad_id")
    ad_status: str = Field(None, alias="ad_status")
