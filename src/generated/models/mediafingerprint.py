"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
MediaFingerprintField = Literal[
    "duration_in_sec",
    "fingerprint_content_type",
    "fingerprint_type",
    "id",
    "metadata",
    "title",
    "universal_content_id",
]


class MediaFingerprintFields(BaseModel):
    """Pydantic model for MediaFingerprint fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    duration_in_sec: float = Field(None, alias="duration_in_sec")
    fingerprint_content_type: str = Field(None, alias="fingerprint_content_type")
    fingerprint_type: str = Field(None, alias="fingerprint_type")
    id: str = Field(None, alias="id")
    metadata: dict[str, Any] = Field(None, alias="metadata")
    title: str = Field(None, alias="title")
    universal_content_id: str = Field(None, alias="universal_content_id")
