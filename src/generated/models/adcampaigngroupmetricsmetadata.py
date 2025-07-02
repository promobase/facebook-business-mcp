"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdCampaignGroupMetricsMetadataField = Literal["budget_optimization", "duplication_flow_tips"]


class AdCampaignGroupMetricsMetadataFields(BaseModel):
    """Pydantic model for AdCampaignGroupMetricsMetadata fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    budget_optimization: list[str] = Field(None, alias="budget_optimization")
    duplication_flow_tips: list[str] = Field(None, alias="duplication_flow_tips")
