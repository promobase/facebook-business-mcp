"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdCampaignGroupIncrementalConversionOptimizationConfigField = Literal[
    "action_type",
    "ad_study_end_time",
    "ad_study_id",
    "ad_study_name",
    "ad_study_start_time",
    "cell_id",
    "cell_name",
    "holdout_size",
    "ico_type",
    "objectives",
]


class AdCampaignGroupIncrementalConversionOptimizationConfigFields(BaseModel):
    """Pydantic model for AdCampaignGroupIncrementalConversionOptimizationConfig fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    action_type: str = Field(None, alias="action_type")
    ad_study_end_time: datetime = Field(None, alias="ad_study_end_time")
    ad_study_id: str = Field(None, alias="ad_study_id")
    ad_study_name: str = Field(None, alias="ad_study_name")
    ad_study_start_time: datetime = Field(None, alias="ad_study_start_time")
    cell_id: str = Field(None, alias="cell_id")
    cell_name: str = Field(None, alias="cell_name")
    holdout_size: float = Field(None, alias="holdout_size")
    ico_type: str = Field(None, alias="ico_type")
    objectives: list[dict[str, Any]] = Field(None, alias="objectives")
