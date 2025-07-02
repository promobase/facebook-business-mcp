"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
ReachFrequencyActivityField = Literal[
    "account_id",
    "campaign_active",
    "campaign_started",
    "creative_uploaded",
    "io_approved",
    "sf_link",
]


class ReachFrequencyActivityFields(BaseModel):
    """Pydantic model for ReachFrequencyActivity fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    account_id: str = Field(None, alias="account_id")
    campaign_active: bool = Field(None, alias="campaign_active")
    campaign_started: bool = Field(None, alias="campaign_started")
    creative_uploaded: bool = Field(None, alias="creative_uploaded")
    io_approved: bool = Field(None, alias="io_approved")
    sf_link: str = Field(None, alias="sf_link")
