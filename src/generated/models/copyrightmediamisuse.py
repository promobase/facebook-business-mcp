"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .videocopyright import VideoCopyrightFields


# Field literal type
CopyrightMediaMisuseField = Literal[
    "audio_segments",
    "creation_time",
    "disabled_audio_segments",
    "disabled_video_segments",
    "entire_file_issue",
    "entire_file_issue_reasons",
    "expiration_time",
    "id",
    "media_asset_id",
    "reasons",
    "requested_audio_segments",
    "requested_video_segments",
    "resolution_type",
    "status",
    "update_time",
    "video_copyright",
    "video_segments",
]


class CopyrightMediaMisuseFields(BaseModel):
    """Pydantic model for CopyrightMediaMisuse fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    audio_segments: list[dict[str, Any]] = Field(None, alias="audio_segments")
    creation_time: datetime = Field(None, alias="creation_time")
    disabled_audio_segments: list[dict[str, Any]] = Field(None, alias="disabled_audio_segments")
    disabled_video_segments: list[dict[str, Any]] = Field(None, alias="disabled_video_segments")
    entire_file_issue: bool = Field(None, alias="entire_file_issue")
    entire_file_issue_reasons: list[str] = Field(None, alias="entire_file_issue_reasons")
    expiration_time: datetime = Field(None, alias="expiration_time")
    id: str = Field(None, alias="id")
    media_asset_id: str = Field(None, alias="media_asset_id")
    reasons: list[str] = Field(None, alias="reasons")
    requested_audio_segments: list[dict[str, Any]] = Field(None, alias="requested_audio_segments")
    requested_video_segments: list[dict[str, Any]] = Field(None, alias="requested_video_segments")
    resolution_type: str = Field(None, alias="resolution_type")
    status: str = Field(None, alias="status")
    update_time: datetime = Field(None, alias="update_time")
    video_copyright: VideoCopyrightFields = Field(None, alias="video_copyright")
    video_segments: list[dict[str, Any]] = Field(None, alias="video_segments")
