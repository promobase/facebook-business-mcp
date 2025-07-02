"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
OfflineConversionDataSetUploadField = Literal[
    "api_calls",
    "creation_time",
    "duplicate_entries",
    "event_stats",
    "event_time_max",
    "event_time_min",
    "first_upload_time",
    "id",
    "is_excluded_for_lift",
    "last_upload_time",
    "match_rate_approx",
    "matched_entries",
    "upload_tag",
    "valid_entries",
]


class OfflineConversionDataSetUploadFields(BaseModel):
    """Pydantic model for OfflineConversionDataSetUpload fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    api_calls: int = Field(None, alias="api_calls")
    creation_time: int = Field(None, alias="creation_time")
    duplicate_entries: int = Field(None, alias="duplicate_entries")
    event_stats: str = Field(None, alias="event_stats")
    event_time_max: int = Field(None, alias="event_time_max")
    event_time_min: int = Field(None, alias="event_time_min")
    first_upload_time: int = Field(None, alias="first_upload_time")
    id: str = Field(None, alias="id")
    is_excluded_for_lift: bool = Field(None, alias="is_excluded_for_lift")
    last_upload_time: int = Field(None, alias="last_upload_time")
    match_rate_approx: int = Field(None, alias="match_rate_approx")
    matched_entries: int = Field(None, alias="matched_entries")
    upload_tag: str = Field(None, alias="upload_tag")
    valid_entries: int = Field(None, alias="valid_entries")
