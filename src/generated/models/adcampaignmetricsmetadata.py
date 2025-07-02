"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdCampaignMetricsMetadataField = Literal[
    "boosted_component_optimization",
    "creation_flow_tips",
    "default_opted_in_placements",
    "delivery_growth_optimizations",
    "duplication_flow_tips",
    "edit_flow_tips",
]


class AdCampaignMetricsMetadataFields(BaseModel):
    """Pydantic model for AdCampaignMetricsMetadata fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    boosted_component_optimization: list[str] = Field(None, alias="boosted_component_optimization")
    creation_flow_tips: list[str] = Field(None, alias="creation_flow_tips")
    default_opted_in_placements: list[dict[str, Any]] = Field(
        None, alias="default_opted_in_placements"
    )
    delivery_growth_optimizations: list[dict[str, Any]] = Field(
        None, alias="delivery_growth_optimizations"
    )
    duplication_flow_tips: list[str] = Field(None, alias="duplication_flow_tips")
    edit_flow_tips: list[str] = Field(None, alias="edit_flow_tips")
