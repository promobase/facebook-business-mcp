"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdvertiserVerificationStatusField = Literal[
    "banner_type", "grace_period_ends_at", "ufac_redirect_uri", "verification_status"
]


class AdvertiserVerificationStatusFields(BaseModel):
    """Pydantic model for AdvertiserVerificationStatus fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    banner_type: str = Field(None, alias="banner_type")
    grace_period_ends_at: datetime = Field(None, alias="grace_period_ends_at")
    ufac_redirect_uri: str = Field(None, alias="ufac_redirect_uri")
    verification_status: str = Field(None, alias="verification_status")
