"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdAccountLiveVideoAdvertiserField = Literal[
    "is_lva_toggle_on",
    "lva_default_budget",
    "should_default_current_live",
    "should_default_scheduled_live",
    "should_show_lva_toggle",
]


class AdAccountLiveVideoAdvertiserFields(BaseModel):
    """Pydantic model for AdAccountLiveVideoAdvertiser fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    is_lva_toggle_on: bool = Field(None, alias="is_lva_toggle_on")
    lva_default_budget: int = Field(None, alias="lva_default_budget")
    should_default_current_live: bool = Field(None, alias="should_default_current_live")
    should_default_scheduled_live: bool = Field(None, alias="should_default_scheduled_live")
    should_show_lva_toggle: bool = Field(None, alias="should_show_lva_toggle")
