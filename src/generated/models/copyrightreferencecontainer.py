"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
CopyrightReferenceContainerField = Literal[
    "content_type",
    "copyright_creation_time",
    "download_hd_url",
    "duration_in_sec",
    "id",
    "iswc",
    "metadata",
    "playable_video_uri",
    "published_time",
    "thumbnail_url",
    "title",
    "universal_content_id",
    "writer_names",
]


class CopyrightReferenceContainerFields(BaseModel):
    """Pydantic model for CopyrightReferenceContainer fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    content_type: str = Field(None, alias="content_type")
    copyright_creation_time: datetime = Field(None, alias="copyright_creation_time")
    download_hd_url: str = Field(None, alias="download_hd_url")
    duration_in_sec: float = Field(None, alias="duration_in_sec")
    id: str = Field(None, alias="id")
    iswc: str = Field(None, alias="iswc")
    metadata: dict[str, Any] = Field(None, alias="metadata")
    playable_video_uri: str = Field(None, alias="playable_video_uri")
    published_time: datetime = Field(None, alias="published_time")
    thumbnail_url: str = Field(None, alias="thumbnail_url")
    title: str = Field(None, alias="title")
    universal_content_id: str = Field(None, alias="universal_content_id")
    writer_names: list[str] = Field(None, alias="writer_names")
