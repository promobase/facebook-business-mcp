"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
ReachFrequencyEstimatesPlacementBreakdownField = Literal[
    "android",
    "audience_network",
    "desktop",
    "facebook_search",
    "fb_reels",
    "fb_reels_overlay",
    "ig_android",
    "ig_ios",
    "ig_other",
    "ig_reels",
    "ig_story",
    "instant_articles",
    "instream_videos",
    "ios",
    "msite",
    "suggested_videos",
]


class ReachFrequencyEstimatesPlacementBreakdownFields(BaseModel):
    """Pydantic model for ReachFrequencyEstimatesPlacementBreakdown fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    android: list[float] = Field(None, alias="android")
    audience_network: list[float] = Field(None, alias="audience_network")
    desktop: list[float] = Field(None, alias="desktop")
    facebook_search: list[float] = Field(None, alias="facebook_search")
    fb_reels: list[float] = Field(None, alias="fb_reels")
    fb_reels_overlay: list[float] = Field(None, alias="fb_reels_overlay")
    ig_android: list[float] = Field(None, alias="ig_android")
    ig_ios: list[float] = Field(None, alias="ig_ios")
    ig_other: list[float] = Field(None, alias="ig_other")
    ig_reels: list[float] = Field(None, alias="ig_reels")
    ig_story: list[float] = Field(None, alias="ig_story")
    instant_articles: list[float] = Field(None, alias="instant_articles")
    instream_videos: list[float] = Field(None, alias="instream_videos")
    ios: list[float] = Field(None, alias="ios")
    msite: list[float] = Field(None, alias="msite")
    suggested_videos: list[float] = Field(None, alias="suggested_videos")
