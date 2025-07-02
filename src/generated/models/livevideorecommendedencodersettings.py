"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
LiveVideoRecommendedEncoderSettingsField = Literal[
    "audio_codec_settings", "streaming_protocol", "video_codec_settings"
]


class LiveVideoRecommendedEncoderSettingsFields(BaseModel):
    """Pydantic model for LiveVideoRecommendedEncoderSettings fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    audio_codec_settings: dict[str, Any] = Field(None, alias="audio_codec_settings")
    streaming_protocol: str = Field(None, alias="streaming_protocol")
    video_codec_settings: dict[str, Any] = Field(None, alias="video_codec_settings")
