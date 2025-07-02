"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
ALMEndAdvertiserInfoField = Literal[
    "estimated_ad_budget", "id", "parent_advertiser_id", "parent_advertiser_name", "tag"
]


class ALMEndAdvertiserInfoFields(BaseModel):
    """Pydantic model for ALMEndAdvertiserInfo fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    estimated_ad_budget: int = Field(None, alias="estimated_ad_budget")
    id: str = Field(None, alias="id")
    parent_advertiser_id: str = Field(None, alias="parent_advertiser_id")
    parent_advertiser_name: str = Field(None, alias="parent_advertiser_name")
    tag: list[str] = Field(None, alias="tag")
