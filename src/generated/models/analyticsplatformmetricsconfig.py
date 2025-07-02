"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AnalyticsPlatformMetricsConfigField = Literal[
    "has_a2u",
    "has_api_calls",
    "has_app_invites",
    "has_fb_login",
    "has_game_requests",
    "has_payments",
    "has_referrals",
    "has_stories",
    "has_structured_requests",
]


class AnalyticsPlatformMetricsConfigFields(BaseModel):
    """Pydantic model for AnalyticsPlatformMetricsConfig fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    has_a2u: bool = Field(None, alias="has_a2u")
    has_api_calls: bool = Field(None, alias="has_api_calls")
    has_app_invites: bool = Field(None, alias="has_app_invites")
    has_fb_login: bool = Field(None, alias="has_fb_login")
    has_game_requests: bool = Field(None, alias="has_game_requests")
    has_payments: bool = Field(None, alias="has_payments")
    has_referrals: bool = Field(None, alias="has_referrals")
    has_stories: bool = Field(None, alias="has_stories")
    has_structured_requests: bool = Field(None, alias="has_structured_requests")
