"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
ShadowIGUserCTXPartnerAppWelcomeMessageFlowField = Literal[
    "compatible_platforms",
    "eligible_platforms",
    "id",
    "is_ig_only_flow",
    "is_used_in_ad",
    "last_update_time",
    "name",
    "welcome_message_flow",
]


class ShadowIGUserCTXPartnerAppWelcomeMessageFlowFields(BaseModel):
    """Pydantic model for ShadowIGUserCTXPartnerAppWelcomeMessageFlow fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    compatible_platforms: list[str] = Field(None, alias="compatible_platforms")
    eligible_platforms: list[str] = Field(None, alias="eligible_platforms")
    id: str = Field(None, alias="id")
    is_ig_only_flow: bool = Field(None, alias="is_ig_only_flow")
    is_used_in_ad: bool = Field(None, alias="is_used_in_ad")
    last_update_time: datetime = Field(None, alias="last_update_time")
    name: str = Field(None, alias="name")
    welcome_message_flow: str = Field(None, alias="welcome_message_flow")
