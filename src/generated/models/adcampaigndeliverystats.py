"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .adcampaigndeliverystatsunsupportedreasons import (
        AdCampaignDeliveryStatsUnsupportedReasonsFields,
    )
    from .adcampaignlearningstageinfo import AdCampaignLearningStageInfoFields


# Field literal type
AdCampaignDeliveryStatsField = Literal[
    "bid_recommendation",
    "current_average_cost",
    "last_significant_edit_ts",
    "learning_stage_exit_info",
    "learning_stage_info",
    "unsupported_features",
]


class AdCampaignDeliveryStatsFields(BaseModel):
    """Pydantic model for AdCampaignDeliveryStats fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    bid_recommendation: int = Field(None, alias="bid_recommendation")
    current_average_cost: float = Field(None, alias="current_average_cost")
    last_significant_edit_ts: int = Field(None, alias="last_significant_edit_ts")
    learning_stage_exit_info: dict[str, Any] = Field(None, alias="learning_stage_exit_info")
    learning_stage_info: AdCampaignLearningStageInfoFields = Field(
        None, alias="learning_stage_info"
    )
    unsupported_features: list[dict[str, AdCampaignDeliveryStatsUnsupportedReasonsFields]] = Field(
        None, alias="unsupported_features"
    )
