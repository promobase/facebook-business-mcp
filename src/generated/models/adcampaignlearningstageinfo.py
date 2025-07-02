"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdCampaignLearningStageInfoField = Literal[
    "attribution_windows", "conversions", "last_sig_edit_ts", "status"
]


class AdCampaignLearningStageInfoFields(BaseModel):
    """Pydantic model for AdCampaignLearningStageInfo fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    attribution_windows: list[str] = Field(None, alias="attribution_windows")
    conversions: int = Field(None, alias="conversions")
    last_sig_edit_ts: int = Field(None, alias="last_sig_edit_ts")
    status: str = Field(None, alias="status")
