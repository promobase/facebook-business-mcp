"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
LiveVideoInputStreamField = Literal[
    "dash_ingest_url",
    "dash_preview_url",
    "id",
    "is_master",
    "secure_stream_url",
    "stream_health",
    "stream_id",
    "stream_url",
]


class LiveVideoInputStreamFields(BaseModel):
    """Pydantic model for LiveVideoInputStream fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    dash_ingest_url: str = Field(None, alias="dash_ingest_url")
    dash_preview_url: str = Field(None, alias="dash_preview_url")
    id: str = Field(None, alias="id")
    is_master: bool = Field(None, alias="is_master")
    secure_stream_url: str = Field(None, alias="secure_stream_url")
    stream_health: dict[str, Any] = Field(None, alias="stream_health")
    stream_id: str = Field(None, alias="stream_id")
    stream_url: str = Field(None, alias="stream_url")
