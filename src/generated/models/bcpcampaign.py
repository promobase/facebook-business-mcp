"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
BCPCampaignField = Literal[
    "ads_permission_required",
    "application_deadline",
    "campaign_goal",
    "campaign_goal_other",
    "content_delivery_deadline",
    "content_delivery_start_date",
    "content_requirements",
    "content_requirements_description",
    "currency",
    "deal_negotiation_type",
    "description",
    "has_free_product",
    "id",
    "name",
    "payment_amount_for_ads",
    "payment_amount_for_content",
    "payment_description",
]


class BCPCampaignFields(BaseModel):
    """Pydantic model for BCPCampaign fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    ads_permission_required: bool = Field(None, alias="ads_permission_required")
    application_deadline: str = Field(None, alias="application_deadline")
    campaign_goal: str = Field(None, alias="campaign_goal")
    campaign_goal_other: str = Field(None, alias="campaign_goal_other")
    content_delivery_deadline: str = Field(None, alias="content_delivery_deadline")
    content_delivery_start_date: str = Field(None, alias="content_delivery_start_date")
    content_requirements: list[dict[str, int]] = Field(None, alias="content_requirements")
    content_requirements_description: str = Field(None, alias="content_requirements_description")
    currency: str = Field(None, alias="currency")
    deal_negotiation_type: str = Field(None, alias="deal_negotiation_type")
    description: str = Field(None, alias="description")
    has_free_product: bool = Field(None, alias="has_free_product")
    id: str = Field(None, alias="id")
    name: str = Field(None, alias="name")
    payment_amount_for_ads: int = Field(None, alias="payment_amount_for_ads")
    payment_amount_for_content: int = Field(None, alias="payment_amount_for_content")
    payment_description: str = Field(None, alias="payment_description")
